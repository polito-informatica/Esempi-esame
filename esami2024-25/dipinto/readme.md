# Dipinto

#### (Esame proposto il 20/06/2025)


Lily Briscoe sta realizzando un dipinto, ma non sa esattamente dove posizionare i vari elementi per ottenere la resa migliore. Per aiutarla, è necessario realizzare un programma in linguaggio Python che permetta di comporre un’immagine partendo da altre più piccole.

Tutte le immagini sono rappresentate da file di testo, in cui ogni carattere corrisponde a un pixel.

Il programma deve leggere il file `input.txt`, contenente, uno per riga, i nomi dei file con le immagini di input, seguiti da due numeri separati da uno spazio, che indicano dove l’immagine contenuta nel file vada inserita nell’immagine finale. La posizione si riferisce a riga e colonna dell'immagine di output in cui si posizionerà l’angolo in alto a sinistra dell’immagine di input. Il pixel in alto a sinistra nell'immagine finale ha coordinate 0, 0.

All’interno delle immagini di input, i numeri da 0 (nero) a 9 (bianco) fanno riferimento alla scala di grigi, mentre il simbolo X indica un pixel trasparente.

L’immagine finale va stampata a console, e deve contenere **10 righe e 10 colonne**. Tutti i pixel dell'immagine finale sono inizialmente bianchi (inizializzati a 9).

Nel fare le operazioni, tenete conto di queste indicazioni:

- Le immagini vanno **incollate nell'ordine in cui compaiono nel file di input**.
- Ogni volta che si incolla un’immagine, questa **sovrascrive quelle precedenti** nelle parti eventualmente sovrapposte.
- I pixel che non vengono mai riscritti nelle varie operazioni devono rimanere bianchi (9).
- I **pixel trasparenti** delle immagini in input (`X`) **non sovrascrivono quelli precedenti**.
- Si può assumere che i copia e incolla **non vadano mai fuori dai limiti del risultato 20x20** (_quindi_: non serve fare controlli sulle coordinate del pixel da sovrascrivere che avrà sempre indici validi).

Prima di stampare l’immagine, stampare a video:

- il numero di file di immagini di input
- il nome del file dell’immagine che occupa più pixel (nel conto dei pixel sono inclusi i pixel trasparenti)
- il nome dell’immagine più scura, dove l'intensità di una immagine è calcolata come media dei valori dei pixel (esclusi quelli trasparenti), e il suo valore di intensità con **due cifre decimali** dopo la virgola (_nota_: l'immagine più scura è quella che ha l'intensità minore tra tutte le immagini)

## Esempio

#### `input.txt`

```
img1.txt 2 1
img2.txt 3 0
````

#### `img1.txt`

```
XX34X
X344X
34543
````

#### `img2.txt`

888888
8XXXX8
8XXXX8
888888

### Output

```
Numero file di immagini di input: 2
Immagine più grande: img2.txt
Immagine più scura: img1.txt 3.70

9999999999
9999999999
9993499999
8888889999
8345489999
8999989999
8888889999
9999999999
9999999999
9999999999
```