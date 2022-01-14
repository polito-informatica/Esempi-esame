# Testo d'esame "Pedaggi autostradali"

Un file `pedaggi.txt` riporta, uno per riga, la lista completa dei caselli di una determinata autostrada con il relativo
pedaggio, nel formato:

	casello1;casello2;pedaggio

dove `casello1` e `casello2` sono due stringhe che rappresentano rispettivamente il casello di entrata e quello di uscita di
una tratta autostradale, mentre `pedaggio` è un numero reale che rappresenta il costo del relativo pedaggio. Le tratte
autostradali sono riportate in ordine sparso e non consecutivo. Ovvero, se una riga (ad esempio) riporta il pedaggio
della tratta tra Torino e Chivasso, non è detto che la riga successiva riporti la tratta da Chivasso al casello
successivo. Si assuma che il file non sia vuoto e che sia privo di errori di formato o ambiguità (ad esempio, non è
possibile che lo stesso casello di entrata compaia più volte associato a diversi caselli di uscita, e viceversa).

Un secondo file `percorsi.txt` riporta una lista di percorsi, uno per riga, nel formato:

	partenza;destinazione

dove `partenza` e `destinazione` sono due stringhe che rappresentano il punto di partenza e il punto di destinazione di un
percorso. Anche in questo caso, si assuma che il file sia privo di errori di formato.

Si scriva un programma Python che:

1. per ciascun percorso del file `percorsi.txt`, stabilisca se la destinazione è raggiungibile mediante l'autostrada
   in questione. Cioè, stabilisca se esiste una successione di tratte consecutive che ha come primo ingresso il punto di
   partenza e come ultima uscita il punto di destinazione. Se questa successione di tratte esiste, occorre stampare a
   video il numero di tratte di cui si compone e il costo totale del relativo pedaggio, con due cifre decimali. In caso
   contrario, occorre segnalare che la destinazione non è raggiungibile.

2. stampi a video il percorso che (tra quelli individuati come raggiungibili al punto 1) ha il pedaggio totale minimo. (In caso non ci sia alcun percorso raggiungibile, occorre stampare un messaggio apposito).

## Esempio file `pedaggi.txt`:

	Torino;Chivasso;3.50
	Santhia;Vercelli;2.50
	Chivasso;Santhia;3.25
	Magenta;Rho;5.50
	Novara;Magenta;3.00
	Rho;Milano;4.35
	Vercelli;Novara;1.20

## Esempio file `percorsi.txt`:

	Torino;Santhia
	Torino;Milano
	Santhia;Magenta
	Bologna;Magenta
	Santhia;Rho
	Chivasso;Venezia

## Esempio di output del programma:

	Percorso Torino-Santhia: 2 caselli, tariffa totale 6.75 euro 
	Percorso Torino-Milano: 7 caselli, tariffa totale 23.30 euro 
	Percorso Santhia-Magenta: 3 caselli, tariffa totale 6.70 euro 
	Percorso Bologna-Magenta: non raggiungibile
	Percorso Santhia-Rho: 4 caselli, tariffa totale 12.20 euro 
	Percorso Chivasso-Venezia: non raggiungibile

	Il percorso con la minima tariffa è Santhia-Magenta
