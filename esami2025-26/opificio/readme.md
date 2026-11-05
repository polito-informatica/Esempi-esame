# Opificio

#### (Esame proposto il 26-27/01/2026)

Monsieur Madeleine gestisce un fiorente opificio di bigiotteria. Tuttavia ha delle difficoltà a gestire il magazzino e la cassa. Scrivere un programma Python per agevolarne la gestione.

Il file `inventario.txt` contiene l'elenco delle materie prime e dei prodotti lavorati presenti in magazzino, ed il saldo della cassa. Il file ha il seguente formato:

    NOME,TIPO,QUANTITA'


Ogni riga rappresenta una voce dell'inventario. I campi sono divisi da una virgola. 

- NOME è il nome del prodotto e non può ripetersi più di una volta.
- TIPO può essere "materia prima", "prodotto lavorato" o "denaro" 
- QUANTITA è un numero.

La cassa è rappresentata dalla riga con NOME franchi e TIPO denaro, sicuramente presente.

Il file `produzione_e_compravendite.txt` contiene l'elenco degli acquisti, delle vendite, della produzione e del consumo. Il file è ordinato per data. Il formato cambia a seconda della categoria (produzione/consumo o compravendita)



Formato produzione (3 PARAMETRI):

    NOME,QUANTITA',DATA


- NOME rappresenta il rappresenta il nome di una materia prima o di un prodotto. 
Tutti i nomi sono già inclusi nel file inventario
- QUANTITA' è un numero. Se è negativo, si tratta del consumo di una materia prima da togliere dall'inventario. Se è positivo, si tratta di un acquisto
- DATA rappresenta la data in formato GG:MM:AAA


Tutti i nomi sono già inclusi nel file inventario

Formato compravendita (4 PARAMETRI):

    NOME,QUANTITA',PREZZO,DATA

- NOME rappresenta il nome di un prodotto. Tutti i nomi sono già inclusi nel file inventario
- QUANTITA' è un numero. Se è negativo, si tratta di una vendita. Se è positivo, si tratta di un acquisto.
- PREZZO indica una spesa totale per l'acquisto di materie prime oppure un guadagno totale. 
I prezzi sono tutti in franchi.
- DATA rappresenta la data in formato GG:MM:AAA

Il processo di produzione include sempre dei consumi e la creazione di un nuovo tipo di prodotto. Le righe riferite allo stesso processo sono sempre contigue, e l'ultima (indicata da un valore di QUANTITA' positivo) rappresenta la creazione del nuovo prodotto, mentre le precedenti sono i consumi di materie prime (indicate da un valore di QUANTITA' negativo) . Possono servire più tipi di materia prima per prodotto. 
Se le materie prime non sono tutte presenti in quantità sufficiente, la produzione è completamente annullata e non avviene nessun consumo.
Se un acquisto di materie prime richiede più franchi di quanti presenti in cassa, l'acquisto è annullato e non avviene nulla. 



Non ci possono essere virgole all'interno dei campi dei file.

Il programma deve stampare a video: 

- il prodotto lavorato presente in maggiore quantità nel file inventario.txt.
- il numero di produzioni tentate (sia quelle riuscite che quelle fallite).
- il numero di produzioni fallite. 
- il numero di acquisti falliti.
- l'inventario finale.

### Esempio

#### File inventario.txt

    anelli in latta,materia prima,2456
    bottoni ornamentali,prodotto lavorato,341
    bracciali,prodotto lavorato,49
    collane,prodotto lavorato,21
    croci,prodotto lavorato,123
    franchi,denaro,12045
    gommalacca,materia prima,124.5
    resina vegetale,materia prima,122.5
    stagno,materia prima,2034.2

#### File produzione_e_compravendite.txt

    croci,-15,600,04:12:1821
    anelli in latta,-800,05:12:1821
    gommalacca,-4.5,05:12:1821
    resina vegetale,-6.5,05:12:1821
    stagno,-8.2,05:12:1821
    bracciali,10,05:12:1821
    gommalacca,-2.5,07:12:1821
    resina vegetale,-3.5,07:12:1821
    stagno,-6.2,07:12:1821
    collane,6,07:12:1821
    bottoni ornamentali,-100,17:12:1821
    anelli in latta,8000,30000,19:12:1821
    gommalacca,20.5,12,20:12:1821
    anelli in latta,-1600,04:01:1822
    gommalacca,-9.2,04:01:1822
    resina vegetale,-12.5,04:01:1822
    stagno,-16.2,04:01:1822
    bracciali,20,04:01:1822
    anelli in latta,800,3000,04:01:1822
    bracciali,-50,4000,06:01:1822
    croci,-12,500,08:01:1822
    resina vegetale,-236.5,05:12:1821
    stagno,-1128.2,05:12:1821
    croci,1000,09:01:18222

#### Esempio di output del programma

    Il prodotto lavorato maggiormente presente è bottoni ornamentali
    Il numero di produzioni tentate è 4
    Il numero di produzioni fallite è 1
    Il numero di acquisti falliti è 1

    Inventario
    anelli in latta,materia prima,856.00
    bottoni ornamentali,prodotto lavorato,241.00
    bracciali,prodotto lavorato,29.00
    collane,prodotto lavorato,27.00
    croci,prodotto lavorato,96.00
    franchi,denaro,14133.00
    gommalacca,materia prima,128.80
    resina vegetale,materia prima,100.00
    stagno,materia prima,2003.60