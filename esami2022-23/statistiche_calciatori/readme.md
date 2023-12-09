# Statistiche Calciatori

#### (Esame proposto il 19/09/2023)

Si devono processare delle statistiche sull'ultima edizione della coppa del mondo. Si ha a disposizione un file `player_stats.csv` che contiene informazioni riguardanti i calciatori del mondiale 2022 separati da virgole. Il file è salvato con codifica Unicode. La prima riga del file riporta i nomi dei campi. Ogni riga successiva si riferisce ad un giocatore diverso e riporta i valori del giocatore per ogni campo considerato. 

I campi sono i seguenti (riportiamo la stringa di intestazione del file, in inglese, e il suo significato):

    player - nome giocatore
    position -  posizione (GK portiere, DF difensore, MF centrocampista, FW attaccante)
    team -  nazionale
    birth_year - anno di nascita
    minutes - minuti giocati
    goals - goal fatti
    assists - assist fatti
    offsides - fuorigiochi 
    crosses -  cross fatti
    interceptions -  palle intercettate
    tackles_won - interventi vinti
    pens_conceded -  punizioni concesse
    ball_recoveries - palle recuperate
    aerials_won - palle aeree vinte
    aerials_lost - palle aeree perse

Il programma deve stampare in output su schermo le suenti 3 informazioni.

1. L'elenco dei tre centrocampisti e dei tre attaccanti più efficaci secondo gli indicatori seguenti:

     -  **efficacia_attaccante** = (goal fatti + assist fatti - fuorigiochi) / minuti giocati
     -  **efficacia_centrocampista** = (palle intercettate + palle recuperate + (assist fatti/ cross fatti)) / minuti giocati


**NOTA**: se un centrocampista non ha fatto cross (cross_fatti == 0), allora il termine (assist fatti / cross fatti) <u>DEVE</u> essere messo a 0.

2. Le tre squadre con l'età media più bassa. Per il calcolo dell'età di ogni giocatore si prenda come riferimento l'anno 2023 e si calcoli il suo valore come differenza tra il 2023 e l'anno di nascita del giocatore.

3. La squadra con l'attacco più efficace. L'efficacia dell'attacco di una squadra si calcola sommando l'efficacia dei suoi tre attaccanti più efficaci. La squadra con l'attacco più efficace è quella con la somma maggiore. ***A parità di squadre con l'attacco più efficace si stampi solo la prima in elenco***.

***Suggerimento***: L'efficacia di tutti gli attaccanti è nota risolvendo il primo punto. Ordinando gli attaccanti per efficacia decrescente, occorre individuare per ogni squadra i suoi primi tre attaccanti in elenco, fare la somma della loro efficacia, e ordinare l'elenco. ***Si supponga che il file sia corretto e contenga almeno tre attaccanti per ogni squadra***.

## Esempio

### File player_stats.csv

    player,position,team,birth_year,minutes,goals,assists,offsides,crosses,interceptions,tackles_won,pens_conceded,ball_recoveries,aerials_won,aerials_lost
    Aaron Mooy,MF,Australia,1990,360,0,0,0,10,3,6,0,35,2,3
    Aaron Ramsey,MF,Wales,1990,266,0,0,0,5,0,0,0,19,0,2
    Abdelhamid Sabiri,MF,Morocco,1996,181,0,1,0,1,5,1,0,7,2,2
    Abdelkarim Hassan,DF,Qatar,1993,270,0,0,1,6,1,3,0,11,3,1
    Abderrazak Hamdallah,FW,Morocco,1990,68,0,0,0,0,0,0,0,4,1,7
    Abdessamad Ezzalzouli,FW,Morocco,2001,93,0,0,0,1,0,2,0,4,1,2
    [...]

### Stampa in output

    I tre attaccanti più efficaci sono:
    Nome                 Squadra      Efficacia
    Niclas Füllkrug      Germany            0.043
    Rafael Leão          Portugal           0.023
    Vincent Aboubakar    Cameroon           0.021

    I tre centrocampisti più efficaci sono:
    Nome                 Squadra      Efficacia
    Roan Wilson          Costa Rica         1.000
    Sorba Thomas         Wales              1.000
    Christian Nørgaard   Denmark            0.333

    Le tre nazionali più giovani sono:
    Ecuador con 25.67 anni
    United States con 25.85 anni
    Ghana con 26.50 anni

    La nazionale con l'attacco più efficace è Germany:
    Niclas Füllkrug con efficacia 0.043
    Leroy Sané con efficacia 0.009
    Jonas Hofmann con efficacia 0.000
