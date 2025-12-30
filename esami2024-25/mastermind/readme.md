# Mastermind

#### (Esame proposto il 20/06/2025)


Si vuole sviluppare un programma Python per giocare a Mastermind. Mastermind è un gioco da tavolo in cui un giocatore, il "decodificatore", deve indovinare il codice segreto composto dal suo avversario, detto "codificatore".

Il codice segreto è di quattro cifre e il codificatore ha a disposizione, per comporlo, le dieci cifre del sistema decimale standard (0, 1, 2, 3, 4, 5, 6, 7, 8, 9). Si noti che le cifre possono essere ripetute. Esempi di codici segreti sono "1234", "3345", "0100", "5436", ecc.

Dopo che il codificatore ha composto il codice, il decodificatore procede a tentativi, cercando di indovinare il codice. In seguito a ogni tentativo, il codificatore comunica al decodificatore:

- **Il numero di cifre giuste al posto giusto**, cioè le cifre del tentativo che sono effettivamente presenti nel codice segreto nel posto corretto. Il numero di cifre giuste è indicato con un piolo nero, qui rappresentato con il carattere X.

- **Il numero di cifre giuste al posto sbagliato**, cioè le cifre del tentativo che sono effettivamente presenti nel codice segreto, ma che sono nel posto sbagliato. Le cifre giuste nel posto sbagliato sono indicate con dei pioli bianchi, qui rappresentate con il simbolo Y.

Si noti che il codificatore non comunica quali cifre sono giuste o sbagliate, ma solo quante cifre sono giuste nel posto giusto (numero di pioli neri) e giuste nel posto sbagliato (numero di pioli bianchi). Se il decodificatore riesce ad indovinare il codice, vince la partita.

Il programma Python sviluppato dovrà:

- **leggere dal file "`sequenze.txt`" le sequenze da indovinare**. Il file riporta, una per riga, le sequenze da indovinare. Nel caso in cui la sequenza da indovinare abbia un numero di cifre diverso da 4, il programma dovrà stampare un messaggio di errore, e scartare la sequenza non conforme;

- per ognuna delle sequenze da indovinare, dovrà provare a indovinarla, seguendo, ad esempio, l'approccio riportato di seguito, oppure applicando altri approcci più efficienti;

- una volta indovinata una sequenza, dovrà riportare quante iterazioni/mosse sono state effettuate prima di indovinare la sequenza.

Un esempio di approccio che si può seguire per indovinare la sequenza consiste nel suddividere il problema in due parti, la prima in cui vengono identificate le cifre corrette della sequenza (in questo caso, non è importante l'ordine), la seconda in cui viene variato l'ordine delle cifre corrette, al fine di identificare l'ordine corretto. 

In particolare:

**FASE 1: Scoprire QUALI cifre ci sono nel codice
**
- Inizia testando "0000" per vedere se ci sono degli zeri
- Poi testa "1111" per vedere se ci sono degli uni
- Continua con "2222", "3333", ecc.
- Ogni volta che ricevi dei pioli (neri + bianchi), significa che quella cifra è presente nel codice
- Combina le cifre già trovate con quella nuova da testare
- **Es: se hai trovato un 7, il prossimo test sarà "7888" (non "8888")**
- Fermati quando la somma dei pioli = 4 (hai trovato tutte le cifre!)

**FASE 2: Scoprire l'ORDINE corretto delle cifre
**

- Ora conosci le 4 cifre corrette (es: 7, 8, 9, 3)
- **Genera tutte le possibili permutazioni di queste cifre** usando `itertools.permutations()`
- ⚠️ IMPORTANTE: Devi importare `from itertools import permutations`
- Testa ogni combinazione finché non ottieni 4X 0Y (vittoria!)
- **Extra**: Per rendere il programma più efficiente è possibile scartare le sequenze già tentate in precedenza e valutare solo quelle per le quali non ha ancora ricevuto una risposta sul numero di pioli bianchi e neri.

## Esempio

#### File `sequenze.txt`

```
7893  
3298  
64389  
4356
````

Output

```
Sequenza 64389 non corretta

La sequenza da indovinare è: 7893
0X 0Y 0000
0X 0Y 1111
0X 0Y 2222
1X 0Y 3333
0X 1Y 3444
0X 1Y 3555
0X 1Y 3666
0X 2Y 3777
0X 3Y 3788
0X 4Y 3789
1X 3Y 3798
1X 3Y 9783
0X 4Y 8379
4X 0Y 7893
Sequenza indovinata dopo 14 iterazioni

La sequenza da indovinare è: 3298
0X 0Y 0000
0X 0Y 1111
1X 0Y 2222
0X 2Y 2333
0X 2Y 2344
0X 2Y 2355
0X 2Y 2366
0X 2Y 2377
1X 2Y 2388
0X 4Y 2389
1X 3Y 8239
1X 3Y 8392
1X 3Y 2938
0X 4Y 9823
4X 0Y 3298
Sequenza indovinata dopo 15 iterazioni

La sequenza da indovinare è: 4356
0X 0Y 0000
0X 0Y 1111
0X 0Y 2222
1X 0Y 3333
0X 2Y 3444
1X 2Y 3455
2X 2Y 3456
2X 2Y 5346
0X 4Y 3645
4X 0Y 4356
Sequenza indovinata dopo 10 iterazioni
```