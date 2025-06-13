# Sportelli Postali

#### (Esame proposto il 10-11/02/2025)

Un ufficio postale ha bisogno di un programma per gestire gli sportelli. Gli sportelli sono numerati da 1 a N. Ogni sportello può supportare uno o più task. Ogni task ha un tempo di esecuzione fisso. Ogni sportello ha un orario di chiusura. Vengono forniti due file di testo, "`sportelli.txt`" e "`clienti.txt`", contenenti rispettivamente informazioni sugli sportelli della posta e sui clienti in attesa di essere serviti.

Il file "`sportelli.txt`" ha la seguente struttura:

```
Sportello_ID1,TaskA,TaskB,TaskC,OrarioChiusura1
Sportello_ID2,TaskA,TaskD,OrarioChiusura2
```

Dove: 
- Sportello_ID è l'identificatore dello sportello. 
- TaskA/B,... rappresenta i task supportati dallo sportello. 
- OrarioChiusura è l'orario di chiusura dello sportello.

**Nota**: Alcuni sportelli possono supportare più task.

Il file "`clienti.txt`" ha la seguente struttura:

```
NomeCliente1,TaskX,TempoNecessario1,OrarioArrivo1
NomeCliente2,TaskY,TempoNecessario2,OrarioArrivo2
```

Dove:
- TempoNecessario è il tempo necessario al cliente per essere servito.
- TaskX rappresenta il task richiesto dal cliente.
- OrarioArrivo è l'orario in cui il cliente è arrivato.

**Nota**: I clienti all'interno del file **sono ordinati per orario di arrivo**.

Implementare un programma in Python che assegni automaticamente ogni cliente a uno sportello libero (*si assuma che tutti gli sportelli siano liberi e aperti all'arrivo del primo cliente*), se disponibile, in base alle seguenti regole:
- Se più sportelli sono liberi, assegna il cliente al primo sportello in ordine numerico.
- Se tutti gli sportelli che possono supportare il task del cliente sono occupati, stampare un messaggio indicando che il cliente non può essere servito.

**Nota**: Gli orari sono scritti in minuti considerando le 00:00 come 0 e le 23.59 come 1439 (essendoci 1440 minuti in un giorno).

Stampare a video in maniera formattata i seguenti dettagli per ogni cliente servito con successo:

```
[Nome Cliente], Arrivo: [Orario di Arrivo], Uscita: [Orario di Fine Servizio], Sportello: [Sportello di servizio]
```

Nel caso in cui il cliente non possa essere servito, stampare a video il seguente messaggio:

```
[Nome Cliente] non può essere servito/a. Tutti gli sportelli occupati o chiusi.
```

Esempio di output con i files dati:

```
Alice. Arrivo: 750. Uscita: 765. Sportello: 1
Lukas. Arrivo: 755. Uscita: 770. Sportello: 2
Renzo. Arrivo: 765. Uscita: 775. Sportello: 1
Meg. Arrivo: 800. Uscita: 818. Sportello: 2
Bob. Arrivo: 825. Uscita: 845. Sportello: 3
Charlie. Arrivo: 900. Uscita: 910. Sportello: 4
David. Arrivo: 990. Uscita: 1015. Sportello: 4
Michelle non può essere servito/a. Tutti gli sportelli occupati o chiusi.
```
