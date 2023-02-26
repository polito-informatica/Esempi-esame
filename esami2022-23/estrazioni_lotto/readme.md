# Estrazioni del Lotto

#### (Esame proposto il 13-14/02/2023)

Un giocatore incallito del gioco del Lotto intende elaborare una strategia
"vincente" sulla base delle statistiche dei numeri estratti in passato. 
Tutti i suoi amici e conoscenti con un minimo di competenza in matematica,
statistica o buon senso hanno cercato di convincerlo che i giochi d'azzardo 
sono sempre perdenti, ma egli decide di proseguire nella sua crociata.

Il file "`storico01-oggi.txt`" contiene tutte le estrazioni del Lotto, 
su tutte le 'ruote' (10 ruote corrispondenti alle città sede di estrazione, 
più la undicesima ruota 'nazionale'). Ciascuna estrazione contiene 5 numeri 
interi, non ripetuti, compresi tra 1 e 90 (estremi inclusi).

Il file contiene una riga per ciascuna estrazione, nel formato illustrato dal seguente frammento:

    2022/09/03  TO  17  71  21  9   1
    2022/09/03  VE  38  69  75  87  29
    2022/09/06  BA  80  82  9   26  3
    2022/09/06  CA  79  49  72  35  1

Vi sono 7 campi separati da spazi, in cui il primo è la data di estrazione 
(nel formato anno/mese/giorno), il secondo è la ruota (la sigla della città, 
oppure la sigla RN per la Ruota Nazionale), ed i successivi 5 campi sono i numeri 
estratti.

Il programma deve verificare le 'sovrapposizioni' tra le diverse ruote.
Nello specifico, l'utente deve inserire da tastiera i codici di due Ruote, ed
il programma, analizzando tutte le estrazioni presenti nel file, deve determinare:

- quali numeri siano stati estratti, nella stessa data, nelle due ruote specificate. In tal caso stampare il numero e la data.
- calcolare la frequenza di ciascuno di tali numeri calcolati nel punto precedente, e stamparli in ordine decrescente di frequenza.

**Nota**: per facilità di sviluppo, è anche presente un file `storicoShort.txt` contenente un sottoinsieme dei dati.

**Nota**: i dati delle estrazioni sono ufficiali e sono disponibili alla pagina
https://www.giocodellotto-online.it/lotto/estrazioni/archivio

### Esempio di esecuzione del programma

    Ruote disponibili BA, CA, FI, GE, MI, NA, PA, RM, RN, TO, VE
    Inserisci la  prima  ruota: TO
    Inserisci la seconda ruota: MI
    
    Numero comune  6 in data 2001/01/27
    Numero comune 36 in data 2001/02/10
    Numero comune 22 in data 2001/02/14
    Numero comune 81 in data 2001/02/17
    . . .
    . . .
    Numero comune  7 in data 2022/08/27
    Numero comune 18 in data 2022/08/30
    Numero comune 17 in data 2022/09/03
    Numero comune 38 in data 2022/09/06
    
    Numero    Frequenza
    --------  ---------
          90         19
          82         16
          38         16
          18         15
           1         15
          53         15
          30         15
    . . .
    . . .
          28          5
           4          3
          74          3
          63          1
