import platform
import logging
import logging.config
import pathlib

p = pathlib.Path(__file__)
package_root = p.parent.absolute().parent.absolute()
logging.config.fileConfig('{}/conf/logging.conf'.format(package_root))
logger = logging.getLogger("GPIO")


def laeuft_auf_raspi():
    return True if platform.machine().startswith("arm") else False


if laeuft_auf_raspi():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
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


def setmode(mode):
    GPIO.setmode(mode)


def cleanup():
    GPIO.cleanup()

def setwarnings(bool):
    GPIO.setwarnings(False)


BCM = GPIO.BCM
HIGH = GPIO.HIGH
LOW = GPIO.LOW

OUT = GPIO.OUT
IN = GPIO.IN
