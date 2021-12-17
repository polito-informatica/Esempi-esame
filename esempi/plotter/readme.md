# Esempio d'esame "Plotter"

Si realizzi in linguaggio Python un programma per disegnare delle figure in un riquadro di 20x20 caselle.

In ciascuna delle caselle del riquadro può essere presente un singolo carattere; inizialmente tutte le caselle
contengono il carattere '.' (punto). Le caselle sono numerate da (0,0) (in basso a sinistra) a (19,19) (in alto a
destra).

Il programma dovrà leggere un file di testo, denominato *plotter.txt*, ed eseguire le istruzioni di disegno in esso
contenute.

Le istruzioni sono riportate nel file una per riga e possono essere le seguenti:

- P x y: punto (P) posizionato nella casella (x,y). Il punto si disegna usando il carattere '*' (asterisco).
- H x y l: linea orizzontale (H) a partire dalla casella (x, y) per una lunghezza di l caselle verso destra (compresa
  quella di partenza). La linea orizzontale si disegna usando il carattere '-' (trattino)
- V x y l: linea orizzontale (H) a partire dalla casella (x, y) per una lunghezza di l caselle verso l'alto  (compresa
  quella di partenza). La linea orizzontale si disegna usando il carattere '|' (barra verticale)
- Quando una linea orizzontale si interseca con una linea verticale (o viceversa), nella casella corrispondente
  occorrerà inserire il simbolo '+' (più). Per il resto, ogni istruzione di disegno _sovrascrive_ quelle precedenti.

Al termine della lettura del file, il programma dovrà stampare il riquadro contenente il disegno costruito.

## Esempio

Per semplicità pensiamo ad un quadrato 5x5, che inizialmente sarà così:

    .....
    .....
    .....
    .....
    .....

e supponiamo che il file *plotter.txt* contenga le seguenti linee:

    P 2 2
    H 1 1 3 
    H 1 3 3
    V 3 0 5
    P 1 1

L'esecuzione del programma genererà il seguente output:

    ...|.
    .--+.
    ..*|.
    .*-+.
    ...|.

