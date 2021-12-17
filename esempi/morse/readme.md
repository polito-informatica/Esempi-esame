# Esempio d'esame 'Morse'

Si scriva un programma in linguaggio Python per la codifica e decodifica di un testo con l'alfabeto Morse. L'alfabeto
Morse è un codice che assegna, ad ogni lettera dell'alfabeto, numero o simbolo di punteggiatura, un codice a lunghezza
variabile, costituito da punti e linee.

La tabella di conversione è contenuta nel file *morse.txt*, di cui si rappresentano le prime righe:

    A .-
    B -...
    C -.-.
    D -..
    E .
    F ..-.
    G --.
    (eccetera...)

Su ogni linea, il primo carattere rappresenta il simbolo alfamumerico, ed è seguito dalla sequenza di punti e linee
corrispondente, separati da uno spazio.

Il programma legge dal file *comandi.txt* la sequenza di traduzioni da compiere. Il file è composto di più righe, e
ciascuna riga è composta da due campi separati da uno spazio:

- il primo campo contiene *c* occorre **c**odificare (da testo a Morse), o contiene *d* se occorre **d**ecodificare (da
  Morse a testo) un messaggio
- il nome del file da codificare/decodificare. Tale file conterrà una sola linea di testo.

Il programma dovrà quindi produrre in output la traduzione (codifica/decodifica) dei vari file richiesti.

## Note

Il programma, nel caso di codifica, dovrà saltare la codifica di tutti i caratteri non presenti nel file *morse.txt*, e
non dovrà distinguere tra caratteri minuscoli e maiuscoli.

Il programma, nel caso di codifica, dovrà separare con uno spazio i simboli Morse stampati come risultato.

Nel caso di decodifica si assuma che il testo da decodificare consista di simboli Morse separati con uno spazio.
Eventuali simboli Morse non riconosciuti devono essere ignorati.

Si assuma che non vi siano errori di formato nei file.

## Esempio di Esecuzione

Supponiamo che il file *comandi.txt* contenga:

    c testo.txt
    d codice.txt

che il file  *testo.txt* contenga:

    Mettetevi in salvo!

e che il file *codice.txt* contenga:

    ... .. ... .- .-.. ...- .. -.-. .... .. .--. ..- --- -.--.-

Il risultato stampato in output sarà:

    Codifica del file testo.txt:
    -- . - - . - . ...- .. .. -. ... .- .-.. ...- --- 
    Decodifica del file codice.txt:
    SISALVICHIPUO'

