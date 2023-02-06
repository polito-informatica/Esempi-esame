# Gestione conto ristorante

#### (Esame proposto il 30-31/01/2023)

Il ristorante Vistamare vi chiede di sviluppare un programma per gestire in maniera automatica la generazione delle
ricevute per i suoi clienti. Le informazioni utilizzate dal programma sono memorizzate in due file diversi. Nel primo
file, che si chiama `menu.txt`, sono elencati i prodotti del menu, uno per riga e caratterizzati dalle seguenti
informazioni, separate da virgole:

    ID, descrizione, costo_unitario, IVA

Dove **ID** è un codice alfanumerico univoco, **descrizione** è la descrizione testuale del prodotto (stringa di lunghezza
massima 25 caratteri), **costo_unitario** è il suo costo in euro (espresso come numero float) e **IVA** è la percentuale di
IVA (espressa come numero intero) compresa nel prezzo finale.

Le informazioni per elaborare la ricevuta sono contenute in un secondo file, `ordine.txt`, che contiene l'elenco dei
prodotti consumati, uno per riga, e caratterizzati dalle seguenti informazioni, separate da virgola:

    ID, quantità

dove **ID** è il codice prodotto e **quantità** è la quantità di quel prodotto ordinata dai commensali.

In base a queste informazioni, il programma deve stampare a video la ricevuta, in cui i prodotti ordinati devono
comparire in ordine crescente di IVA, riportando per ognuno su una singola riga, la quantità ordinata, il nome del
prodotto, l'IVA applicata e il costo totale del prodotto.

Alla fine della ricevuta occorre stampare il costo totale, e indicare la quantità di IVA applicata ai prodotti
consumati. 

NOTA: il costo del singolo prodotto nel menu è inclusivo di IVA. Quindi, dato il costo del prodotto e il
valore in percentuale di IVA applicata al costo finale, occorre trovare la sua IVA. Ad esempio, un prodotto con IVA al
15% e un costo di 6€ ha un costo al netto IVA di 5.22€ e un'IVA di 0.78€.

Si suppone che i file siano tutti corretti, i codici prodotto dell'ordine siano tutti presenti nel menu del ristorante e
un codice prodotto non si ripeta più volte nell'ordine.

## Esempio

### File menu.txt

    0001, Acqua Naturale, 1.5, 7
    0003, Coca Cola, 3, 7
    C243, Agnolotti al Salmone, 14, 22
    0005, Fanta Orange, 3, 7
    A43D, Birra Media, 5, 15
    C240, Antipasto, 9, 22
    A43B, Vino Rosso, 6, 15
    A43C, Birra Piccola, 3, 15
    D100, Filetto, 12, 22
    0004, Fanta Lemon, 3, 7
    C242, Pasta in bianco, 10.5, 22
    D101, Orata, 16, 22
    D102, Branzino, 18, 22
    C241, Pasta al sugo, 5, 22
    0006, Acqua Tonica, 3, 7
    A43A, Vino Bianco, 6, 15
    0002, Acqua Minerale, 1.5, 7
    D103, Arrosto con funghi, 17, 22

### File ordine.txt

    C241, 2
    C243, 1
    0004, 1
    D102, 3
    D100, 2
    0001, 1
    0002, 2
    A43A, 4

### Ricevuta (stampata in output)

    RICEVUTA
     1  Fanta Lemon                3.00 IVA  7.00%
     1  Acqua Naturale             1.50 IVA  7.00%
     2  Acqua Minerale             3.00 IVA  7.00%
     4  Vino Bianco               24.00 IVA 15.00%
     2  Pasta al sugo             10.00 IVA 22.00%
     1  Agnolotti al Salmone      14.00 IVA 22.00%
     3  Branzino                  54.00 IVA 22.00%
     2  Filetto                   24.00 IVA 22.00%
    
    Totale: 133.50€
    Di cui IVA: 22.01€
