# Gestione Esami

#### (Esame proposto il 09-10/02/2026)


Un sistema automatico per la gestione degli esami fornisce i seguenti due file di log: `presenze.csv` e `postazioni.csv`



Il file `presenze.csv` contiene il registro degli iscritti all’esame. Ogni riga del file è organizzata secondo il seguente formato:

    <matricola>, <nome>, <cds>, <presenza>, <compito>

Di seguito il significato di ciascun campo:

- `<matricola>`: id unico studenti

- `<nome>`: nome e cognome studente

- `<cds>`: corso di studi

- `<presenza>`: Y (se studente presente durante l’esame); N (se assente)

- `<compito>`: versione del compito (A o B) assegnata allo studente

Il file `postazioni.csv` contiene l’elenco delle postazioni in aula e loro occupazione durante l’esame. Ogni riga del file è organizzata secondo il seguente formato:

    <postazione>, <matricola>

Di seguito il significato di ciascun campo:

- `<postazione>`: numero intero che identifica il posto occupato dallo studente durante l’esame; la prima cifra rappresenta il numero della fila, le cifre restanti la postazione nella data fila - per esempio il numero 102 indentifica la postazione numero 2 in fila 1. Si consideri una dimensione fissa dell’aula pari a N=7 file (da 0 a 6) da M=4 postazioni (da 0 a 3), con la postazione 000 nell’ angolo in alto a sinistra. Di conseguenza `postazioni.csv` contiene esattamente 28 righe più una di intestazione.

- `<matricola>`: id unico studente che occupa la postazione; nel caso nessuno abbia occupato la postazione, il campo sarà contrassegnato con tre asterischi `’***’`

Nota: il contenuto di entrambi i file è da considerarsi **NON** ordinato. Si assuma che i file esistano, siano formattati correttamente, congrui e coerenti fra di loro.

Si richiede di scrivere un programma Python che verifichi il corretto posizionamento degli studenti durante la prova. Nello specifico, è previsto che i compiti siano assegnati a scacchiera per ridurre quanto possibile i casi di copiatura. Per esempio, se uno studente ha ricevuto la versione A (o B) le postazioni limitrofe (davanti dietro, a destra e sinistra) dovranno essere vuote oppure occupate da studenti che hanno ricevuto la versione B (o A).

Il programma dovrà dunque stampare a video le matricole degli studenti con delle anomalie, la direzione verso la quale si presenta l’anomalia (`UP`, `DOWN`, `RIGHT`, `LEFT`), l’eventuale matricola con cui si verifica l’anomalia, secondo il seguente formato:

    |___ <matricola> --> <direzione> --> <matricola>

Suggerimento/richiesta: utilizzare una struttura dati composta da:

- una matrice NxM per memorizzare la posizione degli studenti

- un array associativo per memorizzare la versione assegnata a ciascun studente

#### Esempio di file presenze.csv

    matricola,nome,cds,presenza,compito
    S001,Marco Rossi,Ingegneria Informatica,Y,A
    S002,Giulia Bianchi,Ingegneria Informatica,Y,B
    S003,Luca Verdi,Matematica,Y,A
    S004,Sara Neri,Fisica,Y,B
    S005,Paolo Conti,Informatica,Y,B
    S006,Elena Greco,Informatica,Y,A
    S007,Davide Romano,Ingegneria Elettronica,Y,B
    S008,Chiara Fontana,Matematica,Y,A
    S009,Alessandro Riva,Fisica,Y,A
    S010,Francesca Moretti,Ingegneria Informatica,Y,B
    S011,Andrea Colombo,Informatica,Y,A
    S012,Laura Galli,Matematica,Y,B
    S013,Simone Ferri,Fisica,Y,B
    S014,Marta Pellegrini,Ingegneria Informatica,Y,A
    S015,Nicola Villa,Informatica,Y,B
    S016,Valentina Costa,Matematica,Y,A
    S017,Federico Marino,Fisica,N,B
    S018,Irene Lombardi,Ingegneria Elettronica,N,A
    S019,Giorgio De Luca,Informatica,Y,B
    S020,Silvia Rinaldi,Matematica,Y,B

#### Esempio di file postazioni.csv

    postazione,matricola
    000,S001
    001,S002
    002,S003
    003,S004
    100,S005
    101,S006
    102,S007
    103,S008
    200,S009
    201,S010
    202,S011
    203,S012
    300,S013
    301,S014
    302,S015
    303,S016
    400,***
    401,***
    402,S019
    403,S020
    500,***
    501,***
    502,***
    503,***
    600,***
    601,***
    602,***
    603,***

#### Esempio di output a monitor

    ANOMALIE:
    |___ S015 --> DOWN  --> S019
    |___ S019 --> UP    --> S015
    |___ S019 --> RIGHT --> S020
    |___ S020 --> LEFT  --> S019
