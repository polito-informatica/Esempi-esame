# Testo d'esame "Astrologia Calciatori"

Si realizzi un programma per verificare se l'astrologia abbia degli effetti sulle prestazioni dei giocatori di Calcio.

Un file di testo denominato `sportivi.csv` contiene le informazioni sui calciatori che hanno segnato più di 500 goal (fonte: https://en.wikipedia.org/wiki/List_of_footballers_with_500_or_more_goals), in cui ciascuna riga contiene le
informazioni relative ad uno sportivo. Le informazioni, riportate in campi separati da virgola, sono: il cognome e nome
dello sportivo, il numero di goal segnati nella propria carriera, la nazionalità ed infine la data di nascita (nel
formato gg/mm/aaaa). Le prime righe del file, ad esempio, sono:

    Abe Lenstra,710,Netherlands,27/11/1920
    Alfredo Di Stéfano,513,Argentina,04/07/1926
    Boy Martin,541,Ireland,01/02/1914
    Cristiano Ronaldo,798,Portugal,05/02/1985


Un secondo file chiamato `zodiaco.csv` contiene, per ogni segno zodiacale, le date di inizio e di fine di quel segno
zodiacale (nel formato gg/mm), in campi separati da virgola. Ad esempio:

    Ariete,21/03,20/04
    Toro,21/04,20/05
    ...ecc...

Il programma dovrà leggere entrambi i file, e sommare i goal segnati dai diversi giocatori appartenenti a ciascuno
dei segni zodiacali, per poi creare un istogramma dei goal attribuibili a ciascun segno e stamparlo a video.
L'istogramma dovrà mostrare, per ciascun segno: il nome del segno, il numero totale di goal, una barra di asterischi di
lunghezza proporzionale al punteggio totale. I dati dovranno essere stampati in ordine decrescente di punteggio totale.
La scala dell'istogramma deve essere determinata in modo che la barra più lunga abbia 50 asterischi.

Esempio:

    Aquario    (5283) **************************************************
    Cancro     (3593) **********************************
    Scorpione  (3344) *******************************
    Bilancia   (3257) ******************************
    ... ecc ecc...

**Suggerimento importante**: per il confronto tra le date, si suggerisce di costruire la data, come stringa, nel
formato 'mmgg' (ad esempio il '25/06/2021' diventa '0625'). Con questo formato, il confronto tra le date (di per sé
molto complesso) si riduce ad un semplice confronto lessicografico tra stringhe.

Si ipotizzi che i file presenti non contengano errori.
