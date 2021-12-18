# Testo d'esame "Bowling"

Si realizzi un programma strutturato in linguaggio Python che gestisca il punteggio di una partita di bowling. 
Lo score della partita è registrato nel file `bowling.txt` che riporta il punteggio di tutti i giocatori iscritti;
ogni riga del file memorizza le informazioni riguardanti un singolo giocatore.
l formato di ogni riga è il seguente:

    <cognome>;<nome>;<punteggio_tiro_1>;<punteggio_tiro_2>;...;<punteggio_tiro_n>

Si facciano le seguenti assunzioni:

- il numero di giocatori non è noto a priori;
- il numero di tiri di un giocatore non è noto a priori e non è uguale per tutti i giocatori (dipende da quanti strike
  un giocatore ha fatto durante la partita);
- i campi di una riga sono separati tra loro dal punto e virgola;
- non sono possibili casi di omonimia;
- il formato del file è corretto.

Il programma deve:

- caricare le informazioni contenute nel file `bowling.txt`
- restituire la classifica ordinata per punteggi decrescenti stampando a video i
  campi: `<cognome> <nome> <punteggio finale>` incolonnati
- restituire i giocatori che hanno collezionato più ‘10’ (se esistono) e più ‘0’ (se esistono)

## Esempio di file "bowling.txt":

	Rossi;Massimo;7;10;6;5;10;4;9;9;5;10;10
	Verdi;Giuseppe;10;10;6;6;7;9;9;8;9;9;10;10;10
	De Piscopo;Tullio;9;9;8;8;7;7;6;6;0;5
	Montalbano;Salvo;10;10;9;10;10;10;9;10;10;10

## Corrispondente output a schermo generato dal programma

	Il programma deve stampare a video: 
	Verdi		Giuseppe	113
	Montalbano	Salvo	98
	Rossi		Massimo	85
	De Piscopo	Tullio	65
	Montalbano Salvo ha abbattuto tutti i birilli 8 volta/e
	De Piscopo Tullio ha mancato tutti i birilli 1 volta/e 
