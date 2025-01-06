# Prodotto di matrici

#### (Esame proposto il 05/07/2024)


Una sequenza di *N matrici di dimensioni diverse* è memorizzata in un file `matrices.txt`. *Ogni riga del file codifica una matrice* con il seguente formato:

```
<r> <c> <v_11> <v_12> ... <v_1c> <v_21> <v_22> ... <v_2c> ... <v_r1> <v_r2> ... <v_rc>
```

I primi due valori, `<r> <c>`, sono due numeri interi, separati da spazi bianchi, corrispondenti al numero di righe e colonne della matrice. Il resto della riga contiene i valori della matrice, separati da spazi bianchi e ordinati per riga (cioè i primi `c` valori si riferiscono alla prima riga, i successivi `c` valori si riferiscono alla seconda riga e così via). I valori della matrice sono interi.

Ad esempio, una riga

```
3 4 1 1 -1 -2 0 1 -2 1 3 -1 0 1
```

codifica la matrice 3 x 4

```
 1  1  -1 -2
 0  1  -2  1
 3 -1   0  1
```

Scrivi un programma Python che carichi le matrici dal file. Il programma deve calcolare il risultato della moltiplicazione di tutte le matrici nel file, nell'ordine in cui appaiono nel file. Ad esempio, se il file contiene tre matrici M1, M2 e M3, corrispondenti alle righe 1, 2 e 3 del file, il programma deve calcolare il prodotto M1 * M2 * M3.

Promemoria: data una matrice A di dimensioni m x n e una matrice B di dimensioni n x p, il loro prodotto è la matrice C di dimensioni m x p con elementi

$$C_{i,j} = \sum_{k=1}^{n}{A_{i,k}B_{k,j}}$$

Il prodotto globale deve essere calcolato utilizzando la seguente procedura:

* Inizializzare una lista con tutte le matrici nel file

* Verificare che tutte le matrici abbiano dimensioni compatibili (se A e B sono matrici adiacenti nel prodotto, cioè sono consecutive nella lista, il numero di colonne di A deve essere uguale al numero di righe di B). Se le matrici non possono essere moltiplicate, il programma deve stampare un messaggio di errore e terminare

* Finché ci sono almeno due matrici da moltiplicare, selezionare iterativamente due matrici consecutive dalla lista, calcolare il loro prodotto e sostituire le due matrici con il risultato nella lista

Ad ogni iterazione, per identificare la coppia successiva di matrici da moltiplicare, il programma deve considerare tutte le coppie di matrici consecutive e selezionare la coppia che richiede il minor numero di operazioni. Se A è una matrice m x n e B è una matrice n x p, il numero di operazioni per calcolare A * B è m * n * p. In caso di più alternative con lo stesso costo, il programma dovrebbe selezionare la prima coppia. Il programma deve stampare la dimensione delle matrici nella lista, la dimensione delle matrici selezionate e la dimensione della matrice risultante dalla moltiplicazione delle matrici selezionate.

Alla fine, il programma deve stampare la matrice corrispondente al prodotto finale di tutte le matrici di input (il formato per i valori è libero, negli esempi seguenti sono utilizzati 12 digit).

**Nota**: Quelli che seguono sono solo esempi, il programma non deve fare **alcuna** assunzione sul numero di matrici nel file `matrices.txt` o sulla loro dimensione, tranne quanto esplicitamente dichiarato nel testo sopra.

## Esempio 1

Dato il seguente file `matrices.txt`

```
4 1 1 -1 -1 1
1 5 2 -1 -1 1 -1
5 3 1 0 -2 1 1 -1 0 1 2 0 1 -1 -1 -1 0
3 4 1 1 -1 -2 0 1 -2 1 1 -1 1 1
4 2 1 0 1 1 -1 1 1 2
2 3 1 2 1 -1 -1 2
```

il programma deve stampare quanto segue

```
Matrici da moltiplicare: 4 x 1, 1 x 5, 5 x 3, 3 x 4, 4 x 2, 2 x 3,
Moltiplicazione delle matrici con dimensioni (1, 5) e (5, 3) -> (1, 3)

Matrici da moltiplicare: 4 x 1, 1 x 3, 3 x 4, 4 x 2, 2 x 3,
Moltiplicazione delle matrici con dimensioni (4, 1) e (1, 3) -> (4, 3)

Matrici da moltiplicare: 4 x 3, 3 x 4, 4 x 2, 2 x 3,
Moltiplicazione delle matrici con dimensioni (3, 4) e (4, 2) -> (3, 2)

Matrici da moltiplicare: 4 x 3, 3 x 2, 2 x 3,
Moltiplicazione delle matrici con dimensioni (3, 2) e (2, 3) -> (3, 3)

Matrici da moltiplicare: 4 x 3, 3 x 3,
Moltiplicazione delle matrici con dimensioni (4, 3) e (3, 3) -> (4, 3)

Risultato:
          22           24          -38
         -22          -24           38
         -22          -24           38
          22           24          -38
```


## Esempio 2

Per le seguenti matrici contenute nel file `matrices_error.txt`

```
4 1 1 -1 -1 1
2 5 2 -1 -1 1 -1
5 3 1 0 -2 1 1 -1 0 1 2 0 1 -1 -1 -1 0
3 4 1 1 -1 -2 0 1 -2 1 1 -1 1 1
4 2 1 0 1 1 -1 1 1 2
2 3 1 2 1 -1 -1 2
```

il programma deve stampare quanto segue

```
Impossibile calcolare il prodotto - le dimensioni non coincidono
```

## Esempio 3

Per le matrici contenute nel file `matrices_large.txt` il programma deve stampare

```
Matrici da moltiplicare: 8 x 5, 5 x 5, 5 x 8, 8 x 5, 5 x 9, 9 x 9, 9 x 9, 9 x 7, 7 x 5, 5 x 6,
Moltiplicazione delle matrici con dimensioni (8, 5) and (5, 5) -> (8, 5)

Matrici da moltiplicare: 8 x 5, 5 x 8, 8 x 5, 5 x 9, 9 x 9, 9 x 9, 9 x 7, 7 x 5, 5 x 6,
Moltiplicazione delle matrici con dimensioni (5, 8) and (8, 5) -> (5, 5)

Matrici da moltiplicare: 8 x 5, 5 x 5, 5 x 9, 9 x 9, 9 x 9, 9 x 7, 7 x 5, 5 x 6,
Moltiplicazione delle matrici con dimensioni (8, 5) and (5, 5) -> (8, 5)

Matrici da moltiplicare: 8 x 5, 5 x 9, 9 x 9, 9 x 9, 9 x 7, 7 x 5, 5 x 6,
Moltiplicazione delle matrici con dimensioni (7, 5) and (5, 6) -> (7, 6)

Matrici da moltiplicare: 8 x 5, 5 x 9, 9 x 9, 9 x 9, 9 x 7, 7 x 6,
Moltiplicazione delle matrici con dimensioni (8, 5) and (5, 9) -> (8, 9)

Matrici da moltiplicare: 8 x 9, 9 x 9, 9 x 9, 9 x 7, 7 x 6,
Moltiplicazione delle matrici con dimensioni (9, 7) and (7, 6) -> (9, 6)

Matrici da moltiplicare: 8 x 9, 9 x 9, 9 x 9, 9 x 6,
Multiplying matrices with sizes (9, 9) and (9, 6) -> (9, 6)

Matrici da moltiplicare: 8 x 9, 9 x 9, 9 x 6,
Moltiplicazione delle matrici con dimensioni (9, 9) and (9, 6) -> (9, 6)

Matrici da moltiplicare: 8 x 9, 9 x 6,
Moltiplicazione delle matrici con dimensioni (8, 9) and (9, 6) -> (8, 6)

Risultato:
     -502922        82660       -36318      -516440        67480      -592274
     -232950       110316         9828      -328896        -9186       480534
      437400      -201464       -32450       624720       -16994      -590176
     -951714       278828       -13704     -1137920        77758        11158
      316256       -79624        15406       354564       -21546        28164
      320816       -64648        31566       348920       -11418       131344
     -369373       146058        18856      -504184        30195       206803
       -5557        35338        25916       -60916         8191       138555
```