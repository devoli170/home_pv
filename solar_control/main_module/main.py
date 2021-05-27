#!/usr/bin/python3 -u
import signal
import logging.config
from time import sleep
from sys import path as sys_path
import pathlib

p = pathlib.Path(__file__)
PACKAGE_ROOT = str(p.parent.absolute().parent.absolute())
logging.config.fileConfig('{}/conf/logging.conf'.format(PACKAGE_ROOT), disable_existing_loggers=False)
logger = logging.getLogger("main")
APPLICATION_ROOT = str(p.parent.absolute().parent.absolute().parent.absolute())
logger.info("Adding {} to sys.path".format(APPLICATION_ROOT))
sys_path.insert(0, APPLICATION_ROOT)
import pip._internal as pip


def install(package):
    pip.main(['install', package])


if __name__ == '__main__':
    try:
        from solar_control.io_wrapper import GPIO
    except ImportError:
        install('rpi.gpio')
        from solar_control.io_wrapper import GPIO
from solar_control.main_module.Pin import OutPin, InPin, StromPins
from solar_control.main_module.StromSteuerung import StromSteuerung


class SIG_handler():
    def __init__(self):
        self.exit_gracefully = False

    def signal_handler(self, signal, frame):
        self.exit_gracefully = True

def main():
    logger.info("Starte Programm")
    handler = SIG_handler()
    signal.signal(signal.SIGINT, handler.signal_handler)
    signal.signal(signal.SIGTERM, handler.signal_handler)
    logger.info("Benutze BCM Nummerierung der Pins")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    logger.info("Initialisiere Pins")
    solar_l1 = OutPin("solar_l1", 17, GPIO.OUT, GPIO.LOW)
    solar_n = OutPin("solar_n", 18, GPIO.OUT, GPIO.LOW)
    haus_l1 = OutPin("haus_l1", 22, GPIO.OUT, GPIO.LOW)
    haus_n = OutPin("haus_n", 23, GPIO.OUT, GPIO.LOW)
    solar_pins = StromPins(solar_n, solar_l1)
    haus_pins = StromPins(haus_n, haus_l1)
    optokoppler = InPin("optokoppler", 24, GPIO.IN)
    warte_zeit = 2
    logger.info('Warte {} Sekunden nach Initialisierung'.format(warte_zeit))
    sleep(2)

    wechsel_zu_solar_strom_wartezeit_in_sec = 600
    strom_steuerung = StromSteuerung(solar_pins, haus_pins, optokoppler, wechsel_zu_solar_strom_wartezeit_in_sec)
    strom_steuerung.start()
    logger.info("Steuerungs Logik als Thread gestartet. Warte auf Signale zum Beenden des Programms")

    while not handler.exit_gracefully:
        sleep(1)
    strom_steuerung.stop()
    GPIO.cleanup()
    logger.info("Programm beendet.")


if __name__ == "__main__":
    main()
