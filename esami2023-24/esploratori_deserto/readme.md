# Gli esploratori nel deserto

#### (Esame proposto il 05-06/02/2024)

Un'azienda specializzata in vacanze 'extreme adventure' vuole valutare come migliorare le possibilità di sopravvivenza dei turisti in caso di situazioni impreviste quali, ad esempio, catastrofi meteorologiche durante un'escursione. A tal scopo, viene commissionata l'implementazione di un simulatore che permetta la raccolta delle statistiche di sopravvivenza. Si riportano di seguito le specifiche per il pacchetto avventura 'desert rose'.

Dopo una tempesta di sabbia, gli esploratori si trovano bloccati senza mezzi di trasporto nel mezzo del deserto e devono cercare di uscirne. I dati degli esploratori sono accessibili tramite il file `survivors.txt.` Per ciascun esploratore vengono riportati un identificativo univoco `id`, le coordinate di partenza `x` e `y`, la velocità `speed` espressa in km/h, il numero massimo di ore di cammino giornaliero `endurance`. Il file è ordinato secondo il campo `id` per ordine crescente.

### Esempio di input `survivors.txt`:

    id,x,y,speed,endurance
    101,117,155,4.882601218952981,10
    104,289,133,6.3657103498491034,9
    109,352,337,3.488151793035853,11
    116,374,261,4.259055631942356,12
    125,112,268,5.736752849438333,10

L'area desertica di interesse è di `250'000` Km^2 ed è rappresentata nel piano cartesiano con un quadrato di lato 500 km il cui angolo inferiore sinistro è centrato nell'origine (coordinata `(0,0)`). Ciascun esploratore è in possesso di una mappa GPS del deserto (risoluzione 1km) su cui sono anche indicate le coordinate '(x,y)' di luoghi specifici quali oasi, gruppi di mercenari, cattedrali e sabbie mobili. Tale mappa è memorizzata in un file `desert.csv` secondo il seguente formato. La prima riga del file riporta i nomi dei campi separati da `','`:

    'coord_x','coord_y', 'location_type'

ogni riga successiva descrive la coordinata di uno specifico luogo, fatto salvo che per ciascuna coordinata il luogo è unico, cioè, nello stesso posto non possono essere presenti luoghi di tipologie differenti. Di seguito un esempio del file:

### Esempio di input `desert.csv`:

    coord_x,coord_y,location_type
    35,33,oasis
    216,329,cathedral
    57,468,oasis
    394,161,oasis
    268,30,oasis
    ...

## Note sul formato dei file e loro contenuti:

I file esistono, il contenuto è corretto, non ci sono righe vuote. I file sono salvati con codifica unicode. Esistono almeno 3 sopravvissuti. Non esistono due luoghi di interesse con le stesse coordinate (le coordinate delle oasi sono uniche).

## Obiettivi della simulazione

Simulare il comportamento degli esploratori considerando che: 

- Ogni esploratore può percorrere al massimo `speed x endurance` km al giorno 
- Se un esploratore può raggiungere uno degli estremi del deserto in una giornata, allora esce dal deserto ed è considerato salvo. 
- Se un esploratore non può uscire dal deserto in una giornata, cerca sulla mappa l'oasi più vicina non ancora visitata e in caso fosse raggiungibile vi si reca. Una volta raggiunta l'oasi l'esploratore si ferma nell'oasi fino al giorno seguente. Il giorno seguente l'esploratore si rimette in viaggio: se possibile esce dal deserto, altrimenti deve controllare se è raggiungibile un'altra oasi. 
- Se un esploratore non può né uscire dal deserto, né ha oasi disponibili all'interno del proprio raggio di percorrenza giornaliero, questo si ferma nell'oasi ma non sopravvive.

## Formato della stampa

1. Stampare la percentuale di esploratori sopravvissuti.
2. Stampare per ogni esploratore non sopravvissuto l'id e le coordinate dell'ultima oasi visitata per recuperare la salma (seguendo l'ordine di ID).

## Suggerimenti:

1. Per calcolare la distanza fra la posizione (x,y) di un esploratore e quella (x', y') di un'oasi usare la distanza euclidea `sqrt((x-x')^2 + (y-y')^2)`.
2. Tenere traccia per ogni esploratore delle oasi visitate.
3. Non è necessario (anzi, è fortemente sconsigliato) creare una tabella che rappresenti il deserto.

## Esempio

### Stampa in output

    Sopravvissuti: 60.00%

    Recupero salme esploratori
    <109>: (363, 362)
    <116>: (411, 263)
