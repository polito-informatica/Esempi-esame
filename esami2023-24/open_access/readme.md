# Pubblicazioni Open Access

#### (Esame proposto il 17/09/2024)


Un centro di ricerca richiede lo sviluppo di un applicativo che calcoli alcune statistiche sulle pubblicazioni dei suoi ricercatori, concentrandosi in particolare sulle pubblicazioni Open Access, cioè le pubblicazioni ad accesso libero e gratuito (eventualmente previo pagamento di un costo di pubblicazione pagato dagli autori).

Scrivere un programma Python che faccia questa analisi, prendendo in input due file.

Il primo file, "`publisher_fees.txt`", elenca gli editori di interesse, e riporta in ogni riga: 
- il nome di un editore
- il costo che gli autori devono pagare per ogni pubblicazione Open Access in euro.

I due dati sono separati da un punto e virgola (';').

Il secondo file, "`PublicationData.csv`", è di tipo CSV e usa come separatore il punto e virgola (';'). Il file contiene una riga per ogni pubblicazione del centro di ricerca.

Ciascuna delle righe contiene: 
- un identificativo univoco e permanente della pubblicazione (DOI) 
- l'editore; si assuma che l'editore sia presente nell'elenco del file "`publisher_fees.txt`" 
- l'indicazione se la pubblicazione è open source ('`TRUE`') o no ('`FALSE`') 
- l'anno di pubblicazione (compreso tra il 2015 e il 2020)

Il programma deve leggere i dati contenuti nei file e riportare: 
- le pubblicazioni di ciascun editore, riportando per ogni editore il numero complessivo delle pubblicazioni e la percentuale di queste che sono Open Access 
- l'editore che ha richiesto il costo massimo per coprire le spese relative a pubblicazioni Open Access, considerando tutte le pubblicazioni riportare nel file "`PublicationData.csv`"

### Esempio di Esecuzione

#### Contenuto del file "`publisher_fees.txt`"

```
Wiley; 3000
ACM; 1660
IOP; 1950
MDPI; 2020
Inderscience; 2800
EDP; 1100
```

#### Estratto del file "`PublicationData.csv`"

```
10.1002/acm2.12345;Wiley;TRUE;2018
10.1002/acm2.12364;Wiley;TRUE;2018
10.1002/acm2.12414;Wiley;TRUE;2018
10.1002/acm2.12744;Wiley;TRUE;2019
10.1002/adfm.201705786;Wiley;FALSE;2018
10.1002/adfm.201805094;Wiley;FALSE;2019
10.1002/adfm.201805491;Wiley;TRUE;2018
10.1002/adma.201603823;Wiley;FALSE;2016
10.1002/adma.202005473;Wiley;TRUE;2020
...
```

#### Esempio di output del programma:

```
Pubblicazioni per editore:
ACM          :    0 articoli
EDP          : 1702 articoli,  99.29% open source
IOP          : 2016 articoli,  77.98% open source
Inderscience :   99 articoli,  22.22% open source
MDPI         :  892 articoli, 100.00% open source
Wiley        : 1663 articoli,  38.30% open source

Editore con costo massimo: IOP (3065400)
```
