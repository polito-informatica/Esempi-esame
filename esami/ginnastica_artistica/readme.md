# Testo d'esame "Ginnastica artistica"

Si realizzi un programma in Python che gestisca i punteggi di una gara di ginnastica artistica. Le informazioni sono
contenute in un file. Ogni riga del file ha il seguente formato (campi separati da spazio):

    nome, cognome, sesso, nazione, i 5 punteggi assegnati dai giudici. 

Si facciano le seguenti assunzioni:

- Il numero di righe del file non è noto a priori
- I campi Nome e Cognome non contengono spazi
- Il sesso dell’atleta è codificato da un carattere `M` o `F`.
- La sigla della nazione è sempre codificata su 3 lettere maiuscole
- Sono sempre assegnati 5 voti per ogni atleta, separati da uno spazio e il valore può variare  
  da un minimo di 0 ad un massimo di 10.

Il programma deve stampare:

1. Il nome della vincitrice femminile. Nel computo dei punti totali, vanno sempre SCARTATI il punteggio massimo e quello
   minimo tra i 5 assegnati. Il punteggio finale è quindi dato dalla somma dei tre punteggi rimanenti.
2. La classifica delle prime 3 nazioni, includendo sia atleti femminili che maschili. Per ogni nazione il punteggio totale è
   calcolato sommando i punteggi di tutti i suoi atleti (M e F, e sempre scartando il punteggio maggiore e quello minore
   di ogni atleta).

Esempio:

    Yuri Chechi M ITA 9.3 8.9 9.7 9.7 9.8
    Veronica Servente F ITA 9.0 9.0 9.0 9.2 9.5 
    Sabrina Vega F USA 8.4 8.7 8.5 8.6 9.0
    Viktoria Komova F RUS 8.3 8.7 9.5 9.6 9.0 
    Rebecca Downie F GRB 8.2 8.9 8.9 8.6 9.3 
    Gabbie Douglas F USA 8.2 8.9 8.9 8.6 9.3 
    Hannah Whelan F GRB 8.0 8.0 8.0 8.0 8.0 

l'output del programma dovrà essere il seguente:

    Vincitrice femminile:
    Veronica Servente, ITA – Punteggio: 27.2
    
    Classifica complessiva nazioni:
    1°) ITA - Punteggio totale: 55.9
    2°) USA – Punteggio Finale: 52.2
    3°) GRB – Punteggio Finale: 50.4
