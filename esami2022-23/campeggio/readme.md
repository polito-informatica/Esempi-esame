# Campeggio

#### (Esame proposto il 30/06/2023)


Il campeggio ''I braccioli'' vuole sviluppare un programma per calcolare il costo del soggiorno dei suoi clienti. In
particolare, il programma deve:

- leggere le informazioni relative ai clienti dal file `occupazione.txt`. Tale file contiene delle righe formattate come
  nel seguente esempio:

      id_cliente;arrivo;partenza;tipo_abitazione;numero_adulti;numero_bambini;elettricità
      1;01/06/23;09/06/23;tenda;2;0;sì
      2;01/06/23;05/06/23;camper;2;1;no
      ...

  In particolare, in ogni riga sono riportati: l'id del cliente, la data di arrivo e di partenza, il tipo di abitazione (
tenda o camper), il numero di adulti e di bambini, e se il cliente intende utilizzare l'elettricità (sì o no);

- leggere le informazioni relative ai prezzi, per periodo, dal file prezzi.txt. Tale file contiene delle righe
  formattate come nel seguente esempio:

      dal;al;prezzo_tenda;prezzo_camper;prezzo_persona;prezzo_elettricità;
      01/06/23;07/06/23;8.00;15.00;2.00;1.00;
      08/06/23;14/06/23;10.00;17.00;2.00;1.00;
      ...

  In particolare, ogni riga contiene i prezzi relativi a ogni periodo: da quando a quando i prezzi sono validi, il prezzo
per una tenda, il prezzo per un camper, il prezzo per ogni persona (non c'è differenza tra adulti e bambini) e il prezzo
per l'uso dell'elettricità. I prezzi sono giornalieri;

- calcolare il costo del soggiorno di ogni cliente, sulla base dei giorni in cui questo soggiorna nel campeggio, del
  numero di persone, del tipo di alloggio (tenda o camper) e dell'utilizzo o meno dell'elettricità. In particolare, si
  sottolinea che i clienti del campeggio pagano il giorno di arrivo presso la struttura, ma non il giorno di partenza (
  si suppone che i clienti liberino la piazzola in mattinata). Si suppone inoltre che ogni cliente possieda un solo
  camper oppure una sola tenda. Il programma dovrà anche riportare il numero di giorni in cui il cliente soggiorna e
  restituire un output stampato su schermo, formattato come segue:


      cliente: 1, arrivo: 01/06/23, partenza: 09/06/23, tipo: tenda, persone: 2, elettricità: sì, prezzo: 106.0, numero notti: 8
      cliente: 2, arrivo: 01/06/23, partenza: 05/06/23, tipo: camper, persone: 3, elettricità: no, prezzo: 84.0, numero notti: 4
      ...

- il programma deve gestire eventuali eccezioni in apertura dei file.

**NOTA**: per semplicità, è fornito anche il file `calendario.txt`, che riporta tutti i giorni dell'anno di riferimento,
in ordine cronologico uno per riga, con formato gg/mm/aa:

    01/01/23
    02/01/23
    ...
    ...
    31/12/23

L'utilizzo o meno di questo file per calcolare il costo del soggiorno è a discrezione dello studente.

### Esempio di output stampato a schermo

    cliente: 1, arrivo: 01/06/23, partenza: 09/06/23, tipo: tenda, persone: 2, elettricità: sì, prezzo: 106.0, numero notti: 8
    cliente: 2, arrivo: 01/06/23, partenza: 05/06/23, tipo: camper, persone: 3, elettricità: no, prezzo: 84.0, numero notti: 4
    cliente: 3, arrivo: 01/06/23, partenza: 05/06/23, tipo: camper, persone: 4, elettricità: sì, prezzo: 96.0, numero notti: 4
    cliente: 4, arrivo: 05/06/23, partenza: 15/06/23, tipo: tenda, persone: 4, elettricità: no, prezzo: 174.0, numero notti: 10
    cliente: 5, arrivo: 10/06/23, partenza: 20/06/23, tipo: tenda, persone: 5, elettricità: sì, prezzo: 225.0, numero notti: 10
    cliente: 6, arrivo: 10/06/23, partenza: 25/06/23, tipo: camper, persone: 4, elettricità: sì, prezzo: 430.0, numero notti: 15
    cliente: 7, arrivo: 20/06/23, partenza: 30/06/23, tipo: camper, persone: 4, elettricità: sì, prezzo: 325.0, numero notti: 10
    cliente: 8, arrivo: 30/06/23, partenza: 05/07/23, tipo: tenda, persone: 5, elettricità: no, prezzo: 161.0, numero notti: 5
    cliente: 9, arrivo: 30/06/23, partenza: 10/07/23, tipo: camper, persone: 1, elettricità: no, prezzo: 275.0, numero notti: 10
