# Testo d'esame "Ricette"

Si scriva un programma in linguaggio Python per la lettura degli ingredienti necessari a realizzare una ricetta, e il
calcolo del costo e delle calorie della ricetta.

Il programma deve:

- leggere dal file di una ricetta gli ingredienti necessari. In particolare, ogni ricetta è descritta nel seguente
  formato:

  ```
  Ingredienti:
  Nome ingrediente 1;grammi necessari ingrediente 1
  Nome ingrediente 2;grammi necessari ingrediente 2
  ...
  Nome ingrediente n;grammi necessari ingrediente n
  Procedimento:
  Descrizione del procedimento per realizzare la ricetta
  ```

  Si noti che la lista degli ingredienti è preceduta dalla parola chiave "Ingredienti", che gli ingredienti sono
  riportati uno per riga, unitamente alla quantità necessaria (in grammi), e che dopo l'elenco degli ingredienti è
  riportato il procedimento, evidenziato dalla parola chiave "Procedimento".

- leggere da un secondo file `cibi.txt` i dati di dettaglio sul costo e sulle calorie di ogni cibo impiegabile come
  ingrediente delle ricette. In particolare, questo file contiene, per ogni riga il cibo, il costo al kg, e le calorie
  al kg, separati da un punto e virgola.
- gestire eventuali eccezioni in lettura da file
- stampare la lista di ingredienti della ricetta, riportandoli uno per riga e separando nome dell'ingrediente e quantità
  da un " - "
- stampare il numero di ingredienti necessari per realizzare la ricetta
- stampare il costo complessivo della ricetta
- stampare le calorie complessive della ricetta

## Esempio di Esecuzione

Esempio di output del programma, basato sul file `polenta_concia.txt`:

```
Ingredienti: 
Farina di mais - 500.0
Toma - 200.0
Fontina - 200.0
Burro - 200.0

Numero di ingredienti: 4
Costo ricetta: 7.52
Calorie ricetta: 2928.00
```
