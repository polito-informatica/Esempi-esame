# Reti Oscure di Neo-Tokyo 7

#### (Esame proposto il 09-10/02/2026)


Nella megalopoli di **Neo-Tokyo 7**, gli *hack-runner* spostano continuamente frammenti di dati attraverso le **reti oscure**. Ogni frammento (pacchetto) può appartenere a categorie diverse, ognuna rappresentata da un tag specifico. I dati disponibili sono contenuti nei seguenti files:

#### File `runners.csv`

File CSV separato da virgola che contiene le informazioni sugli hacker-runner nel seguente formato:

    IDRunner,Alias,Livello

- `IDRunner`: identificatore intero del runner;
- `Alias`: nome in codice;
- `Livello`: intero (più è alto, più il runner è esperto/pericoloso).

#### File `pacchetti.csv`

File CSV separato da virgola che contiene le informazioni dettagliate sui pacchetti trasportati dai runners:

    IDPacchetto,IDRunner,Tag,Dimensione

- `IDPacchetto`: identificatore del pacchetto;
- `IDRunner`: ID del runner che ha gestito il pacchetto;
- `Tag`: stringa identificativa della classe del pacchetto (e.g., ALPHA, BETA, OMEGA, etc...)
- `Dimensione`: intero (dimensione in byte dei dati).

## Obiettivi del programma

L’unità di contro-sorveglianza vi chiede di scrivere un programma Python che:

1. Calcoli la **dimensione totale** (in byte) dei pacchetti trasferiti, per ciascun tag presente.
2. Individui il **runner più pericoloso** come quello che **ha trasferito la quantità maggiore di dati** con tag **`OMEGA`**. Se nessun runner ha trasferito pacchetti `OMEGA`, stampare (nessuno) come nome da indicare
3. Produca infine in uscita un output a schermo organizzato in due sezioni come nell'esempio seguente

### Esempio

Dati i seguenti files in input:

#### runners.csv
    1,NeonShogun,8
    2,ChromeAngel,3
    3,VoidFox,5
    4,HexaDrone,4
    5,Kaito,7
    6,SakuraRift,6
    7,BinaryMonk,2
    8,GhostWire,9
    9,ZeroDay,5
    10,Maelstrom,8
    11,IrisCipher,4
    12,Lumen,3
    13,Patina,2
    14,EchoFrame,6
    15,OrionVex,7

#### pacchetti.csv

    100,1,OMEGA,1200
    101,1,ALFA,150
    102,2,GAMMA,400
    103,3,OMEGA,300
    104,3,BETA,60
    105,4,DELTA,500
    106,4,OMEGA,750
    107,5,ALFA,200
    108,5,OMEGA,2000
    109,6,BETA,120
    110,6,GAMMA,80
    ...
(per brevità, vengono riportate solo le prime righe del file)


si deve ottenere il seguente output:

#### Output

    TAG ALFA: 1965 bytes
    TAG BETA: 2045 bytes
    TAG DELTA: 2515 bytes
    TAG GAMMA: 1705 bytes
    TAG OMEGA: 14360 bytes

    Runner più pericoloso:
    GhostWire (Livello 9) - OMEGA trasferiti: 7500


***Suggerimento***: fate bene attenzione a progettare la struttura dati di supporto per facilitare la soluzione del problema (in particolare, considerate che l'IDRunner è un codice unico, e incluso in entrambi i file di input...)

**NOTA BENE**: non saranno ritenute accettabili soluzioni che possano funzionare solo ed esclusivamente con i file di esempio del compito (**la soluzione deve essere generale** e poter funzionare con qualsiasi file di input)