# Linea Ferroviaria

#### (Esame proposto il 26-27/01/2026)

Si scriva un programma Python per la gestione di una linea ferroviaria regionale. Il programma deve leggere dal file `corse.txt` l’insieme delle corse programmate per una giornata. Ogni riga del file contiene il codice identificativo della corsa, la sequenza ordinata delle stazioni in cui il treno si fermerà e l’orario di arrivo ad ogni stazione, nel seguente formato:

    CodiceCorsa StazionePartenza:hh:min Stazione1:hh:min Stazione2:hh:min Stazione3:hh:min ................StazioneArrivo:hh:min  


dove CodiceCorsa è una stringa, StazionePartenza e StazioneArrivo sono rispettivamente i nomi della stazione da cui inizia la corsa e quella in cui essa termina; StazioneN indica il nome delle N-esima stazione in cui ferma il treno; infine, hh:min corrisponde all'orario di partenza da ogni stazione. Il programma deve eseguire le seguenti tre operazioni numerate da 1 a 3:

1. **Stampa dell’elenco delle stazioni**: il programma stampa a schermo, in ordine alfabetico, l’elenco di tutte le stazioni servite dai treni della linea, senza duplicati.
2. **Stampa dell’orario**: il programma individua tutte le corse che fermano in una stazione indicata a partire da un certo orario e stampa il risultato a schermo. Per ogni corsa individuata occorre stampare: il codice della corsa, l'orario di partenza e la destinazione della corsa.
3. **Ricerca Viaggio più breve**: il programma cerca e stampa a schermo il viaggio diretto (**senza cambi**) con durata totale minima tra una stazione di partenza e una stazione di arrivo, a partire da un orario indicato. Se non esiste alcun treno diretto, il programma stampa: Non ci sono treni diretti tra le stazioni inserite dopo l’orario specificato.

Le operazioni degli utenti da eseguire sono salvate nel file `operazioni.txt`. Ogni riga del file contiene le informazioni di una sola operazione da eseguire. Quando il primo campo della riga del file `operazioni.txt` è la parola `Stazioni`, occorre eseguire l’operazione 1. Se invece è la parola `Orario`, la riga conterrà anche il nome di una stazione e un orario di partenza, che sono dati di input per eseguire l’operazione 2. Infine, se il primo campo è `Viaggio`, la riga conterrà anche una stazione di partenza, un orario di partenza e una stazione di arrivo, che rappresentano dati di input per eseguire l’operazione 3.

**Suggerimento**: essendo tutte le corse eseguite nella stessa giornata, per confrontare due orari di partenza/arrivo, basta convertili in minuti.

### Esempio

#### File corse.txt

    R101 Torino:08:00 Chivasso:08:18 Santhia:08:40 Vercelli:08:55 Novara:09:10 Oleggio:09:25 SestoCalende:09:40 Gallarate:09:55 Busto:10:05 Milano:10:20

    R102 Milano:07:45 Rho:07:58 Legnano:08:10 Busto:08:18 Gallarate:08:28 SestoCalende:08:42 Oleggio:08:55 Novara:09:10 Vercelli:09:28 Santhia:09:45

    R103 Novara:10:00 Oleglio:10:13 SestoCalende:10:28 Gallarate:10:42 Busto:10:55 Legnano:11:05 Rho:11:18 Milano:11:35

    R104 Vercelli:11:20 Novara:11:35 Oleggio:11:48 SestoCalende:12:02 Gallarate:12:18 Busto:12:30 Legnano:12:42 Rho:12:55 Milano:13:10

    R105 Santhia:12:15 Vercelli:12:30 Novara:12:45 Gallarate:13:10 Busto:13:20 Rho:13:35 Milano:13:50

    R106 Milano:15:00 Gallarate:15:38 SestoCalende:15:52 Oleggio:16:05 Novara:16:20 Vercelli:16:40 Santhia:16:55 Chivasso:17:15 Torino:17:35


#### File operazioni.txt

    Stazioni
    Orario Gallarate 10:00
    Viaggio Novara 11:00 Milano


#### Output:

    Elenco ordinato delle stazioni servite 
    Busto, Chivasso, Gallarate, Legnano, Milano, Novara, Oleggio, Rho, Santhia, SestoCalende, Torino, Vercelli

    Orario per la stazione Gallarate dalle 10:00 in poi:
    R103 10:42; diretto a Milano
    R104 12:18; diretto a Milano
    R105 13:10; diretto a Milano
    R101 15:38; diretto a Torino

    Viaggio più breve da Novara a Milano dalle 11:00 in poi
    Treno: R105
    Partenza: Novara 12:45; Arrivo: Milano 13:50; Durata Viaggio: 1h 5min
