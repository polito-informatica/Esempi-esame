# Traiettorie Droni

#### (Esame proposto il 30-31/01/2023)

Un file di testo `drones.txt` contiene la descrizione delle traiettorie di volo che una flotta di droni percorre durante una determinata fascia oraria. Si vuole individuare il drone che necessità della batteria con capacita' piu' grande, ergo, il drone con il più alto valore per il seguente rapporto: distanza complessiva coperta / numero di stazioni di ricarica visitate. Seguono ulteriori dettagli e specifiche.

Il formato del file `drones.txt` è il seguente:

    <id_drone:id_station1,id_station2,...,id_stationN>

dove:
- **id_drone** è il codice identificativo e univoco di un drone;
- **id_station** è il codice identificativo e univoco di una stazione di consegna/ricarica

## Esempio

Per esempio, se il file drones.txt fosse il seguente:

    d01:A,B,D
    d02:C,E,D
    d03:F,C
    d04:A,B,E,D
    d05:A,B,A,B
    d06:A,D,A,D,A

ciò significa che il drone **d01** parte dalla stazione **A** e si ferma per depositare e ricaricare nelle stazioni **B** e poi **D**; il drone **d02** invece segue la traiettoria **C->E->D**; il drone **d03** vola da **F** a **C**, e cosi' via. Si noti il drone **d05**, che segue la traiettoria circolare **A->B->A->B**; lo stesso vale per il drone **d06**.

Un secondo file `stops.txt` contiene le coordinate di tutte le stazioni all'interno dell'area di volo. Il formato del file `stops.txt` è il seguente:

    <id_station:x,y>

dove:
- **id_station** è il codice identificativo e univoco di una stazione di ricarica (lo stesso usato nel file `drones.txt`)
- **x,y** è la coordinata **x**=colonna,**y**=riga nello spazio cartesiano che rappresenta l'area di volo; con (0,0) la coordinata dell'angolo in alto a sx dell'area.

## Esempio

### Esempio `stops.txt`

    A:0,1
    B:2,1
    C:1,4
    D:3,5
    E:2,7
    F:0,7

Si facciano le seguenti assunzioni:
- poiche' tra due stazioni i droni volano sempre in linea retta, la distanza tra due stazioni e' quella Euclidea,
- non ci sono limiti al numero di stazioni in una singola traiettoria,
- un drone può toccare la stessa stazione più volte,
- il numero di droni ed il numero di stazioni non è noto a priori,
- non esistono due stazioni con stessa coordinata,
- ogni drone segue una sola traiettoria,
- il contenuto dei file è da considerarsi corretto,

Considerati gli esempi sopra indicati, il programma deve produrre a video il messaggio

    highest battery capacity for d06
    total distance = 20.0
    number of stops = 4

Suggerimento: per la comprensione del testo e degli esempi e' bene disegnare la posizione delle stazioni in una matrice a due dimensioni, ma il programma puo' essere risolto senza ricorrere a strutture dati tabellari.