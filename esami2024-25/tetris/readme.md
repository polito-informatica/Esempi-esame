# Tetris

#### (Esame proposto il 27-28/01/2025)


Si vuole realizzare un programma per giocare a Tetris. Nel gioco del Tetris, il giocatore muove e ruota dei blocchi, chiamati tetramini, mentre cadono. Se il giocatore, posizionando i blocchi, riesce a completare una riga orizzontale di blocchi senza interruzioni, questa riga sparisce. Esistono 7 tetramini, rappresentati di seguito:

```
x    
x      x     x                              x
x      x     x      xx      xx     xx      xx
x     xx     xx     xx     xx       xx      x  
```

I tetramini possono essere ruotati, ma si noti che, in ogni configurazione, un tetramino può essere sempre rappresentato in una matrice 4x4.

La partita si svolge in un'area di gioco formata da 6 righe e 8 colonne. La cella in basso a sinistra ha indice di riga 0 e indice di colonna 0.

Il programma legge in input il file `tetraminoes.txt`, contenente l'elenco delle mosse giocate. Ogni mossa è descritta in 5 righe: 

- la prima riga indica la posizione dove il giocatore piazza il tetramino. Più precisamente, la prima riga riporta l'indice di riga e l'indice di colonna dove dovrà essere collocato l'elemento in basso a sinistra del tetramino. 
- Le successive 4 righe contengono 4 caratteri ciascuna, e rappresentano il tetramino, opportunamente ruotato. In particolare, il carattere '1' indica la presenza di un blocco mentre il carattere '0' indica uno spazio vuoto.

## Esempio 1

```
0, 4
0000
0000
1100
1100
0, 6
0000
0100
1100
0100
0, 1
0000
0000
0110
1100
1, 1
0000
0000
1110
1000
0, 0
1000
1000
1000
1000
1, 4
0000
0000
0010
1110
```

Il programma deve innanzitutto creare una tabella di 6 righe e 8 colonne corrispondente all'area di gioco. Successivamente, **per ogni mossa dell'utente**, deve: 

- aggiornare la tabella posizionando il tetramino nelle celle corrette (partendo dalle coordinate della cella in basso a sinistra del tetramino) 
- controllare se dopo il posizionamento del tetramino il giocatore ha completato una o più righe. In caso affermativo, il giocatore ottiene 10 punti per ogni riga completata. Le righe completate devono essere rimosse (liberando spazio per le righe soprastanti). 
- stampare il numero della mossa e il punteggio del giocatore 
- visualizzare l'area di gioco aggiornata.

Il giocatore vince se posiziona tutti i tetramini indicati nel file in input senza uscire dall'area di gioco (nella parte superiore). In questo caso il programma stampa il messaggio "Congratulazioni, hai vinto!". Altrimenti, non appena il posizionamento di un tetramino è al di fuori dell'area di gioco, la partita si interrompe e il programma stampa il messaggio "Mi dispiace, hai perso".

Si supponga che il file esista, non contenga errori, e che le mosse siano corrette (non si verificano sovrapposizioni fra i tetramini). Per il formato di output, si vedano gli esempi seguenti.

## Esempio di output 1

```
Mossa 1, punteggio 0
|        |
|        |
|        |
|        |
|    xx  |
|    xx  |
----------

Mossa 2, punteggio 0
|        |
|        |
|        |
|       x|
|    xxxx|
|    xx x|
----------

Mossa 3, punteggio 0
|        |
|        |
|        |
|       x|
|  xxxxxx|
| xx xx x|
----------

Mossa 4, punteggio 0
|        |
|        |
|        |
| xxx   x|
| xxxxxxx|
| xx xx x|
----------

Mossa 5, punteggio 10
|        |
|        |
|        |
|x       |
|xxxx   x|
|xxx xx x|
----------

Mossa 6, punteggio 20
|        |
|        |
|        |
|        |
|x     x |
|xxx xx x|
----------

Congratulazioni, hai vinto!
```

## Esempio 2

È qui visualizzato il contenuto del file `tetraminoes2.txt`

```
0, 2
0000
0000
1100
0110
2, 0
0000
0000
0000
1111
0, 6
0000
0000
1100
1100
2, 3
0000
0100
1100
0100
3, 1
0000
0100
0100
1100
5, 3
0000
0000
0110
1100
```

L'output è:

```
Mossa 1, punteggio 0
|        |
|        |
|        |
|        |
|  xx    |
|   xx   |
----------

Mossa 2, punteggio 0
|        |
|        |
|        |
|xxxx    |
|  xx    |
|   xx   |
----------

Mossa 3, punteggio 0
|        |
|        |
|        |
|xxxx    |
|  xx  xx|
|   xx xx|
----------

Mossa 4, punteggio 0
|        |
|    x   |
|   xx   |
|xxxxx   |
|  xx  xx|
|   xx xx|
----------

Mossa 5, punteggio 0
|  x     |
|  x x   |
| xxxx   |
|xxxxx   |
|  xx  xx|
|   xx xx|
----------

Mossa 6, punteggio 0
|  xxx   |
|  x x   |
| xxxx   |
|xxxxx   |
|  xx  xx|
|   xx xx|
----------

Mi dispiace, hai perso
```