import platform


def laeuft_auf_raspi():
    return True if platform.machine().startswith("arm") else False


if laeuft_auf_raspi():
    import RPi.GPIO as GPIO
    print("RPI loaded as GPIO")
else:
    import Mock.GPIO as GPIO
    print("Mock.GPIO loaded as GPIO")


def setup(*args):
    GPIO.setup(*args)


def output(*args):
    GPIO.output(*args)


def input(*args):
    GPIO.input(*args)


HIGH = GPIO.HIGH
LOW = GPIO.LOW

OUT = GPIO.OUT
IN = GPIO.IN
