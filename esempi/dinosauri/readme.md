# Esempio esame "Dinosauri"

Si scriva un programma in linguaggio Python che simuli una partita al gioco “DINOSAURI”. DINOSAURI è un semplice gioco
di carte per due giocatori. Il mazzo è composto da 30 carte: 10 rosse, 10 verdi e 10 gialle. Sulle rosse è raffigurato
un dinosauro grande, sulle verdi un dinosauro medio e sulle gialle un dinosauro piccolo.

Unica regola: il dinosauro più grosso mangia il dinosauro più piccolo.

Le carte rosse valgono 5 punti, le carte verdi 3 punti, le carte gialle 1 punto. Inizialmente ogni giocatore ha in mano
15 carte, estratte dal mazzo completo di 30 carte, che si trova già mescolato come contenuto del file.

In ogni mano, ciascuno dei due giocatori gira *la prima carta* del suo mazzo e la posa sul tavolo. Se le carte giocate
hanno colori diversi chi ha buttato il dinosauro più grande vince la mano e prende tutte le carte sul tavolo. Se invece
le due carte appena giocate hanno lo stesso colore si lasciano sul tavolo. Vince chi, al termine delle 15 mani,
totalizza il punteggio più alto. Se all'esaurimento delle 15 mani rimangono ancora carte sul tavolo, queste non vengono
conteggiate.

Il programma deve:

- leggere dal file  *mazzo.txt* le 30 carte del mazzo
- distribuire ai due giocatori le carte, distribuendole in ordine alternato (prima carta al giocatore 1, seconda carta
  al giocatore 2, terza al giocatore 1, e così via).
- simulare le 15 mani della partita; per ciascuna mano:
    - giocare la carta girata dal primo giocatore in ogni mano e stamparla a video
    - giocare la carta girata dal secondo giocatore in ogni mano e stamparla a video
    - determinare il vincitore della mano, ed il punteggio corrente dei due giocatori.
- al termine delle 15 mani, stampare il nome del vincitore e il punteggio totale ottenuto dal vincitore.

## Esempio

Ad esempio, supponendo di avere un mazzo di 6 carte, se il file *mazzo.txt* contiene le seguenti carte:

    Gialla 
    Gialla
    Verde 
    Rossa
    Rossa 
    Verde

Il programma dovrà generare il seguente output:

    Punteggio giocatore 1: 0 
    Punteggio giocatore 2: 0 
     
    Mano n. 1 
    Carta giocatore 1: Gialla 
    Carta giocatore 2: Gialla 
    Risultato: Pareggio 
    Punteggio giocatore 1: 0 
    Punteggio giocatore 2: 0 
     
    Mano n. 2 
    Carta giocatore 1: Verde 
    Carta giocatore 2: Rossa 
    Risultato: Vince la mano il giocatore 2 
    Punteggio giocatore 1: 0 
    Punteggio giocatore 2: 10 
     
    Mano n. 3 
    Carta giocatore 1: Rossa 
    Carta giocatore 2: Verde 
    Risultato: Vince la mano il giocatore 1 
    Punteggio giocatore 1: 8 
    Punteggio giocatore 2: 10 
     
    Vince il giocatore 2 con 10 punti. 
