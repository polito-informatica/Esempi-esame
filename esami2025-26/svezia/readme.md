# Svezia

#### (Esame proposto il 26-27/01/2026)


Scrivere un programma in Python che consenta di visualizzare statistiche meteorologiche relative ad alcune città svedesi, a partire dai dati contenuti nel file `sweden.csv`.

Il file ha la seguente struttura. La prima riga è l'intestazione. Ogni riga successiva rappresenta una rilevazione meteorologica relativa a una città. I valori sono separati da virgole e sono, in ordine:

- nome della città
- temperatura rilevata
- umidità rilevata
- velocità del vento rilevata. 

Ogni città può avere un numero diverso di rilevazioni, e le righe del file non sono ordinate (né per città né per altro criterio).


Il programma risponde alle interrogazioni presenti nel file `ricerche.txt`. Ogni riga del file corrisponde ad una interrogazione. Se la riga contiene una singola lettera, il programma mostra la statistica corrispondente. Le opzioni disponibili sono: 

- 'U': umidità media, 
- 'V': velocità media del vento, 
- 'T': temperatura massima

Il programma deve: 

- stampare, per ogni città, il valore della statistica selezionata 
- visualizzare un istogramma testuale, in cui al valore massimo corrispondono 20 asterischi, e agli altri valori corrisponde un numero di asterischi proporzionale.

Se la statistica indicata nel file `ricerche.txt` non è valida (non è inclusa fra le lettere indicate), il programma deve stampare un messaggio di errore.

Se la riga del file `ricerche.txt` contiene più lettere, il programma le interpreta come il nome di una città. Per quella città, deve calcolare e stampare:

- temperatura minima 
- temperatura massima 
- umidità media 
- velocità media del vento.


Se la città non è presente, il programma deve stampare un messaggio di errore.

Il programma deve gestire tramite eccezioni il caso in cui i file `sweden.csv` e/o `ricerche.txt` non siano presenti.

### Esempio

#### File sweden.csv (sono mostrate solo le prime righe del file)

    city,avg(temperature),avg(humidity),avg(wind_speed)
    Alafors,-0.14666666587193808,92.33333333333333,1.746666669845581
    Alafors,5.792307706979605,94.3076923076923,2.6830769089552073
    Alafors,6.134705852059757,96.0,3.3611764662406025
    Alafors,4.567647092482623,96.23529411764706,2.907058866585002
    Alafors,0.21299999989569188,92.3,2.222000002861023
    Alafors,4.960000038146973,96.0,0.44999998807907104
    Alafors,6.300000190734863,97.0,4.619999885559082
    ...


#### File ricerche.txt

    Alafors
    Malmo
    V
    P


#### Output

    Rilevazioni meteorologiche ad Alafors:
    - temperatura min: -4.24
    - temperatura max: 11.36
    - umidità        : 78.11
    - velocità vento : 2.58

    Non sono disponibili rilevazioni meteorologiche a Malmo.

    Rilevazioni per velocità media del vento:
    Alafors      ( 2.58): ************
    Boden        ( 2.26): **********
    Lidkoping    ( 4.26): ********************
    Stockholm    ( 3.45): ****************

    La statistica P non è disponibile.
