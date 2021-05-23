# Home Pv
Dieses Repo enthält die Relais-Steuerungs Logik für das Garten PV Projekt.  
Umsetzung in Phyton als systemd service für Raspbian

## Garten PV Projekt
- Wechsel zwischen Haus und Pv strom im Garten Kreis
- Elektrotechnik und Hardware nicht Teil dieses Repos 

## Repo Struktur
```
├───.idea                                   # Intellij Projekt Metadaten
└───solar_initial_bash_service              # Ursprüngliche Versionen des Bash Skriptes
    ├───...

```
# Software Life Cycle:
`<...>` wird als Platzhalter verwenden. 

1. Feature Branch anlegen. Entweder...
   1. per UI
   1. per Konsole mit: ``git checkout -b "<feature_branch_name>"``
2. Code & Unit Tests schreiben.
   1. Wenn Tests erfolgreich waren ein git commit erstellen. Entweder...
      1. per UI
      1. per Konsole ``git commit -am "<commit_message>"``   
3. Wenn Feature fertig ist mit Main-Branch mergen. Entweder...
   1. per UI
   1. per Konsole mit: ``git checkout main && git merge <feature_branch_name>"``
4. Von Main-Branch .deb file bauen  
   [.deb packaging intro](https://wiki.debian.org/Packaging/Intro?action=show&redirect=IntroDebianPackaging)  
   [How To Package for Debian](https://wiki.debian.org/HowToPackageForDebian)
5. Git release erstellen und .deb file bereitstellen
6. .deb file auf raspberry Pi downloaden und upgraden:  
   ``dpkg --install <TODO>.deb``

## Coding Guide

 
## Build Guide
Da Python eine Interpreter Sprache ist, ist kein Build von Bytecode nötig. Jedoch wird die Logik als Systemd Service deployed, weshalb einige kopier Operationen nötig sind. Um dies sauberer umzusetzen sollte ein .deb Paket gebaut werden und hier in diesem Repo als Download zur Verfügung gestellt werden

A program that specifies python3 as its interpreter may require its own private Python modules. These modules should be installed in /usr/share/module, or /usr/lib/module if the modules are architecture-dependent (e.g. extensions).
https://www.debian.org/doc/packaging-manuals/python-policy/#programs-shipping-private-modules

## Release Guide


## Install und Upgrade Guide