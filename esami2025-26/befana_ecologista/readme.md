# Befana Ecologista

#### (Esame proposto il 26-27/01/2026)


Nell'anno 2026 la Befana ha deciso di premiare i cittadini italiani con il miglior senso ecologico, identificando le province nelle quali la raccolta differenziata è più diffusa.

La Befana premierà con i dolciumi le province italiane che abbiano una percentuale di raccolta differenziata maggiore di quella della regione di appartenenza, mentre punirà con il carbone le province con percentuale di raccolta inferiore alla media regionale.

La Befana si basa sulle infomazioni contenute in due file di testo: `regioni.csv` e `province.csv`.

Nel file regioni.csv vi è l'elenco delle 20 regioni italiane, indicando per ciascuna regione la media regionale di raccolta differenziata (nota: l'indicatore rappresenta la percentuale dei rifiuti solidi urbani oggetto di raccolta differenziata sul totale dei rifiuti solidi urbani).

Il file province.csv rappresenta il dato a livello regionale, e ciascuna riga è composta da 3 campi: la regione di appartenenza, il nome della provincia e la percentuale di differenziata.

Il nome della regione presente nel file province.csv coincide esattamente con il nome di una delle regioni del file regioni.csv.

Il programma dovrà stampare, per ciascuna provincia, le seguenti informazioni:

- il nome della provincia
- il nome della regione di appartenenza
- l'indicatore di raccolta differenziata della provincia
- l'indicatore di raccolta differenziata della regione
- il dono consegnato dalla befana (carbone oppure dolciumi)

Si devono stampare prima tutte le province che ricevono dolciumi (in ordine alfabetico), e poi tutte le province che ricevono carbone (sempre in ordine alfabetico). I dati devono essere correttamente incolonnati, con i valori numerici espressi con una cifra decimale.

### Esempio
#### File regioni.csv (estratto parziale)

    ...
    Veneto,77.70
    Friuli Venezia Giulia,72.50
    Emilia Romagna,77.10
    Toscana,66.60
    Umbria,68.80
    Marche,72.20
    Lazio,55.40
    Abruzzo,64.60
    Molise,60.80
    Campania,56.60
    ...

#### File province.csv (estratto parziale)

    ...
    Calabria,Cosenza,58.90
    Calabria,Crotone,43.90
    Calabria,Catanzaro,65.50
    Calabria,Vibo Valentia,59.40
    Calabria,Reggio di Calabria,44.60
    Trentino Alto Adige,Bolzano,69.30
    Trentino Alto Adige,Trento,81.20
    Sardegna,Sassari,71.10
    Sardegna,Nuoro,79.60
    Sardegna,Cagliari,78.20
    Sardegna,Oristano,81.30
    Sardegna,Sud Sardegna,79.40
    ...

#### Esempio di output del programma (estratto parziale)
    Agrigento                   Sicilia                      60.9   55.2    dolciume
    Asti                        Piemonte                     68.9   67.9    dolciume
    Avellino                    Campania                     62.2   56.6    dolciume
    Bari                        Puglia                       66.4   59.0    dolciume
    Belluno                     Veneto                       85.8   77.7    dolciume
    Benevento                   Campania                     72.8   56.6    dolciume
    Bergamo                     Lombardia                    80.5   73.9    dolciume
    ...
    ...
    Vicenza                     Veneto                       79.4   77.7    dolciume
    Viterbo                     Lazio                        66.5   55.4    dolciume
    Alessandria                 Piemonte                     66.1   67.9    carbone
    Ancona                      Marche                       71.4   72.2    carbone
    Aosta                       Valle d'Aosta                69.4   69.4    carbone
    Arezzo                      Toscana                      56.4   66.6    carbone
    Ascoli Piceno               Marche                       68.4   72.2    carbone
    ...
    ...
    Trieste                     Friuli Venezia Giulia        50.8   72.5    carbone
    Venezia                     Veneto                       72.9   77.7    carbone
    Verona                      Veneto                       72.4   77.7    carbone


Nota: dati elaborati da IRES Piemonte, su dati ISTAT e Ispra (https://www.sisreg.it/index.php?option=com_content&view=article&id=90&Itemid=121)