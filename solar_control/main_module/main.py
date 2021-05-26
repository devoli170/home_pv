#!/usr/bin/python3 -u
import threading, signal
from time import sleep
from solar_control.io_wrapper import GPIO
from solar_control.main_module.Pin import OutPin, InPin, StromPins
from solar_control.main_module.StromSteuerung import StromSteuerung


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self):
        self.kill_now = True


def main():
    solar_l1 = OutPin("solar_l1", 17, GPIO.OUT, GPIO.LOW)
    solar_n = OutPin("solar_n", 18, GPIO.OUT, GPIO.LOW)
    haus_l1 = OutPin("haus_l1", 22, GPIO.OUT, GPIO.LOW)
    haus_n = OutPin("haus_n", 23, GPIO.OUT, GPIO.LOW)
    solar_pins = StromPins(solar_n, solar_l1)
    haus_pins = StromPins(haus_n, haus_l1)
    optokoppler = InPin("optokoppler", 24, GPIO.IN)
    sleep(2)

    wechsel_zu_solar_strom_wartezeit_in_sec = 600
    strom_steuerung = StromSteuerung(solar_pins, haus_pins, optokoppler, wechsel_zu_solar_strom_wartezeit_in_sec)
    strom_steuerung.start()

    killer = GracefulKiller()
    while not killer.kill_now:
        sleep(1)
    strom_steuerung.stop()
    print("Program ending gracefully.")


if __name__ == "__main__":
    main()
