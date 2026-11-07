# Torneo Videogiochi

#### (Esame proposto il 09-10/02/2026)


Scrivere un programma in Python per gestire un torneo di videogiochi.

I dati da gestire sono memorizzati nei seguenti due file:

#### File giocatori.csv

    nickname;nome

dove nickname è un identificatore unico per ogni giocatore e nome è il suo nome reale

#### File partite.csv

    id_match;nickname1;nickname2;punteggio1;punteggio2

dove ogni riga rappresenta una partita tra nickname1 e nickname2. Vince chi fa più punti; se i punteggi sono uguali, è pareggio.

Il programma Python deve:

1. Caricare i dati in strutture dati opportune e stampare per ogni giocatore - numero di partite giocate - vittorie - sconfitte - pareggi

2. Calcolare i punti totali fatti da ogni giocatore (somma dei punteggi totali realizzati) e stampare i primi 5 giocatori per punti totali (ordine decrescente).

3. Calcolare la percentuale di vittorie = vittorie / partite_giocate e stampare il nickname del giocatore con la percentuale più alta. A parità di percentuale, stamparli tutti.

### Esempio

#### File giocatori.csv

    nickname;nome
    Pro1;Alice
    Pro2;Bob
    Noob1;Carla
    Noob2;Diego
    Elite;Elena
    Casual;Franco


#### File partite.csv

    id_match;nickname1;nickname2;punteggio1;punteggio2
    1;Pro1;Pro2;10;5
    2;Pro1;Noob1;8;8
    3;Noob1;Noob2;3;7
    4;Elite;Pro2;6;6
    5;Elite;Noob2;9;4
    6;Casual;Pro1;2;3
    7;Casual;Noob1;5;5
    8;Pro2;Noob2;7;10
    9;Elite;Casual;4;1


#### OUTPUT

    Statistiche giocatori:
    Pro1   partite: 3  vittorie: 2  sconfitte: 0  pareggi: 1
    Pro2   partite: 3  vittorie: 0  sconfitte: 2  pareggi: 1
    Noob1  partite: 3  vittorie: 0  sconfitte: 1  pareggi: 2
    Noob2  partite: 3  vittorie: 2  sconfitte: 1  pareggi: 0
    Elite  partite: 3  vittorie: 2  sconfitte: 0  pareggi: 1
    Casual partite: 3  vittorie: 0  sconfitte: 2  pareggi: 1

    Primi 5 giocatori per punti totali:
    Pro1   punti: 21
    Noob2  punti: 21
    Elite  punti: 19
    Pro2   punti: 18
    Noob1  punti: 16

    Giocatore con migliore percentuale di vittoria:
    Elite percentuale: 0.6666666666666666
    Noob2 percentuale: 0.6666666666666666
    Pro1 percentuale: 0.6666666666666666
