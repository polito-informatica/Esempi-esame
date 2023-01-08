# Separa conti

#### (Esame proposto il 13/09/2022)

Due coinquilini hanno il problema di far tornare i conti quando uno dei due va a fare la spesa. Nelle regole che si sono
dati, chi va a fare la spesa paga per tutti e due e poi chiede il dovuto al coinquilino, in base alla lista di prodotti
che questi necessitava (e che erano disponibili). Per pigrizia, una volta alla cassa, entrambi hanno il vizio di non
dividere i prodotti, per cui devono fare i conti, scontrino e lista alla mano.

Si scriva un programma che aiuti i poveri coinquilini a calcolare quanto il coinquilino che è andato a fare la spesa
deve ricevere dall'altro. Il programma riceverà in input due file: uno scontrino e una lista.

Lo scontrino è un file di testo che contiene, in ogni riga, due campi separati da virgola:

- il nome del prodotto
- il prezzo unitario (con due cifre decimali).

Le stesso prodotto può comparire più volte nello scontrino se ne sono stati acquistati più pezzi (esempio: comprando 3
pacchi di latte, lo scontrino avrà 3 righe per il latte).

La lista dei prodotti richiesti dal coinquilino è un file di testo che contiene anch'esso due campi separati da virgola:

- il nome del prodotto
- la quantità desiderata.

Il programma deve stampare a video:

- l'importo totale della spesa
- il totale dovuto da chi non è andato a fare la spesa
- i nomi e le quantità dei prodotti non trovati nello scontrino.


## Esempio file `scontrino.csv` (in input)

    Latte intero,1.59
    Latte intero,1.59
    Uova,1.99
    Latte intero,1.59
    Uova,1.99
    Pane,2.20
    Carta igienica,5.60
    Detersivo piatti,2.99
    Detersivo piatti,2.99
    Birra,1.29
    Birra,1.29
    Birra,1.29
    Birra,1.29
    Birra,1.29
    Fazzoletti,3.50
    Mozzarella,1.80
    Rum,12.59
    Olio,6.99
    Olio,6.99
    Riso,2.50
    Mozzarella,1.80
    Sale grosso,0.80
    Sale fino,0.80
    Acqua,2.40
    Acqua,2.40
    Acqua,2.40
    Acqua,2.40
    Chewing gum,1.20
    Rasoi,4.99

## Esempio file `lista.csv` (in input)

    Birra,2
    Pane,1
    Olio,3
    Prosciutto cotto,2
    Latte parzialmente scremato,2
    Carta igienica,1
    Mozzarella,4
    Acqua,1
    Pile AAA,2

## Esempio di esecuzione

    Totale speso: 82.54 euro
    Totale dovuto: 30.36 euro
    Prodotti mancanti:
    1 Olio
    2 Prosciutto cotto
    2 Latte parzialmente scremato
    2 Mozzarella
    2 Pile AAA
