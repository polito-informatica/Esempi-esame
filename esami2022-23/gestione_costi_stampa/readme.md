# Gestione costi stampa

#### (Esame proposto il 30-31/01/2023)

Un editore di libri vi chiede di sviluppare un programma per gestire in maniera automatica la generazione dei costi di
stampa per i suoi clienti. Le informazioni utilizzate dal programma sono memorizzate in due file diversi. Nel primo
file, che si chiama **_costipagine.txt_**, sono elencati i costi delle pagine, uno per riga e caratterizzati dalle seguenti
informazioni, separate da punti e virgole:

    N_Pag_min;N_Pag_max;costo_singola_pagina

Dove `N_Pag_min` e `N_Pag_max` sono il numero di pagine (minimo e massimo) a cui si riferisce il `costo_singola_pagina` in
euro (il simbolo `€` è presente nel file).

Il software deve aprire un file (il cui nome è fornito dall'utente) che contiene l'elenco dei libri da quotare, uno per
riga, e caratterizzati dalle seguenti informazioni, separate da punto e virgola:

    Titolo;numero_pagine

dove `Titolo` è il titolo del libro e `numero_pagine` è il numero di pagine del libro.

Si suppone che:
- 
- I file siano tutti corretti 
- Nel file `costipagine.txt` non ci sono "sovrapposizioni" tra range di pagine MA NON E' DETTO CHE LE RIGHE SIANO ORDINATE 
- Nei titoli dei libri NON compaiano punti e virgola
- Il numero di pagine dei libri da prezzare cada sempre in uno degli intervalli del file costipagine.txt.

In base a queste informazioni, il programma deve:

- Caricare il listino prezzi in memoria in una struttura dati opportuna 
- Stampare il listino prezzi IN ORDINE CRESCENTE DI PAGINE 
- Stampare a video la previsione dei costi di stampa di ciascun libro, possibilmente ordinati alfabeticamente per titolo, riportando per ognuno su una singola riga, il titolo, il numero di pagine, e il costo calcolato.

## Esempio

### File `costipagine.txt`

    1;100;2.5€
    101;200;2€
    301;400;1.6€
    201;300;1.8€
    501;700;1.2€
    1001;2000;0.8€
    701;1000;1€
    401;500;1.4€

### File `libri.txt`

    Luci e Ombre in Python;232
    Liste nascoste;125
    Brevi poemi in Python;15
    Dizionario di Python;666
    Python Wars;1342

### Stampa output

    LISTINO PREZZI
    Fino a 100 pagine: 2.5€/pagina
    Fino a 200 pagine: 2.0€/pagina
    Fino a 300 pagine: 1.8€/pagina
    Fino a 400 pagine: 1.6€/pagina
    Fino a 500 pagine: 1.4€/pagina
    Fino a 700 pagine: 1.2€/pagina
    Fino a 1000 pagine: 1.0€/pagina
    Fino a 2000 pagine: 0.8€/pagina
    
    COSTI DI STAMPA
    Brevi poemi in Python - Pagine: 15 - Costo:   37.50€
    Dizionario di Python - Pagine: 666 - Costo:  799.20€
    Liste nascoste - Pagine: 125 - Costo:  250.00€
    Luci e Ombre in Python - Pagine: 232 - Costo:  417.60€
    Python Wars - Pagine: 1342 - Costo: 1073.60€
    Totale: 2577.90€
