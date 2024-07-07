# Trivia Game

#### (Esame proposto il 19/02/2024)

Si vuole realizzare un programma in Python per gestire un gioco di Trivia, basato su domande di cultura generale.

Tutte le domande sono elencate nel file `domande.txt`. Ogni domanda è memorizzata in sei righe consecutive: 

- la prima riga contiene il testo della domanda 

- la seconda riga contiene un numero intero positivo, che indica il livello di difficoltà della domanda 

- la terza riga contiene la risposta corretta 

- la quarta, quinta e sesta riga contengono le risposte errate.

Tra una domanda e la successiva è sempre presente una riga vuota.

#### Esempio file "domande.txt"

    Capitale dell'Italia?
    0
    Roma
    Milano
    Berlino
    Parigi

    Autore del dipinto "L'urlo"?
    2
    Edvard Munch
    Vincent van Gogh
    Pablo Picasso
    Claude Monet

    Lingua ufficiale del Brasile?
    0
    Portoghese
    Spagnolo
    Inglese
    Francese

    Elemento chimico con simbolo "H"?
    1
    Idrogeno
    Ossigeno
    Carbonio
    Ferro

Il numero totale di domande e il numero di domande per ogni livello di difficoltà non sono noti a priori. Il livello massimo di difficoltà non è noto a priori: si garantisce però che il livello minimo è zero e sono presenti domande per ogni livello successivo (fino al livello massimo). Le domande nel file `domande.txt` non hanno alcun ordinamento particolare.

All'inizio del gioco l'utente deve inserire il proprio *Nickname*.

Il programma deve proporre una domanda e la lista di risposte. Il gioco comincia da una domanda di livello di difficoltà 0. Se il giocatore risponde correttamente, il programma incrementa di 1 il livello di difficoltà e propone una nuova domanda.

La domanda proposta è selezionata casualmente da quelle del livello di difficoltà corrente. Anche le risposte proposte devono essere proposte in ordine casuale.

Il giocatore deve rispondere con un numero compreso tra 1 e 4, ed il programma deve verificare tutti i possibili errori di immissione.

Il gioco termina quando il giocatore ha dato una risposta errata oppure quando risponde correttamente ad una domanda di livello massimo.

Per ogni risposta corretta, il giocatore guadagna un punto. Al termine del gioco, il programma visualizza il punteggio raggiunto.

Infine, il programma deve aggiornare il file `punti.txt` (già esistente), che contiene la classifica di tutti i giocatori, uno per riga, nel formato `Nickname punteggio`. Il risultato della partita dovrà essere sommato alla riga corrispondente al nickname inserito, o se il nickname non esiste si dovrà creare una nuova riga. Il file deve essere salvato in ordine decrescente di punteggio.

#### Esempio file "punti.txt"

    Paolo 4
    Lucia 1
    Mario 1
    Giuseppe 0

#### Esempio di esecuzione

    Inserisci il tuo nickname: Marta

    Livello 0) Lingua ufficiale del Brasile?
            1. Spagnolo  
            2. Francese  
            3. Portoghese
            4. Inglese
    Inserisci la risposta: 3
    Risposta corretta!

    Livello 1) Elemento chimico con simbolo "H"?
            1. Ferro
            2. Idrogeno
            3. Carbonio
            4. Ossigeno
    Inserisci la risposta: 2
    Risposta corretta!

    Livello 2) Autore del dipinto "L'urlo"?
            1. Edvard Munch
            2. Claude Monet
            3. Pablo Picasso
            4. Vincent van Gogh
    Inserisci la risposta: 4
    Risposta sbagliata! La risposta corretta era: 1

    Hai totalizzato 2 punti!

Al termine della partita di esempio, il contenuto del file `punti.txt` è il seguente:

    Paolo 4
    Marta 2
    Lucia 1
    Mario 1
    Giuseppe 0
