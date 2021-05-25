from solar_control.io_wrapper import GPIO
from time import sleep


class Pin:
    def __init__(self, name, nummer, modus):
        self.name = name
        self.nummer = nummer
        self.modus = modus
        GPIO.setup(self.nummer, self.modus)


class OutPin(Pin):
    def __init__(self, name, nummer, modus, wert):
        Pin.__init__(self, name, nummer, modus)
        self.wert = wert
        self.schreibe_wert_an_pin()

    def schreibe_wert_an_pin(self):
        GPIO.output(self.nummer, self.wert)


class InPin(Pin):
    def __init__(self, name, nummer, modus):
        Pin.__init__(self, name, nummer, modus)

    def lese_pin_wert(self):
        return GPIO.input(self.nummer)


class StromPins:
    def __init__(self, n, l1):
        self._n = n
        self._l1 = l1

    def ausschalten(self):
        self._n.wert = GPIO.LOW
        self._l1.wert = GPIO.LOW
        self.flush()

    def anschalten(self):
        self._n.wert = GPIO.HIGH
        self._l1.wert = GPIO.HIGH
        self.flush()

    def flush(self):
        self._l1.schreibe_wert_an_pin()
        self._n.schreibe_wert_an_pin()

    def lese_zustand(self):
        return GPIO.HIGH if self._n == GPIO.HIGH and self._l1 == GPIO.HIGH else GPIO.LOW

