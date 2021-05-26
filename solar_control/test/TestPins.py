class TestPin:
    def __init__(self, name, nummer, modus):
        self.name = name
        self.nummer = nummer
        self.modus = modus
        self.pinState = 0


class OutTestPin(TestPin):
    def __init__(self, name, nummer, modus, wert):
        TestPin.__init__(self, name, nummer, modus)
        self.wert = wert
        self.schreibe_wert_an_pin()

    def schreibe_wert_an_pin(self):
        self.pinState = self.wert


class InTestPin(TestPin):
    def __init__(self, name, nummer, modus):
        TestPin.__init__(self, name, nummer, modus)

    def lese_pin_wert(self):
        return self.pinState

    def simuliere_optokoppler_signal(self, wert):
        self.pinState = wert
