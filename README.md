# Home Pv
WORK IN PROGRESS.

Dieses Repo enthält die Relais-Steuerungs Logik für das Garten PV Projekt.  
Umsetzung in Phyton als systemd service für Raspbian

## Garten PV Projekt
- Wechsel zwischen Haus und Pv strom im Garten Kreis
- Elektrotechnik und Hardware nicht Teil dieses Repos 

## Repo Struktur
```
├───.idea                                    # Intellij Projekt Metadaten
├───aruido                                   # Arduino Spielerei mit webserver und Prometheus exporter
│   └─── ...
├───debian_resources                         # Statische dateien die mit in die .deb packetiert werden
│   └─── ...
├───solar_control                            # Eigentliches Python Paackage mit allen Modules für die Schaltung
│   └─── ...
├───solar_initial_bash_service(deprecated)   # Ursprüngliche Versionen des Bash Skriptes
│   └─── ... 
│
└───solar_initial_bash_service              


```
# Software Life Cycle:
`<...>` wird als Platzhalter verwenden. 

1. Feature Branch anlegen. Branch mit feature/ prefixes, damit die Info im Release landet. Entweder...
   1. per UI
   1. per Konsole mit: ``git checkout -b "feature/<branch_name>"``
2. Code & Unit Tests schreiben.
   1. Wenn Tests erfolgreich waren ein git commit erstellen. Entweder...
      1. per UI
      1. per Konsole ``git commit -am "<commit_message>"``   
3. Wenn Feature fertig ist Pull Request(PR) an main branch erstellen.
   - per github.com Web UI
4. Wenn PR gemerged ist, kann ein automatischer release erstellt werden durch:
   - ``git checkout main``  
   - ``git pull``          # da die änderungen per web UI auf den main branch gelandet sind
   - ``git tag vx.y.z``    
     - einfach Patch version +1 seit letztem release.  
     - [Idealer weise per Semantic Versioning](https://semver.org/)
     - das führende v ist wichtig, da die github action sonst nicht startet.
   - ``git push origin vx.y.z``
   - ca. 2 min warten bis release mit .deb package bereit ist
   
    
## Build Guide
Python wird z.Z nicht kompiliert. Interpreter ist 'gut genug'. Hier kann noch viel optimiert werden.  
Alle Module werden als .py dateien im .deb mitgeliefert.
RPi.GPIO wird im moment automatisch zur Laufzeit per pip installiert.  
Der .deb Build ist zur Zeit nur bei Release automatisiert.  


## Install und Upgrade Guide
- ``wget https://github.com/devoli170/home_pv/releases/download/vx.y.z/solar_vx.y.z_armhf.deb``
- z.B. ``wget https://github.com/devoli170/home_pv/releases/download/v0.1.14/solar_v0.1.14_armhf.deb``
   - Achtung das 'v' ist im pfad "v0.1.14", aber nicht mehr im datei namen: "solar_0.1.14_armhf.deb"
- Am besten mit apt installieren um das pip Packet zusätzlich zu installieren:  
  ``sudo apt install ./solar_x.y.z_armhf.deb``