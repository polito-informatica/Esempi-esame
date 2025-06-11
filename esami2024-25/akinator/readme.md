# Akinator, il bot indovino

#### (Esame proposto il 27-28/01/2025)

Sviluppare il gioco di “Gira la Ruota” in Python, dove **Akinator**, il bot indovino, deve indovinare una singola parola nascosta, estratta casualmente, selezionando una lettera alla volta in modo casuale.


## Specifiche del Gioco

**Livello di difficoltà della partita:**

All’inizio di ogni nuova partita il bot seleziona casualmente il livello di difficoltà della parola da indovinare (`facile`, `medio`, `difficile`).

**Lettura della parola da file:**

In base al livello di difficoltà selezionato, il programma estrae casualmente la parola da indovinare da uno dei seguenti file:

- `facile.txt`
- `difficile.txt`
- `medio.txt`

I file contengono una parola per riga.

**Visualizzazione della parola:**

La parola selezionata è nascosta e mostrata come una serie di caratteri `_`, dove ogni carattere rappresenta una lettera della parola nascosta.

**Selezione casuale delle lettere:**

Il bot tenta di indovinare una lettera appartenente alla parola nascosta selezionandola casualmente dall'alfabeto.

**Vincoli per la scelta delle lettere:**

Il bot deve escludere le lettere già provate. Non è consentito selezionare numeri, caratteri di punteggiatura o lettere accentate. La scelta delle lettere è insensibile al maiuscolo/minuscolo.

**Verifica:**

Per ogni lettera scelta dal bot:

- Se la lettera è presente nella parola nascosta, essa viene rivelata in tutte le sue posizioni.
- Se la lettera non è presente, il bot perde 1 punto.

**Punteggio:**

Il bot inizia ogni partita con **10 punti**. Per ogni lettera errata, il punteggio si riduce di 1 punto. Il gioco termina quando il bot indovina tutte le lettere della parola o quando i punti scendono a zero.

**Esito della partita:**

Alla fine della partita, il programma mostra un messaggio appropriato: Se il bot ha indovinato la parola, un messaggio di vittoria. Se il bot non ha indovinato la parola, un messaggio di sconfitta con la rivelazione della parola nascosta.

**Ciclo di gioco:**

Dopo la fine di una partita, a prescindere dall’esito, l'utente sceglie se il bot deve giocare una nuova partita: in questo caso si riparte dal punto 1.

**Fine del gioco:**

Alla fine delle partite (quando l'utente non vuole che il bot giochi un'altra partita), il programma mostra:

- Il numero di partite vinte.
- Il numero di partite perse.

## Esempi

### Esempio del file `facile.txt` (i file `medio.txt` e `difficile.txt` sono analoghi)

    gatto
    persona
    computer
    prova

### Esempio di Gameplay

```
Partita numero 1
Il bot seleziona la difficoltà: facile

Punti 10 - La parola da indovinare è: _ _ _ _ _ _ _
    Lettera scelta dal bot: g
    Lettera 'g' non presente
Punti 9 - La parola da indovinare è: _ _ _ _ _ _ _
    Lettera scelta dal bot: a
    Lettera 'a' presente: _ _ _ _ _ _ a
Punti 9 - La parola da indovinare è: _ _ _ _ _ _ a
    Lettera scelta dal bot: T
    Lettera 't' non presente
Punti 8 - La parola da indovinare è: _ _ _ _ _ _ a
    Lettera scelta dal bot: C
    Lettera 'c' non presente
    
------ dopo un po’ di tentativi ------

Punti 3 - La parola da indovinare è: p e r s _ n a
    Lettera scelta dal bot: o
    Lettera ‘o’ presente: p e r s o n a

Complimenti, il bot ha vinto! La parola PERSONA è stata indovinata correttamente

Vuoi continuare a giocare?[S|N] S

Partita numero 2
Il bot seleziona la difficoltà: difficile

Punti 10 - La parola da indovinare è: _ _ _ _ _ _ _ _ _
    Lettera scelta dal bot: a
    Lettera ‘a’ presente: a _ _ _ _ _ a _ _
---- dopo un po’ di tentativi ------
Punti 1 - La parola da indovinare è: a _ _ r o _ a _ _
    Lettera scelta dal bot: i
    Lettera 'i' non presente
    
Peccato, il bot ha perso! La parola da indovinare era ASTRONAVE
Vuoi continuare a giocare?[S|N] N

SESSIONE TERMINATA
    Il bot ha vinto 1 partita/e
    Il bot ha perso 1 partita/e
```