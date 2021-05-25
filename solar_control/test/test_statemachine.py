import unittest
from solar_control.main_module.StromStateMachine import StromStateMachine

class TestStatemachine(unittest.TestCase):

    def test_schnellstart_funktioniert(self):
        testMachine = StromStateMachine()
if __name__ == '__main__':
    unittest.main()
