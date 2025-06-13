# Skateboard

#### (Esame proposto il 10-11/02/2025)

Recentemente, alcuni appassionati di skateboard hanno condotto una serie di contest in diverse città degli Stati Uniti, raccogliendo dati sulle performance dei partecipanti. Parallelamente, è stato stilato un elenco dello skate park più rappresentativo di ogni città, ognuno con una propria valutazione di "difficoltà", che indica quanto possa essere impegnativo e competitivo allenarsi in quella determinata città.

Il tuo compito è quello di analizzare questi dati, reperibili in due file di testo, e di creare un **ranking degli skateboarder**, in cui si tenga conto non solo dei punteggi ottenuti nei vari contest, ma anche del contesto in cui si allenano, ovvero la difficoltà del loro skate park di riferimento.

I dati sono contenuti in due file. Il **primo** contiene informazioni sugli **skateboarders**, specificando per ciascuno il **nome**, la **città di residenza** e **una serie di punteggi** ottenuti durante i contest. **I primi due campi sono separati da '`;`'**, la **lista dei punteggi** contiene i valori per ogni contest **separati dal carattere '`,`'**.

Il secondo file, invece, contiene per ogni riga: città, nome dello skate park e il relativo livello di difficoltà (valore intero). I campi sono separati da ';'.

*Nota*: il file contiene **un solo skate park** per città.


## Ranking degli Skateboarders

Per ogni skateboarder che vive in una città in cui esiste uno skate park devono essere stampate le seguenti informazioni:

- Il **punteggio medio** dello skateboarder (i.e., media dei suoi voti dei contest)
- Lo skate park della sua città e il suo valore di **difficoltà**
- L'**indice di sfida** calcolato come: `Indice = Punteggio Medio * Difficoltà`

Gli skateboarder devono essere stampati per **ordine decrescente di indice di sfida**.

*Nota 1*: Gli skateboarder che vivono in città **senza skate park** non devono essere inclusi in questo ranking.

*Nota 2*: La stampa **deve riportare esattamente il formato dell'esempio** qui sotto (quindi, **su due righe**, **con indentazione e numero d'ordine** dell'elenco, con numeri float su due cifre decimali, e con tutti i campi richiesti in output)

## Esempio

**NOTA**: nel compito avrete anche a disposizione anche ***altri due file più corti***, che potete usare per i test iniziali (i nomi sono uguali a questi, senza Long nel nome, e sono un sottoinsieme dei dati dell'esempio)

#### Esempio di file `skateboardersLong.txt`:

```
Tony Hawk;San Francisco;95,88,92,94
Rodney Mullen;Simi Valley;89,90,93,87
Nyjah Huston;Los Angeles;94,91,90,96
Chris Cole;Los Angeles;88,85,90,92,89
Jhon Eagle;Pasadena;85,91,94
Leticia Bufoni;Los Angeles;92,95,88,91
Ryan Sheckler;San Diego;90,87,89,92
Lizzie Armanto;Santa Monica;86,88,90,85
Bam Margera;Philadelphia;84,89,91
Paul Rodriguez;Los Angeles;92,94,90,87
Eric Koston;Los Angeles;91,90,92,94
Shane O’Neill;New York;95,97,94
Alex Sorgente;San Diego;89,91,94,96
Evan Smith;Philadelphia;88,89,90,92
Tom Schaar;San Francisco;94,92,96,95
David Gonzalez;Houston;87,90,92,85
Jamie Foy;Miami;93,94,89,87
Kevin Hoefler;New York;94,96,95,97
Zion Wright;Miami;89,88,92,91
Kelvin Hoefler;New York;95,97,98
Tyshawn Jones;New York;96,94,95,98
Luan Oliveira;Denver;90,89,92,91
Carlos Ribeiro;Denver;89,91,90,92
```

#### Esempio di file `skateparksLong.txt`:

```
San Francisco;Dogpatch Skate Park;3
Simi Valley;Downtown Ramp;4
New York;Central Skate Park;5
Los Angeles;Venice Beach Skate Park;2
San Diego;Ocean Beach Skatepark;3
Santa Monica;The Cove Skatepark;4
Philadelphia;FDR Skatepark;5
Houston;Lee and Joe Jamail Skatepark;3
Miami;Lot 11 Skatepark;4
Denver;Denver Skatepark;2
```

#### Output atteso:

```
Ranking Skateboarders:
1. Kelvin Hoefler - Indice di Sfida: 483.33 - Punteggio medio: 96.67
    New York - Central Skate Park (Difficoltà: 5)
2. Tyshawn Jones - Indice di Sfida: 478.75 - Punteggio medio: 95.75
    New York - Central Skate Park (Difficoltà: 5)
3. Kevin Hoefler - Indice di Sfida: 477.50 - Punteggio medio: 95.50
    New York - Central Skate Park (Difficoltà: 5)
4. Shane O’Neill - Indice di Sfida: 476.67 - Punteggio medio: 95.33
    New York - Central Skate Park (Difficoltà: 5)
5. Evan Smith - Indice di Sfida: 448.75 - Punteggio medio: 89.75
    Philadelphia - FDR Skatepark (Difficoltà: 5)
6. Bam Margera - Indice di Sfida: 440.00 - Punteggio medio: 88.00
    Philadelphia - FDR Skatepark (Difficoltà: 5)
7. Jamie Foy - Indice di Sfida: 363.00 - Punteggio medio: 90.75
    Miami - Lot 11 Skatepark (Difficoltà: 4)
8. Zion Wright - Indice di Sfida: 360.00 - Punteggio medio: 90.00
    Miami - Lot 11 Skatepark (Difficoltà: 4)
9. Rodney Mullen - Indice di Sfida: 359.00 - Punteggio medio: 89.75
    Simi Valley - Downtown Ramp (Difficoltà: 4)
10. Lizzie Armanto - Indice di Sfida: 349.00 - Punteggio medio: 87.25
    Santa Monica - The Cove Skatepark (Difficoltà: 4)
11. Tom Schaar - Indice di Sfida: 282.75 - Punteggio medio: 94.25
    San Francisco - Dogpatch Skate Park (Difficoltà: 3)
12. Alex Sorgente - Indice di Sfida: 277.50 - Punteggio medio: 92.50
    San Diego - Ocean Beach Skatepark (Difficoltà: 3)
13. Tony Hawk - Indice di Sfida: 276.75 - Punteggio medio: 92.25
    San Francisco - Dogpatch Skate Park (Difficoltà: 3)
14. Ryan Sheckler - Indice di Sfida: 268.50 - Punteggio medio: 89.50
    San Diego - Ocean Beach Skatepark (Difficoltà: 3)
15. David Gonzalez - Indice di Sfida: 265.50 - Punteggio medio: 88.50
    Houston - Lee and Joe Jamail Skatepark (Difficoltà: 3)
16. Nyjah Huston - Indice di Sfida: 185.50 - Punteggio medio: 92.75
    Los Angeles - Venice Beach Skate Park (Difficoltà: 2)
17. Eric Koston - Indice di Sfida: 183.50 - Punteggio medio: 91.75
    Los Angeles - Venice Beach Skate Park (Difficoltà: 2)
18. Leticia Bufoni - Indice di Sfida: 183.00 - Punteggio medio: 91.50
    Los Angeles - Venice Beach Skate Park (Difficoltà: 2)
19. Paul Rodriguez - Indice di Sfida: 181.50 - Punteggio medio: 90.75
    Los Angeles - Venice Beach Skate Park (Difficoltà: 2)
20. Luan Oliveira - Indice di Sfida: 181.00 - Punteggio medio: 90.50
    Denver - Denver Skatepark (Difficoltà: 2)
21. Carlos Ribeiro - Indice di Sfida: 181.00 - Punteggio medio: 90.50
    Denver - Denver Skatepark (Difficoltà: 2)
22. Chris Cole - Indice di Sfida: 177.60 - Punteggio medio: 88.80
    Los Angeles - Venice Beach Skate Park (Difficoltà: 2)
```