# ComputAir

#### (Esame proposto il 30/04/2024)

*ComputAir* è una società dello stato di *Upsidedown* che mira ad analizzare le informazioni sui voli e sul meteo nelle sue città.

È richiesto di scrivere un programma Python in grado di leggere due file:

**1.** Il file flights.txt contiene l'elenco dei voli da analizzare. Ogni riga del file ha:

    flight_id;city_destination;number_passengers

dove `flight_id` è il codice del volo, `city_destination` è la città verso cui è diretto il volo e `number_passengers` è il numero di passeggeri prenotati per quel volo. Tutti i campi sono separati da "`;`".

**2.** Il file `weather.txt` contiene informazioni sul tempo in tutte le città dello stato. Ogni riga del file ha:

    city;weather_condition

dove `city` è il nome della città e `weather_condition` è una stringa che può essere: "Sunny", "Cloudy", "Windy", "Rainy" o " Stormy". Tutti i campi sono separati da "`;`".

Il programma deve stampare le seguenti statistiche: 

-    Il numero medio di passeggeri per tutti i voli analizzati. 
-    Per ogni volo la cui `city_destination` ha una condizione meteorologica "Rainy" o "Stormy", occorre stampare il `flight_id` e la condizione meteorologica corrispondente. 
-    Per ogni città che è **almeno una volta destinazione di un volo**, stampa le condizioni meteorologiche corrispondenti e il numero totale di passeggeri che viaggiano verso di essa. Ogni città deve essere visualizzata **una sola volta**.

Si supponga che i file esistano e non contengano errori. Per il formato di output, si veda l'esempio seguente.

### Esempio

#### `flights.txt`

    F001;Anchorage;100
    F020;Firebanks;10
    F201;Anchorage;200
    F304;Seward;50

#### `weather.txt`

    Anchorage;Rainy
    Firebanks;Sunny
    Seward;Stormy
    Whittier;Rainy

#### Output

    Numero medio di passeggeri: 90.0

    Codice dei voli verso città con condizione meteorologica Rainy o Stormy:
    * F001 verso Anchorage: Rainy
    * F201 verso Anchorage: Rainy
    * F304 verso Seward: Stormy

    Condizione meteorologica delle città che sono destinazione di almeno un volo:
    * Anchorage: Rainy. 300 passeggeri in arrivo.
    * Firebanks: Sunny. 10 passeggeri in arrivo.
    * Seward: Stormy. 50 passeggeri in arrivo.
