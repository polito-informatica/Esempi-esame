# Miglior Vista

#### (Esame proposto il 27-28/01/2025)

Si vogliono classificare i quadranti di una mappa di una città in base alla vista (ostruzione visiva dovuta agli edifici). La mappa viene fornita come un rettangolo di altezze di edifici misurate in numero di piani, ed è contenuta in un file di nome `mappa.txt`, ad esempio:

```
125432
011233
443442
551121
445000
```

Ogni valore indica un quadrante, e il valore 0 indica l’assenza di edifici. La “vista” di un quadrante viene definita come la **sommatoria delle differenze delle altezze del quadrante e dei quadranti adiacenti nelle 8 direzioni** (NO, N, NE, O, E, SO, S, SE dove N=nord, S=sud, O=ovest, E=est). Si assuma che i quadranti sul bordo abbiano altezza zero nelle direzioni non presenti (in pratica come se la mappa fosse circondata da una cornice di 0).

Ad esempio per il quadrante in posizione (0,2) nella mappa (contenente 5) il suo valore di vista è, scandendo i punti nell'ordine NO,N,NE,O,E,SO,S,SE:

(5-0) + (5-0) + (5-0) + (5-2) + (5-4) + (5-1) + (5-1) + (5-2)

dove i primi tre termini si riferiscono ai punti fuori dalla mappa.

Il programma deve produrre l’elenco, **ordinato per valore di “vista”** di ogni quadrante nel formato indicato di seguito. Nel caso di esempio si otterrebbe la seguente statistica:

```
 1 (0, 2) : Valore =  30
 2 (4, 2) : Valore =  29
 3 (3, 0) : Valore =  19
 4 (0, 3) : Valore =  18
 5 (4, 0) : Valore =  18
 6 (2, 0) : Valore =  17
 7 (2, 3) : Valore =  15
 8 (2, 4) : Valore =  14
 9 (2, 1) : Valore =  12
 10 (4, 1) : Valore =  12
 11 (0, 4) : Valore =  10
 12 (1, 5) : Valore =  10
 13 (3, 1) : Valore =  10
 14 (0, 1) : Valore =  8
 15 (0, 5) : Valore =  7
 16 (0, 0) : Valore =  5
 17 (2, 2) : Valore =  5
 18 (3, 4) : Valore =  4
 19 (2, 5) : Valore =  3
 20 (1, 4) : Valore =  0
 21 (3, 5) : Valore =  0
 22 (4, 5) : Valore =  -3
 23 (4, 4) : Valore =  -4
 24 (4, 3) : Valore =  -9
 25 (1, 3) : Valore =  -11
 26 (3, 3) : Valore =  -11
 27 (1, 0) : Valore =  -12
 28 (1, 1) : Valore =  -12
 29 (1, 2) : Valore =  -17
 30 (3, 2) : Valore =  -18
```