# Performance mercati

#### (Esame proposto il 27-28/01/2025)


È richiesto di implementare un programma in Python per calcolare e visualizzare il rendimento mensile medio dei principali settori di mercato in cui operano le aziende dell'indice S&P500.

Alcune informazioni operative e di contesto. - L'indice S&P500 lista le principali (502) aziende quotate su borse americane e operanti in 11 diversi settori, quali *Technology*, *Energy*, *Healthcare*, *Real Estate*, etc.

Il file `sp500_companies.csv` contiene la lista delle aziende indicizzate. Per ogni azienda le informazioni di interesse sono il simbolo univoco con cui l'azienda viene identificata in borsa (colonna `Symbol`) ed il settore di mercato dell'azienda (colonna `Sector`). Per esempio, l'azienda `Apple` ha simbolo `AAPL` ed opera nel settore `Technology`.

### Esempio del file `sp500_companies.csv`

```
Exchange,Symbol,Shortname,Longname,Sector,Industry,Currentprice,Marketcap,Ebitda,Revenuegrowth,City,State,Country,Fulltimeemployees,Weight
NMS,AAPL,Apple Inc.,Apple Inc.,Technology,Consumer Electronics,249.79,3.77578E+12,1.34661E+11,0.061,Cupertino,CA,United States,164000,0.06866361
NMS,MSFT,Microsoft Corporation,Microsoft Corporation,Technology,Software - Infrastructure,437.03,3.24927E+12,1.36552E+11,0.16,Redmond,WA,United States,228000,0.059088874
NMS,NVDA,NVIDIA Corporation,NVIDIA Corporation,Technology,Semiconductors,130.68,3.20035E+12,61184000000,1.224,Santa Clara,CA,United States,29600,0.058199382065913345
NMS,AMZN,"Amazon.com, Inc.","Amazon.com, Inc.",Consumer Cyclical,Internet Retail,223.29,2.34789E+12,1.11583E+11,0.11,Seattle,WA,United States,1551000,0.042697164
NMS,GOOGL,Alphabet Inc.,Alphabet Inc.,Communication Services,Internet Content & Information,188.51,2.31724E+12,1.2347E+11,0.151,Mountain View,CA,United States,181269,0.04213971
```

Un secondo file chiamato `sp500_historical.csv` contiene i dati di un mese delle giornate operative delle borse americane organizzati in ordine cronologico crescente (nel file di esempio dal 11/1 al 11/29). Ogni riga del file riporta la data nel formato anglosassone mm/gg/aaaa (colonna `Date`), il simbolo dell'azienda a cui la riga fa riferimento (colonna `Symbol`). Di interesse per l’analisi richiesta è la colonna `Close`, che riporta il valore del titolo alla chiusura delle negoziazioni nella giornata di riferimento. **Si noti che il file potrebbe essere incompleto e quindi non contenere tutte le aziende del S&P500; per esempio l'azienda `Mastercard Incorporated` con simbolo `MA` non è presente.**

### Esempio del file `sp500_companies.csv`

```
Date,Symbol,Close,High,Low,Open,Volume
11/1/2024,MMM,127.22,128.52,126.85,128.47,3068700
11/1/2024,AOS,75.4,76.31,75.03,75.41,811300
…
11/4/2024,MMM,125.85,128.81,125.48,127.24,3642900
11/4/2024,AOS,75.14,76.28,74.8,75.4,716400
…
11/5/2024,MMM,126.52,127.9,124.83,125.5,3943800
11/5/2024,AOS,75.92,75.99,74.8,75,709000
…
```

Il programma deve per ogni settore presente nel file `sp500_companies.csv`:

- Calcolare il rendimento mensile di ogni azienda del settore calcolato come: 100 * (valore di chiusura nell’ultimo giorno del mese - valore di chiusura nel primo giorno del mese / (valore di chiusura nel primo giorno del mese)
- Stampare il rendimento mensile del settore, come media dei rendimenti mensili delle aziende del settore.

Con i dati forniti nei file di riferimento (Novembre 2024), l’output del vostro programma dovrà essere il seguente:

```
Sector: Technology, Average return: 2.79%
Sector: Consumer Cyclical, Average return: 3.40%
Sector: Communication Services, Average return: 2.26%
Sector: Financial Services, Average return: 5.96%
Sector: Consumer Defensive, Average return: 1.38%
Sector: Healthcare, Average return: 1.14%
Sector: Energy, Average return: 5.34%
Sector: Basic Materials, Average return: -1.59%
Sector: Industrials, Average return: 4.64%
Sector: Utilities, Average return: 2.70%
Sector: Real Estate, Average return: 3.93%
```
