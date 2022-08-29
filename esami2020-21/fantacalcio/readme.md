# Testo d'esame "Fantacalcio"

Nel gioco del fantacalcio, occorre formare una squadra virtuale composta da calciatori reali. I calciatori reali sono
elencati nel file `fantacalcio.txt`, così organizzato:

	cognome, squadra, ruolo, quotazione

I calciatori sono elencati nel file in ordine alfabetico per cognome. Il ruolo del calciatore è uno fra i seguenti:
portiere, difensore, centrocampista, attaccante. La quotazione è un numero intero strettamente positivo e rappresenta il
valore (in FantaMilioni) del calciatore.

La rosa della squadra virtuale è composta da 25 calciatori:

- 3 portieri
- 8 difensori
- 8 centrocampisti
- 6 attaccanti.

Il budget disponibile per formare la squadra è 260 FantaMilioni.

Si scriva un programma per formare la rosa della squadra virtuale. Sono destinati 20 FantaMilioni ai portieri, 40 ai
difensori, 80 ai centrocampisti e 120 agli attaccanti. Per ogni ruolo, il programma acquista il calciatore più costoso
fra quelli che rispettano le due condizioni seguenti:

- la quotazione del calciatore è inferiore o uguale al budget
- dopo l'acquisto, devono rimanere disponibili almeno tanti FantaMilioni quanti sono i calciatori dello stesso ruolo
  ancora da acquistare.

La seconda condizione assicura di poter acquistare tutti i calciatori richiesti per ruolo. Infatti, per ogni ruolo ci
sono molti calciatori con valutazione 1 FantaMilione. Ad esempio, il budget per l'acquisto del primo attaccante è 120 –
5 = 115 FantaMilioni. Se la quotazione dell'attaccante acquistato è 56, il budget rimanente è 120 – 56 = 64. Il budget
per l'acquisto del secondo attaccante è quindi 64 – 4 = 60. Per ogni ruolo, il programma stampa a video l'elenco dei
calciatori acquistati e la loro quotazione.

**N.B.:** Dopo aver acquistato un calciatore, occorre rimuoverlo dalla lista dei calciatori reali per evitare di
acquistarlo una seconda volta.

A parità di quotazione, non ci sono criteri su quale calciatore acquistare (la scelta è libera).

Se il budget per un ruolo non è completamente consumato, si può scegliere se aggiungerlo al budget per il ruolo
successivo oppure perderlo (entrambe le soluzioni vanno bene).

## Esempio file fantacalcio.txt (per brevità, sono riportati solo i portieri, ma il file reale contiene tutti i ruoli):

	Alia, Lazio, portiere, 1
	Aresti, Cagliari, portiere, 1
	Audero, Sampdoria, portiere, 17
	Consigli, Sassuolo, portiere, 14
	Cragno, Cagliari, portiere, 14
	Donnarumma G, Milan, portiere, 25
	Dragowski, Fiorentina, portiere, 21
	Gollini, Atalanta, portiere, 21
	Handanovic, Inter, portiere, 20
	Pau Lopez, Roma, portiere, 18
	Perin, Genoa, portiere, 13
	Skorupski, Bologna, portiere, 11
	Strakosha, Lazio, portiere, 17
	Szczesny, Juventus, portiere, 22

## Esempio output del programma:

	Portieri: Pau Lopez 18 Alia 1 Aresti 1

	Difensori: Hakimi 33 Armini 1 Balogh 1 Buongiorno 1 Calafiori 1 Dragusin 1 Ferigra 1 Khailoti 1
 
	Centrocampisti: Mkhitaryan 39 Chiesa 33 Anderson D 3 Adopo 1 Baldursson 1 Basit 1 Danzi 1 Ebongue 1
 
	Attaccanti: C Ronaldo 56 Immobile 46 Caprari 15 Adorante 1 Caso 1 Cleonise 1
