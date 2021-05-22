from time import sleep
from datetime import datetime

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this "
          "by using 'sudo' to run your script")


class OutPin:
    modus = ""
    name = ""
    nummer = None
    wert = None

    def __init__(self, name, nummer, modus, wert):
        self.name = name
        self.nummer = nummer
        self.modus = modus
        self.wert = wert


HIGH = GPIO.LOW
LOW = GPIO.HIGH
solar_l1 = OutPin("solar_l1", 17, "out", LOW)
solar_n = OutPin("solar_n", 18, "out", LOW)
haus_l1 = OutPin("haus_l1", 22, "out", LOW)
haus_n = OutPin("haus_n", 23, "out", LOW)
out_pins = [solar_l1, solar_n, haus_l1, haus_n]
optokoppler = 24
input_pins = [optokoppler]


def init():
    print("starte init")
    for pin in out_pins:
        GPIO.setup(pin.nummer, GPIO.OUT)
    GPIO.setup(input_pins, GPIO.IN)
    schreibe_wert_auf_pin()
    sleep(2)
    solarstrom = GPIO.input(optokoppler)
    if solarstrom == GPIO.HIGH:
        schnell_start()
    print("init fertig")


def schnell_start():
    print("schalte hausstrom aus")
    hausstrom_aus()
    print("schalte solarstrom an")
    solar_l1.wert = HIGH
    solar_n.wert = HIGH
    schreibe_wert_auf_pin()


def hausstrom_aus():
    print("schalte hausstrom aus")
    haus_l1.wert = LOW
    haus_n.wert = LOW
    schreibe_wert_auf_pin()
    sleep(2)


def solarstrom_aus():
    print("solarstrom aus")
    solar_l1.wert = LOW
    solar_n.wert = LOW
    schreibe_wert_auf_pin()
    sleep(2)


def hausstrom_an():
    if haus_l1.wert != HIGH and haus_n.wert != HIGH:
        solarstrom_aus()
        print("schalte hausstrom an")
        haus_l1.wert = HIGH
        haus_n.wert = HIGH
        schreibe_wert_auf_pin()
    else:
        print("hausstrom ist an")


'''
def solarstrom_an():

    if solar_l1.wert != HIGH and solar_n.wert != HIGH:
        print(datetime.now())
        print("warte 10 minuten bis solarstrom angeschaltet wird")
        sleep(600)
        print(datetime.now())
        hausstrom_aus()
        print("schalte solarstrom an")
        solar_l1 = HIGH
        solar_n = HIGH
        schreibe_wert_auf_pin()
    else:
        print("solarstrom ist an")
'''


def schreibe_wert_auf_pin():
    for pin in out_pins:
        GPIO.output(pin.nummer, pin.wert)


def main():
    init()
    '''
    while true;
do
  solarstrom=$(gpio -g read 24)
  if (( $solarstrom == 1 ))
  then
    solarstrom_an
    sleep 1
  else
    hausstrom_an
    sleep 1
  fi;
done
'''


def beep():
    return "bleep"


if __name__ == "__main__":
    main()
