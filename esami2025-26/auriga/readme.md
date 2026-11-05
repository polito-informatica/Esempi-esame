# Le Rotte Stellari della Confederazione Auriga

#### (Esame proposto il 26-27/01/2026)

Nell’anno 7421, la **Confederazione Auriga** governa decine di sistemi stellari collegati da rotte iperspaziali. Ogni nave cargo effettua numerosi salti tra portali, trasportando una sostanza rarissima: la **Xenonite**, fondamentale per alimentare gli scudi delle colonie più remote.

L’**Istituto Logistico Intergalattico** vuole analizzare i flussi commerciali di Xenonite per capire: 

- quali classi di nave contribuiscono di più al trasporto, 
- quali singole navi sono più efficienti rispetto alla loro capacità di carico.

I dati per questa analisi sono inclusi in due file di testo.

#### File `navi.csv`

File CSV con separatore **punto e virgola** (`;`).
Ogni riga rappresenta una nave della Confederazione con il seguente formato:

    ID;NomeNave;Classe;Capacita

- `ID`: valore intero, identificatore univoco della nave
- `NomeNave`: nome della nave
- `Classe`: una delle tre stringhe: `Corvetta`, `Freighter`, `Titan`
- `Capacita`: intero che rappresenta la capacità massima di Xenonite trasportabile in un singolo salto

Esempio:

    1;Solar Breeze;Corvetta;80

#### File `salti.log`

File di log in formato testuale con **uno spazio** come separatore. Ogni riga descrive un salto iperspaziale effettuato da una nave, con la quantità di Xenonite trasportata in quel salto con il formato:

    DATA IDNave QUANTITA

- `DATA`: stringa con la data del salto (formato `YYYY-MM-DD`)
- `IDNave`: identificatore della nave, corrispondente a un ID presente in `navi.csv`
- `QUANTITA`: quantità di Xenonite trasportata in quel salto (valore intero)

Esempio:

    7421-03-12 1 35


Si assume che tutti gli ID presenti nel file dei salti corrispondano a navi definite in `navi.csv`.

### Obiettivo del programma

Scrivere un programma in Python che:

1. Per ogni **classe di nave** (`Corvetta`, `Freighter`, `Titan`) calcoli:
    - il **totale complessivo** di Xenonite trasportata da **tutte le navi** di quella classe;
    - la **media per salto** (totale Xenonite della classe diviso il numero totale di salti effettuati da tutte le navi di quella classe).
2. Per ogni **nave**, calcoli:
    - il **totale di Xenonite trasportata** da quella nave (somma di tutte le quantità dei salti registrati per la nave);
    - la sua **efficienza**, definita come:` efficienza = (totale_Xenonite_nave) / (capacita_nave * salti_nave)`
3. Produca in uscita due sezioni:

**Sezione A – Riepilogo per classe**

Per ogni classe (**in ordine alfabetico**), stampare il totale trasportato e la media per salto con il seguente formato:

    Classe: <nome_classe>
        Totale Xenonite: <totale>
        Media per salto: <media_con_due_decimali>

**Sezione B – Classifica di efficienza**

Stampare l’elenco delle navi ordinate per **efficienza decrescente** con il seguente formato:

    Classifica Efficienza:
    1. <NomeNave> - Efficienza: <valore_con_due_decimali>
    2. ...

In caso di parità di efficienza, l’ordine tra navi con lo stesso valore non è rilevante.

### Esempio

#### File navi.csv

    1;Solar Breeze;Corvetta;80
    2;Iron Whale;Freighter;150
    3;Obsidian Crown;Titan;300
    4;Silver Dart;Corvetta;90


#### File salti.log

    7421-03-12 1 35
    7421-03-12 2 70
    7421-03-12 3 120
    7421-03-13 1 20
    7421-03-13 3 60
    7421-03-13 4 45


#### Output

    Classe: Corvetta
        Totale Xenonite: 100
        Media per salto: 33.33
    Classe: Freighter
        Totale Xenonite: 70
        Media per salto: 70.00
    Classe: Titan
        Totale Xenonite: 180
        Media per salto: 90.00

    Classifica Efficienza:
    1. Silver Dart - Efficienza: 0.50
    2. Iron Whale - Efficienza: 0.47
    3. Solar Breeze - Efficienza: 0.34
    4. Obsidian Crown - Efficienza: 0.30

NOTA BENE: non saranno ritenute accettabili soluzioni che possano funzionare solo ed esclusivamente con i file di esempio del compito (la soluzione deve essere generale e poter funzionare con qualsiasi file di input).