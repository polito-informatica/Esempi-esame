# Collegamenti e Carichi

#### (Esame proposto il 09-10/02/2026)

Un sistema tecnico è costituito da una serie di nodi collegati tra loro tramite collegamenti. Ogni collegamento ha una capacità massima e su di esso viene misurato un carico.

La configurazione del sistema e le misure rilevate sono fornite tramite due file di testo.

Il file `collegamenti.txt` descrive i collegamenti del sistema. Ogni riga contiene tre campi separati dal carattere `;`:

    nodo1;nodo2;capacita

dove `capacita` è un numero intero positivo. I collegamenti sono da considerarsi bidirezionali.

Il file `misure.txt` descrive i carichi misurati sui collegamenti. Ogni riga contiene tre campi separati dal carattere `;`:

    nodo1;nodo2;carico

dove `carico` è un numero intero maggiore o uguale a zero.

Si può assumere che i collegamenti (coppie di nodi) descritti nei due file siano gli stessi.

Scrivere un programma Python che legga i due file e produca un file `report.txt` contenente le elaborazioni richieste.

Il programma deve:

- contare il numero totale di collegamenti e il numero totale di misure lette;
- calcolare, per ogni nodo, il carico totale associato, sommando tutti i carichi dei collegamenti in cui il nodo compare;
- individuare i collegamenti per cui il carico supera la capacità;
- per ogni nodo, determinare quanti collegamenti sovraccarichi lo coinvolgono;
- individuare i nodi critici, ossia quelli coinvolti in almeno due collegamenti sovraccarichi;
- individuare il nodo con il carico totale massimo.

Il formato del file `report.txt` è libero, ma deve essere chiaro, leggibile e coerente con le informazioni richieste.

### Esempio

(attenzione: i file presenti nel progetto potrebbero avere dei valori diversi da quelli dell'esempio. Il programma deve funzionare correttamente anche con dati diversi da quelli riportati)

#### Contenuto del file `collegamenti.txt`

    N01;N02;80
    N02;N03;80
    N03;N04;60
    N01;N04;80

#### Contenuto del file `misure.txt`

    N01;N02;90
    N02;N03;100
    N03;N04;40
    N01;N04;70

#### Esempio di contenuto del file `report.txt`

    Collegamenti totali: 4
    Misure totali: 4

    Carico totale per nodo:
    N01: 160
    N02: 190
    N03: 140
    N04: 110

    N01-N02 carico=80 capacità=90
    N02-N03 carico=80 capacità=100

    Nodi critici:
    N02: 2 sovraccarichi

    Nodo con il carico massimo: N02 con carico 190
