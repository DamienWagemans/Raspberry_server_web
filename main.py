import os
import sys


# if app.env == 'development':
#     import FakeRPi.GPIO as GPIO
# else:
#     import RPi.GPIO as GPIO
import time
try:
  os.environ['API_KEY']
  print()
except KeyError:
  print('[error]: `API_KEY` environment variable required')
  sys.exit(1)
channel = 21

# # GPIO setup
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(channel, GPIO.OUT)
#
#
# def motor_on(pin):
#     GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(1)
        motor_off(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
