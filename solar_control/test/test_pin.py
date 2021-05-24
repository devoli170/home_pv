import unittest
from solar_control.main_module.Pin import InPin, OutPin


class TestPin(unittest.TestCase):

    def test_instanciating_out_pin_works(self):
        testName="foo"
        testNummer=23
        testModus=1
        testWert=1
        testPin = OutPin(testName, testNummer, testModus, testWert)

        self.assertEqual(testPin.name, testName)
        self.assertEqual(testPin.nummer, testNummer)
        self.assertEqual(testPin.modus, testModus)
        self.assertEqual(testPin.wert, testWert)

    def test_instanciating_in_pin_works(self):
        testName="foo"
        testNummer=23
        testModus=0
        testPin = InPin(testName, testNummer, testModus)

        self.assertEqual(testPin.name, testName)
        self.assertEqual(testPin.nummer, testNummer)
        self.assertEqual(testPin.modus, testModus)


if __name__ == '__main__':
    unittest.main()