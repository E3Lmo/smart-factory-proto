# smart-factory-proto
In Zusammenarbeit mit dem Kompetenzzentrum [Data Science & Business Analytics](https://www.hs-neu-ulm.de/forschung/institute-kompetenzzentren-netzwerke/data-science-and-business-analytics/) an der Hochschule Neu-Ulm, ist eine erste prototypische Umsetzung einer smart Factory Produktionsstraße gelungen. Der daraus resultierende Source Code für das System ist in diesem Repository abgelegt und dokumentiert. Desweiteren wird der aktuelle Stand der Entwicklung beschrieben und eventuelle Ansätze für die Weiterentwicklung gegeben.

## Genutze Technologie und Programmiersprache

### Python 2

### Raspberry Py 3 mit Raspbian

### RFID Reader Modul MFRC522

### RFID Tag (Mifare Standard Chip)


## RFID Chips Sektorbelegung

In der nachfolgenden Tabelle ist die aktuelle Belgung der Sektoren in einem RFID Tag abgebildet. In Sektor 1 sind die jeweiligen Artikelnummer des zu fertigenden Produkts abgespeichert. In Sektor 2 ist es vorstellbar eine einmalige ID zu definieren, um das Produkt beim Auslesen des RFID Tags mit seiner genauen Bezeichnung zu bestimmen. Da wie bereits schon erwähnt nur Integer Werte in die Sektoren abspeicherbar sind, müsste man hier also mit Metadaten (Verlinkung zur Datenbank) arbeiten. Im Sektor 3 ist ein Status definerit, welcher sicherstellt, das der Produktionsprozessablauf auch eingehalten wird. In Sektor 4 wird die Durchlaufzeit abgespeichert, beginnend bei 0 wird an jeder durchlaufenen Fertigungsmaschine die Fertigungszeit aufsummiert.

| Sektor | Daten         | blau | rot | lila | gelb |
|-------:|---------------|:----:|:---:|:----:|:----:|
|      1 | Artikelnummer |  11  |  22 |  33  |  44  |
|      2 | Bezeichnung   |   1  |  2  |   3  |   4  |
|      3 | Status        |  0-5 | 0-5 |  0-5 |  0-5 |
|      4 | Durchlaufzeit |  Int | Int |  Int |  Int |
|      5 |               |      |     |      |      |
|      6 |               |      |     |      |      |
|      7 |               |      |     |      |      |
|      8 |               |      |     |      |      |
|      9 |               |      |     |      |      |
|     10 |               |      |     |      |      |
|     11 |               |      |     |      |      |
|     12 |               |      |     |      |      |
|     13 |               |      |     |      |      |
|     14 |               |      |     |      |      |
|     15 |               |      |     |      |      |
|     16 |               |      |     |      |      |


## Vorbereitung

Raspberry Pi mit den RFID Modulen verkabeln. Bei Maschine 1 bietet sich aktuell schon ein 7 Zoll Touch Display an, weil dort die GUI schon umgesetzt ist. Allerdings ist alles auch über einen normalen Bildschirm aber dann mit Maus und Tastatur möglich.

1. Verkablen der RasPi mit den RFID Modulen

Dafür benötigt wird:

* Raspberry Pi
* Mifare RC522 RFID Modul
* Female -Female Jumper Kabel

Im folgenden Bild nun die Verkabelung.

![Verkabelung RaspBerry Pi mit MFRC522](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-RFID-RC522-NFC_Steckplatine-600x391.png)

2. Installation des Moduls

Für die Installation des Moduls benötigen wir nun ein Terminal. In diesme tippen wir den Befehl:

`sudo nano /boot/config.txt`

Am Ende der geöffneten Datei müssen nun folgende zwei Zeilen hinzugefügt werden:

```
device_tree_param=spi=on
dtoverlay=spi-bcm2708
```

Speichern und Beenden.
Anschließend muss die SPI Schnittstelle noch aktivirt werden. Dazu tippen wir im Terminal den Befehel `sudo raspi-config` ein. 
Im nun geöffneten Config Menü navigieren wir in Advanced Options $\to$ SPI und setzen die Schnittstelle dort auf aktiv. Danach muss der Raspberry Pi neu gestartet werden.

Nach dem Neustart können wir die Aktivierung über `dmesg | grep spi` überprüfen. 

```
pi@raspberrypi:~ $ dmesg | grep spi
[   10.784368] bcm2708_spi 20204000.spi: master is unqueued, this is deprecated
[   10.813403] bcm2708_spi 20204000.spi: SPI Controller at 0x20204000 (irq 80)
```

Wenn dann der Output so ähnlich wie oben dargestellt aussieht, ist alles in Ordnung.

Für die SPI Schnittstelle müssen nun noch ein paar Pakete installiert werden.

`sudo apt-get install git python-dev --yes`

Anschließen klonen wir das Python SPI Modul von GitHub und installieren es:

```
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
sudo python setup.py install
cd ..
```

> Die vorbereitende Installation des RFID Moduls ist nun abgeschlossen. Unter Installation der Maschine(n) gehen wir nun zum Projektspezifischen Setup über.

## Installation der Maschine(n)

Für die weitere Installation der Maschinen benötigen wir nun den entsprechenden Source Code auf den Raspberry Pi's. Dafür wechseln wir über `cd /Desktop` im Terminal auf den Desktop. Anschließend klonen wir nun dieses Projekt.

`git clone https://github.com/E3Lmo/smart-factory-proto.git`

Visuell sollte nun ein neuer Ordner auf dem Desktop erschienen sein. 

> Nach Abschluss des Clone-Vorgangs sind wir nun Ready-To-Use, beschrieben in Usage.

## Usage

Wenn wir uns nun weiter im Terminal befinden wählen wir nun den entsprechenden Ordner `cd` an und starten die Maschine. Im Folgenden sind die Schritte nun für jede Maschine (1-5) erklärt.

***Für Maschine 1***

1. `cd smart-factory-proto/maschine1`
2. `python main.py`

Jetzt ist die Maschine 1 gestartet und es müsste sich eine grafische Bedienoberfläche geöffnet haben. Wenn wir nun ein Produkt wählen, können wir den Chip mit den gewählten Daten beschreiben.

***Für Maschine 2***

1. `cd smart-factory-proto/maschine2`
2. `python main_maschine2.py`

***Für Maschine 3***

1. `cd smart-factory-proto/maschine3`
2. `python main_maschine3.py`

***Für Maschine 4***

1. `cd smart-factory-proto/maschine4`
2. `python main_maschine4.py`

***Für Maschine 5***

1. `cd smart-factory-proto/maschine5`
2. `python main_maschine5.py`

Für die Maschinen 2-5 wurden noch keine grafischen Benutzeroberflächen entwickelt. Deshalb öffnet sich beim starten der Python Softwarekomponente kein eigenes Fenster sondern wird im gestarteten Terminal ausgeführt. Sobald die jeweilige Maschine im Terminal läuft kann auch hier der Chip mit den, im Source Code konfigurierten Daten beschrieben werden.

*Falls die Anleitung an der ein oder anderen Stelle nciht weiterhilft, dann werde ich das auf Hinweis hin ausbessern. Also einfach bei mir melden.*
Bei weiteren Fragen stehe ich jederzeit zur Verfügung. Und nun viel Spaß beim coden und ausprobieren.
