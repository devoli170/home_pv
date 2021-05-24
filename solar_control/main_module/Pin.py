from solar_control.io_wrapper import GPIO

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