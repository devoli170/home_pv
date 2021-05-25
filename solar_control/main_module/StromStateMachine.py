from time import sleep

SOLARSTROM = 1
HAUSSTROM = 0


class StromStateMachine:
    def __init__(self, solar_pins, haus_pins, input_pin, solar_wechsel_wartezeit):
        self.boot = True
        self.solar_pins = solar_pins
        self.haus_pins = haus_pins
        self.input_pin = input_pin
        self.solar_wartezeit = solar_wechsel_wartezeit
        self.aktiver_strom = None

    def run_logic(self):
        while True:
            if self.boot and self.input_pin.lese_pin_wert() == 1:
                self.solar_pins.schnellsart()
                self.aktiver_strom = SOLARSTROM
                self.boot = False
                sleep(2)
                continue

            aktuelles_signal = self.input_pin.lese_pin_wert()
            if aktuelles_signal != self.aktiver_strom:
                self.schalte_relais_je_nach_optokoppler_signal(aktuelles_signal)

    def schalte_relais_je_nach_optokoppler_signal(self, aktuelles_signal):
        if aktuelles_signal == HAUSSTROM:
            self.solar_pins.ausschalten()
            sleep(1)
            self.haus_pins.anschalten()
            self.aktiver_strom = HAUSSTROM

        if aktuelles_signal == SOLARSTROM:
            sleep(self.solar_wartezeit)
            self.haus_pins.ausschalten()
            sleep(1)
            self.solar_pins.anschalten()
            self.aktiver_strom = SOLARSTROM

