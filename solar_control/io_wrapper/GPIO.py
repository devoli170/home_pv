import platform


def raspi_check():
    return True if platform.machine().startswith("ARM") else False


if raspi_check():
    import RPi.GPIO as GPIO
else:
    import Mock.GPIO as GPIO


def setup(*args):
    GPIO.setup(args)


def output(*args):
    GPIO.output(args)


def input(*args):
    GPIO.input(args)

HIGH = GPIO.HIGH
LOW = GPIO.LOW

OUT = GPIO.OUT
IN = GPIO.IN
