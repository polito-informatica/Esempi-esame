# Riscaldamento

#### (Esame proposto il 10/09/2025)

Scrivere un programma Python che permette di gestire dati relativi ai consumi di riscaldamento di due edifici gestiti dalla medesima società. Ciascun edificio è descritto da un file di tipo CSV, rispettivamente '`Building1.csv`' e '`Building2.csv`'.

I file CSV contengono le informazioni nel medesimo formato. La prima riga contiene l'intestazione delle colonne ed è costante. Le righe successive contengono le informazioni relative ai consumi in Watt per il riscaldamento a intervalli di un'ora. Le informazioni riportate, separate da virgola (`','`), sono: 
- timestamp, inteso come data (nel formato gg-mm-aaaa) e ora (nel formato hh:mm) separate da spazio; 
- consumo corrispondente (in W). 

Il programma deve segnalare un errore in caso un file risulti mancante o non processabile, e terminare l'esecuzione.

Il programma deve:

1. Riportare la durata del periodo analizzato nei file, riportata in mesi e giorni
2. Calcolare il consumo complessivo mese per mese, comprendendo tutti gli edifici
3. Riportare il consumo massimo mensile complessivo e il consumo minimo mensile complessivo
4. Elencare il consumo complessivo mese per mese
5. Calcolare il consumo giornaliero per ciascun edificio
6. Riportare per ciascuno edificio il consumo medio giornaliero e il consumo massimo giornaliero, riportando in quest'ultimo caso anche la data corrispondente (in caso di parità, la scelta è arbitraria)

## Esempio di Esecuzione

#### Estratto di file "`Building1.csv`"

```
timestamp,value
21-11-16 0:00,0
21-11-16 1:00,0
21-11-16 2:00,0
21-11-16 3:00,0
21-11-16 4:00,0
21-11-16 5:00,0
21-11-16 6:00,0
21-11-16 7:00,1989.304313
21-11-16 8:00,1989.304313
21-11-16 9:00,1989.304313
21-11-16 10:00,1989.304313
21-11-16 11:00,1989.304313
21-11-16 12:00,1989.304313
21-11-16 13:00,1989.304313
...
````

#### Esempio di output:

```
Periodo analizzato: 7 mesi, 175 giorni
Consumi nel periodo analizzato:
- consumo mensile massimo: 1019628.69W
- consumo mensile minimo:  61376.38W

Consumi mensili:
  November: 280746
  December: 1019628
  January : 879074
  February: 640318
  March   : 521610
  April   : 297058
  May     : 61376

Statistiche:
- edificio 1: consumo giornaliero medio 14395.52W, consumo giornaliero massimo 36514.18W (26-12-16)
- edificio 2: consumo giornaliero medio 6746.27W, consumo giornaliero massimo 17111.90W (26-12-16)
```