# Esempio esame "Potenze binomio"

Si scriva un programma in grado di calcolare la _potenza di un binomio_ del tipo "(ax + by)**N", dove "x" e "y" sono le
variabili indipendenti, "a" e "b" sono coefficienti reali, ed "N" è un intero positivo.

Il programma deve acquisire da un file denominato *potenze.txt* le seguenti informazioni:

- nella prima riga del file sono presenti i valori dei coefficienti "a" e "b", separati da uno spazio
- nelle righe successive sono riportati diversi valori di "N", uno per riga.

Per ciascun valore di "N" presente nel file, il programma stamperà l'espressione del polinomio potenza.

Per il calcolo dei coefficienti del polinomio potenza, costruire una funzione "tartaglia(N)" che calcoli e restituisce
il _triangolo di Tartaglia_ fino all'ordine "N", sotto forma di lista di liste:

    [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1], ... ]

## Esempio:

Supponiamo che il file *potenze.txt* abbia il seguente contenuto:

    1 -2
    3
    5

Il programma dovrà produrre in output il seguente testo:

    Potenze del binomio (1.0x + -2.0y)^N
    N = 3
    1.0 x^3 + -6.0 x^2 y + 12.0 x y^2 + -8.0 y^3 
    N = 5
    1.0 x^5 + -10.0 x^4 y + 40.0 x^3 y^2 + -80.0 x^2 y^3 + 80.0 x y^4 + -32.0 y^5 



