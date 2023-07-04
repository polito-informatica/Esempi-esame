# Battaglia Navale

#### (Esame proposto il 30/06/2023)

Si vuole realizzare una versione base del gioco di battaglia navale. 
La posizione delle navi di ciascun giocatore è salvata in una matrice di dimensione 10x10
come nei file riportati di seguito, in cui la cifra
(1 per il primo giocatore, 2 per il secondo giocatore)
indica la presenza di una parte di nave.

#### File `navi1.txt`

        ,,,1,1,,,,,
        ,,1,,,,,,,
        ,,1,,,,,,,
        ,,1,,,,,,,
        ,,1,,,,,,,
        ,,,,,,,,,
        ,,,1,1,1,1,,,
        ,,,,1,1,1,,,
        ,,,,,,,,,
        ,,,1,1,,,,,

#### File `navi2.txt`

        ,2,2,2,2,,,,,
        ,,,,,,,,,
        ,,2,,,,,,,
        ,,2,,,,,,,
        ,,2,,,,,,,
        ,,,,,,,,,
        ,,,2,2,2,2,,,
        ,,,,2,2,2,,,
        ,,,,,,,,,
        ,2,2,,,,,,,

Il programma dovrà chiedere in input ad ogni giocatore il nome del file da
caricare e salvarlo all'interno di una tabella. 
(Per fare ciò si consiglia la creazione di una funzione
`read_data()`
).

Successivamente il programma legge le mosse dei giocatori dal file mosse.txt. Ciascuna riga del file indica le coordinate di un colpo, espresse nel formato

        R,C

dove `R` (indice di riga) è una lettera compresa tra A e J, e `C` (indice di colonna)
è un numero compreso tra 1 e 10. I colpi si alternano (prima riga giocatore 1, seconda riga giocatore 2, terza riga giocatore 1, ecc.).

#### File `mosse.txt`

        A,1
        F,5
        A,4
        C,1
        A,5
        C,3
        A,6
        B,3
        A,3
        A,3
        A,2
        D,3
        H,2
        E,3

Il programma deve stampare a schermo: 

- il giocatore che sta effettuando il colpo 
- le coordinate del colpo 
- l'esito del colpo:
  - `acqua` o `colpito`
- la tabella dell'avversario in seguito al colpo effettuato (senza far vedere la posizione delle barche). I colpi in cui è stata presa acqua sono indicati con `o`, mentre i colpi a segno con `*`.

(Si consiglia la creazione di una funzione `play_round(tabella)` che prende in input la tabella dell'avversario e la modifica in base all'esito del colpo. Si consiglia inoltre la creazione di una funzione
`stampa_matrice` per la stampa e visualizzazione della matrice.)

La partita si conclude quando vengono affondate tutte le navi di uno dei due giocatori, oppure quando il file `mosse.txt` termina (se entrambi gli avversari hanno ancora navi, la partita si considera sospesa).

### Esempio di esecuzione

        Giocatore 1
        Inserire il nome del file con le navi: navi1.txt
        Giocatore 2
        Inserire il nome del file con le navi: navi2.txt
        
        E' il turno del giocatore 1
        Coordinate dell'attacco: A, 1
        Acqua
          | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|
        _________________________________
        A |o |  |  |  |  |  |  |  |  |  |
        _________________________________
        B |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        C |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        D |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        E |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        F |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        G |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        H |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        I |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        J |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        
        E' il turno del giocatore 2
        Coordinate dell'attacco: F, 5
        Acqua
          | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|
        _________________________________
        A |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        B |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        C |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        D |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        E |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        F |  |  |  |  |o |  |  |  |  |  |
        _________________________________
        G |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        H |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        I |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        J |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        
        E' il turno del giocatore 1
        Coordinate dell'attacco: A, 4
        Colpito
          | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|
        _________________________________
        A |o |  |  |* |  |  |  |  |  |  |
        _________________________________
        B |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        C |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        D |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        E |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        F |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        G |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        H |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        I |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        J |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        
        E' il turno del giocatore 2
        Coordinate dell'attacco: C, 1
        Acqua
          | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|
        _________________________________
        A |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        B |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        C |o |  |  |  |  |  |  |  |  |  |
        _________________________________
        D |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        E |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        F |  |  |  |  |o |  |  |  |  |  |
        _________________________________
        G |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        H |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        I |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        J |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        
        E' il turno del giocatore 1
        Coordinate dell'attacco: A, 5
        Colpito
          | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|
        _________________________________
        A |o |  |  |* |* |  |  |  |  |  |
        _________________________________
        B |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        C |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        D |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        E |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        F |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        G |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        H |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        I |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        J |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        
        E' il turno del giocatore 2
        Coordinate dell'attacco: C, 3
        Colpito
          | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|
        _________________________________
        A |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        B |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        C |o |  |* |  |  |  |  |  |  |  |
        _________________________________
        D |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        E |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        F |  |  |  |  |o |  |  |  |  |  |
        _________________________________
        G |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        H |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        I |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        J |  |  |  |  |  |  |  |  |  |  |
        _________________________________
        
