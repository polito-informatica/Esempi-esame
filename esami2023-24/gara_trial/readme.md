# Calcolo delle statistiche di una gara di Trial

#### (Esame proposto il 05-06/02/2024)

Si scriva un programma Python in grado di calcolare alcune statistiche di una gara di Trial motociclistico. Nel trial si devono superare un numero fisso di prove (N) e ad ogni prova sono associate le penalità assegnate al concorrente, che corrispondono al numero di volte in cui appoggia per terra i piedi. Ci sono due file di in input.

Il primo (`penalita.txt`) ha il seguente formato

    pettorale:penalità1:penalità2:penalità3 ... :penalitàN

Dove tutti i campi sono separati dal carattere `":"` (e.g.: `1:0:1:0:4:3:5`). Tutti i partecipanti affrontano lo stesso numero di prove (N, dove il valore di N non è noto a priori, ma dipende da quanti valori sono scritti nel file per ogni partecipante).

Esiste un secondo file di input (`partecipanti.txt`) che associa i numeri di pettorale con i nomi dei concorrenti. Ad esempio:

    1:Mario Rossi

Il programma deve generare in output le seguenti informazioni:

1. ***Classifica della gara***
    - Il programma deve stampare l'ordine di arrivo, dal primo all'ultimo, considerando che vince il concorrente con meno penalità totali.
    - In caso di pari numero di penalità, i partecipanti possono essere stampati in un ordine qualsiasi
    - L'output deve essere formattato come da esempio
5. ***Calcolo della migliore sequenza di prove***
    - Il programma deve stampare il nome del corridore che ha fatto la sequenza più lunga di prove con zero penalità
    - In caso due o più corridori abbiano la stessa sequenza più lunga se ne stampi uno qualunque tra questi

## Esempio di input penalita.txt:

    1:1:2:0:0:1:5
    2:0:2:0:3:1:4
    3:2:2:2:0:1:1
    4:2:0:0:0:0:5
    5:0:3:3:0:1:2
    6:1:1:1:0:1:3

## Esempio di input partecipanti.txt:

    1:Mario Rossi
    2:Luca Verdi
    3:Giovanni Parisi
    4:Matteo Blangino
    5:Andrea Nardi
    6:Vincenzo Spada

## Output generato dal programma:

    Classifica: 
    Matteo Blangino   7 penalità
    Vincenzo Spada    7 penalità
    Giovanni Parisi   8 penalità
    Mario Rossi       9 penalità
    Andrea Nardi      9 penalità
    Luca Verdi       10 penalità

    Ha realizzato la più lunga sequenza Matteo Blangino con 4 prove consecutive superate senza errori
