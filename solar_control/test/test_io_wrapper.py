from solar_control.io_wrapper import GPIO

import unittest


class Test_IO_Wrapper(unittest.TestCase):

    def test_laeuft_auf_raspi(self):
        try:
            GPIO.laeuft_auf_raspi()
        except Exception:
            self.fail("GPIO.laeuft_auf_raspi() raised an Exception")

    def test_gpio_wrapper_smoke_test(self):
        try:
            GPIO.setup(1,1)
            GPIO.input(1)
            GPIO.output(1,1)
        except Exception:
            self.fail("Exception in wrapper function")

        self.assertEqual(GPIO.HIGH, 1)
        self.assertEqual(GPIO.LOW, 0)
        self.assertEqual(GPIO.IN, 1)
        self.assertEqual(GPIO.OUT, 0)
