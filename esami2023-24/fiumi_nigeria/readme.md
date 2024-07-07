# Rilevamenti meteo nella zona dei fiumi del Sud Est della Nigeria

#### (Esame proposto il 19/02/2024)

Un programma Python viene usato per monitorare le condizioni meteo in corrispondenza dei principali fiumi del Sud Est della Nigeria. I fiumi da monitorare sono elencati in un file chiamato `rivers.txt` che riporta in ogni riga il nome di fiume.

Per ogni sito di installazione, viene fornito un file dat, il cui nome è dato dal nome del fiume (in minuscolo) seguito da `.dat` (ad esempio, il file che si riferisce al fiume Ajali si chiama `ajali.dat`).

Le prime due righe di ciascuno di questi file contengono una intestazione che descrive il sito in cui vengono effettuati i rilevamenti, indicando: 

-    lo stato in cui si trova il fiume 
-    la località nei pressi del fiume in cui vengono fatti i rilevamenti 
-    la latitudine e la longitudine di tale località 
-    l'area presa in osservazione, in chilometri quadrati 

La prima riga elenca le etichette, mentre la seconda riporta i valori corrispondenti. In entrambi i casi i valori sono separati da spazi (si assume che non ci siano spazi nel nome degli stati o delle località). A queste due righe segue una riga vuota.

Segue poi una tabella che riporta i seguenti dati, rilevati con cadenza settimanale per un anno: 

-    umidità (espressa in percentuale)
-    pressione (espressa in Pascal) 
-    velocità del vento (espressa in m/s)
-    precipitazioni (espresse in mm di pioggia caduta) 
-    radiazione (espressa in mm) 
-    temperatura dell'aria (espressa in gradi Celsius)
-    temperatura al livello del suolo (espressa in gradi Celsius) 
-    portata del fiume (espressa in m³/s)

Scrivere un programma Python che legga i due file e stampi a video: 

-    le caratteristiche di ogni zona di rilevamento, riportando nome del fiume, nome e posizione della località, umidità media, velocità massima del vento, temperatura media e massima 
-    il valore medio delle piogge, calcolato facendo la media settimana per settimana su tutte le zone di rilevamento 
-    il valore medio annuale delle piogge

Se non viene trovato il file relativo ad una installazione, il programma deve avvisare l'utente con un messaggio di errore.

## Esempio

### Contenuto del file `rivers.txt`

    ajali 
    ivo 
    otamiri 
    adada

### Contenuto parziale del file `ajali.dat`

    State Station Lat Long Area 
    Enugu Aguobuumumba 07°19’N 07°13’E 900

    Humidity Pressure Windspeed Rainfall Radiation Tair Tearth-skin Discharge 
    64.75 986.73 0.37 1.72 18.85 24.03 23.35 12.01 
    66.16 985.5 0.8 15.25 18.6 25.53 25.05 12.36 
    76.33 985.7 2.83 48.63 17.58 26.31 26.26 12.85 
    80.89 985.11 2.73 78.29 17.86 26.54 26.61 13.45 
    ...

### Esempio di output

    AJALI    measured in Aguobuumumba (07°19’N 07°13’E)
    Avg. humidity: 78.61%
    Max wind speed: 3.99m/s
    Average temperature: 24.71°C (max: 27.23°C)

    IVO      measured in Imezi-Olo    (06°28’N 06°11’E)
    Avg. humidity: 82.70%
    Max wind speed: 4.09m/s
    Average temperature: 24.88°C (max: 26.98°C)

    OTAMIRI  measured in Nekede       (05°26’ 07°02’E)
    Avg. humidity: 82.80%
    Max wind speed: 3.87m/s
    Average temperature: 25.04°C (max: 27.22°C)

    ADADA    measured in Umulokpa     (06°38’N 07°11’E)
    Avg. humidity: 78.84%
    Max wind speed: 4.19m/s
    Average temperature: 24.78°C (max: 27.22°C)

    IMO      file not found

    Average weekly rain (mm):
    28.09   27.36   69.06  101.24  327.18  173.80  348.25 
    305.82  261.31  265.90  152.81    4.72   31.84   63.34 
    288.78  136.89  284.16  359.95  226.12  160.41  355.64 
    507.93  104.29   75.04    0.01   17.91   26.40  100.16 
    236.38  356.00  276.95  184.24  350.37  203.76   75.40 
    108.68    1.66   19.15  112.61  185.57  188.61  169.68 
    296.06  365.77  306.10  423.86  100.33   11.19   55.37 
    1.37  122.24  127.51 
    Yearly average: 174.68mm
