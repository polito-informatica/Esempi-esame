# Superenalotto

#### (Esame proposto il 27-28/01/2025)

Un incallito giocatore, che si è già rivolto agli studenti del Politecnico in passato, sostiene di aver escogitato un metodo per giocare una schedina vincente al Superenalotto. Il giocatore ha visto un po' di video di statistica su TikTok e si è convinto che il modo più promettente per vincere sia quello di giocare dei numeri che non sono mai usciti (o che sono usciti raramente) nelle precedenti estrazioni. Per questo motivo, ha escogitato un algoritmo basato sull'analisi delle precedenti estrazioni. L'algoritmo prevede di estrarre 6 numeri nel seguente modo:

1. Si identificano (se esistono) i numeri che non sono mai stati estratti e si inseriscono nella schedina (se sono meno di 6, tutti, altrimenti si pescano a caso 6 di questi numeri).

2. Se dopo il punto 1 la schedina non è ancora completa, si identificano gli N numeri meno frequenti nelle precedenti estrazioni (con N impostato in maniera costante nel programma, ad esempio N=10). Si seleziona casualmente uno di questi numeri: se si trova una precedente estrazione in cui questo numero compare assieme ad almeno un altro numero già presente nella schedina, si scarta, altrimenti, si aggiunge alla schedina (Suggerimento: pensare all'operazione di intersezione tra insiemi). Si ripete la stessa operazione fino a quando la schedina non è completa o si esauriscono i tentativi, in quanto tutti gli N numeri identificati sono stati valutati.

3. Se nel punto 2 non si riesce a completare la schedina, questa viene completata estraendo numeri a caso (ovviamente, diversi da quelli già presenti nella schedina).

In questo algoritmo, **non si tiene conto** dei numeri estratti come *jolly* o *superstar*.

Scrivere un programma Python in grado di analizzare una serie storica di estrazioni del Superenalotto, contenuta nel file `estrazioni.txt`, e implementare l'algoritmo proposto dal giocatore. Il file contiene una estrazione per riga, e riporta in ordine:

- la data di estrazione
- il numero di concorso all'interno di quell'anno
- i 6 numeri estratti
- il numero jolly
- il numero superstar

Le prime due righe del file contengono un'intestazione, non utile ai fini dell'algoritmo. Le estrazioni sono ordinate dalla più recente alla meno recente, fino ai primi mesi del 2006, quando è stato introdotto il numero superstar.

Il programma deve **richiedere in input un anno** e considerare solo le estrazioni dalla più recente fino a quelle di quell'anno (incluso) nell'implementare l'algoritmo. In uscita, il programma deve stampare la schedina, **ordinando i 6 numeri dal minore al maggiore**.

## Esempio di file `estrazioni.txt`


```
data        conc.  1  2  3  4  5  6   jolly  supers.
-------------------------------------------------------
14/01/2025   08   04 15 17 40 64 75   23      80
11/01/2025   07   05 06 11 22 35 85   30      53
10/01/2025   06   19 25 33 49 57 72   46      38
09/01/2025   05   15 33 40 71 74 82   89      15
07/01/2025   04   07 10 11 29 32 87   34      51
04/01/2025   03   31 42 43 63 83 86   37      86
03/01/2025   02   13 30 43 49 74 89   04      32
02/01/2025   01   19 21 29 74 77 88   07      56
31/12/2024   208   05 16 23 40 47 80   17      13
30/12/2024   207   03 08 18 25 58 75   12      54
28/12/2024   206   28 29 46 68 81 88   79      40
27/12/2024   205   09 13 15 43 53 68   58      69
...
```

## Esempi di esecuzione (N=10)

### Esempio 1 (2025, basta il punto 1)

```
Inserisci anno limite: 2025
Punto 1: Cerco numeri mai estratti e pesco da quelli
Schedina dopo il punto 1: [9, 27, 55, 73, 76, 78]
Schedina finale: [9, 27, 55, 73, 76, 78]
```

### Esempio 2 (2024, serve anche il punto 2)

```
Inserisci anno limite: 2024
Punto 1: cerco numeri mai estratti e pesco da quelli
Schedina dopo il punto 1: []
Mancano 6 numeri per completare la schedina
Punto 2: provo a cercare tra gli N meno frequenti (N=10)
Numero 1 mai estratto assieme a []
Schedina corrente: [1]
Numero 37 mai estratto assieme a [1]
Schedina corrente: [1, 37]
Numero 65 già estratto assieme a [1]
Numero 12 mai estratto assieme a [1, 37]
Schedina corrente: [1, 12, 37]
Numero 38 già estratto assieme a [37]
Numero 62 mai estratto assieme a [1, 12, 37]
Schedina corrente: [1, 12, 37, 62]
Numero 30 già estratto assieme a [62]
Numero 19 mai estratto assieme a [1, 12, 37, 62]
Schedina corrente: [1, 12, 19, 37, 62]
Numero 90 già estratto assieme a [37]
Numero 9 mai estratto assieme a [1, 12, 19, 37, 62]
Schedina corrente: [1, 9, 12, 19, 37, 62]
Schedina finale: [1, 9, 12, 19, 37, 62]
```

### Esempio 3 (sempre 2024, ma stavolta serve il punto 3)

```
Inserisci anno limite: 2024
Punto 1: cerco numeri mai estratti e pesco da quelli
Schedina dopo il punto 1: []
Mancano 6 numeri per completare la schedina
Punto 2: provo a cercare tra gli N meno frequenti (N=10)
Numero 65 mai estratto assieme a []
Schedina corrente: [65]
Numero 19 mai estratto assieme a [65]
Schedina corrente: [19, 65]
Numero 62 mai estratto assieme a [19, 65]
Schedina corrente: [19, 62, 65]
Numero 30 già estratto assieme a [62]
Numero 90 mai estratto assieme a [19, 62, 65]
Schedina corrente: [19, 62, 65, 90]
Numero 9 già estratto assieme a [65]
Numero 1 già estratto assieme a [65]
Numero 12 mai estratto assieme a [19, 62, 65, 90]
Schedina corrente: [12, 19, 62, 65, 90]
Numero 38 già estratto assieme a [62]
Numero 37 già estratto assieme a [90]
Ho esaurito i tentativi con i numeri meno frequenti
Mancano 1 numeri per completare la schedina
Punto 3: genero in modo random i numeri mancanti
Nuovo numero random: 42
Schedina finale: [12, 19, 42, 62, 65, 90]
```

### Esempio 4 (2006, sicuramente si arriva al punto 3)

```
Inserisci anno limite: 2006
Punto 1: cerco numeri mai estratti e pesco da quelli
Schedina dopo il punto 1: []
Mancano 6 numeri per completare la schedina
Punto 2: provo a cercare tra gli N meno frequenti (N=10)
Numero 36 mai estratto assieme a []
Schedina corrente: [36]
Numero 13 già estratto assieme a [36]
Numero 53 già estratto assieme a [36]
Numero 18 già estratto assieme a [36]
Numero 70 già estratto assieme a [36]
Numero 2 già estratto assieme a [36]
Numero 7 già estratto assieme a [36]
Numero 3 già estratto assieme a [36]
Numero 12 già estratto assieme a [36]
Numero 50 già estratto assieme a [36]
Ho esaurito i tentativi con i numeri meno frequenti
Mancano 5 numeri per completare la schedina
Punto 3: genero in modo random i numeri mancanti
Nuovo numero random: 65
Nuovo numero random: 59
Nuovo numero random: 41
Nuovo numero random: 63
Nuovo numero random: 70
Schedina finale: [36, 41, 59, 63, 65, 70]
```