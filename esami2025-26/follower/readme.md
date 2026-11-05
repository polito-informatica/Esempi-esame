# Gestione dei follower

#### (Esame proposto il 26-27/01/2026)


In una semplice piattaforma social, gli utenti sono identificati da un ID numerico e da un nome, mentre le relazioni di “follow” sono rappresentate come coppie di ID in cui il primo utente segue il secondo. Queste informazioni sono conservate in due file CSV separati, entrambi con separatore `;`:

- `utenti.csv`, contenente per ogni riga un utente: id_utente;nome
- `follow.csv`, contenente per ogni riga una relazione di follow (`id_follower` segue `id_followed`): id_follower;id_followed

A partire da questi due file, si richiede di sviluppare un programma Python che analizzi la rete social e produca alcune statistiche di base. Il programma deve:

1. Caricare i due file in memoria, e stampare: - il numero totale di utenti presenti nel sistema; - il numero totale di relazioni di follow registrate.

2. Determinare e stampare per ogni utente quanti follower possiede e quante persone lo seguono.

3. Individuare tutte le relazioni reciproche, cioè quelle coppie di utenti A e B in cui: A segue B, e B segue A. La coppia (A, B) è considerata equivalente alla coppia (B, A), quindi ciascuna relazione reciproca va contata una sola volta. Il programma deve stampare le coppie reciproche presenti nei dati e il loro numero totale.

### Esempio

#### File utenti.csv

    id_utente;nome
    1;Alice
    2;Bob
    3;Carla
    4;Diego
    5;Elena
    6;Franco
    7;Gina
    8;Hassan


#### File follow.csv

    id_follower;id_followed
    1;2
    2;1
    1;3
    3;1
    2;3
    4;3
    5;3
    6;3
    3;4
    7;3
    8;2


#### Output

    Numero totale di utenti: 8
    Numero totale di relazioni di follow: 11
    id  nome    follower followed
    1   Alice   2       2
    2   Bob     2       2
    3   Carla   6       2
    4   Diego   1       1
    5   Elena   0       1
    6   Franco  0       1
    7   Gina    0       1
    8   Hassan  0       1

    Numero totale di coppie reciproche: 3
    Coppie: (1, 3), (3, 4), (1, 2)
