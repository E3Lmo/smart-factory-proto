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

## Usage

