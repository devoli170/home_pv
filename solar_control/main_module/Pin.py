from solar_control.io_wrapper import GPIO
import logging.config
import pathlib

p = pathlib.Path(__file__)
package_root = p.parent.absolute().parent.absolute()
logging.config.fileConfig('{}/conf/logging.conf'.format(package_root), disable_existing_loggers=False)
logger = logging.getLogger("Pin")


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
        logger.debug("Schreibe Wert: {} an Pin: {}-{}".format(self.nummer, self.name, self.wert))
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
        logger.debug(
            "Setze Pins ({}-{}, {}-{}) auf Wert: {}".format(self._n.name, self._n.nummer, self._l1.name, self._l1.nummer,
                                                            GPIO.LOW))
        self._n.wert = GPIO.LOW
        self._l1.wert = GPIO.LOW
        self.flush()

    def anschalten(self):
        logger.debug(
            "Setze Pins ({}-{}, {}-{}) auf Wert: {}".format(self._n.name, self._n.nummer, self._l1.name, self._l1.nummer,
                                                            GPIO.HIGH))
        self._n.wert = GPIO.HIGH
        self._l1.wert = GPIO.HIGH
        self.flush()

    def flush(self):
        self._l1.schreibe_wert_an_pin()
        self._n.schreibe_wert_an_pin()

    def lese_zustand(self):
        return GPIO.HIGH if self._n == GPIO.HIGH and self._l1 == GPIO.HIGH else GPIO.LOW
