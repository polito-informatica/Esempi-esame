# Magazzini

#### (Esame proposto il 05/07/2024)

Un file chiamato `stockOld.csv` contiene una lista di articoli in magazzino di un negozio, riportati uno per riga con il seguente formato:

```
codiceArticolo;codiceUPC;categoria
```

dove codiceUPC è il codice UPC (Universal Product Code) che identifica univocamente un determinato prodotto, mentre codiceArticolo è un codice alfanumerico che identifica univocamente ogni articolo fisico. In altre parole, nel caso in cui il magazzino abbia diverse unità dello stesso prodotto, queste saranno riportate con lo stesso codiceUPC ma diversi codiceArticolo. L’inventario riporta tutti gli articoli senza un ordine specifico. Si supponga che nessuno dei campi contenga il carattere punto e virgola, che è presente nel file solamente come separatore.

All'inizio del programma occorre assegnare alla variabile **n** un valore a piacere compreso tra 1 e 10 (estremi inclusi).

Il programma deve selezionare tutti i prodotti presenti in numero maggiore di **n** unità: le unità in eccesso di questi prodotti saranno infatti trasferite ad un altro punto vendita. Il programma Python deve pertanto:

* solo nel caso in cui ci siano dei prodotti che superano il numero di **n** unità, generare un file `stockTrasferimento.csv`, che contenga l’elenco dei prodotti in eccesso da trasferire. In caso contrario, bisogna stampare un opportuno messaggio a monitor che indichi l’assenza di prodotti in eccesso. Per semplicità, la scelta degli articoli da destinare al trasferimento dipende dall’ordine di lettura.

* generare un nuovo inventario del magazzino `stockNew.csv`, privato di tutte le unità trasferite al nuovo punto vendita e riformattato come descritto di seguito.

Entrambi i file `stockTrasferimento.csv` e `stockNew.csv` devono riportare i prodotti in una forma più compatta rispetto all’inventario originale. In particolare, i prodotti devono essere riportati ordinati alfabeticamente per codiceUPC, e ciascun codiceUPC dovrà comparire una sola volta nel file. Il nuovo formato delle righe di questi file è il seguente:

```
codiceUPC;categoria;codiceArticolo1;codiceArticolo2;…;codiceArticoloN
```

in cui codiceArticolo1, codiceArticolo2,…codiceArticoloN rappresentano i codici delle N diverse unità del prodotto, riportate in ordine alfabetico per codiceArticolo.

NB. il programma deve gestire opportunamente le eventuali eccezioni sollevate in fase di apertura dei file.

### Esempio di contenuto del file in input `stockOld.csv`

```
D004;001333333333;Dolci
A126;001234567890;Alimentari
A123;001234567890;Alimentari
D002;001333333333;Dolci
A125;001234567890;Alimentari
D001;001333333333;Dolci
B001;001111111111;Alimentari
B002;001111111111;Alimentari
C001;001222222222;Bevande
A124;001234567890;Alimentari
C002;001222222222;Bevande
D003;001333333333;Dolci
```

Ne caso in cui sia definito un valore n pari a 3, i file generati in output avrebbero il seguente contenuto:

#### `stockTrasferimento.csv`

```
001234567890;Alimentari;A124
001333333333;Dolci;D003
```

#### `stockNew.csv`

```
001111111111;Alimentari;B001;B002
001222222222;Bevande;C001;C002
001234567890;Alimentari;A123;A125;A126
001333333333;Dolci;D001;D002;D004
```