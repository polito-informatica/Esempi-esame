# Gestione stazioni meteo

#### (Esame proposto il 13-14/02/2023)

Il centro meteorologico piemontese vi chiede di realizzare un software per la gestione dei dati delle stazioni meteorologiche. Il programma riceve in input un file di testo che contiene i dati di una stazione meteorologica e restituisce una serie di informazioni statistiche sulle condizioni meteo registrate.

Il file contiene un record per ogni riga ed i campi sono separati da `;` e da 
considerarsi come valori float.

La prima riga del file contiene i nomi delle variabili meteorologiche misurate 
dalla stazione meteo. Il numero ed i nomi delle variabili <u>non sono noti a priori</u>: 
l'unica colonna nota è la prima contenente data e ora della misurazione. La lunghezza massima di ogni variabile è 25 caratteri.

Il centro vuole un programma Python che prenda in input il nome del file da
elaborare e restituisca per ogni variabile misurata il valore massimo, minimo, 
medio e la moda della serie temporale di ogni giornata presente nel file. 
Si ricorda che la moda è il valore che si ripete più volte all'interno di una 
serie di valori. Se più valori si ripetono lo stesso numero massimo di volte, 
se ne stampi uno a piacere.

### Esempi di file di input:

#### `Torino.csv`

    Data;Temp;Rugiada;Pressione;Umidita'
    01-01-17 00:00;4.6;2.1;1028;84
    01-01-17 00:14;4.6;2.1;1027.7;84
    01-01-17 00:29;4.6;2.1;1027.7;84
    01-01-17 00:44;4.5;2.1;1027.7;84
    01-01-17 01:00;4.5;2.2;1027.7;85
    ...
    03-01-17 22:29;1.9;1.1;1008;94
    03-01-17 22:44;1.9;1.1;1007.3;94
    03-01-17 22:59;1.9;1.1;1007;94
    03-01-17 23:14;1.9;1.1;1007;94
    03-01-17 23:29;1.9;1.1;1006.7;94
    03-01-17 23:44;2.1;1.2;1006.7;94
    03-01-17 23:59;2.1;1.2;1006.3;94

#### `Pinerolo.csv`

    Data;Pressione;DirVento;VelVento;Umidita';Pioggia;Radiazione
    01-06-17 00:29;1013.8;306;1.6;90;0;0
    01-06-17 00:59;1013.8;0;0;90;0;0
    01-06-17 01:29;1013.8;0;0;90;0;0
    01-06-17 01:59;1013.4;0;0;90;0;0
    01-06-17 02:29;1013.4;0;0;90;0;0
    01-06-17 02:59;1013.4;0;0;91;0;0
    01-06-17 03:29;1013.4;42;1.6;90;0;0
    01-06-17 03:59;1013.1;349;1.6;90;0;0
    01-06-17 04:14;1013.1;337;1.6;90;0;0
    ...
    04-06-17 21:44;1013.1;106;1.6;92;0;0
    04-06-17 21:59;1013.1;0;0;92;0;0
    04-06-17 22:14;1013.4;0;0;92;0;0
    04-06-17 22:29;1013.4;253;3.2;92;0;0
    04-06-17 22:44;1013.8;252;1.6;92;0;0
    04-06-17 22:59;1013.8;261;1.6;92;0;0
    04-06-17 23:14;1013.8;269;3.2;92;0;0
    04-06-17 23:29;1013.8;260;1.6;92;0;0
    04-06-17 23:44;1013.8;245;1.6;91;0;0
    04-06-17 23:59;1014.1;245;0;91;0;0

#### Esempi di output:

    Report meteorologico per la stazione di Torino
                 Temp     Rugiada  Pressione   Umidita' 
    01-01-17
       media     4.62     2.11     1026.59     83.82
     massimo     5.60     2.80     1028.00     88.00
      minimo     3.60     1.70     1024.60     79.00
        moda     5.20     2.50     1024.60     88.00
    02-01-17
       media     3.49     1.92     1019.11     89.52
     massimo     4.70     2.40     1024.60     93.00
      minimo     2.60     1.40     1012.80     82.00
        moda     3.40     1.40     1023.90     93.00
    03-01-17
       media     2.28     1.34     1010.31     93.43
     massimo     2.90     1.90     1012.80     94.00
      minimo     1.80     0.80     1006.30     93.00
        moda     1.80     0.80     1011.10     94.00

    Report meteorologico per la stazione di Pinerolo
                 Pressione   DirVento   VelVento Umidita'  Pioggia  Radiazione 
    01-06-17
       media     1012.83     171.30     3.08     73.50     0.00     311.38
     massimo     1013.80     349.00     8.00     91.00     0.00     1294.00
      minimo     1011.40     0.00       0.00     56.00     0.00     0.00
        moda     1011.40     119.00     8.00     91.00     0.00     633.00
    02-06-17
       media     1010.86     170.82     1.82     78.13     0.13     131.81
     massimo     1012.80     355.00     4.80     87.00     2.80     561.00
      minimo     1009.40     0.00       0.00     68.00     0.00     0.00
        moda     1009.40     253.00     4.80     87.00     1.80     371.00
    03-06-17
       media     1010.54     182.77     1.65     79.32     0.32     178.25
     massimo     1011.40     353.00     6.40     93.00     7.60     1034.00
      minimo     1009.00     0.00       0.00     57.00     0.00     0.00
        moda     1009.00     122.00     6.40     93.00     7.60     127.00
    04-06-17
       media     1011.95     161.22     2.64     85.99     0.57     145.10
     massimo     1014.10     347.00     9.70     93.00     13.50    1320.00
      minimo     1010.70     0.00       0.00     69.00     0.00     0.00
        moda     1014.10     253.00     9.70     93.00     13.50    118.00
