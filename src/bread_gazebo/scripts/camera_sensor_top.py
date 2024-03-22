#!/usr/bin/env python3
import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32, Int32
from bread_gazebo.srv import BaggingStatus,BaggingStatusResponse
from bread_gazebo.msg import LogMsg, ConveyorMotorAction, ConveyorMotorGoal
import rospkg
from tflite_support import metadata
from typing import List, NamedTuple
import json
import os
import cv2 as cv
import time
import actionlib
import numpy as np
try:
  # Import TFLite interpreter from tflite_runtime package if it's available.
  from tflite_runtime.interpreter import Interpreter
  from tflite_runtime.interpreter import load_delegate
except ImportError:
  # If not, fallback to use the TFLite interpreter from the full TF package.
  import tensorflow as tf

  Interpreter = tf.lite.Interpreter
  load_delegate = tf.lite.experimental.load_delegate
flag_start_stop = True
dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
out_publisher = rospy.Publisher('top_camera_topic', UInt32, queue_size=10)
conveyor_motor_client = actionlib.SimpleActionClient("conveyor_motor",ConveyorMotorAction)
component_name = "Top Camera"
rospack = rospkg.RosPack()
path = rospack.get_path('bread_gazebo')+"/scripts/data/detect_model.tflite"
def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=640,
    display_height=360,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor_id=1 ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
cam = cv.VideoCapture(gstreamer_pipeline(), cv.CAP_GSTREAMER)

x1 = 540
y1 = 0
x2 = 0
y2 = 0
def sync_motor():
    global x1,x2,y1,y2
    goal = ConveyorMotorGoal(moving_steps=50)
    conveyor_motor_client.send_goal(goal)
    conveyor_motor_client.wait_for_result()
    time.sleep(5)
    if not cam.isOpened():
        raise IOError("Cannot open webcam")
    prev = None
    flag = True
    count = 0
    while not rospy.is_shutdown():
        
        # ret can be used to detect if capture was successful 
        ret, frame = cam.read()
        if count < 10:
            
            count+=1
            rospy.Rate(1).sleep()
            continue
        if not ret:
            continue
        
        frame_gr= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gr = cv.medianBlur(frame_gr, 11)
        if flag:
            lower = np.array([30, 80, 127], dtype = "uint8")
            upper = np.array([52, 100, 165], dtype = "uint8")
            # lower = np.array([39, 20, 35], dtype = "uint8")
            # upper = np.array([59, 50, 60], dtype = "uint8")
            mask = cv.inRange(frame, lower, upper)
            output = cv.bitwise_and(frame, frame, mask = mask)
            # ms  = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
            threshold = cv.threshold(mask, 20, 255, cv.THRESH_BINARY)[1]
            threshold = cv.dilate(threshold, None, iterations=1)
            
            cnts, _ = cv.findContours(threshold, cv.RETR_EXTERNAL,
            cv.CHAIN_APPROX_SIMPLE)

            for c in cnts:
                if cv.contourArea(c) < 500 or cv.contourArea(c)>10000:
                    continue
                (x, y, w, h) = cv.boundingRect(c)
                print(str(x)+str(x+w))
                # (x1,y1,x2,y2) = (x,y,x+w,y+h)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.imwrite(dirpath+"/red.png", np.hstack([frame,output]))
            prev = frame_gr
            flag = False
            continue
        diff = cv.absdiff(prev, frame_gr)
        threshold = cv.threshold(diff, 20, 255, cv.THRESH_BINARY)[1]
        threshold = cv.dilate(threshold, None, iterations=5)
        
        cnts, _ = cv.findContours(threshold, cv.RETR_EXTERNAL,
            cv.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv.contourArea(c) < 2000:
                continue
            (x, y, w, h) = cv.boundingRect(c)
            if x1-(x+w)<10:
                print("DONE")
                return
            
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        goal = ConveyorMotorGoal(moving_steps=-40)
        conveyor_motor_client.send_goal(goal)
        conveyor_motor_client.wait_for_result()
        cv.imwrite(dirpath+"/test.png", frame)
        prev = frame_gr

        
        rospy.Rate(8).sleep()
    cleanup()
def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)



def cleanup():
    rospy.signal_shutdown("SYNC CLOSE ISSUED")    
def status_ping(req):
    if req.flag == 5:
        
        loop_thread = threading.Thread(target=cleanup)
        loop_thread.setDaemon(True)
        loop_thread.start()
        return BaggingStatusResponse(0, "CLOSING")


class ObjectDetectorOptions(NamedTuple):
  """A config to initialize an object detector."""

  enable_edgetpu: bool = False
  """Enable the model to run on EdgeTPU."""

  label_allow_list: List[str] = None
  """The optional allow list of labels."""

  label_deny_list: List[str] = None
  """The optional deny list of labels."""

  max_results: int = -1
  """The maximum number of top-scored detection results to return."""

  num_threads: int = 1
  """The number of CPU threads to be used."""

  score_threshold: float = 0.0
  """The score threshold of detection results to return."""


class Rect(NamedTuple):
  """A rectangle in 2D space."""
  left: float
  top: float
  right: float
  bottom: float


class Category(NamedTuple):
  """A result of a classification task."""
  label: str
  score: float
  index: int


class Detection(NamedTuple):
  """A detected object as the result of an ObjectDetector."""
  bounding_box: Rect
  categories: List[Category]


def edgetpu_lib_name():
  """Returns the library name of EdgeTPU in the current platform."""
  return {
      'Darwin': 'libedgetpu.1.dylib',
      'Linux': 'libedgetpu.so.1',
      'Windows': 'edgetpu.dll',
  }.get(platform.system(), None)


class ObjectDetector:
  """A wrapper class for a TFLite object detection model."""

  _OUTPUT_LOCATION_NAME = 'location'
  _OUTPUT_CATEGORY_NAME = 'category'
  _OUTPUT_SCORE_NAME = 'score'
  _OUTPUT_NUMBER_NAME = 'number of detections'

  def __init__(
      self,
      cam, 
      model_path: str,
      options: ObjectDetectorOptions = ObjectDetectorOptions()
  ) -> None:
    """Initialize a TFLite object detection model.
    Args:
        model_path: Path to the TFLite model.
        options: The config to initialize an object detector. (Optional)
    Raises:
        ValueError: If the TFLite model is invalid.
        OSError: If the current OS isn't supported by EdgeTPU.
    """

    # Load metadata from model.
    displayer = metadata.MetadataDisplayer.with_model_file(model_path)

    # Save model metadata for preprocessing later.
    model_metadata = json.loads(displayer.get_metadata_json())
    process_units = model_metadata['subgraph_metadata'][0][
        'input_tensor_metadata'][0]['process_units']
    mean = 127.5
    std = 127.5
    for option in process_units:
      if option['options_type'] == 'NormalizationOptions':
        mean = option['options']['mean'][0]
        std = option['options']['std'][0]
    self._mean = mean
    self._std = std

    # Load label list from metadata.
    file_name = displayer.get_packed_associated_file_list()[0]
    label_map_file = displayer.get_associated_file_buffer(file_name).decode()
    label_list = list(filter(len, label_map_file.splitlines()))
    self._label_list = label_list

    # Initialize TFLite model.
    if options.enable_edgetpu:
      if edgetpu_lib_name() is None:
        raise OSError("The current OS isn't supported by Coral EdgeTPU.")
      interpreter = Interpreter(
          model_path=model_path,
          experimental_delegates=[load_delegate(edgetpu_lib_name())],
          num_threads=options.num_threads)
    else:
      interpreter = Interpreter(
          model_path=model_path, num_threads=options.num_threads)

    interpreter.allocate_tensors()
    input_detail = interpreter.get_input_details()[0]

    # From TensorFlow 2.6, the order of the outputs become undefined.
    # Therefore we need to sort the tensor indices of TFLite outputs and to know
    # exactly the meaning of each output tensor. For example, if
    # output indices are [601, 599, 598, 600], tensor names and indices aligned
    # are:
    #   - location: 598
    #   - category: 599
    #   - score: 600
    #   - detection_count: 601
    # because of the op's ports of TFLITE_DETECTION_POST_PROCESS
    # (https://github.com/tensorflow/tensorflow/blob/a4fe268ea084e7d323133ed7b986e0ae259a2bc7/tensorflow/lite/kernels/detection_postprocess.cc#L47-L50).
    sorted_output_indices = sorted(
        [output['index'] for output in interpreter.get_output_details()])
    self._output_indices = {
        self._OUTPUT_LOCATION_NAME: sorted_output_indices[0],
        self._OUTPUT_CATEGORY_NAME: sorted_output_indices[1],
        self._OUTPUT_SCORE_NAME: sorted_output_indices[2],
        self._OUTPUT_NUMBER_NAME: sorted_output_indices[3],
    }

    self._input_size = input_detail['shape'][2], input_detail['shape'][1]
    self._is_quantized_input = input_detail['dtype'] == np.uint8
    self._interpreter = interpreter
    self._options = options
    self.stream = cam

  def detect(self) -> List[Detection]:
    """Run detection on an input image.
    Args:
        input_image: A [height, width, 3] RGB image. Note that height and width
          can be anything since the image will be immediately resized according
          to the needs of the model within this function.
    Returns:
        A Person instance.
    """
    s, image = self.stream.read()
    frame = np.array(image)
    image_height, image_width, _ = frame.shape

    input_tensor = self._preprocess(frame)
 
    self._set_input_tensor(input_tensor)
    self._interpreter.invoke()

    # Get all output details
    boxes = self._get_output_tensor(self._OUTPUT_LOCATION_NAME)
    classes = self._get_output_tensor(self._OUTPUT_CATEGORY_NAME)
    scores = self._get_output_tensor(self._OUTPUT_SCORE_NAME)
    count = int(self._get_output_tensor(self._OUTPUT_NUMBER_NAME))

    return self._postprocess(boxes, classes, scores, count, image_width,
                             image_height)

  def _preprocess(self, input_image: np.ndarray) -> np.ndarray:
    """Preprocess the input image as required by the TFLite model."""

    # Resize the input
    input_tensor = cv.resize(input_image, self._input_size)

    # Normalize the input if it's a float model (aka. not quantized)
    if not self._is_quantized_input:
      input_tensor = (np.float32(input_tensor) - self._mean) / self._std

    # Add batch dimension
    input_tensor = np.expand_dims(input_tensor, axis=0)

    return input_tensor

  def _set_input_tensor(self, image):
    """Sets the input tensor."""
    tensor_index = self._interpreter.get_input_details()[0]['index']
    input_tensor = self._interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image

  def _get_output_tensor(self, name):
    """Returns the output tensor at the given index."""
    output_index = self._output_indices[name]
    tensor = np.squeeze(self._interpreter.get_tensor(output_index))
    return tensor

  def _postprocess(self, boxes: np.ndarray, classes: np.ndarray,
                   scores: np.ndarray, count: int, image_width: int,
                   image_height: int) -> List[Detection]:
    """Post-process the output of TFLite model into a list of Detection objects.
    Args:
        boxes: Bounding boxes of detected objects from the TFLite model.
        classes: Class index of the detected objects from the TFLite model.
        scores: Confidence scores of the detected objects from the TFLite model.
        count: Number of detected objects from the TFLite model.
        image_width: Width of the input image.
        image_height: Height of the input image.
    Returns:
        A list of Detection objects detected by the TFLite model.
    """
    results = []

    # Parse the model output into a list of Detection entities.
    for i in range(count):
      if scores[i] >= self._options.score_threshold:
        y_min, x_min, y_max, x_max = boxes[i]
        bounding_box = Rect(
            top=int(y_min * image_height),
            left=int(x_min * image_width),
            bottom=int(y_max * image_height),
            right=int(x_max * image_width))
        class_id = int(classes[i])
        category = Category(
            score=scores[i],
            label=self._label_list[class_id],  # 0 is reserved for background
            index=class_id)
        result = Detection(bounding_box=bounding_box, categories=[category])
        results.append(result)

    # Sort detection results by score ascending
    sorted_results = sorted(
        results,
        key=lambda detection: detection.categories[0].score,
        reverse=True)

    # Filter out detections in deny list
    filtered_results = sorted_results
    if self._options.label_deny_list is not None:
      filtered_results = list(
          filter(
              lambda detection: detection.categories[0].label not in self.
              _options.label_deny_list, filtered_results))

    # Keep only detections in allow list
    if self._options.label_allow_list is not None:
      filtered_results = list(
          filter(
              lambda detection: detection.categories[0].label in self._options.
              label_allow_list, filtered_results))
    # Only return maximum of max_results detection.
    if self._options.max_results > 0:
      result_count = min(len(filtered_results), self._options.max_results)
      filtered_results = filtered_results[:result_count]
    return filtered_results
def on_call(data):
  global flag_start_stop
  if data.data == 0:
    flag_start_stop = True
def top_cam_init():
    rospy.init_node('camera_sensor_top', anonymous=False)
    # sync_motor()
    rospy.Subscriber('top_cam_input', UInt32, on_call)
    rospy.Service('Top_Cam_Status', BaggingStatus, status_ping)
    # time.sleep(25)
    # out_publisher.publish(0)
    
    detect = ObjectDetector(cam,path)
    while True:
      if not flag_start_stop:
        time.sleep(5)
        continue
      boxes = detect.detect()
      if len(boxes)>0:
        if boxes[0].bounding_box.top<10:
          out_publisher.publish(0)
          flag_start_stop = False
      else:
        time.sleep(2)
    rospy.spin()

if __name__ == '__main__':

    top_cam_init()
