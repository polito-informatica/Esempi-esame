# Materia Oscura

#### (Esame proposto il 20/06/2025)

La dottoressa Malone ha costruito una macchina per comunicare con la materia oscura tramite immagini. Ha bisogno di un programma Python che riconosca le immagini e le traduca in parole.

Il file `dizionario.txt` contiene le immagini e la loro traduzione. Il file contiene gruppi di 6 righe composti così: una riga con la parola legata all'immagine, 5 righe composte da 5 caratteri `'_'` e `'.'` in un ordine specifico.

Le parole e le immagini sono univoche.

Un secondo file, `text.txt`, contiene le immagini 5x5 del messaggio da tradurre, una ogni 5 righe.

Il programma Python deve tradurre il messaggio e stampare a video alcune statistiche: 

- numero di immagini nel messaggio 
- percentuale di punti nel messaggio 
- nome associato all'immagine del vocabolario con più punti 
- testo del messaggio tradotto

## Esempio

#### `dizionario.txt`

```
Alveare
__._.
.____
__.__
_..._
.....
Angelo
.___.
.....
_..._
_..._
__.__
Cammello
.._..
.....
.....
..._.
..._.
Coccodrillo
_.._.
__.._
__...
___._
.....
````

#### `text.txt`

```
__._.
.____
__.__
_..._
.....
.___.
.....
_..._
_..._
__.__
_.._.
__.._
__...
___._
.....
```

### Output

```
Il numero di immagini nel messaggio è 3
La percentuale di punti nel messaggio è 0.53
Il nome dell'immagine del dizionario con più punti è Cammello

Il messaggio è:
Alveare
Angelo
Coccodrillo
```
