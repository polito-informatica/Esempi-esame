# Fusione anulare

#### (Esame proposto il 19/02/2024)

Le centrali elettriche a fusione anulare alternano due fasi: fusione nucleare (FN), fusione anulare (FA). La prima fase, FN, consuma del materiale fissile e genera delle scorie. La seconda fase, FA, consuma le scorie generate dalla prima fase e produce materiale fissile utile per la prossima FN. Scrivere un programma python che simuli l'alternarsi delle due fasi.

Nel file `risorse.txt` troviamo tre numeri interi separati da spazio rappresentanti le quantità delle tre risorse (A, B e C) necessarie alla FN.

### La FN:
- per ogni gruppo di risorse che consuma composto esattamente da **10 A**, **3 B** e **7 C**, produce 1 MW (megawatt).
- consuma la quantità massima di gruppi di risorse disponibili proporzionali a quelle indicate.
- per ogni gruppo di risorse consumate genera le seguenti scorie di 2 tipi: **10 D** e **15 E**. Tali scorie si sommano ad eventuali riserve precedenti.

#### Esempio FN

Se le risorse sono 110 A, 40 B, 36 C, 0 D, 0 E.
La FN consuma multipli di 10 A, 3 B e 7 C, quindi in totale consuma 50 A, 15 B, 35 C, lasciando inutilizzati 60 A, 25 B, 1 C, 
producendo 5MW e generando 50 D, 75 E.

### La FA:
- per ogni gruppo di risorse che consuma composto esattamente da **6 D** e **5 E**, produce 2 MW.
-consuma la quantità massima di gruppi di risorse disponibili proporzionali a quelle indicate.
-per ogni gruppo di risorse consumate genera le seguenti scorie di 3 tipi: **5 A**, **7 B** e **11 C**. Tali scorie si sommano ad eventuali riserve precedenti.

#### Esempio FA

Se le risorse sono 10 A, 10 B, 10 C, 10 D, 15 E
la FA consuma solo 6 D, 5 E, lasciando inutilizzati 4 D, 10 E, 
producendo 2MW e generando 5 A, 7 B, 11 C che si sommano alle risorse precedenti: 15 A, 17 B, 21 C, 4 D, 10 E.

Il programma dovrà:
- simulare 1000 cicli anulari, o fermarsi all'esaurimento delle scorte.
- stampare il valore totale di energia prodotta
- stampare il numero del ciclo anulare, partendo da 0, composto dalle due fasi FN e FA, che ha prodotto più energia (in parità scegliere l'ultimo)

## Esempio Generale

#### `risorse.txt`
    15 40 36

#### dati non stampati (risorse alla fine della fase ed energia prodotta):
    inizio 15A 40B 36C 0D 0E
    ciclo anulare numero 0 FN - 5A 37B 29C 10D 15E 1MW
    ciclo anulare numero 0 FA - 10A 44B 40C 4D 10E 2MW
    ciclo anulare numero 1 FN - 0A 41B 33C 14D 25E 1MW
    ciclo anulare numero 1 FA - 10A 55B 55C 2D 15E 4MW
    ciclo anulare numero 2 FN - 0A 52B 48C 12D 30E 1MW
    ciclo anulare numero 2 FA - 10A 66B 70C 0D 20E 4MW
    ciclo anulare numero 3 FN - 0A 63B 63C 10D 35E 1MW
    ciclo anulare numero 3 FA - 5A 70B 74C 4D 30E 2MW
    ciclo anulare numero 4 FN - 5A 70B 74C 4D 30E 0MW


#### stampa:
    energia totale 16MW
    ciclo anulare più produttivo: 2
