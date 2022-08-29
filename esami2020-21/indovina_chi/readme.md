# Testo d'esame "Indovina Chi"

Si realizzi un programma Python per simulare una partita (semplificata) a Indovina Chi.

Indovina Chi è un gioco caratterizzato da 24 personaggi/caricature. Ogni personaggio ha dei tratti distintivi (sesso,
lunghezza e colore dei capelli, occhiali, cappello, baffi, barba o calvizie).

L'obiettivo del gioco è indovinare il personaggio scelto dall'avversario ponendo una serie di domande a cui l'avversario
potrà rispondere con "SI" o "NO".

Il programma da realizzare prevede di svolgere una partita semplificata, nella quale si suppone che il giocatore vinca
se, dopo aver filtrato i personaggi con una serie di domande, è rimasto un solo personaggio.

In particolare, il programma dovrà:

1. leggere le caratteristiche dei personaggi dal file `personaggi.txt` e memorizzarle. Tale file riporta i singoli campi
   separati da un `";"` e contiene una prima riga di intestazione, utile per identificare i campi riportati per ogni
   personaggio.

2. leggere le domande dell'utente da un secondo file (ad esempio, "domande1.txt" o "domande2.txt"). Il file delle
   domande contiene, una per riga, le domande poste dall'utente, nel formato

        nome_caratteristica=valore_caratteristica

(ad esempio, Barba=SI, o Lunghezza Capelli=Corti).

3. stampare a video tutti i personaggi presenti e le relative informazioni

4. mostrare, in seguito a ogni domanda, i personaggi che rispondono a quella caratteristica e alle precedenti (ad
   esempio, se la domanda è "Colore Capelli=Biondo", verranno mostrati solo i personaggi biondi), stampando il numero
   della domanda e la domanda, seguiti dall'elenco dei personaggi

5. stampare a video il risultato finale: in particolare, se alla fine delle domande sarà rimasto un solo personaggio, il
   giocatore ha vinto. Altrimenti, il giocatore ha perso. Sia in caso di vincita che in caso di sconfitta, il programma
   stamperà a video un messaggio nel quale comunica l'esito della partita.

Nota bene: man mano che il giocatore fa domande, l'insieme dei personaggi si riduce sempre di più. Ad esempio, se il
giocatore seleziona prima i personaggi biondi, poi quelli con occhiali, i personaggi che resteranno saranno biondi e con
occhiali (non con capelli castani, rossi, ecc.).

## Esempio di esecuzione del programma con il file "domande1.txt":

	Personaggi del gioco:
	Alex - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Baffi
	Alfred - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Lunghi, Baffi
	Anita - Sesso: Donna, Colore capelli: Biondo, Lunghezza capelli: Lunghi
	Anne - Sesso: Donna, Colore capelli: Nero, Lunghezza capelli: Corti
	Bernard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Cappello
	Bill - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Barba, Pelato
	Charles - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Baffi
	Claire - Sesso: Donna, Colore capelli: Rosso, Lunghezza capelli: Corti, Occhiali, Cappello
	David - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Barba
	Eric - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Cappello
	Frans - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti
	George - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Cappello
	Herman - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Pelato
	Joe - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Occhiali
	Maria - Sesso: Donna, Colore capelli: Castano, Lunghezza capelli: Lunghi, Cappello
	Max - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Baffi
	Paul - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Occhiali
	Peter - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti
	Philip - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Barba
	Richard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Baffi, Barba, Pelato
	Robert - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti
	Sam - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Occhiali, Pelato
	Susan - Sesso: Donna, Colore capelli: Bianco, Lunghezza capelli: Lunghi
	Tom - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Occhiali, Pelato
	
	Mossa 1 - domanda: Colore Capelli =  Biondo 
	Personaggi selezionati:
	Anita - Sesso: Donna, Colore capelli: Biondo, Lunghezza capelli: Lunghi
	Charles - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Baffi
	David - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Barba
	Eric - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Cappello
	Joe - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Occhiali
	
	Mossa 2 - domanda: Lunghezza Capelli =  Corti 
	Personaggi selezionati:
	Charles - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Baffi
	David - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Barba
	Eric - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Cappello
	Joe - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Occhiali
	
	Mossa 3 - domanda: Occhiali =  True 
	Personaggi selezionati:
	Joe - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Occhiali
	
	Gioco terminato, hai vinto! E' stato selezionato:
	Joe - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Occhiali

## Esempio di esecuzione del programma con il file "domande2.txt":

	Personaggi del gioco:
	Alex - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Baffi
	Alfred - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Lunghi, Baffi
	Anita - Sesso: Donna, Colore capelli: Biondo, Lunghezza capelli: Lunghi
	Anne - Sesso: Donna, Colore capelli: Nero, Lunghezza capelli: Corti
	Bernard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Cappello
	Bill - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Barba, Pelato
	Charles - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Baffi
	Claire - Sesso: Donna, Colore capelli: Rosso, Lunghezza capelli: Corti, Occhiali, Cappello
	David - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Barba
	Eric - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Cappello
	Frans - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti
	George - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Cappello
	Herman - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Pelato
	Joe - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Occhiali
	Maria - Sesso: Donna, Colore capelli: Castano, Lunghezza capelli: Lunghi, Cappello
	Max - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Baffi
	Paul - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Occhiali
	Peter - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti
	Philip - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Barba
	Richard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Baffi, Barba, Pelato
	Robert - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti
	Sam - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Occhiali, Pelato
	Susan - Sesso: Donna, Colore capelli: Bianco, Lunghezza capelli: Lunghi
	Tom - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Occhiali, Pelato

	Mossa 1 - domanda: Sesso =  Uomo 
	Personaggi selezionati:
	Alex - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Baffi
	Alfred - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Lunghi, Baffi
	Bernard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Cappello
	Bill - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Barba, Pelato
	Charles - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Baffi
	David - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Barba
	Eric - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Cappello
	Frans - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti
	George - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Cappello
	Herman - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Pelato
	Joe - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Occhiali
	Max - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Baffi
	Paul - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Occhiali
	Peter - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti
	Philip - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Barba
	Richard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Baffi, Barba, Pelato
	Robert - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti
	Sam - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Occhiali, Pelato
	Tom - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Occhiali, Pelato
	
	Mossa 2 - domanda: Lunghezza Capelli =  Corti 
	Personaggi selezionati:
	Alex - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Baffi
	Bernard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Cappello
	Bill - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Barba, Pelato
	Charles - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Baffi
	David - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Barba
	Eric - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Cappello
	Frans - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti
	George - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Cappello
	Herman - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Pelato
	Joe - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Occhiali
	Max - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Baffi
	Paul - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Occhiali
	Peter - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti
	Philip - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Barba
	Richard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Baffi, Barba, Pelato
	Robert - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti
	Sam - Sesso: Uomo, Colore capelli: Bianco, Lunghezza capelli: Corti, Occhiali, Pelato
	Tom - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Occhiali, Pelato
	
	Mossa 3 - domanda: Barba =  True 
	Personaggi selezionati:
	Bill - Sesso: Uomo, Colore capelli: Rosso, Lunghezza capelli: Corti, Barba, Pelato
	David - Sesso: Uomo, Colore capelli: Biondo, Lunghezza capelli: Corti, Barba
	Philip - Sesso: Uomo, Colore capelli: Nero, Lunghezza capelli: Corti, Barba
	Richard - Sesso: Uomo, Colore capelli: Castano, Lunghezza capelli: Corti, Baffi, Barba, Pelato
	
	Peccato, hai perso :-(
