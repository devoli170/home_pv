#!/bin/bash

HIGH=0
LOW=1

haus_l1_pin=22
haus_n_pin=23
haus_l1=$LOW
haus_n=$LOW

solar_l1_pin=17
solar_n_pin=18
solar_l1=$LOW
solar_n=$LOW

setze_out_pins() {
  gpio -g write $haus_l1_pin $haus_l1
  gpio -g write $haus_n_pin $haus_n
  gpio -g write $solar_l1_pin $solar_l1
  gpio -g write $solar_n_pin $solar_n
}

hausstrom_aus() {
  echo "hausstrom aus"
  haus_l1=$LOW
  haus_n=$LOW
  setze_out_pins
  sleep 2
}

solarstrom_aus() {
  echo "solarstrom aus"
  solar_l1=$LOW
  solar_n=$LOW
  setze_out_pins
  sleep 2
}

hausstrom_an() {
  if (( $haus_l1 != $HIGH && $haus_n != $HIGH))
  then
    solarstrom_aus
    echo "hausstrom an"
    haus_l1=$HIGH
    haus_n=$HIGH
    setze_out_pins
  else
    echo "hausstrom ist an"
  fi
}

solarstrom_an() {
  if (( $solar_l1 != $HIGH && $solar_n != $HIGH))
  then
    echo $(date)
    echo "warte 10 minuten bis solarstrom an"
    sleep 600
    echo $(date)
    hausstrom_aus
    echo "solarstrom  an"
    solar_l1=$HIGH
    solar_n=$HIGH
    setze_out_pins
  else
    echo "solarstrom ist an"
  fi
}

solar_schnell_start() {
  hausstrom_aus
  echo "solarstrom  an"
  solar_l1=$HIGH
  solar_n=$HIGH
  setze_out_pins
}

init() {
  echo "starte init"
  # wenn outpins = 1, dann kein strom (alle relays aus)
  gpio -g mode $solar_l1_pin out
  gpio -g mode $solar_n_pin out
  gpio -g mode $haus_l1_pin out
  gpio -g mode $haus_n_pin out
  gpio -g mode 24 in

  haus_l1=$LOW
  haus_n=$LOW
  solar_l1=$LOW
  solar_n=$LOW
  setze_out_pins
  sleep 2

  solarstrom=$(gpio -g read 24)
  if (( $solarstrom == 1 ))
  then
    solar_schnell_start      # TODO code smell entfernen. andere solar_an re-usen, if aus an_ funktion raus ziehen
  fi
  echo "init fertig"
}

init

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