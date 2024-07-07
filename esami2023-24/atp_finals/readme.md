# Sorteggio gironi e calendario ATP Finals 2023

#### (Esame proposto il 19/02/2024)

Per l'ATP Finals 2023, vi è richiesto di gestire le operazioni di sorteggio dei gironi e preparazione del calendario di tutti gli incontri. Avete a disposizione l'elenco dei giocatori qualificati al torneo in un file di testo (`qualificati.txt`). In ogni riga di questo file, sono presenti il numero di testa di serie ed il cognome del giocatore, separati da `,` come nell'esempio seguente:

#### qualificati.txt
    1,Djokovic
    2,Alcaraz
    3,Medvedev
    4,Sinner
    5,Rublev
    6,Tsitsipas
    7,Zverev
    8,Rune


Il sorteggio dei gironi deve rispettare i seguenti vincoli: 

-    la testa di serie numero 1 è inserita nel Gruppo A (verde) e la numero 2 nel Gruppo B (rosso) 
-    le altre teste di serie vengono assegnate ai due gironi estraendo dalle coppie (3,4), (5,6) e (7,8): la prima estratta di ciascuna coppia è inserita nel Gruppo A, l'altra nel gruppo B. 
-    non possono essere inseriti nello stesso girone entrambi i componenti della stessa coppia (per esempio, Rublev n.5 e Tsitsipas n.6 devono essere in due gironi diversi)

Per la preparazione del calendario, l'incontro *Giocatore2 vs Giocatore3* è equivalente all'incontro *Giocatore3 vs Giocatore2*, e la duplicazione deve essere evitata.

Vi è richiesto un programma Python che legga l'elenco dei giocatori qualificati e restituisca tre file di output: 

-    `rosso.txt` e `verde.txt` contenenti i due gironi sorteggiati, in cui devono essere specificati sia i nomi dei giocatori sia il loro numero di testa di serie (in ordine crescente) con la seguente formattazione riga per riga: `numero - Giocatore`
-    `calendario.txt` contenente l’elenco di tutti gli incontri, divisi per girone e per giornata, con la seguente formattazione:

    GIRONE VERDE
    Giornata n:
    Giocatore1 vs Giocatore2
    Giocatore3 vs Giocatore4
    Giornata n+1:
    Giocatore3 vs Giocatore1
    Giocatore2 vs Giocatore4
    GIRONE ROSSO
    Giornata n:
    Giocatore4 vs Giocatore3
    Giocatore1 vs Giocatore2
    Giornata n+1:
    Giocatore2 vs Giocatore4
    Giocatore3 vs Giocatore1

### Suggerimenti

-    Oltre a `random.randint` è possibile utilizzare `random.choice`.
    Esempio di utilizzo: `selected = random.choice([1,2,3])`

### Esempio di files di output generati utilizzando come input `qualificati.txt`:

#### `verde.txt`
    1 - Djokovic
    4 - Sinner
    5 - Rublev
    8 - Rune

#### `rosso.txt`
    2 - Alcaraz
    3 - Medvedev
    6 - Tsitsipas
    7 - Zverev

#### `calendario.txt`

    GIRONE VERDE
    Giornata 1:
    Djokovic vs Sinner
    Rublev vs Rune
    Giornata 2:
    Djokovic vs Rune
    Sinner vs Rublev
    Giornata 3:
    Djokovic vs Rublev
    Rune vs Sinner
    GIRONE ROSSO
    Giornata 1:
    Alcaraz vs Medvedev
    Tsitsipas vs Zverev
    Giornata 2:
    Alcaraz vs Zverev
    Medvedev vs Tsitsipas
    Giornata 3:
    Alcaraz vs Tsitsipas
    Zverev vs Medvedev 