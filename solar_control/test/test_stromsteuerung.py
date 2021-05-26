import unittest
from solar_control.main_module.StromSteuerung import StromSteuerung, HAUSSTROM, SOLARSTROM
from solar_control.main_module.Pin import StromPins
from solar_control.io_wrapper.GPIO import GPIO
from solar_control.test.TestPins import *
from time import sleep


class TestStromsteuerung(unittest.TestCase):

    def setUp(self):
        self.solar_l1 = OutTestPin("solar_l1", 17, GPIO.OUT, GPIO.LOW)
        self.solar_n = OutTestPin("solar_n", 18, GPIO.OUT, GPIO.LOW)
        self.haus_l1 = OutTestPin("haus_l1", 22, GPIO.OUT, GPIO.LOW)
        self.haus_n = OutTestPin("haus_n", 23, GPIO.OUT, GPIO.LOW)
        self.solar_pins = StromPins(self.solar_n, self.solar_l1)
        self.haus_pins = StromPins(self.haus_n, self.haus_l1)
        self.optokoppler = InTestPin("optokoppler", 24, GPIO.IN)
        self.optokoppler.simuliere_optokoppler_signal(HAUSSTROM)

    def reset_test_objekte(self):
        self.solar_pins.ausschalten()
        self.solar_pins.ausschalten()
        self.optokoppler.simuliere_optokoppler_signal(HAUSSTROM)

    def test_schnellstart_funktioniert(self):
        wechsel_zu_solar_strom_wartezeit_in_sec = 1000
        strom_steuerung = StromSteuerung(self.solar_pins, self.haus_pins, self.optokoppler,
                                         wechsel_zu_solar_strom_wartezeit_in_sec)

        self.optokoppler.simuliere_optokoppler_signal(SOLARSTROM)
        strom_steuerung.start()
        # race condition due to sleeps in logik :(
        sleep(3)
        self.assertTrue(self.solarstrom_ist_angeschalten())
        strom_steuerung.stop()
        self.reset_test_objekte()

    def test_hausstrom_zu_solar_funktioniert(self):
        wechsel_zu_solar_strom_wartezeit_in_sec = 1
        self.haus_pins.anschalten()
        strom_steuerung = StromSteuerung(self.solar_pins, self.haus_pins, self.optokoppler,
                                         wechsel_zu_solar_strom_wartezeit_in_sec)
        strom_steuerung.start()
        sleep(3)
        self.optokoppler.simuliere_optokoppler_signal(SOLARSTROM)
        sleep(3)
        self.assertTrue(self.solarstrom_ist_angeschalten())
        strom_steuerung.stop()
        self.reset_test_objekte()

    def test_solar_zu_hausstrom_funktioniert(self):
        wechsel_zu_solar_strom_wartezeit_in_sec = 1000
        strom_steuerung = StromSteuerung(self.solar_pins, self.haus_pins, self.optokoppler,
                                         wechsel_zu_solar_strom_wartezeit_in_sec)

        self.optokoppler.simuliere_optokoppler_signal(SOLARSTROM)
        strom_steuerung.start()
        # race condition due to sleeps in logik :(
        sleep(3)
        self.assertTrue(self.solarstrom_ist_angeschalten())
        self.optokoppler.simuliere_optokoppler_signal(HAUSSTROM)
        sleep(3)
        self.assertTrue(self.hausstrom_ist_angeschalten())
        strom_steuerung.stop()
        self.reset_test_objekte()

    def solarstrom_ist_angeschalten(self):
        return self.solar_n.wert == 1 and self.solar_l1.wert == 1 and self.haus_n.wert == 0 and self.haus_l1.wert == 0

    def hausstrom_ist_angeschalten(self):
        return self.solar_n.wert == 0 and self.solar_l1.wert == 0 and self.haus_n.wert == 1 and self.haus_l1.wert == 1


if __name__ == '__main__':
    unittest.main()
