from time import sleep
import threading
import logging.config
import pathlib

p = pathlib.Path(__file__)
package_root = p.parent.absolute().parent.absolute()
logging.config.fileConfig('{}/conf/logging.conf'.format(package_root), disable_existing_loggers=False)
logger = logging.getLogger("Steuerungslogik")

SOLARSTROM = 1
HAUSSTROM = 0


class StromSteuerung(threading.Thread):
    def __init__(self, solar_pins, haus_pins, input_pin, solar_wechsel_wartezeit):
        super(StromSteuerung, self).__init__()
        self._stop_event = threading.Event()
        self.boot = True
        self.solar_pins = solar_pins
        self.haus_pins = haus_pins
        self.input_pin = input_pin
        self.solar_wartezeit = solar_wechsel_wartezeit
        self.aktiver_strom = None

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        logger.info("Thread gestartet")
        while not self.stopped():
            aktuelles_signal = self.input_pin.lese_pin_wert()
            if self.boot:
                if aktuelles_signal == SOLARSTROM:
                    logger.info("Solarstrom bei Start des Programms. Überspringe Wartezeit und schalte auf Solarstrom")
                    self._schalte_relais_je_nach_optokoppler_signal(aktuelles_signal, warten=False)
                self.boot = False
                continue

            if aktuelles_signal != self.aktiver_strom:
                logger.info("Änderung erkannt...")
                self._schalte_relais_je_nach_optokoppler_signal(aktuelles_signal)
        self._clean_up()

    def _schalte_relais_je_nach_optokoppler_signal(self, aktuelles_signal, warten=True):
        if aktuelles_signal == HAUSSTROM:
            logger.info("Schalte von Solarstrom zu Hausstrom")
            self.solar_pins.ausschalten()
            sleep(1)
            self.haus_pins.anschalten()
            sleep(1)
            self.aktiver_strom = HAUSSTROM

        if aktuelles_signal == SOLARSTROM:
            logger.info("Schalte von Hausstrom zu Solarstrom nach {} Sekunden".format(self.solar_wartezeit))
            if warten:
                sleep(self.solar_wartezeit)
            self.haus_pins.ausschalten()
            sleep(1)
            self.solar_pins.anschalten()
            sleep(1)
            self.aktiver_strom = SOLARSTROM

    def _clean_up(self):
        logger.info("Thread beendet sauber")
