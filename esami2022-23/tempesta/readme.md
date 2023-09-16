# Tempesta

#### (Esame proposto il 19/09/2023)

Una tremenda tempesta si muove da ovest a e est. I Guardatempesta hanno bisogno di un programma Python per prevedere l’evolversi della tempesta e i danni che causerà sul territorio.

La posizione iniziale della tempesta è salvata nel file **mappa.txt**, corrispondente ad una mappa cartesiana con coordinate (0, 0) in alto a sinistra. La mappa contiene dei numeri interi indicanti l'intensità iniziale della tempesta (1-9) oppure il simbolo '_' dove non si trovi la tempesta.

### Esempio del file mappa.txt:

    _22____
    1431___
    34_____

Innanzitutto si chiede di calcolare e stampare le coordinate e l'intensità dell'ombelico della tempesta nella sua configurazione iniziale, corrispondente all'incrocio della riga con la somma più alta di intensità e della colonna con la somma più alta (in caso di parità scegliere una riga o colonna a piacere).

Inoltre, la tempesta si sposta progressivamente a destra. Avanzando diminuisce la propria intensità. Ogni volta che il fronte della tempesta (le caselle più a destra) si spostano perdono una unità (a 0 spariscono assottigliando la tempesta.) Si assuma che la tempesta nella configurazione iniziale non possa toccare il bordo destro. Il programma deve stampare l’evoluzione della tempesta, fermandosi quando la tempesta è completamente uscita dalla mappa oppure si è esaurita.

### Output generato dal programma:

    Ombelico: riga 1, colonna 1, intensità 4

    _22____
    1431___
    34_____

    __21___
    _143___
    _33____

    ___2___
    __142__
    __32___

    ____1__
    ___141_
    ___31__

    _______
    ____14_
    ____3__

    _______
    _____13
    _____2_

    _______
    ______1
    ______1

