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

init() {
  echo "$(date) starte init"
  # wenn outpins = 1, dann kein strom (alle relays aus)
  gpio -g mode $solar_l1_pin out
  gpio -g mode $solar_n_pin out
  gpio -g mode $haus_l1_pin out
  gpio -g mode $haus_n_pin out
  gpio -g mode 24 in
}

init

while true;
do
    echo "$(date) hi"
    sleep 10
done
