# Pedaggi autostradali

#### (Esame proposto il 19/09/2023)


Si vuole scrivere un programma per elaborare statistiche sui pedaggi autostradali pagati dagli automobilisti lungo l'autostrada A4 Torino-Milano. Il file **pedaggi.txt** elenca ciascuna tratta autostradale, una per riga, con il relativo pedaggio, nel formato:

    casello1;casello2;pedaggio

dove *casello1* e *casello2* sono due stringhe che indicano l'inizio e la fine della tratta autostradale, identificandola univocamente. *pedaggio* è un numero reale che rappresenta il costo del pedaggio per quella tratta. Le tratte autostradali sono riportate in ordine consecutivo lungo la direzione Torino-Milano. Si noti però che l’autostrada può essere percorsa in entrambi i sensi di marcia (ossia, anche da Milano verso Torino).

Un secondo file **auto.txt** riporta la lista delle automobili (identificate dal numero di targa) che sono transitate lungo l'autostrada A4, con l'indicazione del casello di entrata, quello di uscita e il giorno di percorrenza:

    targa;casello1;casello2;giorno

La stessa targa può comparire più volte nel file: significa che l'automobile è entrata più volte in autostrada (in date differenti).

Per ogni targa, il programma deve visualizzare in output:
1. il pedaggio totale pagato
2. il numero totale di tratte autostradali percorse
3. il numero di ingressi distinti.

L'ordine con cui sono elencate le targhe è indifferente.

Infine, il programma deve visualizzare in output la targa dell'automobile che ha pagato il pedaggio più alto.

## Esempio

### Contenuto del file pedaggi.txt

    Torino;Settimo Torinese;1.30
    Settimo Torinese;Volpiano;1.00
    Volpiano;Rondissone;2.10
    Rondissone;Borgo d'Ale;2.10
    Borgo d'Ale;Santhia;1.30
    Santhia;Carisio;0.30
    Carisio;Balocco;0.70
    Balocco;Greggio;0.90
    Greggio;Biandrate;1.00
    Biandrate;Novara;1.00 
    Novara;Marcallo Mesero;3.20
    Marcallo Mesero;Arluno;0.70
    Arluno;Rho;0.90
    Rho;Milano;2.90

### Contenuto del file auto.txt

    FI245LE;Torino;Santhia;4/9/2024
    BY010TE;Torino;Milano;7/9/2024
    EX456OR;Carisio;Balocco;7/9/2024
    EX456OR;Rho;Santhia;8/9/2024
    BY010TE;Novara;Borgo d'Ale;11/9/2024
    TR472UE;Biandrate;Greggio;12/9/2024
    TR472UE;Milano;Torino;14/9/2024

### Esempio di output

    FI245LE: 7.80 pedaggio pagato (5 tratte percorse in 1 ingressi)
    BY010TE: 24.60 pedaggio pagato (20 tratte percorse in 2 ingressi)
    EX456OR: 9.40 pedaggio pagato (9 tratte percorse in 2 ingressi)
    TR472UE: 20.40 pedaggio pagato (15 tratte percorse in 2 ingressi)
    L'auto che ha pagato il pedaggio maggiore ha targa BY010TE.
