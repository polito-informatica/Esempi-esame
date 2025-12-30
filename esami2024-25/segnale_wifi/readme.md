# Monitoraggio Segnale Wi-Fi

#### (Esame proposto il 20/06/2025)

 
All’interno di un grande centro commerciale, sono stati installati una serie di rilevatori del segnale Wi-Fi. Questi dispositivi misurano periodicamente l’intensità del segnale (potenza, in dBm) nelle varie aree dell’edificio e inviano i dati a un sistema centrale.

Il sistema elabora i dati e produce un file (`segnale.txt`) contenente una mappa 2D (vista dall’alto) dei livelli di segnale in un determinato momento. Poiché l’edificio ha una forma irregolare, la mappa è una griglia di dimensione RxC, in cui il carattere `-` indica le zone non monitorate.

Un secondo file (`zone.txt`) riporta, per ciascuna posizione della griglia, una lettera che identifica la zona del centro commerciale (come negozi, corridoi, aree ristoro ecc.), oppure - se la posizione non è monitorata. I due file hanno la stessa dimensione.

### Obiettivi

Scrivere un programma Python che:

1. Stampi una **tabella, ordinata alfabeticamente per codice zona**, che riporti, per ciascuna zona, il livello di segnale **minimo, massimo e medio** rilevato. La tabella deve essere stampata con i valori allineati e le intensità espresse con una cifra decimale.

2. Stampi **l'escursione di segnale**, calcolata come differenza tra il valore massimo e minimo dell’intero edificio. Il valore va stampato con una sola cifra decimale

#### Esempio di contenuto del file `segnale.txt`

```
-    -    -56.0 -55.5 -50.2 -49.9 -49.8
-56.1 -56.0 -55.8 -55.2 -50.1 -49.8 -49.5
-56.2 -56.2 -55.7 -55.1 -50.0 -49.7 -49.4
-56.4 -56.3 -55.5 -55.0 -50.0 -49.6 -49.3
-60.0 -59.8 -55.0 -54.9 -54.8 -60.0 -59.9
-60.2 -60.1 -54.8 -54.7 -54.6 -60.2 -60.1
-60.5 -60.4 -60.3 - - - -
-60.6 -60.5 -60.4 - - - -
````

#### Esempio di contenuto del file `zone.txt`

```
- - A A B B B
A A A A B B B
A A A A B B B
A A C C C B B
D D C C C E E
D D C C C E E
D D D - - - -
D D D - - - -
````

#### Output atteso

```
Zona  S.Min  S.Max  S.Medio
A     -56.4  -55.1  -55.9
B     -50.2  -49.3  -49.8
C     -55.5  -54.6  -55.0
D     -60.6  -60.0  -60.3
E     -60.2  -59.9  -60.1

Escursione di segnale: 11.3 dBm
````

### Note

- Non sono note a priori le dimensioni RxC della tabella.
- Il simbolo `-` rappresenta celle non monitorate e va ignorato nei calcoli. Le celle contenenti `-` sono le stesse nei due file.
- Il segnale Wi-Fi è espresso in dBm (i valori sono sempre negativi, un valore più vicino a 0 indica segnale più forte).
- Tutti i valori devono essere stampati con **una cifra decimale**.
- Le colonne devono essere **allineate** per facilitare la lettura.