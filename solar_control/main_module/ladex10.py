from time import sleep
from datetime import datetime
from solar_control.io_wrapper import GPIO


class Pin:
    def __init__(self, name, nummer, modus):
        self.name = name
        self.nummer = nummer
        self.modus = modus
        GPIO.setup(self.nummer, self.modus)


class OutPin(Pin):
    def __init__(self, name, nummer, modus, wert):
        Pin.__init__(name, nummer, modus)
        self.wert = wert
        self.schreibe_wert_an_pin()

    def schreibe_wert_an_pin(self):
        GPIO.output(self.nummer, self.wert)


class InPin(Pin):
    def __init__(self, name, nummer, modus):
        Pin.__init__(name, nummer, modus)

    def lese_pin_wert(self):
        return GPIO.input(self.nummer)


class StromKontrolle:
    def __init__(self, solar_pins, hausstrom_pins, in_pin, solar_wechsel_wartezeit ):
        self.solar_pins = solar_pins
        self.hausstrom_pins = hausstrom_pins
        self.in_pin = in_pin
        self.solar_wechsel_wartezeit = solar_wechsel_wartezeit
        self.jetzt_geschalten = "nichts"

    def lese_jetzige_schaltung(self):




    def evaluiereZustand(self):
        self.in_pin.lese_pin_wert()

    def start(self):
        while(True):
            evaluiereZustand():

def beep():
    return "beep"


def main():
    solar_l1 = OutPin("solar_l1", 17, "out", GPIO.LOW)
    solar_n = OutPin("solar_n", 18, "out", GPIO.LOW)
    haus_l1 = OutPin("haus_l1", 22, "out", GPIO.LOW)
    haus_n = OutPin("haus_n", 23, "out", GPIO.LOW)
    solar_pins = [solar_n, solar_l1]
    hausstrom_pins = [haus_n, haus_l1]
    optokoppler = InPin("optokoppler", 24, "in")
    sleep(2)
    strom_kontrolle = StromKontrolle(solar_pins, hausstrom_pins, optokoppler, 600)
    strom_kontrolle.start()


if __name__ == "__main__":
    main()
