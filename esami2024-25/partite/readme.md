# Partite giocate

#### (Esame proposto il 10-11/02/2025)

Si chiede di realizzare un programma in Python che sia in grado di gestire due liste di record dei giocatori di calcio: una con i dati relativi all'inizio della loro carriera professionistica e una con il totale di partite giocate fino a una determinata data.

I record sono memorizzati in due file CSV (rispettivamente: `inizio_carriera.txt` e `partite_giocate.txt`), contenenti le seguenti informazioni:

**`inizio_carriera.txt`**

```
id_giocatore,nome,cognome,data_inizio_carriera  
```

**`partite_giocate.txt`**

```
id_giocatore,nome,cognome,data_aggiornamento,partite_giocate  
```

Ogni record include:
- `id_giocatore`: un identificatore numerico univoco per il calciatore
- `nome`: il nome del calciatore
- `cognome`: il cognome del calciatore
- `data_inizio_carriera`/`data_aggiornamento`: rispettivamente, la data di inizio carriera oppure la data dell'ultimo aggiornamento (nel formato AAAA-MM-GG)
- `partite_giocate`: il numero di partite giocate dal calciatore fino alla data di aggiornamento

## Obiettivi

Il programma Python dovrà:

1. Memorizzare le informazioni relative all'inizio della carriera e alle partite giocate in opportune strutture dati verificando che:
    - non ci siano record di partite giocate per calciatori non presenti nel file inizio_carriera.txt (stampare un messaggio di errore per ogni incongruenza);
    - la data di aggiornamento delle partite giocate sia sempre posteriore alla data di inizio carriera (stampare un messaggio in caso di errore).
2. Calcolare e stampare il numero medio di partite giocate all'anno per ogni calciatore (come numero reale con due cifre decimali). 
3. Stampare i nomi dei 3 calciatori con la media più alta e dei 3 con la media più bassa di partite giocate all'anno.

**N.B.** I giocatori per cui sono state riscontrate incongruenze o errori al punto 1 devono essere esclusi dalle analisi del punto 2 e 3.
Per semplicità, è lecito assumere che tutti i mesi dell'anno abbiano 30 giorni, e che un anno sia sempre costituito da 365 giorni.

### Esempio

#### File `inizio_carriera.txt`

```
id_giocatore,nome,cognome,data_inizio_carriera
101,Lionel,Messi,2004-10-16
102,Cristiano,Ronaldo,2002-08-14
103,Neymar,Junior,2009-03-07
104,Zlatan,Ibrahimovic,1999-09-19
105,Kylian,Mbappe,2015-12-02
106,Luka,Modric,2003-05-01
```

#### File `partite_giocate.txt`

```
id_giocatore,nome,cognome,data_aggiornamento,partite_giocate
101,Lionel,Messi,2023-06-01,1002
102,Cristiano,Ronaldo,2023-06-01,1150
103,Neymar,Junior,2023-06-01,620
104,Zlatan,Ibrahimovic,2023-06-01,980
105,Kylian,Mbappe,2013-06-01,390
107,Andres,Iniesta,2023-06-01,700
```

#### Output

```
Errore: La data di aggiornamento per Kylian Mbappe non è posteriore alla data di inizio carriera.
Errore: Andres Iniesta non è presente nella lista di inizio carriera.

Numero medio di partite giocate all'anno per ogni calciatore:
Lionel Messi: 53.78 partite/anno
Cristiano Ronaldo: 55.29 partite/anno
Neymar Junior: 43.57 partite/anno
Zlatan Ibrahimovic: 41.34 partite/anno

I 3 calciatori con la media più alta di partite giocate all'anno:
Cristiano Ronaldo: 55.29 partite/anno
Lionel Messi: 53.78 partite/anno
Neymar Junior: 43.57 partite/anno

I 3 calciatori con la media più bassa di partite giocate all'anno:
Zlatan Ibrahimovic: 41.34 partite/anno
Neymar Junior: 43.57 partite/anno
Lionel Messi: 53.78 partite/anno
```