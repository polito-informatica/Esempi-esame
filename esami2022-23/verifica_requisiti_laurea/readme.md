# Verifica requisiti di Laurea

#### (Esame proposto il 13-14/02/2023)

Un'università monitora le carriere universitarie dei propri studenti utilizzando 
un'applicazione che tiene traccia dei dati legati agli appelli sostenuti.
Nello specifico, i dati vengono riportati in un file di nome "`esami.log`", 
che salva i dati relativi agli esami sostenuti con il seguente formato:

    matricola,data_esame,codice_esame,voto

Dove:

- matricola: è unica per studente ed è nel formato S+Numero su 6 cifre
- data_esame: e una stringa nel formato GG/MM/AAAA
- codice_esame: è una stringa alfanumerica di 3 caratteri che indica in modo univoco un esame (ad esempio INF, per informatica o AM1 per Analisi Matematica 1).
- voto: può avere qualsiasi valore tra 18 e 30L (18, 19, ... 30, 30L), oppure può essere la lettera "R" (che indica uno studente insufficiente) o la lettera "A" (che indica uno studente assente).

Dato che un esame può essere sostenuto più volte, è possibile che uno studente
possa comparire in più righe con lo stesso codice esame; in tal caso l'ultimo voto è quello da considerare per la media dei voti di uno studente. I dati compaiono nel file senza un ordine particolare.

In un secondo file di nome "`cfu.dati`" sono salvati i dati relativi ad ogni esame con il seguente formato:

    codice_esame,CFU,obbligatorio

Dove:

- codice_esame: ha lo stesso formato descritto sopra.
- CFU: numero intero compreso tra 1 e 15
- obbligatorio: è 0 (Falso) o 1 (Vero)

Il programma deve elaborare il file contenente tutti gli esami svolti (`esami.log`) 
e stampare a schermo la lista di matricole degli studenti che possono essere
ammessi all'esame finale di laurea. Le condizioni per l'ammissione sono **aver 
accumulato almeno 30 CFU totali di cui almeno 10 CFU obbligatori**.
Uno studente ottiene i CFU solo se l'esame è superato.

La lista stampata a schermo deve contenere le seguenti informazioni accessorie:

- CFU ottenuti, con indicazioni di quelli obbligatori
- Media pesata per i CFU (somma dei prodotti tra voto e CFU di ciascun esame, divisa per il numero di CFU totali). Ai fini delle medie 30L conta come 33, mentre A ed R sono da escludere.

### Esempio di esecuzione

Dato il file di log

    s000001,01/01/2022,in1,A
    s000001,01/01/2022,am1,30
    s000001,20/01/2022,in1,30
    s000001,30/01/2022,scZ,20
    s000002,01/01/2022,am1,30
    s000002,20/01/2022,in2,30
    s000002,30/01/2022,scA,30

ed il file `cfu.dati`

    in1,10,1
    in2,10,1
    am1,10,1
    am2,10,1
    scA,6,0
    scZ,15,0

Produrrà come risultato

    STUDENTE s000001
    Studente con 35 CFU totali; 20 CFU obbligatori, 25.71 di media 
    STUDENTE s000002
    Studente con 26 CFU totali; 20 CFU obbligatori; 30.00 di media; no laurea
