# Viaggio della slitta

#### (Esame proposto il 30-31/01/2023)

Come ogni anno, Santa Claus ha appena terminato il proprio giro di consegna dei regali ai bambini italiani. Quest'anno, per la prima volta, si è fatto aiutare da un programma Python per pianificare il proprio viaggio.

In particolare, il file `bambini.csv` contiene le informazioni su tutti i bambini a cui è necessario consegnare un regalo, e ciascun bambino è rappresentato nel seguente formato:

    cognome,nome,regalo,provincia

I bambini nel file compaiono in un ordine arbitrario.

Per ottimizzare il viaggio, è necessario minimizzare gli spostamenti tra le province di residenza dei diversi bambini. In particolare, il programma dovrà realizzare il seguente algoritmo (che non garantisce il minimo assoluto, il quale sarebbe molto più complesso da calcolare):

- selezionare come primo bambino quello che abita più a Nord di tutti (perché più vicino al Polo Nord, quindi con latitudine piu' grande)
- una volta consegnato un regalo ad un bambino, selezionare il bambino successivo, trovando quello non ancora visitato che si trova più vicino al bambino appena visitato.

Il programma deve stampare l'elenco dei bambini nell'ordine di visita calcolato.

Per il calcolo delle distanze, il programma si avvale di un file `province.csv` che contiene i dati delle province nel seguente formato:

    id,id_regione,codice_citta_metropolitana,nome,sigla_automobilistica,latitudine,longitudine

dove le province sono descritte dalla loro sigla automobilistica, e nelle ultime due colonne sono riportate le coordinate (espresse in gradi).

Per determinare le distanze tra due punti A e B si utilizzano le seguenti formule:

- h = sin^2(delta_lat/2) + cos(lat_A)cos(lat_B)sin^2(delta_long/2)
- distanza = 2 * R * arcsin( sqrt(h) )

dove R è il raggio della terra (6731 km), le coordinate lat_A, lat_B, long_A, long_B devono essere espresse **in radianti**, ed infine delta_lat e delta_long sono le differenze tra le coordinate dei due punti (1° = π/180 radianti)

Si assuma che i file siano privi di errori.

## Esempio

### File `bambini.csv`

    cognome,nome,regalo,provincia
    Potter,Harry,Bacchetta,VE
    Granger,Hermione,Libro,RM
    Weasley,Ron,Cioccolato,TO
    Malfoy,Draco,Serpente,ME
    Lovegood,Luna,Gioiello,PA
    Scamander,Newt,Animale,RM
    Hagrid,Rubeus,Mantello,BA

### File `province.csv`

    id,id_regione,codice_citta_metropolitana,nome,sigla_automobilistica,latitudine,longitudine
    84,19,,Agrigento,AG,37.31109,13.576548
    6,1,,Alessandria,AL,44.817559,8.704663
    42,11,,Ancona,AN,43.549325,13.266348
    51,9,,Arezzo,AR,43.466896,11.88236
    44,11,,Ascoli Piceno,AP,42.863893,13.589973
    5,1,,Asti,AT,44.900765,8.206432
    64,15,,Avellino,AV,40.996451,15.125896
    72,16,272,Bari,BA,41.117123,16.871976
    110,16,,Barletta-Andria-Trani,BT,41.200454,16.205148
    25,5,,Belluno,BL,46.249766,12.196957
    62,15,,Benevento,BN,41.203509,14.752094
    16,3,,Bergamo,BG,45.85783,9.881998
    ...............

### Esempio di percorso visualizzato in output

    Consegnato Bacchetta a Harry Potter (VE)
        Viaggio di 395.70216525174317 km
    Consegnato Cioccolato a Ron Weasley (TO)
        Viaggio di 555.4852774876166 km
    Consegnato Libro a Hermione Granger (RM)
        Viaggio di 0.0 km
    Consegnato Animale a Newt Scamander (RM)
        Viaggio di 396.44941684588036 km
    Consegnato Mantello a Rubeus Hagrid (BA)
        Viaggio di 397.3080031954206 km
    Consegnato Serpente a Draco Malfoy (ME)
        Viaggio di 150.3085087723676 km
    Consegnato Gioiello a Luna Lovegood (PA)
