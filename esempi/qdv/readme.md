# Esempio d'esame "Qualità della Vita"

Consideriamo gli indicatori della _Qualità della vita_ nelle diverse province italiane, pubblicate da _Il Sole 24 ORE_
il 14/12/2020 e disponibili on-line alla pagina https://github.com/IlSole24ORE/QDV in formato CSV, nel file denominato
*20201214_QDV2020_001.csv*.

Si realizzi un programma Python che dovrà compiere due azioni:

- a partire dai dati presenti nel file, scoprire gli indicatori presenti (campo *INDICATORE*, nella sesta colonna), e
  stamparne in output l'elenco (si noti che esistono 90 indicatori diversi definiti nel file)
- leggere la prima riga del file *indicatore.txt*, che conterrà il nome di uno degli indicatori. A questo punto il
  programma stampi il valore di tale indicatore (campo *VALORE*
  nella quinta colonna) per tutte le province, in ordine decrescente, a fianco del nome della provincia stessa (campo
  *DENOMINAZIONE CORRENTE*, quarta colonna).

## Formato del file dati

Il formato del file contenente i dati è documentato alla pagina https://github.com/IlSole24ORE/QDV e la prima riga
contiene i nomi dei campi. Tale prima riga è la seguente:

    "NOME PROVINCIA (ISTAT)","CODICE NUTS 3 2021","CODICE PROVINCIA ISTAT (STORICO)","DENOMINAZIONE CORRENTE","VALORE","INDICATORE","UNITA' DI MISURA","RIFERIMENTO TEMPORALE","FONTE ORIGINALE"

Tutti i campi sono delimitati da virgole, e i campi di tipo testuale sono ulteriormente delimitati da virgolette doppie
(che non fanno parte del dato). Nota: nel file originale, in alcuni casi il carattere ',' compariva all'interno di
alcuni campi testuali. Questo è stato rimosso nel file fornito in questo esercizio, per semplicità di lettura.

Alcune righe di esempio del file (prese a caso) sono:

    "Torino","ITC11",1,"Torino",-1.073873061,"Sportività 2020 - ""effetto Covid-19""","Indice elaborato in base a 4 indicatori che misurano l'impatto sullo sport","A settembre 2020","Pts Clas"
    "Viterbo","ITI41",56,"Viterbo",6.17,"Tasso di mortalità","Standardizzato per 10mila abitanti","gennaio - agosto 2020","Nebo Ricerche Pa"
    "Pisa","ITI17",50,"Pisa",0.075641026,"Imprenditorialità giovanile","Imprese con titolare under 35 - In % su imprese registrate","A settembre 2020","Infocamere"

Si più assumere che il formato del file sia corretto.

## Esempio

All'avvio il programma mostrerà l'elenco degli indicatori disponibili (nota: l'ordine non è importante):

    Indicatori della qualità della vita:
     1. Assegni sociali
     2. Assorbimento del settore residenziale
     3. Banda larga
     4. Bar
     5. Biblioteche
    ...ecc...

Poi, supponendo che il file *indicatore.txt* contenga la seguente linea:

    Pos attivi

il programma stamperà la classifica delle province secondo tale indicatore (dal valore più grande al più
piccolo):

    Classifica secondo l'indicatore 'Pos attivi': 
    Rimini                 : 102.8882035
    Milano                 : 94.75893491
    Aosta                  : 90.40565414
    Grosseto               : 84.43055461
    Venezia                : 84.37374877
    Siena                  : 81.19051375
    Roma                   : 80.3457155
    ...ecc...
    Crotone                : 35.56156937
    Foggia                 : 35.18359267
    Monza e Brianza        : 33.8484766
    Barletta-Andria-Trani  : 22.59841911
