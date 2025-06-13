# Sensori di Monitoraggio Ambientale

#### (Esame proposto il 10-11/02/2025)


Un'applicazione Python è utilizzata per monitorare i dati provenienti da una rete di sensori ambientali posizionati in diverse aree della città. I sensori sono elencati in un file chiamato `sensori.`txt, dove ogni riga contiene le seguenti informazioni:
- Codice identificativo del sensore (es. "SENSOR_001")
- Posizione del sensore (es. "ParcoCentrale")
- Tipo di sensore installato (es. "Temperatura", "Inquinamento", "Luminosità")

Per ciascun sensore, vengono registrati i dati in un file CSV specifico, il cui nome è dato dal codice identificativo seguito da .csv (es. `SENSOR_001.csv`). Il file CSV contiene una tabella con le seguenti colonne:
- Data, nel formato `yyyy-mm-dd`
- Ora, nel formato `hh:mm`
- Valore rilevato dal sensore

Scrivere un programma Python che legga i dati da entrambi i file e stampi a video:
- Le informazioni di ogni sensore, inclusi codice identificativo, posizione, tipo di sensore e media dei valori rilevati
- Il sensore con la massima lettura registrata
- Il tipo di sensore con la media più alta tra tutti i sensori
- Avvisare l'utente nel caso in cui il file relativo a un sensore non venga trovato

### Esempio di file "`sensori.txt`"

```
SENSOR_001 ParcoCentrale Temperatura
SENSOR_002 PiazzaPrincipale Inquinamento
SENSOR_003 ViaVerde Luminosità
```

#### Esempio (parziale) del file "`SENSOR_001.csv`"
```
Data,Ora,Temperatura
2022-01-01,12:00,20.5
2022-01-01,12:10,21.2
2022-01-01,12:20,19.8
2022-01-01,12:30,22.0
```

#### Contenuto del file "`SENSOR_002.csv`"

```
Data,Ora,Inquinamento
2022-01-01,12:00,75.3
2022-01-01,12:10,70.2
2022-01-01,12:20,80.5
2022-01-01,12:30,65.8
```

#### Contenuto del file "`SENSOR_003.csv`"
```
Data,Ora,Luminosità
2022-01-01,12:00,500.0
2022-01-01,12:10,600.0
2022-01-01,12:20,450.0
2022-01-01,12:30,700.0
```

### Output

```
File non trovato per il sensore: SENSOR_004

SENSOR_001: ParcoCentrale - Temperatura - Media: 19.20 SENSOR_002: PiazzaPrincipale - Inquinamento - Media: 69.28 SENSOR_003: ViaVerde - Luminosità - Media: 550.00

Sensore con massima lettura: SENSOR_003 a ViaVerde - Luminosità - Valore massimo: 620.0 Tipo di sensore con media più alta: Luminosità - Media: 550.0
```