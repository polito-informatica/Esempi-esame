# Gestione database studenti

#### (Esame proposto il 17/09/2024)


Si chiede di realizzare un programma in Python che sia in grado di gestire una lista di record di studenti.

I record sono memorizzati in un file CSV (studenti.csv) e ogni record contiene le seguenti informazioni:

```
ID,cognome_studente,grado,GPA
```

dove:

* ID: un identificatore numerico univoco per lo studente
* cognome: il cognome dello studente 
* grado: il livello scolastico dello studente (codice alfanumerico) 
* GPA: la media dei voti dello studente (float)

Un secondo file (criteria.txt) di sole 3 righe contiene le seguenti informazioni:

```
<lista ID separati da virgola>
<cognome da ricercare>
<livello scolastico da analizzare>
```

Il codice Python dovrà: 

1. Caricare la lista degli studenti in una struttura dati. 
2. Cercare nella lista e stampare i record degli studenti il cui ID è contenuto nella prima riga del secondo file. 
3. Cercare e stampare i record di tutti gli studenti il cui cognome sia uguale a quello presente nella seconda riga del secondo file. 
4. Stampare la media del GPA degli studenti che appartengono al livello scolastico indicato nella terza riga del secondo file.

### Esempio

#### File `studenti.txt`

```
ID,cognome_studente,grado,GPA
1,Rossi,10A,3.5
2,Bianchi,10B,3.7
3,Verdi,10A,3.9
4,Neri,11A,3.2
5,Viola,11B,3.8
6,Rossi,11B,3.1
```

#### File `criteria.txt`

```
1,3,5
Rossi
10A
```

#### OUTPUT:

```
Studenti trovati per ID:
{'ID': 1, 'cognome_studente': 'Rossi', 'grado': '10A', 'GPA': 3.5}
{'ID': 3, 'cognome_studente': 'Verdi', 'grado': '10A', 'GPA': 3.9}
{'ID': 5, 'cognome_studente': 'Viola', 'grado': '11B', 'GPA': 3.8}

Studenti trovati per cognome:
{'ID': 1, 'cognome_studente': 'Rossi', 'grado': '10A', 'GPA': 3.5}
{'ID': 6, 'cognome_studente': 'Rossi', 'grado': '11B', 'GPA': 3.1}

Media del GPA per il grado 10A: 3.70
```
