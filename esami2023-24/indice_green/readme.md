# Indice Green

#### (Esame proposto il 20/02/2024)

Scrivi un programma in Python che, partendo dai dati sulla popolazione di diverse nazioni, il numero di animali e piante in ognuna di esse, identifichi per ogni nazione:

-    la densità di animali per popolazione,
-    la densità di piante per popolazione e
-    calcoli l'Indice Green.

Si stampino quindi i seguenti risultati:

-    la nazione con la più alta densità di animali per popolazione,
-    la nazione con la più alta densità di piante per popolazione e
-    le prime tre nazioni, in ordine decrescente di Indice Green.

### Input

Il programma dovrà leggere due file di testo: uno contenente i dati sulla popolazione e l'altro contenente il numero di animali e piante in diverse nazioni.

Il primo file, chiamato `population.txt`, contiene i dati sulla popolazione secondo il seguente formato:

    <nome nazione>;<popolazione>

Il secondo file, chiamato `animal_plant_count.txt`, contiene il numero di animali e piante in diverse nazioni secondo il seguente formato:

    <nome nazione>;<numero di animali>;<numero di piante>

Si assuma che il formato di entrambi i file sia corretto e che tutte le nazioni presenti nel file `animal_plant_count.txt` siano anche presenti nel file `population.txt`.

### Calcoli

Il programma dovrà calcolare la densità di animali e piante, per ciascuna nazione, secondo le formule:

    Densità Animali = Numero di animali / Popolazione

    Densità Piante = Numero di piante / Popolazione

Successivamente, si calcoli l'Indice Green per ogni nazione secondo la formula:

    Indice Green(nazione) = media( densità di animali(nazione), densità di piante(nazione) ) * 100

### Output

Occorrerà infine identificare e stampare, rispettando il formato dell'esempio di output proposto:

-    la nazione con la più alta densità di animali,
-    la nazione con la più alta densità di piante e
-    le prime 3 nazioni in ordine decrescente di Indice Green.

### Esempio di output:

    La nazione con il più alto rapporto di animali per popolazione è USA con un rapporto di 0.018.
    La nazione con il più alto rapporto di piante per popolazione è China con un rapporto di 0.0049.
    Le prime 3 nazioni in ordine decrescente di Indice Green sono:
    1. China - Indice Green: 2.45
    2. USA - Indice Green: 2.33
    3. Brazil - Indice Green: 1.35

Infine, stampi le tre informazioni richieste.

#### Esempio di contenuto nel file `population.txt`

    Italy;60360000
    Germany;83190556
    France;67076000
    Spain;47351567
    USA;331002651
    China;1439323776
    India;1380004385
    Brazil;212559417
    Japan;126476461
    Russia;145912025

#### Esempio di contenuto nel file `animal_plant_count.txt`

    Italy;234500;1200000
    Germany;300000;800000
    France;280000;950000
    Spain;200000;600000
    USA;6000000;4500000
    China;8000000;7000000
    India;7000000;5800000
    Brazil;2500000;2200000
    Japan;1800000;1500000
    Russia;3200000;2800000
