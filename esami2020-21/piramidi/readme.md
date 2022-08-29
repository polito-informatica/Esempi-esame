# Testo d'esame "Piramidi"

Il Prof Otto Lidenbrock, durante un viaggio in val Vermenagna, ha scoperto un sorprendente complesso di costruzioni
piramidali composte da cubi di un metro di lato. Ogni struttura ha il punto più alto al centro, circondato da un secondo
livello più basso di un metro e più largo di un metro in ogni direzione, seguito da innumerevoli successivi livelli che
degradano o fino al suolo, oppure fino ad incontrare il lato di un'altra piramide, oppure fino alle pareti rocciose che
delimitano l'area. Data l'alta regolarità della zona, il Prof. Lindenbrock ha diviso l'area in una griglia di quadrati
larghi un metro. Dopo di che, considerando il suolo ad altezza 0, ha annotato in un file una tabella rappresentante
tutte le altezze (numeri interi). Si noti che una cima deve avere altezza maggiore di 0 e può essere riconosciuta
dall’assenza di punti adiacenti più alti. Si noti anche che ogni cima non ha cime direttamente adiacenti, nemmeno in
diagonale.

Si richiede di scrivere un programma in grado di acquisire il file scritto dal Professore, il cui nome è `mappa.txt`. Il
programma dovrà stampare a video l’elenco delle cime, seguendo il seguente formato. Numerare le righe e le colonne
partendo da 0. Si assume che il contenuto del file sia corretto e conforme alla descrizione. Se non ci sono cime,
segnalarlo.

    altezza riga colonna
    altezza riga colonna

Al termine stampare l’altezza media delle cime.

# Esempio

## mappa.txt

    3 4 4 4 3 2 1 0 0 0 
    3 4 5 4 3 2 1 1 1 1 
    3 4 4 4 3 2 2 2 2 1 
    3 3 3 3 3 3 3 3 2 1 
    2 2 2 2 2 3 4 3 2 1 
    1 1 1 1 2 3 3 3 2 1 
    0 0 0 1 2 2 2 2 2 1 
    0 0 0 1 1 1 1 1 1 1 
    0 1 0 0 0 0 0 0 0 0 
    0 0 0 0 0 0 1 0 0 0 

## Output

    5 1 2
    4 4 6
    1 8 1
    1 9 6

    Altezza media: 2.75 m
