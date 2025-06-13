# Australian Open

#### (Esame proposto il 27-28/01/2025)

Si vuole realizzare un programma Python per estrarre delle statistiche da un file che riporta i dati riguardanti un torneo di tennis. Il file in questione si chiama "`australian_open.csv`" ed è fornito dall'Association of Tennis Professionals (ATP).

La prima riga riporta le etichette dei vari campi, separati da "`;`", che rappresentano, uno per riga, le statistiche degli incontri svolti nel torneo dal primo turno fino alla finale:

#### Alcune righe del file "`australian_open.csv`"

```
Tournament;Date;Series;Court;Surface;Round;Best of;Player_1;Player_2;Winner;Rank_1;Rank_2;Pts_1;Pts_2;Odd_1;Odd_2;Score
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;Arnaldi M.;Walton A.;Arnaldi M.;41;174;1077;354;1.2;4.5;7-6 6-2 6-4
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;Shevchenko A.;Munar J.;Munar J.;48;82;975;706;1.36;3.2;3-6 3-6 1-6
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;Sinner J.;Van De Zandschulp B.;Sinner J.;4;59;6490;890;1.06;10.0;6-4 7-5 6-3
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;Rinderknech A.;Kotov P.;Kotov P.;94;65;629;835;2.3;1.62;5-7 1-6 7-6 7-6 3-6
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;Cerundolo F.;Sweeny D.;Cerundolo F.;21;257;1760;228;1.36;3.2;3-6 6-3 6-4 2-6 6-2
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;Seyboth Wild T.;Rublev A.;Rublev A.;77;5;718;5010;17.0;1.03;5-7 4-6 6-3 6-4 6-7
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;Machac T.;Mochizuki S.;Machac T.;75;136;748;457;1.25;4.0;7-5 6-1 7-5
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;Garin C.;O Connell C.;O Connell C.;86;68;680;814;2.75;1.44;6-3 5-7 6-4 1-6 5-7
Australian Open;14/01/2024;Grand Slam;Outdoor;Hard;1st Round;5;De Jong J.;Cachin P.;De Jong J.;161;74;393;763;1.36;3.2;4-6 6-2 6-3 6-4
...
```

Il programma deve permettere all'utente di:

1) selezionare un giocatore tra quelli che hanno partecipato al torneo. I giocatori devono essere stampati in ordine alfabetico uno per riga;

2) visualizzare i dati (avversario e punteggio) di tutti i match del tennista scelto.

### Esempio di esecuzione

```
1. Alcaraz C.
2. Altmaier D.
3. Arnaldi M.
4. Auger-Aliassime F.
5. Baez S.
...
120. Wawrinka S.
121. Zapata Miralles B.
122. Zeppieri G.
123. Zhang Zh.
124. Zverev A.

Scegli un giocatore: 4

Auger-Aliassime vs. F. Thiem D. 6-3 7-5 6-7 5-7 6-3
Grenier H. vs. Auger-Aliassime F. 1-6 6-3 1-6 2-6
Auger-Aliassime F. vs. Medvedev D. 3-6 4-6 3-6
```
