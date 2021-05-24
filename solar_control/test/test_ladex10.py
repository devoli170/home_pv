import unittest
from solar_control.main_module import ladex10


class TestPin(unittest.TestCase):

    def test_one_is_one(self):
        self.assertEqual(1, 1)

    def test_beep(self):
        self.assertEqual(ladex10.beep(), "beep")


if __name__ == '__main__':
    unittest.main()
