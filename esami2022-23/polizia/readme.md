# Polizia

#### (Esame proposto il 30-31/01/2023)

Il poliziotto della narcotici sotto copertura Bob Arctor deve esaminare la trascrizione delle intercettazioni
telefoniche effettuate nella casa in cui lavora in incognito e cancellare tutti i riferimenti che potrebbero
identificarlo. Per aiutarlo dovete sviluppare un programma Python che automatizzi questa procedura.

Le intercettazioni telefoniche sono salvate nel file `intercettazione.txt`, che contiene solo caratteri minuscoli,
spazi, e ‘a capo’, quindi non contiene né punteggiatura né apostrofi. Le parole sono separate usando un numero di spazi
proporzionale alla durata delle pause e, quando cambia la voce registrata, il file va a capo.

Il programma dovrà leggere il file `intercettazione.txt` e scrivere un nuovo file `censurato.txt`, dove il testo originale
sarà modificato eliminando le righe che contengono le parole _bob_ e/o _arctor_ ed eliminando anche le due righe precedenti
e le due righe successive a queste.

Inoltre, il programma deve verificare se l’identità segreta di Bob sia in pericolo. Per farlo, dovrà stampare a video
se, nel testo originale del file `intercettazione.txt`, siano state trascritte sia la parola 'polizia' sia i nomi bob e/o
arctor, e in caso affermativo dovrà stampare qual è la distanza minima (misurate come numero di righe del file) fra la
parola 'polizia' e la più vicina delle parole 'bob' e 'arctor'. Altrimenti dovrà segnalare che la parola polizia e i
nomi Bob e Arctor non sono stati pronunciati insieme.

Nel file `intercettazione.txt` non ci sono parole composte che contengano 'bob', 'arctor' o 'polizia'.

### Esempio di file intercettazione.txt in input

    pronto
    salve signor arctor     come sta
    molto bene ma chiamami bob
    okay   ti chiamavo riguardo alla riparazione del auto
    è tutto okay
    si ma non trovo un pezzo    non posso procedere finché non me lo procuro
    sarà un problema
    non credo    potrei comprarlo al mercato nero ma ho paura della polizia
    procedi lo stesso   la macchina mi serve

### Esempio di file censurato.txt in output

    si ma non trovo un pezzo    non posso procedere finché non me lo procuro
    sarà un problema
    non credo    potrei comprarlo al mercato nero ma ho paura della polizia
    procedi lo stesso   la macchina mi serve

### Testo stampato in output

    la parola polizia è stata pronunciata a 5 righe di distanza dal nome
