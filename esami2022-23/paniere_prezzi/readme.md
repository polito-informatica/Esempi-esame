# Paniere dei prezzi in Newfoundland

#### (Esame proposto il 13-14/02/2023)

La provincia canadese Newfoundland sta facendo un'analisi sui prezzi dei principali prodotti
alimentari dei suoi abitanti, per monitorare l'aumento del costo della vita.
Per questo motivo, ha fatto raccogliere in un file .csv il prezzo di diversi
alimenti nel tempo in diverse località e in negozi di diverse catene di supermercati. 
I dati sono raccolti nel file `NLFoodPricing.csv` che riporta le seguenti informazioni:

    Date,Place,Grocery store,Food item,Essential/optional,$/kilo

dove **Date** è la data nel formato gg/mm/aaaa, **Place** è la località, **Grocery store**
la catena del negozio, **Food item** il nome dell'alimento, **Essential/optional**
una lettera che indica se l'alimento è considerato essenziale (`E`) o opzionale (`O`),
**$/kilo** il prezzo al chilo dell'alimento alla data e nel luogo indicato.
I campi solo separati da virgole, e ogni riga si riferisce ad una diversa rilevazione 
(diverso prodotto e/o data e/o negozio).

Un secondo file, chiamato `shops.txt`, elenca le catene sotto osservazione, 
elencate una per riga.

Si assuma che il formato dei due file sia corretto, e che i dati siano coerenti
(non è necessario ad esempio verificare che le righe del file .csv siano
effettivamente diverse tra loro).

Si scriva un programma Python che supporti le analisi della provincia. Il programma deve:

- elencare i prodotti alimentari ritenuti essenziali in ordine alfabetico
- indicare per ogni catena riportata nel file `shops.txt` (in ordine alfabetico), il prezzo minimo rilevato per ciascuno dei prodotti alimentari considerati essenziali (riportati in ordine alfabetico)
- infine, deve consentire all'utente di indicare uno dei prodotti alimentari essenziali e rispondere con il prezzo minimo rilevato e la catena di negozi dove si è riscontrato questo prezzo; l'inserimento termina se l'utente inserisce un carattere di controllo (ad esempio 'q'), mentre se il prodotto non è tra quelli essenziali si deve restituire un messaggio di errore e consentire di continuare l'inserimento

### Esempio 

#### `NLFoodPricing.csv` (estratto)

    Date,Place,Grocery store,Food item,Essential/optional,$/kilo
    08/10/2020,Clarenville,Sobeys,Apple,E,5.49
    08/10/2020,Clarenville,Coop,Apple,E,6.59
    08/10/2020,Clarenville,Coop,Black tea,E,18.70
    08/10/2020,Clarenville,Sobeys,Black tea,E,19.07
    08/10/2020,Clarenville,Sobeys,Bread whole wheat,O,4.54
    08/10/2020,Clarenville,Coop,Carrot,O,3.85
    08/10/2020,Clarenville,Sobeys,Carrot,O,2.64

#### File `shops.txt`

    Colemans
    Walmart
    Sobeys

#### Output del programma (stampato a monitor; Apple, Ground beef, Bread e q sono inseriti dall'utente, senza asterischi)

```
Prodotti:
- Apple
- Black tea
- Ground beef
- Peanut butter
- Tomato
- Tuna canned

Colemans
- Apple: 3.3 $/kg
- Black tea: 8.79 $/kg
- Ground beef: 7.69 $/kg
- Peanut butter: 4.49 $/kg
- Tomato: 4.38 $/kg
- Tuna canned: 7.35 $/kg

Sobeys
- Apple: 3.3 $/kg
- Black tea: 13.17 $/kg
- Ground beef: 4.69 $/kg
- Peanut butter: 2.98 $/kg
- Tomato: 2.18 $/kg
- Tuna canned: 7.18 $/kg

Walmart
- Apple: 2.92 $/kg
- Black tea: 9.45 $/kg
- Ground beef: 8.75 $/kg
- Peanut butter: 3.27 $/kg
- Tomato: 2.14 $/kg
- Tuna canned: 5.12 $/kg

Che cibo vuoi cercare? (q per smettere)
*Apple*
Prezzo minimo: 2.5 $/kg da North Mart

Che cibo vuoi cercare? (q per smettere) 
*Ground beef*
Prezzo minimo: 1.32 $/kg da Coop

Che cibo vuoi cercare? (q per smettere)
*Bread*
Cibo Bread non trovato

Che cibo vuoi cercare? (q per smettere) q
Arrivederci
```
