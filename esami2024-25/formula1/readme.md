# Formula 1

#### (Esame proposto il 10/09/2025)

Si vuole realizzare un programma Python per estrarre delle statistiche da un file che riporta i dati riguardanti la stagione 2024 di Formula 1. Il file in questione si chiama "`Formula1_2024season_raceResults.csv`" ed è scaricabile dal sito: https://github.com/toUpperCase78/formula1-datasets/blob/master/.

La prima riga riporta le etichette dei vari campi, separati da `","`, che rappresentano, uno per riga, le statistiche di tutti i piloti nelle varie gare:

#### Alcune righe del file "`Formula1_2024season_raceResults.csv`"

```
Track,Position,No,Driver,Team,Starting Grid,Laps,Time/Retired,Points,Set Fastest Lap,Fastest Lap Time
Bahrain,1,1,Max Verstappen,Red Bull Racing Honda RBPT,1,57,1:31:44.742,26,Yes,1:32.608
Bahrain,2,11,Sergio Perez,Red Bull Racing Honda RBPT,5,57,+22.457,18,No,1:34.364
Bahrain,3,55,Carlos Sainz,Ferrari,4,57,+25.110,15,No,1:34.507
Bahrain,4,16,Charles Leclerc,Ferrari,2,57,+39.669,12,No,1:34.090
Bahrain,5,63,George Russell,Mercedes,3,57,+46.788,10,No,1:35.065
Bahrain,6,4,Lando Norris,McLaren Mercedes,7,57,+48.458,8,No,1:34.476
Bahrain,7,44,Lewis Hamilton,Mercedes,9,57,+50.324,6,No,1:34.722
Bahrain,8,81,Oscar Piastri,McLaren Mercedes,8,57,+56.082,4,No,1:34.983
Bahrain,9,14,Fernando Alonso,Aston Martin Aramco Mercedes,6,57,+74.887,2,No,1:34.199
...
````

Il programma deve permettere all'utente di:

1) determinare il pilota che per più volte nella stagione ha ottenuto il giro veloce in gara. Il giro veloce è indicato da Yes nella colonna Set Fastest Lap;

2) determinare la scuderia (team) che per più volte nella stagione ha visto le sue macchine non completare le gare. Il valore indicante il ritiro è DNF nella colonna Time/Retired.

Si supponga che il pilota che ha ottenuto più giri veloci sia unico (non ci sono pari meriti). Allo stesso modo, la squadra che ha avuto più ritiri è unica.

### Esecuzione

```
Il maggior numero di giri veloci è 6, ottenuto da: Lando Norris

Il maggior numero di ririti è 11, ottenuto da: Williams Mercedes
```