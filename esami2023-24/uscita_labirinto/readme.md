# Trovare l'uscita da un labirinto

#### (Esame proposto il 05-06/02/2024)

Si chiede di realizzare un programma in Python in grado di guidare un robot per uscire da un labirinto. Le informazioni sul labirinto sono specificate nel file `"labirinto.txt"`. La prima riga del file riporta le coordinate iniziali del robot; la seconda riga riporta le coordinate dell'uscita del labirinto. Le righe successive specificano come è formato il labirinto: il carattere 'X' indica la presenza di un muro, mentre lo spazio indica un passaggio percorribile dal robot.

## Esempio file "labirinto.txt"

    1,1
    14,9
    XXXXXXXXXXX
    X         X
    X XXX XXX X
    X XXX XXX X
    X         X
    X X XXX X X
    X X XXX X X
    X X     X X
    X X XXX X X
    X X XXX X X
    X         X
    X XXX XXX X
    X XXX XXX X
    X         X
    XXXX  XX  X
    XXXXXXXXXXX

Le coordinate sono indicate come indice di riga e indice di colonna. La coordinata (0, 0) si riferisce al primo carattere della prima riga (ossia, al vertice in alto a sinistra del labirinto). Nell'esempio, il robot si trova nella cella (1, 1) e deve raggiungere la cella (14, 9). Il bordo esterno del labirinto è sempre costituito da mura.

All'inizio del programma, occorre creare una lista **elenco_movimenti** vuota.

Il robot può effettuare 4 movimenti: spostamento in avanti, a sinistra, a destra e indietro. Ad ogni movimento il robot effettua le seguenti operazioni:

- contrassegna la cella in cui si trova con la lettera `'V'` per indicare che è una cella già visitata.
- Identifica i movimenti che può compiere nella posizione corrente: il robot si può spostare in una cella limitrofa (davanti, a destra, a sinistra, o indietro) se tale cella non è un muro (`'X'`) o non è già stata visitata in precedenza (`'V'`).
- Se ci sono uno o più movimenti possibili, il robot aggiunge in fondo alla lista **elenco_movimenti** le coordinate della cella corrente. Poi sceglie casualmente uno fra i movimenti possibili e aggiorna le sue coordinate, stampandole a video.
- Se invece non è possibile nessun movimento, il robot torna sui suoi passi, rimuovendo l'ultimo elemento inserito nella lista **elenco_movimenti** e ponendo le sue coordinate uguali a questo ultimo elemento.

Il programma termina quando il robot raggiunge la cella finale.

## Esempio di output

    posizione iniziale: (1, 1)
    movimento 1: (2, 1)
    movimento 2: (3, 1)
    movimento 3: (4, 1)
    movimento 4: (5, 1)
    movimento 5: (6, 1)
    movimento 6: (7, 1)
    movimento 7: (8, 1)
    movimento 8: (9, 1)
    movimento 9: (10, 1)
    movimento 10: (10, 2)
    movimento 11: (10, 3)
    movimento 12: (9, 3)
    movimento 13: (8, 3)
    movimento 14: (7, 3)
    movimento 15: (6, 3)
    movimento 16: (5, 3)
    movimento 17: (4, 3)
    movimento 18: (4, 2)
    movimento 19: (4, 3)
    movimento 20: (4, 4)
    movimento 21: (4, 5)
    movimento 22: (3, 5)
    movimento 23: (2, 5)
    movimento 24: (1, 5)
    movimento 25: (1, 6)
    movimento 26: (1, 7)
    movimento 27: (1, 8)
    movimento 28: (1, 9)
    movimento 29: (2, 9)
    movimento 30: (3, 9)
    movimento 31: (4, 9)
    movimento 32: (5, 9)
    movimento 33: (6, 9)
    movimento 34: (7, 9)
    movimento 35: (8, 9)
    movimento 36: (9, 9)
    movimento 37: (10, 9)
    movimento 38: (10, 8)
    movimento 39: (10, 7)
    movimento 40: (9, 7)
    movimento 41: (8, 7)
    movimento 42: (7, 7)
    movimento 43: (7, 6)
    movimento 44: (7, 5)
    movimento 45: (7, 4)
    movimento 46: (7, 5)
    movimento 47: (7, 6)
    movimento 48: (7, 7)
    movimento 49: (6, 7)
    movimento 50: (5, 7)
    movimento 51: (4, 7)
    movimento 52: (4, 6)
    movimento 53: (4, 7)
    movimento 54: (4, 8)
    movimento 55: (4, 7)
    movimento 56: (5, 7)
    movimento 57: (6, 7)
    movimento 58: (7, 7)
    movimento 59: (8, 7)
    movimento 60: (9, 7)
    movimento 61: (10, 7)
    movimento 62: (10, 6)
    movimento 63: (10, 5)
    movimento 64: (11, 5)
    movimento 65: (12, 5)
    movimento 66: (13, 5)
    movimento 67: (13, 6)
    movimento 68: (13, 7)
    movimento 69: (13, 8)
    movimento 70: (13, 9)
    movimento 71: (12, 9)
    movimento 72: (11, 9)
    movimento 73: (12, 9)
    movimento 74: (13, 9)
    movimento 75: (14, 9)
