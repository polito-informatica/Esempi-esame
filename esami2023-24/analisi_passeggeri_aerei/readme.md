# Analisi dei passeggeri delle compagnie aeree

#### (Esame proposto il 05-06/02/2024)

Si chiede di realizzare un programma in Python che sia in grado di analizzare dati di passeggeri di compagnie aeree. In particolare il programma deve: 

- Passo 1: Leggere il file CSV rappresentando i dati in una struttura adatta. 
- Passo 2: Calcolare e stampare la media dell'età (precisione di una cifra decimale) dei passeggeri provenienti da ciascuna origine (ordinata per età media decrescente). 
- Passo 3: Identificare il numero di volo più popolare 
- Passo 4: Stampare il numero di passeggeri su quel volo per ogni genere (M/F)

Il file di ingresso, chiamato "passeggeri.txt" è in formato csv ed include i seguenti campi:

    nome_passeggero,età,sesso,origine,destinazione,numero_volo

## Esempio

### File passeggeri.txt

    nome_passeggero,età,sesso,origine,destinazione,numero_volo
    Michael Jackson,50,M,Chicago,Miami,AA123
    Beyoncé,35,F,Miami,Chicago,AA124
    John Smith,30,M,New York,Los Angeles,UA123
    Jane Doe,25,F,New York,New York,UA123
    Madonna,55,F,New York,New York,UA123
    Barack Obama,60,M,Washington DC,London,BA123
    Michelle Obama,58,F,Washington DC,London,BA124
    Elon Musk,50,M,Austin,Tokyo,DL123
    Greta Thunberg,18,F,Stockholm,Paris,AF123
    Jeff Bezos,58,M,Seattle,San Francisco,DL1277

stampa output 

    Media dell'età per ciascuna origine 
    Origine: Chicago, Media età: 50.0 
    Origine: Miami, Media età: 35.0 
    Origine: New York, Media età: 36.6 
    Origine: Washington DC, Media età: 59.0 
    Origine: Austin, Media età: 50.0 
    Origine: Stockholm, Media età: 18.0 
    Origine: Seattle, Media età: 58.0

    Numero di volo più popolare: UA123, Passeggeri M: 1 / F: 2

