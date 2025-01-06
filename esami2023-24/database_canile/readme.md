# Gestione database canile

#### (Esame proposto il 17/09/2024)


Si chiede di realizzare un programma in Python che sia in grado di gestire una lista di record di animali.

I record sono memorizzati in un file CSV (`dogs.csv`) e ogni record contiene le seguenti informazioni:

```
ID,Name,Breed,Training Level,Obedience Score
``` 
dove:

- ID: è un identificatore numerico univoco per l'animale 

- Name: è il nome del cane 

- Breed: è la razza di cane 

- Training Level: è il livello di addestramento (uno fra i seguenti valori: Beginner, Intermediate, Advanced, Expert).

- Obedience Score: è il punteggio ottenuto in un test (numero float)

La prima riga del file riporta l'intestazione con i nomi dei campi. 

**Per ogni razza e per ogni livello di addestramento**, il programma dovrà elencare **la media dei punteggi ottenuti** dai cani corrispondenti. L'elenco deve essere raggruppato per razze (non è richiesto un ordine particolare). Se per una determinata razza non sono presenti cani con un determinato livello di addestramento, quel livello di addestramento non deve essere elencato fra i risultati.

Infine, il programma deve indicare **qual è la razza** con la media di punteggio più alta per i cani di **livello Expert**.

### Esempio

#### File `dogs.csv` (estratto)

```
ID,Name,Breed,Training Level,Obedience Score
6866-7072,Luna,German Shepherd,Intermediate,58.0
5663-6602,Charlie,Rottweiler,Beginner,73.99
4227-9206,Max,German Shepherd,Advanced,91.1
8237-3584,Sadie,Poodle,Advanced,60.18
9946-1840,Bailey,Yorkshire Terrier,Intermediate,64.33
7025-5197,Bailey,Golden Retriever,Intermediate,70.11
8503-3925,Rocky,Beagle,Beginner,54.11
6821-1190,Daisy,Beagle,Advanced,90.22
1179-6647,Sadie,Yorkshire Terrier,Advanced,81.65
4620-7694,Sadie,German Shepherd,Expert,90.18
2664-1420,Daisy,Poodle,Expert,95.3
```

#### Output:

```
Razza: German Shepherd
    Livello Beginner: media 83.87
    Livello Intermediate: media 70.70
    Livello Advanced: media 91.08
    Livello Expert: media 84.16

Razza: Rottweiler
    Livello Beginner: media 77.13
    Livello Intermediate: media 73.88
    Livello Advanced: media 56.07

Razza: Poodle
    Livello Beginner: media 74.87
    Livello Intermediate: media 73.47
    Livello Advanced: media 77.14
    Livello Expert: media 82.90

Razza: Yorkshire Terrier
    Livello Beginner: media 99.26
    Livello Intermediate: media 77.55
    Livello Advanced: media 71.09
    Livello Expert: media 76.89

Razza: Golden Retriever
    Livello Intermediate: media 66.44
    Livello Advanced: media 69.75
    Livello Expert: media 66.97

Razza: Beagle
    Livello Beginner: media 65.83
    Livello Intermediate: media 54.36
    Livello Advanced: media 78.51
    Livello Expert: media 72.28

Razza: Dachshund
    Livello Beginner: media 64.67
    Livello Intermediate: media 57.12
    Livello Expert: media 86.13

Razza: Boxer
    Livello Beginner: media 62.49
    Livello Advanced: media 85.34
    Livello Expert: media 73.13

Razza: Bulldog
    Livello Beginner: media 72.20
    Livello Intermediate: media 72.83
    Livello Advanced: media 80.98
    Livello Expert: media 77.25

Razza: Labrador Retriever
    Livello Beginner: media 75.97
    Livello Intermediate: media 81.45
    Livello Advanced: media 74.95

La razza con il punteggio medio più alto per il livello Expert è Dachshund.
```
