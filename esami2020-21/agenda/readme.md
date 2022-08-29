# Testo d'esame "Gestione appuntamenti in agenda"

Si realizzi un programma Python che sia in grado di gestire un’agenda elettronica per un anno solare. Tutti gli
appuntamenti sono memorizzati nel file `agenda.txt`, uno per riga, con il seguente formato:

    giorno;ora;descrizione dell’appuntamento

Si facciano le seguenti assunzioni:

1. Il campo `giorno` è codificato da 1 a 365
2. Il campo `ora` è codificato su due cifre [00-23]
3. Il campo `descrizione dell’appuntamento` è una stringa di caratteri
4. Il numero di righe nel file agenda non è noto a priori
5. Ci possono essere più appuntamenti per lo stesso giorno (non alla stessa ora)
6. Non esiste nessun tipo di ordinamento nel file
7. Il formato del file `agenda.txt` è corretto.

Si realizzi un programma che supporti le seguenti opzioni:

- visualizzare, in ordine crescente di orario, tutti gli appuntamenti di una giornata
- inserire un nuovo appuntamento (specificando giorno, ora e descrizione) se allo stesso giorno e alla stessa ora non ne
  è già presente uno. Nel caso non sia possibile inserire l'appuntamento il programma deve stampare il messaggio "*Impossibile inserire appuntamento*"; altrimenti, deve stampare il messaggio "Appuntamento inserito correttamente"
  seguito dalla visualizzazione degli appuntamenti del giorno indicato

Per semplicità si supponga che i comandi siano contenuti nel file `comandi.txt`, uno per riga, e devono essere
processati tutti. I comandi posso essere del tipo:

    v giorno

oppure

    i giorno ora descrizione

## Esempio di file agenda.txt:

	10;12;Pranzo con il capo
	17;09;Esame di Informatica
	17;17;Riunione di condominio
	100;10;Visita dal dottore
	75;19;Aperitivo con amici

## Esempio di file comandi.txt:

	v 17
	i 100 10 Conferenza stampa
	i 120 10 Conferenza stampa

## Messaggi stampati a video dal programma:

	giorno 17 ore 09: Esame di Informatica
	giorno 17 ore 17: Riunione di condominio
	Impossibile inserire appuntamento		
	Appuntamento inserito correttamente
	giorno 120 ore 10: Conferenza stampa
