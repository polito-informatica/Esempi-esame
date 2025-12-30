# Creature, Lotte e Allenatori

#### (Esame proposto il 10/09/2025)

Un famoso videogioco di ruolo consiste nel prendere i panni di un Allenatore e migliorare le statistiche di combattimento di una squadra di fantasiose creature, visitando nuove città e scoprendo nuove creature con cui lottare. Il candidato è stato contattato da uno di questi Allenatori che desidera un programma Python in grado di fornire maggiori informazioni sulla sua squadra, con statistiche ordinate e la possibilità di simulare combattimenti.

Si scriva un programma Python che

- legga e salvi all'interno di opportune strutture dati le caratteristiche di ciascun combattente nella propria squadra, contenute nel file `squadra.csv`. Le caratteristiche sono salvate riga per riga nel formato seguente: `nome univoco, punti vita, potenza attacco 0, potenza attacco 1, potenza attacco 2` . 
- Una volta ottenuti i dati, stampi un elenco dell'intera squadra, ordinata **in ordine decrescente per punti vita**. 
- Chieda all'utente il nome di due lottatori separati da ; e simuli la lotta tra i due, finché uno dei due non esaurisce i suoi punti vita. Se il programma non trova i lottatori inseriti, avverte l'utente e si chiude. Altrimenti, la lotta deve avvenire nel modo seguente:

    1. Il primo lottatore inserito dall'utente sceglie un attacco a caso tra i tre disponibili.
    2. Il secondo lottatore perde dai suoi punti vita un punteggio pari alla potenza dell'attacco ricevuto. Se rimane un numero maggiore di zero punti vita, procede con la sua mossa, anch'essa scelta a caso.
    3. Il primo lottatore aggiornerà i suoi punti vita e, se possibile, ricambierà nuovamente l'attacco con un'altra mossa casuale.
    4. La lotta procede in questo modo e termina quando uno dei due contendenti ottiene un valore negativo di punti vita. Il programma stampa il nome del vincitore, che avrà il valore più alto di punti vita, ed esce.

Suggerimento: è possibile far generare un numero casuale tra 0 e 2 nel modo seguente.

```python
from random import randint
...
numero_casuale = randint(0,2)
````

## Esempio

#### File `squadra.csv`

```
nome univoco, punti vita, potenza attacco 1, potenza attacco 2, potenza attacco 3
Awaitchu, 23, 6.8, 8.0, 9.3  
Tuplattata, 21, 6.6, 9.4, 8.2  
Fromasaur, 20, 7.8, 6.3, 6.3  
Awaittoise, 22, 5.0, 5.0, 6.2  
Asyncnite, 17, 7.5, 5.6, 5.0  
Finallychu, 27, 6.7, 7.1, 5.0  
Lambdamon, 19, 7.2, 5.3, 7.6  
Importgon, 19, 6.6, 6.1, 9.8  
Lambdatoise, 21, 5.4, 8.2, 5.2  
Importtoise, 22, 5.0, 5.0, 7.3  
Finallygon, 24, 7.3, 6.8, 6.5  
Assertnite, 16, 5.9, 6.3, 8.6  
Globalchu, 23, 5.0, 7.5, 6.4  
Listoise, 19, 7.9, 8.5, 8.4  
Raisebat, 18, 6.5, 7.5, 8.5  
````

#### Output del programma:

```
Finallychu: Punti Vita 27, Attacco 1: 6.7, Attacco 2: 7.1, Attacco 3: 5.0
Finallygon: Punti Vita 24, Attacco 1: 7.3, Attacco 2: 6.8, Attacco 3: 6.5
Awaitchu: Punti Vita 23, Attacco 1: 6.8, Attacco 2: 8.0, Attacco 3: 9.3
Globalchu: Punti Vita 23, Attacco 1: 5.0, Attacco 2: 7.5, Attacco 3: 6.4
Awaittoise: Punti Vita 22, Attacco 1: 5.0, Attacco 2: 5.0, Attacco 3: 6.2
Importtoise: Punti Vita 22, Attacco 1: 5.0, Attacco 2: 5.0, Attacco 3: 7.3
Tuplattata: Punti Vita 21, Attacco 1: 6.6, Attacco 2: 9.4, Attacco 3: 8.2
Lambdatoise: Punti Vita 21, Attacco 1: 5.4, Attacco 2: 8.2, Attacco 3: 5.2
Fromasaur: Punti Vita 20, Attacco 1: 7.8, Attacco 2: 6.3, Attacco 3: 6.3
Lambdamon: Punti Vita 19, Attacco 1: 7.2, Attacco 2: 5.3, Attacco 3: 7.6
Importgon: Punti Vita 19, Attacco 1: 6.6, Attacco 2: 6.1, Attacco 3: 9.8
Listoise: Punti Vita 19, Attacco 1: 7.9, Attacco 2: 8.5, Attacco 3: 8.4
Raisebat: Punti Vita 18, Attacco 1: 6.5, Attacco 2: 7.5, Attacco 3: 8.5
Asyncnite: Punti Vita 17, Attacco 1: 7.5, Attacco 2: 5.6, Attacco 3: 5.0
Assertnite: Punti Vita 16, Attacco 1: 5.9, Attacco 2: 6.3, Attacco 3: 8.6

Inserire il nome dei combattenti separati da ';': Assertnite;Raisebat
Assertnite attacca con mossa 1
Raisebat attacca con mossa 2
Assertnite attacca con mossa 0
Raisebat attacca con mossa 0
Assertnite attacca con mossa 0
Vince Assertnite
````

*N.B. le mosse scelte sono casuali e possono variare, l'output non sarà identico caso per caso.*