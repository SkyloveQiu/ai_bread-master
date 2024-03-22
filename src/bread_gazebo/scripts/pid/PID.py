class PID:

    def __init__(self,
                 Kp,                # Controller gains
                 Ki,                # Controller gains
                 Kd,                # Controller gains
                 tau,               # Derivative low - pass filter timeconstant
                 limMin,            # Output limits
                 limMax,            # Output limits
                 limMinInt,         # Integrator limits
                 limMaxInt,         # Integrator limits
                 T,                 # Sample time( in seconds)
                 int_clamp_margin,  # Active integrator clamping margin 
                 integrator = 0,        # Controller "memory"
                 prevError = 0,         # Controller "memory"
                 differentiator = 0,    # Controller "memory"
                 prevMeasurement = 0,   # Controller "memory"
                 out = 0,
                 integrator_clamping = False):   # Active integrator clamping margin             # Controller output

        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.tau = tau
        self.limMin = limMin
        self.limMax = limMax
        self.limMinInt = limMinInt
        self.limMaxInt = limMaxInt
        self.T = T
        self.integrator = integrator
        self.prevError = prevError
        self.differentiator = differentiator
        self.prevMeasurement = prevMeasurement
        self.out = out
        self.integrator_clamping = integrator_clamping
        self.int_clamp_margin = int_clamp_margin

    def PID_controller_update(self, error, measurement):

        # Proportional term
        proportional = self.Kp * error

        # Integral term
        if self.integrator_clamping:
            self.integrator == 0
        else:
            self.integrator = self.integrator + 0.5 * self.Ki * self.T * (error + self.prevError)

        # Anti wind-up
        if self.integrator > self.limMaxInt:
            self.integrator = self.limMaxInt
        elif self.integrator < self.limMinInt:
            self.integrator = self.limMinInt

        # Differential term
        self.differentiator = -1 * (2 * self.Kd * (measurement - self.prevMeasurement) + (2 * self.tau - self.T) * self.differentiator) / (2 * self.tau + self.T)

        # Generate output
        self.out = proportional + self.integrator + self.differentiator

        # Output limitation
        if self.out > self.limMax:
            self.out = self.limMax
        elif self.out < self.limMin:
            self.out = self.limMin

        # Store error and measurement for next iteration
        self.prevError = error
        self.prevMeasurement = measurement

        # Return output
        return self.out






#PID 1 constants
pid1_Kp = 5
pid1_Ki = 1
pid1_Kd = 0
pid1_tau = 1
pid1_limMin = -2
pid1_limMax = 2
pid1_limMinInt = -0.1
pid1_limMaxInt = 0.1
pid1_T = 0.01
pid1_int_clamp_margin = 2

# PID 2 constants
pid2_Kp = 3
pid2_Ki = 1
pid2_Kd = 0
pid2_tau = 1
pid2_limMin = -2
pid2_limMax = 2
pid2_limMinInt = -1
pid2_limMaxInt = 1
pid2_T = 0.01
pid2_int_clamp_margin = 10


# Initialize PID controllers
pid1 = PID(pid1_Kp, pid1_Ki, pid1_Kd, pid1_tau, pid1_limMin, pid1_limMax, pid1_limMinInt, pid1_limMaxInt, pid1_T, pid1_int_clamp_margin)
pid2 = PID(pid2_Kp, pid2_Ki, pid2_Kd, pid2_tau, pid2_limMin, pid2_limMax, pid2_limMinInt, pid2_limMaxInt, pid2_T, pid2_int_clamp_margin)
