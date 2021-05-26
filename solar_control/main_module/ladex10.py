#!/usr/bin/python3 -u
from time import sleep
from solar_control.io_wrapper import GPIO
from solar_control.main_module.Pin import OutPin, InPin, StromPins
from solar_control.main_module.StromStateMachine import StromStateMachine


def main():
    solar_l1 = OutPin("solar_l1", 17, GPIO.OUT, GPIO.LOW)
    solar_n = OutPin("solar_n", 18, GPIO.OUT, GPIO.LOW)
    haus_l1 = OutPin("haus_l1", 22, GPIO.OUT, GPIO.LOW)
    haus_n = OutPin("haus_n", 23, GPIO.OUT, GPIO.LOW)
    solar_pins = StromPins(solar_n, solar_l1)
    haus_pins = StromPins(haus_n, haus_l1)
    optokoppler = InPin("optokoppler", 24, GPIO.IN)
    sleep(2)

    strom_schaltungs_logik = StromStateMachine(solar_pins, haus_pins, optokoppler, 600)
    strom_schaltungs_logik.run_logic()


if __name__ == "__main__":
    main()
