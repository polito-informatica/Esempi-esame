# Profilo di temperatura di un edificio

#### (Esame proposto il 19/09/2023)

All'interno di un edificio, sono stati installati una serie di sensori ambientali di temperatura, i quali periodicamente comunicano un valore di temperatura ad un sistema centrale. Il sistema interpola i dati provenienti dai sensori e produce un file (***temperature.txt***) con la mappa 2D (vista dall'alto) delle temperature presenti nell'edifico in un certo istante. Dato che l'area monitorata non è perfettamente rettangolare, la mappa è una griglia di valori di dimensione *RxC*, in cui il carattere '-' indica le zone escluse.

Un secondo file (***mappa.txt***) riporta, per ogni locazione della griglia, un **carattere** che identifica il **codice della stanza** a cui quella locazione appartiene, oppure il **carattere '-'** se quella locazione è esclusa. Notare che questo file è composto dallo stesso numero di locazioni del primo.

Scrivere un programma Python in grado di riportare: 

- la ***temperatura minima, massima e media*** (considerando tutte le locazioni di una certa stanza) rilevate ***in ogni stanza***. 

- il valore di ***escursione termica*** (pari alla differenza tra la massima e la minima temperatura) ***nell'intero edificio***.

La tabella prodotta deve essere ***ordinata alfabeticamente per codice di stanza*** e le informazioni devono essere incolonnate. Inoltre, tutte le temperature devono essere stampate con una sola cifra decimale.

## Esempio

### Contenuto del file temperature.txt

    -    -    19.0 19.1 20.5 20.4 20.2
    18.8 18.8 18.9 19.0 20.4 20.2 20.1
    18.7 18.7 18.7 18.9 20.2 20.1 20.0
    18.6 18.6 18.6 18.6 18.6 20.0 20.0
    20.8 20.8 18.5 18.5 18.5 17.8 17.8
    20.9 20.9 18.4 18.4 18.4 17.8 17.7
    21.0 20.9 20.9 -    -    -    -
    21.1 21.0 20.9 -    -    -    -

Nell'esempio, le prime due celle della prima riga sono delle locazioni escluse.

### Contenuto del file mappa.txt (per semplicità, ad ogni stanza è associata una lettera)


    - - A A E E E
    A A A A E E E
    A A A A E E E
    A A C C C E E
    B B C C C D D
    B B C C C D D
    B B B - - - -
    B B B - - - -

Nell'esempio, la terza cella della prima riga si riferisce alla stanza A ed ha una temperatura di 19 gradi (indicata nel primo file).

### Esempio di output

    Stanza T.Min T.Max T.Media
    A      18.6  19.1  18.8
    B      20.8  21.1  20.9
    C      18.4  18.6  18.5
    D      17.7  17.8  17.8
    E      20.0  20.5  20.2

    Escursione termica: 3.4 gradi
