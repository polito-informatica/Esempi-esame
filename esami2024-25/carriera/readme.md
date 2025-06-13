# Carriera universitaria

#### (Esame proposto il 10-11/02/2025)

Si chiede di realizzare un programma in Python che sia in grado di gestire due liste di record di studenti: uno con le date di immatricolazione e uno con le date di laurea. I record sono memorizzati in due file CSV (`immatricolazione.txt` e `laurea.txt`) e ogni record contiene le seguenti informazioni:

```
immatricolazione.txt
matricola,nome,cognome,data_immatricolazione
```

```
laurea.txt
matricola,nome,cognome,data_laurea
```

Ogni record include: 

- matricola: un identificatore numerico univoco per lo studente 
- nome: il nome dello studente
- cognome: il cognome dello studente
- data_immatricolazione/data_laurea: la data di immatricolazione o di laurea (nel formato AAAA-MM-GG)
- N.B.: non è detto che tutti gli studenti immatricolati siano laureati, mentre vale il viceversa.

Il codice Python dovrà:
- Caricare le liste di immatricolazioni e lauree in opportune strutture dati verificando che:
    - Non ci siano studenti laureati non precedentemente immatricolati e, solo per loro, stampare un messaggio di errore.
    - La data di laurea sia sempre posteriore alla data di immatricolazione (stampare un messaggio in caso di errore ma non interrompere l'esecuzione) 
- Calcolare e stampare la durata della carriera universitaria di ogni studente (in anni, come float).
- Stampare i nomi dei 3 studenti più veloci e dei 3 più lenti a laurearsi, in base alla durata della carriera.

### Esempio

#### File `immatricolazione.txt`

```
matricola,nome,cognome,data_immatricolazione
123,Marco,Rossi,2015-10-01
223,Giorgia,Bianchi,2016-09-15
323,Luca,Verdi,2017-10-01
423,Sara,Neri,2015-09-25
523,Elena,Viola,2016-10-01
723,Pino,Abete,2019-01-01
```

#### File `laurea.txt`

```
matricola,nome,cognome,data_laurea
123,Marco,Rossi,2020-07-10
223,Giorgia,Bianchi,2021-06-15
323,Luca,Verdi,2022-09-30
423,Sara,Neri,2021-07-25
523,Elena,Viola,2021-10-01
623,Alberto,Rosso,2021-10-20
723,Pino,Abete,2018-01-01
```

#### Output

```
Manca la data di immatricolazione di Alberto Rosso
Le date di immatricolazione/laurea di Pino Abete non sono compatibili

Lista studenti e anni di carriera universitaria:  
Marco Rossi: 4.77 anni
Giorgia Bianchi: 4.75 anni  
Luca Verdi: 4.99 anni
Sara Neri: 5.83 anni
Elena Viola: 5.00 anni

I 3 studenti più veloci a laurearsi:  
Giorgia Bianchi: 4.75 anni
Marco Rossi: 4.77 anni
Luca Verdi: 4.99 anni

I 3 studenti più lenti a laurearsi:  
Sara Neri: 5.83 anni
Elena Viola: 5.00 anni
Luca Verdi: 4.99 anni
```