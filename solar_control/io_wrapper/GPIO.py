import platform, logging, logging.config

import logging.config
logging.config.fileConfig('../conf/logging.conf')
logger = logging.getLogger("GPIO")

def laeuft_auf_raspi():
    return True if platform.machine().startswith("arm") else False


if laeuft_auf_raspi():
    import RPi.GPIO as GPIO
    logger.debug("RPI loaded as GPIO")
else:
    import Mock.GPIO as GPIO
    logger.debug("Mock.GPIO loaded as GPIO")


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
