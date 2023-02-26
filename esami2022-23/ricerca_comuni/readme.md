# Ricerca Comuni

#### (Esame proposto il 13-14/02/2023)

Una rivista di turismo vi chiede di sviluppare un programma per effettuare un'analisi 
statistica dei dati dei Comuni Italiani.

Il software deve aprire un primo file con estensione .csv (il cui nome è fornito 
dall'utente) che contiene informazioni relative a Comuni italiani nel seguente formato:

    Comune;Regione;Provincia;Abitanti;Altitudine

dove `Comune` è il nome del comune, `Provincia` è la sigla della provincia di 
appartenenza e `Altitudine` è l'altezza sul livello del mare.

Il programma legge in un secondo file (il cui nome è fornito dall'utente) 
le sigle delle province dei comuni da analizzare. Questo file contiene una 
sigla di provincia su ciascuna riga.

Si suppone che i file siano tutti corretti.

In base a queste informazioni, il programma deve cercare per ogni provincia specificata nel secondo file, il comune che si trova alla massima altitudine.

Qualora non esista il file indicato dall'utente, si richiede di gestire un possibile
errore nell'immissione del nome del file richiedendo all'utente di fornire un nuovo nome.

### Esempio

#### File `comuni.csv`

    Torino;Piemonte;TO;842754;239
    Bardonecchia;Piemonte;TO;3039;1312
    Carmagnola;Piemonte;TO;28163;240
    Moncenisio;Piemonte;TO;44;1460
    Asti;Piemonte;AT;73326;123
    Castelnuovo Don Bosco;Piemonte;AT;3126;245
    Roccaverano;Piemonte;AT;382;759
    Alessandria;Piemonte;AL;91099;95
    Carrega Ligure;Piemonte;AL;89;958
    Casale Monferrato;Piemonte;AL;32467;116
    Aosta;Valle d'Aosta;AO;35261;583
    Cogne;Valle d'Aosta;AO;1356;1544

#### File `province.txt`

    AL
    AT

#### Stampa output

    Comune più alto nella provincia di AL e' Carrega Ligure che si trova a 958 metri
    Comune più alto nella provincia di AT e' Roccaverano che si trova a 759 metri
