# Forza quattro

#### (Esame proposto il 05-06/02/2024)

Si vuole realizzare un programma per giocare a "Forza 4". Il gioco "Forza 4" è simile al gioco del "Tris", poichè richiede che, per vincere, i giocatori creino una fila di 4 pedine dello stesso colore (in verticale, orizzontale, e diagonale). L'elemento fondamentale del gioco, che lo rende del tutto originale, è la "forza di gravità": la scacchiera è posta in verticale fra i giocatori, e le pedine vengono fatte cadere lungo una griglia verticale, in modo tale che una pedina inserita in una certa colonna vada sempre a occupare la posizione libera situata più in basso nella colonna stessa.

La griglia del gioco è formata da sei righe e sette colonne.

In particolare, il programma deve: 

- preparare la griglia a inizio partita e stamparla. Ogni posizione vuota della griglia è indicata con il carattere "-"; 

- leggere le mosse dei giocatori dal file `mosse.txt`. Tale file contiene delle righe, in numero non noto a priori, formattate come le seguenti:

    G1 0  
    G2 1  
    G1 2  
    G2 2

In cui il primo campo è il giocatore (`G1` o `G2`) e il secondo campo è la colonna in cui ha inserito la pedina (si supponga che le colonne siano rappresentate da indici da `0` a `6`, da sinistra a destra). Per semplicità, si assuma che il file non contenga nessun errore di formato. Quindi, è richiesto di gestire soltanto l'eccezione legata ad una eventuale non esistenza del file.

- una volta letta la mossa, il programma dovrà "inserire" la pedina del giocatore nella griglia, tenendo conto della forza di gravità (la pedina scende fino alla posizione libera più in basso). Si noti che, in una cella della griglia **non** possono esserci contemporaneamente due pedine, bensì, quando vengono fatte cadere dall'alto, le pedine si posizionano una sopra l'altra; 

- una volta identificata la cella della griglia in cui è finita la pedina del giocatore, il programma dovrà aggiornare la griglia, inserendo il simbolo `"O"` per il giocatore 1 e `"X"` per il giocatore 2, e dovrà stampare chi è che ha appena effettuato la mossa, e la griglia aggiornata; 

- a ogni nuova mossa, il programma dovrà verificare se il giocatore che ha appena effettuato la mossa ha vinto, controllando se è presente una sequenza di quattro pedine uguali (di fila) in orizzontale, verticale e diagonale. Per semplicità, si supponga che ci possano solo essere combinazioni di quattro pedine che iniziano dall'ultima pedina inserita, e proseguono in una sola direzione. In altre parole, il programma deve verificare se esistono quattro pedine uguali a partire dall'ultima inserita, verificando le seguenti direzioni: 1) verso sinistra; 2) verso destra; 3) verso il basso; 4) in diagonale verso il basso a sinistra; 5) in diagonale verso il basso a destra;

- nel caso in cui il giocatore avesse vinto, il programma deve stampare a video chi ha vinto e dopo quante mosse (complessive) ha vinto. Dopo la vittoria, il programma non deve più lasciar proseguire il gioco anche se nel file ci fossero altre mosse rimanenti.

# Esempio

    Griglia vuota
    -------
    -------
    -------
    -------
    -------
    -------

    Gioca il giocatore G1
    -------
    -------
    -------
    -------
    -------
    O------

    Gioca il giocatore G2
    -------
    -------
    -------
    -------
    -------
    OX-----

    Gioca il giocatore G1
    -------
    -------
    -------
    -------
    -------
    OXO----

    Gioca il giocatore G2
    -------
    -------
    -------
    -------
    --X----
    OXO----

    Gioca il giocatore G1
    -------
    -------
    -------
    -------
    -OX----
    OXO----

    Gioca il giocatore G2
    -------
    -------
    -------
    -------
    -OX----
    OXOX---

    Gioca il giocatore G1
    -------
    -------
    -------
    --O----
    -OX----
    OXOX---

    Gioca il giocatore G2
    -------
    -------
    -------
    -XO----
    -OX----
    OXOX---

    Gioca il giocatore G1
    -------
    -------
    -------
    -XO----
    -OXO---
    OXOX---

    Gioca il giocatore G2
    -------
    -------
    -------
    -XOX---
    -OXO---
    OXOX---

    Gioca il giocatore G1
    -------
    -------
    ---O---
    -XOX---
    -OXO---
    OXOX---

    Ha vinto G1 in 11 mosse
