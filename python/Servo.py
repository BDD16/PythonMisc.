#!/usr/bin/env python3
#import python libraries
import time, math
import getopt, sys

#import rcpy library
# This automatically initizalizes the robotics cape
import rcpy
import rcpy.servo as servo
import rcpy.clock as clock


me = '[Servo]'


class Servo:

  def __init__(self,channel=8, Frequency=10, duty=1.5,period=0.02, sweep=False):
    # defaults
    self.duty = duty
    self.sweep = sweep
    self.period = period
    if channel > 0 or channel <=8:
        self.num = channel
    else:
        print(me + 'ERROR> Servo Channel is out of range 1<= num <= 8')
        exit()
    self.num = channel
    self.rcpy_state = None
    self.currentState = None
    self.frequency = Frequency
    #self.pulseWidth = PulseWidth #units in microSeconds
    self.srvo = None
    self.clk = None
    self.setup()


  def setup(self):
    # # Set the two LEDs as outputs:
    # GPIO.setup(self.inputpin, GPIO.OUT)
    # GPIO.setup(self.inputpin, GPIO.OUT)
    #
    # # Start one high and one low:
    # GPIO.output(self.inputpin, GPIO.HIGH)
    #GPIO.output("SERVO_PWR", GPIO.HIGH)
    # set state to rcpy.RUNNING
    rcpy.set_state(rcpy.RUNNING)
    self.rcpy_state = rcpy.RUNNING
    # set servo duty (only one option at a time)
    #Enable Servos
    servo.enable()
    self.srvo = servo.Servo(self.num)
    if self.duty != 0:
        print('Setting servo {} to {} duty'.format(self.num, self.duty))
        self.srvo.set(self.duty)
    self.currentState = True
    self.clk = clock.Clock(self.srvo, self.period)

    # start clock
    self.clk.start()

  def toggle(self):
    if self.currentState:
      GPIO.output(self.inputpin, GPIO.LOW)
      self.currentState = False
    elif self.currentState == False:
      GPIO.output(self.inputpin, GPIO.HIGH)
      self.currentState = True

  def output(self,flag):
    if flag:
      GPIO.output(self.inputpin, GPIO.HIGH)
      self.currentState = True
    else:
      GPIO.output(self.inputpin, GPIO.LOW)
      self.currentState = False


  def RotateByAngle(self, angleInDegrees ):
      #+90 is 2ms and -90 is 1ms
      #remap to make +90 to be 0 degrees and -90 to be 180 degrees
      if angleInDegrees >= 0 and angleInDegrees <=90:
          dutycycle = ((angleInDegrees % 180) * 1500 / 180)*(10**(-3))
      elif angleInDegrees < 0 and angleInDegrees >= -90:
        dutycycle = ((abs(angleInDegrees) % 180) * 1500 / 180)*(10**(-3))
        dutycycle = dutycycle * (-1)

      print(me + "INFO> DUTY: " + str(dutycycle))
      self.duty = dutycycle
      self.srvo.set(self.duty)


  def closeAll(self):
    #GPIO.cleanup()
    self.clk = clock.Clock(self.srvo, self.period)
    # stop clock
    self.clk.stop()
    # disable servos
    servo.disable()

# Start the loop:
if __name__ == '__main__':
  SERVO = Servo(8)
  print("Press Ctrl-C to exit")
  angle = -90
  while True:
    try:
      SERVO.RotateByAngle(angle)
      angle += 1
      if angle == 91:
        angle = -90
      time.sleep(0.02)
    except KeyboardInterrupt:
      # handle what to do when Ctrl-C was pressed
      SERVO.closeAll()
      break
