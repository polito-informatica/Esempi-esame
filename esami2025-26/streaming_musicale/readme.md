# Piattaforma di Streaming Musicale

#### (Esame proposto il 06/06/2026)


Si chiede di realizzare un programma in Python che sia in grado di analizzare una serie di ascolti musicali da parte di utenti.

I record sono memorizzati in due file CSV distinti (separatore `;`): `brani.csv` e `ascolti.csv`.

#### File brani.csv

    id_brano;titolo;artista;genere;durata_secondi

con

- id_brano: identificativo univoco del brano.

- titolo: titolo del brano.

- artista: nome dell'artista.

- genere: genere musicale.

- durata_secondi: durata del brano, espressa in secondi (numero intero).

#### File ascolti.csv

    id_utente;id_brano;device


- id_utente: identificativo dell'utente che ha effettuato l'ascolto.

- id_brano: identificativo del brano ascoltato (come in brani.csv).

-  device: dispositivo utilizzato per l'ascolto (es. "Mobile", "Desktop").

Si suppone che i formati dei due file siano corretti.

Il codice Python dovrà eseguire le seguenti operazioni:

1. **Caricamento Dati e Statistiche di Base**

    - Caricare i dati da entrambi i file (brani.csv e ascolti.csv) in memoria.
    - Stampare il numero totale di brani presenti nel catalogo.
    - Stampare il numero totale di ascolti registrati nel file ascolti.csv.
    - Stampare il numero di utenti distinti che hanno effettuato almeno un ascolto.

2. **Analisi degli Ascolti per Genere Musicale**

- Calcolare per ogni genere musicale il numero totale di ascolti dei brani di quel genere.

### Esempio

#### File brani.csv

    id_brano;titolo;artista;genere;durata_secondi
    101;Starlight;Muse;Rock;250
    102;Levitating;Dua Lipa;Pop;203
    103;Smooth;Santana;Latin;285
    104;Smells Like Teen Spirit;Nirvana;Grunge;301
    105;Billie Jean;Michael Jackson;Pop;294
    106;Take Five;Dave Brubeck;Jazz;324
    107;Bohemian Rhapsody;Queen;Rock;354
    108;Hips Don't Lie;Shakira;Latin;218
    109;My Heart Will Go On;Celine Dion;Pop;287


#### File ascolti.csv

    id_utente;id_brano;device
    U001;102;Mobile
    U005;101;Desktop
    U001;105;Mobile
    U003;102;Mobile
    U005;107;Tablet
    U001;103;Desktop
    U004;105;Mobile
    U003;108;Desktop
    U005;102;Mobile


#### Output

    Numero totale di brani nel catalogo 9
    Numero totale di ascolti registrati 9
    Numero di utenti distinti   5

    Genere  Ascolti
    Latin       2
    Pop         5
    Rock        2
