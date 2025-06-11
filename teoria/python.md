# Domande di Teoria - Programmazione Python

## 1

Spiegare il concetto di **alias** in Python ed i potenziali problemi ad esso correlati durante la scrittura del codice.

## 2

Perché in Python i dizionari sono chiamati così?

## 3

Qual è lo scopo principale dell'indentazione nel linguaggio Python? Fare un esempio in cui essa risulti di vitale
importanza.

## 4

Fornire un esempio in cui l'ordine delle istruzioni `elif` influenzi il risultato finale.

## 5

Un programmatore vuole rappresentare delle matrici di numeri nella propria applicazione. Ad esempio vuole rappresentare
la matrice

    /         \
    |  1   2  |
    |  3   4  |
    \         /

Il programmatore ha pensato a 3 possibili rappresentazioni di questa matrice. Si discutano brevemente ai vantaggi e
svantaggi delle 3 opzioni, indicando se alcune di esse si devono considerare errate.

- `[ 1, 2, 3, 4 ]`
- `[[1,2], [3,4]]`
- `[[1,3], [2,4]]`

## 6

Spiegare il concetto di visibilità di una variabile e indicare la differenza fra variabili locali e variabili globali.

## 7

Quali vantaggi e quali svantaggi fornisce un insieme rispetto ad una lista?

## 8

Si considerino Liste e Insiemi:

- elencare le differenze tra queste due strutture dati
- evidenziarne i vantaggi e gli svantaggi
- fornire un esempio di dati per la cui rappresentazione è più opportuno utilizzare una lista e dati per la cui
  rappresentazione è più opportuno utilizzare un insieme.

## 9

Quale tra le istruzioni seguenti permette di creare una variabile `d2` che contiene *una copia* del dizionario `d1`?

1. `d2 = d1`
2. `d2 = dict(d1.values())`
3. `d2 = dict(d1.keys())`
4. `d2 = dict(d1)`

## 10

Il linguaggio Python mette a disposizione dei programmatori **dizionari** (`dict`) e **insiemi** (`set`). Si richiede di
fornire una sintetica descrizione di queste due strutture dati complesse, indicando almeno una caratteristiche comune.

## 11

Quali di queste strutture non si può realizzare in Python e perché?

1. dizionario di liste
2. set di dizionari
3. dizionario di set
4. lista di liste.

## 12

Si supponga di leggere un dato da tastiera. Cosa succede se si usa tale dato direttamente in un'operazione aritmetica?
Come si dovrebbe procedere per gestire dati numerici introdotti da tastiera?

## 13

È possibile che in un dizionario siano presenti due chiavi associate a valori uguali? E due valori associati alla stessa
chiave?

## 14

In una funzione Python, qual è la differenza tra argomenti e valori restituiti? Quanti argomenti può avere una
invocazione di funzione? E quanti valori può restituire una funzione?

## 15

Come si può fare in Python a convertire una stringa in minuscolo?

## 16

Quali sono i tipi di dato validi per gli elementi contenuti in una lista? e di un insieme?

## 18

Quali caratteristiche devono avere i valori memorizzati in un insieme? Elencare sia i valori memorizzabili sia quelli
non memorizzabili in un insieme.

## 19

Qual è la differenza tra tipo mutabile e immutabile in Python? Si elenchino un tipo mutabile ed uno immutabile a scelta.

## 20

Qual è la differenza tra liste e insiemi in Python? Dire se è possibile convertire una lista in un insieme
(e viceversa) e con quali effetti.

## 21

Spiegare la differenza tra liste e tuple. Una funzione può restituire una tupla? E una lista?

## 22

Spiegare brevemente la differenza tra Liste e Dizionari in Python.

## 23

Quali sono gli **operatori** booleani? Scrivere un'istruzione Python contenente un operatore booleano.

## 24

Descrivere il fenomeno di **aliasing** in Python per mezzo di un esempio sulle liste. Indicare (sempre per mezzo di un
esempio sulle liste) come effettuare una copia senza aliasing.

## 25

In un dizionario Python, che caratteristica fondamentale deve avere il tipo di dato usato come chiave del dizionario?

## 26

Discutere la differenza tra parametro formale e parametro attuale di una funzione.

## 27

Spiegare almeno due approcci per confrontare numeri reali tenendo conto di possibili errori di arrotondamento.

## 28

Spiegare il concetto di alias nel contesto del passaggio di parametri ad una funzione, evidenziando se e quando si
applica.

## 29

Qual è la differenza tra liste e insiemi?

## 30

Come si esegue un controllo di flusso in Python utilizzando "if", "elif" e "else"? Fornire un esempio

## 31

Spiegare la differenza tra liste e tuple. Una funzione puo' restituire una tupla? E una lista?

## 32

Nel linguaggio Python, cosa si intende quando si parla della differenza tra la *copia*
di una lista e un *alias* alla lista stessa? Fornire un esempio.

## 33

Quali sono le principali caratteristiche di un insieme in Python?

## 34

Quali sono gli operatori booleani? Scrivere un'istruzione 
Python contenente un operatore booleano.

## 35

Spiegare brevemente la differenza tra Liste e Insiemi in Python.

## 36

Che cosa succede se dopo aver costruito l'insieme Python `colori` come segue:
```python
colori = set(['bianco','giallo','verde','rosso','viola'])
``` 
viene eseguita la riga di codice `print(colori[2])`? Motivare la risposta.

## 37 

Come si può fare in Python a convertire una stringa in maiuscolo?

## 38 

È possibile usare una lista come chiave di un dizionario Python? E una tupla?
Rispondere si o no, motivando la risposta.

## 39

In una funzione Python, qual è la differenza tra argomenti e valori restituiti?
Quanti argomenti può avere una invocazione di funzione?
E quanti valori può restituire una funzione?

## 40 

Quali sono le differenze tra lista e set?

## 41

Come si può fare in Python a convertire un carattere numerico in intero?

## 42

In un insieme (set) di Python, quale caratteristica fondamentale deve avere il tipo di dato memorizzato?

## 43

Descrivere il costrutto try/except. Motivare la risposta con un (brevissimo) esempio.

## 44

Quali sono le caratteristiche principali degli insiemi (set) in Python? Quali sono le differenze fondamentali tra liste e insiemi?

## 45

Nella gestione delle eccezioni, quando è eseguita la clausola except? Aggiungere un (breve) esempio esplicativo in Python

## 46

Come si può determinare se una stringa sia trasformabile in un int?

## 47

Si consideri il seguente codice Python, che vorrebbe creare una lista dei numeri da 0 a 9, ma che genera un errore `AttributeError: 'NoneType' object has no attribute 'append'`. Si spieghi il motivo dell'errore e si corregga il codice (basta indicare la singola istruzione da correggere).

```python
    a = []
    for i in range(10):
        a = a.append(i)
    print(a)
```

## 48

Spiegare brevemente la differenza tra Set e Dizionari in Python.

## 49

Qual è la differenza tra warning ed eccezioni? Come vengono gestite queste ultime in Python? Motivare la risposta con un breve esempio.

## 50

In una funzione Python, qual è la differenza tra argomenti e valori restituiti?

## 51

Dati due insiemi così definiti: `colori_1 = set(["bianco","rosso","verde","giallo"])` e `colori_2 = set(["rosa","azzurro","nero","marrone"])`, cosa stamperà la seguente istruzione?

```python
print(len(colori_1.intersection(colori_2)))
```

## 52

La funzione `read_list_of_studs()` intende ritornare una lista di record, ciascuno con i seguenti campi `'nome'`, `'cognome'`, `'matricola'`. Cosa c'e' di errato nel codice che segue? Dare una risposta sintetica ma esaustiva, indicando una possibile soluzione al problema.

```python
def read_list_of_studs(): 
    lista = [] 
    stud = {} 
    for i in range(2): 
        stud['nome'] = input("Nome: ") 
        stud['cognome'] = input("Cognome: ") 
        stud['matricola'] = input("Matricola: ") 
        lista.append(stud) 
    return lista
```

## 53

Costruire un esempio di un dizionario che usa come chiave una coppia di valori (tupla) a cui è associato un valore stringa.

## 54 

Un insieme (set) di Python può contenere delle liste? si/no e perchè?

## 55

Quali sono i tipi di dato immutabili in Python? È possibile assegnare un nuovo valore ad una variabile il cui tipo di dato è immutabile?

## 56

Spiegare brevemente cosa fa il codice seguente, evidenziando soprattutto cosa stampa a video e se contiene errori.

```python
NOME_FILE = "mary.txt"

filastrocca = open(NOME_FILE, "r", encoding="utf-8")
righe = filastrocca.readlines()

for riga in filastrocca:
    riga = riga.strip()
    parole = riga.split()
    for parola in parole:
        parola_pulita = parola.strip(',."?').lower()
        print(parola_pulita)

filastrocca.close()
```


## 57

Che differenza c'è tra *sollevare* un'eccezione e *gestire* un'eccezione?

## 58

Indicare il/i valore/i contenuto/i nella variabile `a`:

```python
def f(indice, lista):
    lista[indice], lista[0] = 0, indice
    return sum(lista)

a = f(2, [1,2,3,4])
```

## 59

Cosa succede in un programma Python se si tenta di aprire un file in modalità lettura avendo sbagliato il nome del file? Come si può porre rimedio a tale situazione?

## 60

Quale tipo di dato si ottiene leggendo da tastiera con la funzione `input()`? Come bisogna procedere per sommare un valore intero ed uno decimale letti (separatamente) da tastiera e assegnati a due variabili diverse?

## 61

Come si può fare in Python a convertire una stringa in maiuscolo?

## 62

Siano dati due insiemi creati nel seguente modo: 
```python
colori1 = set(["giallo","verde","rosso","viola"])
colori2 = set(["rosso","ciano","verde","magenta","ciano","viola","giallo"])
```
Cosa produce l'istruzione seguente? 
```python
print(colori2 >= colori1)
```

## 63

In Python, può un set contenere una tupla generica? E può una tupla contenere un set generico? Motiva la risposta.

## 64

In un dizionario, si può usare una lista come chiave e associarle come valore un set? si, no e perchè?

## 65

Si supponga di avere le seguenti strutture dati in Python:

```python
a = ["c","i","a","o"]

b = "ciao"
```

- Con quale istruzione si può accedere e modificare il primo elemento di `a`?
- È possibile fare lo stesso con `b`? Motivare la risposta.

## 66

Scrivere il codice Python per creare, popolare con due voci e stampare un set di tuple.

## 67

Quale differenze ci sono tra una tupla e una lista?

## 68 

Considerando il linguaggio Python, spiega brevemente le somiglianze e le differenze tra: set, dizionari e liste.

## 69

Si illustri, anche mediante esempi, il concetto di dizionario come array associativo. 

## 70

Spiegare brevemente cosa sono le eccezioni in Python e come vengono gestite, anche mediante l'uso di esempi. 

## 71

Quale funzione può essere utilizzata in un ciclo `for` per ottenere contemporaneamente sia l'indice che il valore dell'elemento corrente? Fornire un esempio.

## 72

Spiegare brevemente le differenze tra Set e Liste in Python.

## 73

Si vuole memorizzare un polinomio $P(x)$ tramite un dizionario Python in cui la chiave è il grado della $x$ e il valore ` il coefficiente di quel grado. Scrivere come verrebbe memorizzato in python il polinomio $P(x) = -2x^3 + 2x^2 + 5x - 1$.

## 74

Spiegare brevemente la differenza tra Set e Dizionari in Python.

## 75

Cosa fa il seguente frammento di codice?

```python
personaggi = set(['bianconiglio','alice','cheshire','dodo','brucaliffo'])
print(max(personaggi))
print(personaggi[2])
```

## 76

Spiegare le differenze che ci sono tra liste e dizionari in Python.

## 77

Scrivere un pezzo di codice per richiedere due numeri `x` ed `y` in input all'utente e stampare il rapporto `x/y`. Il codice deve gestire le eccezioni che si possono verificare. Indicare inoltre quali linee di codice possono sollevare eccezioni (e di che tipo).

## 78

Individuare (se presenti) eventuali malfunzionamenti della seguente funzione Python scritta per leggere e memorizzare una lista di 10 interi letti da tastiera. Indicare una possibile soluzione.

```python
def read(lista):
    intList = []
    for i in range(10):
        val = int(input(f'val {i:2d}:'))
        intList.append(val)
    lista = intList
    return
```

## 79

Cosa si intende per indentazione del codice? È necessaria in Python?



