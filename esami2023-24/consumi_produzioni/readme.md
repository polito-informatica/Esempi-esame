# Analisi dei Consumi e Produzioni

#### (Esame proposto il 05/07/2024)

Un'azienda energetica vuole stimare il beneficio energetico dato dall'installazione di impianti fotovoltaici presso una serie di abitazioni. L'azienda ha raccolto i dati di radiazione solare dell'area di interesse (cioè dell'energia radiante per $m^2$ emessa dal sole che può essere utilizzata dall'impianto fotovoltaico per produrre energia, espressa in $kWh/m^2$). Per ogni abitazione si conosce poi: 

- la dimensione dell'impianto fotovoltaico installabile (in $m^2$)
- l'efficienza di tale impianto (espressa come intero da 0 a 1, rappresenta la percentuale di potenza della radiazione solare che viene effettivamente trasformata in energia elettrica, 0 = 0%, 1 = 100%)
- i consumi energetici, campionando un dato ogni 15 minuti.

L'obiettivo è analizzare questi dati per calcolare alcuni indicatori per ciascuna abitazione (e per l'aggregato di abitazioni) e generare un report di statistiche.

## Definizioni degli indicatori:

* **Energia Prodotta**: Quantità totale di energia prodotta dall'impianto fotovoltaico. Calcolabile con la seguente formula: 

```
energia_prodotta = efficienza_impianto × dimensione_impianto × radiazione_solare
```

* **Energia Immessa in Rete**: Quantità di energia prodotta che supera il consumo e viene immessa nella rete.
* **Energia Autoconsumata**: Quantità di energia prodotta dall'impianto fotovoltaico e consumata internamente.
* **Autoconsumo**: Percentuale di energia consumata dall'abitazione che è prodotta internamente. Si calcola come `(energia autoconsumata / produzione totale) * 100`.
* **Autosufficienza**: Percentuale di energia autoprodotta rispetto al consumo totale. Si calcola come `(energia autoconsumata / consumo totale) * 100`.

**Suggerimento**: Calcolare per ogni abitazione e per ogni istante di tempo:

- Energia Prodotta 
- Energia Immessa in Rete 
- Energia Autoconsumata

**Calcolare e _stampare a video_ poi le seguenti statistiche per l'aggregato di tutte le abitazioni:**
- Consumo totale
- Energia Prodotta
- Energia Immessa in Rete
- Energia Autoconsumata
- Autoconsumo
- Autosufficienza.

Inoltre occorre stampare l'`ID` delle **tre abitazioni con il più alto autoconsumo**, e l'`ID` delle **tre abitazioni con la più alta autosufficienza**.

**Formato dei dati in input**: I dati sono forniti in tre file di testo: `consumi.txt`, `impianti.txt` e `meteo.txt`. Ogni file ha il seguente formato:

#### `consumi.txt`

```
ID_Abitazione;Data;Ora;Consumo_energetico
ID1;01/01/2023;00:00;1.86
ID2;01/01/2023;00:00;1.69
ID3;01/01/2023;00:00;2.64
ID4;01/01/2023;00:00;1.61
ID5;01/01/2023;00:00;1.65
ID6;01/01/2023;00:00;2.2
ID7;01/01/2023;00:00;2.89
ID8;01/01/2023;00:00;1.27
ID9;01/01/2023;00:00;2.05
ID10;01/01/2023;00:00;2.01
ID1;01/01/2023;00:15;2.07
ID2;01/01/2023;00:15;2.69
ID3;01/01/2023;00:15;1.08
ID4;01/01/2023;00:15;1.97
ID5;01/01/2023;00:15;2.28
ID6;01/01/2023;00:15;1.62
ID7;01/01/2023;00:15;1.95
ID8;01/01/2023;00:15;1.51
ID9;01/01/2023;00:15;1.79
ID10;01/01/2023;00:15;1.03
```

I dati di `consumi.txt` sono separati da punto e virgola e hanno il seguente formato: 

- ID_Abitazione: Identificativo unico dell'abitazione (una stringa senza spazi). 
- Data: Data in formato "GG/MM/AAAA" (giorno/mese/anno). 
- Ora: Ora in formato "HH:MM" (ore:minuti). 
- Consumo_energetico: Consumo energetico ogni 15 minuti in $kWh$ (numero decimale).

#### `impianti.txt`

```
ID_Abitazione;Dimensione_impianto;Eta;
ID1;23.51;0.19
ID2;30.33;0.25
ID3;41.99;0.2
ID4;14.38;0.23
ID5;30.67;0.18
ID6;52.65;0.21
ID7;16.84;0.23
ID8;28.15;0.16
ID9;81.43;0.22
ID10;24.33;0.25
```

I dati di `impianti.txt` sono separati da punto e virgola e hanno il seguente formato: 

- ID_Abitazione: Identificativo unico dell'abitazione (una stringa senza spazi). 
- Dimensione_impianto: Dimensione dell'impianto fotovoltaico in $m^2$ (numero decimale). 
- Eta: Efficienza dell'impianto espressa come numero da 1 (efficienza massima) a 0.

#### `meteo.txt`

```
DATA;ORA;GHI
01/01/2023;00:00;0
01/01/2023;00:15;0
01/01/2023;00:30;0
01/01/2023;00:45;0
01/01/2023;01:00;0
01/01/2023;01:15;0
01/01/2023;01:30;0
01/01/2023;01:45;0
01/01/2023;02:00;0
...
...
01/01/2023;09:15;0.0986
01/01/2023;09:30;0.1291
01/01/2023;09:45;0.1582
01/01/2023;10:00;0.1887
01/01/2023;10:15;0.2211
01/01/2023;10:30;0.2503
01/01/2023;10:45;0.278
01/01/2023;11:00;0.3021
01/01/2023;11:15;0.3225
01/01/2023;11:30;0.3345
```

I dati di `meteo.txt` sono separati da punto e virgola e hanno il seguente formato: 

- Data: Data in formato "GG/MM/AAAA" (giorno/mese/anno). 
- Ora: Ora in formato "HH:MM" (ore:minuti). 
- GHI: Radiazione solare in $kWh/m^2$ (numero decimale).

## Esempio di Esecuzione

```
Report aggregato:
 Energia Prodotta:1747.96 kWh
 Energia Consumata:1885.54 kWh
 Energia autoconsumata:565.67 kWh
 Energia Immessa:1182.29 kWh
 Pecentuale Autoconsumo:32.36%
 Percentuale Autosufficienza:30.00% 

Le tre abitazioni con il più alto autoconsumo sono: ID10, ID3, ID7
Le tre abitazioni con la più alta autosufficienza sono: ID2, ID5, ID9
```