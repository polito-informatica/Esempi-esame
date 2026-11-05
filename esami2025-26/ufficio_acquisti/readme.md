# Ufficio Acquisti

#### (Esame proposto il 26-27/01/2026)


Si scriva un programma in Python che gestisca alcune operazioni dell’ufficio acquisti di un’azienda. I dati relativi ai fornitori sono memorizzati in un file chiamato `fornitori.txt`. Ogni riga del file contiene i seguenti dati, separati da uno spazio:

- il codice alfanumerico univoco del fornitore (es. FNT-00123)

- il codice alfanumerico univoco del prodotto fornito (es. PRD-2025-A01)

- il costo unitario in euro

I dati relativi alle richieste di acquisto da gestire sono riportate in un file chiamato `richieste.txt`. Ogni riga del file contiene i seguenti dati, separati da uno spazio:

- il codice alfanumerico univoco della richiesta (es. REQ-000457)

- il codice alfanumerico identificativo della persona che ha effettuato la richiesta (es. USR-0091)

- la data della richiesta in formato DD-MM-YYYY

- il codice del prodotto richiesto

- il numero di unità richieste

Per semplicità, si assuma che per ogni prodotto richiesto esista sempre almeno un fornitore, e che i file siano entrambi non vuoti e formattati correttamente. È richiesto soltanto di gestire opportunamente le eccezioni sollevate dall'eventuale non esistenza dei file.

Il programma deve:

1. Stampare a monitor un report con le seguenti informazioni

    - numero totale delle richieste d'acquisto

    - numero totale di prodotti diversi richiesti

    - l'elenco dei codici delle persone che hanno effettuato richieste, con il numero di richieste effettuate da ciascuna. I codici devono essere riportati in ordine alfabetico uno per riga, come nell'esempio di output sottostante.

2. Generare un file `ordini.txt` con la lista degli ordini da effettuare. Per ogni prodotto richiesto il programma deve

    - sommare tutte le unità richieste di quel prodotto

    - individuare il fornitore con il prezzo più basso

    - calcolare il costo totale

Gli ordini vanno stampati sul file uno per riga in ordine crescente di codice prodotto nel formato:

    codice_prodotto numero_totale_unità codice_fornitore costo_totale_ordine

dove costo_totale_ordine è un numero reale con due cifre decimali.


### Esempio

#### Esempio di file fornitori.txt
    FNT-00123 PRD-2025-A01 5.50
    FNT-00489 PRD-2025-A01 5.20
    FNT-00210 PRD-2025-B15 3.00
    FNT-00123 PRD-2025-C07 12.00

#### Esempio di file richieste.txt
    REQ-000457 USR-0091 01-10-2025 PRD-2025-A01 3
    REQ-000458 USR-1022 01-11-2025 PRD-2025-B15 5
    REQ-000459 USR-0091 01-12-2025 PRD-2025-A01 2
    REQ-000460 USR-5500 02-12-2025 PRD-2025-C07 1
    REQ-000461 USR-0091 02-12-2025 PRD-2025-B15 4

#### Esempio di output a monitor
    Numero totale richieste: 5
    Numero di prodotti diversi: 3
    Persone che hanno effettuato richieste:
      USR-0091: 3 richieste
      USR-1022: 1 richieste
      USR-5500: 1 richieste

#### Esempio di file ordini.txt generato
    PRD-2025-A01 5 FNT-00489 26.00
    PRD-2025-B15 9 FNT-00210 27.00
    PRD-2025-C07 1 FNT-00123 12.00
