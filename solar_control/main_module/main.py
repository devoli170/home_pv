#!/usr/bin/python3 -u
import signal
import logging.config
from time import sleep
from sys import path as sys_path
import os.path as path
from os import getcwd
sys_path.insert(0, path.abspath(path.join(getcwd(), "../..")))
from solar_control.io_wrapper import GPIO
from solar_control.main_module.Pin import OutPin, InPin, StromPins
from solar_control.main_module.StromSteuerung import StromSteuerung


logging.config.fileConfig('../conf/logging.conf')
logger = logging.getLogger("main")


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self):
        logger.info("Signal zum Beenden erhalten")
        self.kill_now = True


def main():
    logger.info("Starte Programm")
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
    killer = GracefulKiller()
    while not killer.kill_now:
        sleep(1)
    strom_steuerung.stop()
    logger.info("Programm beendet.")


if __name__ == "__main__":
    main()
