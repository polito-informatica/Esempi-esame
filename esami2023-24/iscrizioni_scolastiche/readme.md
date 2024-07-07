# Analisi delle iscrizioni al sistema scolastico piemontese

#### (Esame proposto il 20/02/2024)

Il file `regpie-studenti.csv` contiene un estratto delle iscrizioni al sistema scolastico piemontese, di ogni ordine e grado, riferite all'anno 2022-2023. La prima riga del file contiene i nomi dei vari campi:

    "Annoscolastico","Provincia","Comune","GradoScolastico","Numeroscuole","Numtotclassi","Numtotiscrittifemmine","Numtotiscrittimaschi","Numtotaleiscritti"

Le righe seguenti del file riportano i valori dei vari campi separati da `,` e ogni valore è racchiuso tra doppie virgolette (il file fornito è un CSV completo). Il campo `GradoScolastico` può contenere i seguenti valori:

-    "1 - Scuola dell'infanzia" 
-    "2 - Scuola primaria"
-    "3 - Scuola secondaria di I grado" 
-    "4 - Scuola secondaria di II grado"

Assumendo che il formato del file sia corretto, si scriva un programma Python in grado di calcolare e visualizzare le seguenti informazioni:

-    Le province considerate ordinate alfabeticamente 
-    Il numero totale di studenti iscritti per ogni provincia 
-    Il numero totale di studenti piemontesi iscritti alla scuola dell'infanzia

#### File regpie-studenti.csv:

    "Annoscolastico","Provincia","Comune","GradoScolastico","Numeroscuole","Numtotclassi","Numtotiscrittifemmine","Numtotiscrittimaschi","Numtotaleiscritti"
    "2022-2023","CUNEO","BAGNOLO PIEMONTE","3 - Scuola secondaria di I grado","1","9","81","90","171"
    "2022-2023","NOVARA","CAMERI","1 - Scuola dell'infanzia","2","11","94","111","205"
    "2022-2023","CUNEO","CANALE","3 - Scuola secondaria di I grado","1","10","102","100","202"
    "2022-2023","BIELLA","CAVAGLIA'","2 - Scuola primaria","1","8","49","79","128"
    "2022-2023","VERCELLI","CELLIO CON BREIA","1 - Scuola dell'infanzia","1","1","7","5","12"
    "2022-2023","ALESSANDRIA","CREMOLINO","1 - Scuola dell'infanzia","1","1","10","8","18"
    "2022-2023","CUNEO","FARIGLIANO","2 - Scuola primaria","1","5","43","46","89"
    "2022-2023","ASTI","MONASTERO BORMIDA","1 - Scuola dell'infanzia","1","1","20","6","26"
    "2022-2023","TORINO","MONTALTO DORA","1 - Scuola dell'infanzia","2","3","27","27","54"
    "2022-2023","VERBANO-CUSIO-OSSOLA","OMEGNA","2 - Scuola primaria","6","35","271","264","535"
    "2022-2023","TORINO","PECETTO TORINESE","1 - Scuola dell'infanzia","2","4","36","33","69"
    "2022-2023","CUNEO","PEVERAGNO","2 - Scuola primaria","2","13","107","108","215"
    "2022-2023","TORINO","PINEROLO","2 - Scuola primaria","9","75","737","775","1512"
    "2022-2023","NOVARA","PRATO SESIA","2 - Scuola primaria","1","5","35","33","68"
    "2022-2023","CUNEO","SANTA VITTORIA D'ALBA","1 - Scuola dell'infanzia","2","3","34","30","64"
    "2022-2023","VERCELLI","SERRAVALLE SESIA","3 - Scuola secondaria di I grado","1","6","50","58","108"
    "2022-2023","ALESSANDRIA","VILLALVERNIA","2 - Scuola primaria","1","5","13","20","33"
    "2022-2023","ALESSANDRIA","BASALUZZO","3 - Scuola secondaria di I grado","1","3","31","34","65"
    "2022-2023","VERBANO-CUSIO-OSSOLA","BEURA-CARDEZZA","2 - Scuola primaria","1","5","24","25","49"
    "2022-2023","CUNEO","BOSSOLASCO","2 - Scuola primaria","1","5","13","19","32"
    "2022-2023","TORINO","BRICHERASIO","3 - Scuola secondaria di I grado","1","9","91","87","178"
    "2022-2023","TORINO","AVIGLIANA","4 - Scuola secondaria di II grado","6","54","366","552","918"

#### Stampa in output

    Le province per le quali vengono fornite le statistiche sono: 
    ALESSANDRIA
    ASTI
    BIELLA
    CUNEO
    NOVARA
    TORINO
    VERBANO-CUSIO-OSSOLA
    VERCELLI

    Totale studenti iscritti ALESSANDRIA: 116
    Totale studenti iscritti ASTI: 26
    Totale studenti iscritti BIELLA: 128
    Totale studenti iscritti CUNEO: 773
    Totale studenti iscritti NOVARA: 273
    Totale studenti iscritti TORINO: 2731
    Totale studenti iscritti VERBANO-CUSIO-OSSOLA: 584
    Totale studenti iscritti VERCELLI: 120

    Gli studenti iscritti alla scuola dell'infanzia in Piemonte sono: 448
