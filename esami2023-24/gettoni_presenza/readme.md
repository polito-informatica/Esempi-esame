# Gettoni di presenza

#### (Esame proposto il 05/07/2024)

Un file chiamato `presenze.csv`, tratto dalla pagina degli open data del comune di Torino https://servizi.comune.torino.it/consiglio/prg/web/opendata.php, contiene le presenze dei componenti del Consiglio Comunale per l'anno solare 2023. Vengono riportate le presenze dei consiglieri, divise per mese, e i relativi importi lordi corrisposti con il seguente formato:

```
nominativo;periodo;sedute_liquidate;importo_lordo
```

dove nominativo è composto dal cognome e dal nome del consigliere separati da spazio, il periodo è il mese di riferimento (espresso nel formato 2023-MM-GG-2023-MM-GG), seguito dal numero di sedute del consiglio a cui il consigliere ha partecipato nel mese di riferimento; l'ultimo campo identifica l'importo lordo corrisposto per il mese. I campi sono separati dal carattere ";".

Il programma deve:

* stampare, se esistono, i nomi dei consiglieri che non hanno mai partecipato ad una seduta del Consiglio Comunale; se più consiglieri risultano assenti durante tutto l'anno 2023 i loro nomi devono essere stampati consecutivamente e separati da ",". Nel caso in cui tutti i consiglieri abbiano partecipato ad almeno una seduta stampare il messaggio *Tutti i consiglieri hanno partecipato ad almeno una seduta*;

* stampare nome, numero di sedute mensili e importo complessivo percepito per i 5 consiglieri che hanno registrato il maggior numero medio di presenze durante l'anno

NB. il programma deve gestire opportunamente almeno le eventuali eccezioni sollevate in fase di apertura dei file.

### Esempio di contenuto del file in input `presenzeShort.csv`

```
ABBRUZZESE PIETRO;2023-01-01-2023-01-31;26;3075
ABBRUZZESE PIETRO;2023-02-01-2023-02-28;26;3075
ABBRUZZESE PIETRO;2023-03-01-2023-03-31;26;3075
ABBRUZZESE PIETRO;2023-04-01-2023-04-30;26;3075
ABBRUZZESE PIETRO;2023-05-01-2023-05-31;26;3075
ABBRUZZESE PIETRO;2023-06-01-2023-06-30;26;3075
ABBRUZZESE PIETRO;2023-07-01-2023-07-31;26;3075
ABBRUZZESE PIETRO;2023-08-01-2023-08-31;9;1087
ABBRUZZESE PIETRO;2023-09-01-2023-09-30;26;3075
ABBRUZZESE PIETRO;2023-10-01-2023-10-31;26;3075
ABBRUZZESE PIETRO;2023-11-01-2023-11-30;26;3075
AMBROGIO PAOLA;2023-01-01-2023-01-31;0;0
AMBROGIO PAOLA;2023-02-01-2023-02-28;0;0
AMBROGIO PAOLA;2023-03-01-2023-03-31;0;0
AMBROGIO PAOLA;2023-04-01-2023-04-30;0;0
AMBROGIO PAOLA;2023-05-01-2023-05-31;0;0
APOLLONIO ELENA;2023-01-01-2023-01-31;22;2658
APOLLONIO ELENA;2023-02-01-2023-02-28;26;3075
APOLLONIO ELENA;2023-03-01-2023-03-31;26;3075
APOLLONIO ELENA;2023-04-01-2023-04-30;26;3075
APOLLONIO ELENA;2023-05-01-2023-05-31;13;1571
APOLLONIO ELENA;2023-06-01-2023-06-30;25;3021
APOLLONIO ELENA;2023-07-01-2023-07-31;26;3075
APOLLONIO ELENA;2023-08-01-2023-08-31;8;966
APOLLONIO ELENA;2023-09-01-2023-09-30;26;3075
APOLLONIO ELENA;2023-10-01-2023-10-31;26;3075
APOLLONIO ELENA;2023-11-01-2023-11-30;26;3075
BORASI ANNA MARIA;2023-01-01-2023-01-31;21;2537
BORASI ANNA MARIA;2023-02-01-2023-02-28;24;2900
BORASI ANNA MARIA;2023-03-01-2023-03-31;19;2296
BORASI ANNA MARIA;2023-04-01-2023-04-30;26;3075
BORASI ANNA MARIA;2023-05-01-2023-05-31;26;3075
BORASI ANNA MARIA;2023-06-01-2023-06-30;26;3075
BORASI ANNA MARIA;2023-07-01-2023-07-31;26;3075
BORASI ANNA MARIA;2023-08-01-2023-08-31;5;604
BORASI ANNA MARIA;2023-09-01-2023-09-30;26;3075
BORASI ANNA MARIA;2023-10-01-2023-10-31;26;3075
BORASI ANNA MARIA;2023-11-01-2023-11-30;26;3075
CAMARDA VINCENZO ANDREA;2023-01-01-2023-01-31;20;2417
CAMARDA VINCENZO ANDREA;2023-02-01-2023-02-28;26;3075
CAMARDA VINCENZO ANDREA;2023-03-01-2023-03-31;26;3075
CAMARDA VINCENZO ANDREA;2023-04-01-2023-04-30;21;2537
CAMARDA VINCENZO ANDREA;2023-05-01-2023-05-31;26;3075
CAMARDA VINCENZO ANDREA;2023-06-01-2023-06-30;26;3075
CAMARDA VINCENZO ANDREA;2023-07-01-2023-07-31;22;2658
CAMARDA VINCENZO ANDREA;2023-08-01-2023-08-31;7;845
CAMARDA VINCENZO ANDREA;2023-09-01-2023-09-30;25;3021
CAMARDA VINCENZO ANDREA;2023-10-01-2023-10-31;25;3021
CAMARDA VINCENZO ANDREA;2023-11-01-2023-11-30;23;2779
```

#### Output generato dal programma:

```
Il consigliere AMBROGIO PAOLA non ha mai partecipato a sedute del Consiglio Comunale nel 2023 

Consiglieri con più sedute mensili:
ABBRUZZESE PIETRO               24.45   31837.00
AHMED ABDULLAHI ABDULLAHI       24.18   31675.00
BORASI ANNA MARIA               22.82   29862.00
APOLLONIO ELENA                 22.73   29741.00
CAMARDA VINCENZO ANDREA         22.45   29578.00
```