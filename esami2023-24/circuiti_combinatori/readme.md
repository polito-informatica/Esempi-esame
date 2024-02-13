# Circuiti combinatori

#### (Esame proposto il 05-06/02/2024)

In un circuito elettronico combinatorio, una funzione è implementata da una serie di **Gate** (porte logiche) interconnessi per mezzo di **Net** (segnali). Le net sono connesse agli input/output dei vari gate. In particolare, ogni net può essere connessa all'output di un solo gate (al massimo), mentre non ci sono limitazioni riguardo le connessioni agli input.

Il linguaggio di descrizione dell'hardware Verilog offre una serie di tipi di gate combinatori, tra cui:

- **and**, **nand**, **or**, **nor**, **xor**, **xnor**: ciascuno di questi gate ha una uscita e due o più ingressi
- **not**, **buf**: ciascuno con esattamente una uscita e un ingresso.

A partire da un file Verilog, è stata estratta la sezione che riporta le instanze dei vari gate del circuito e riportata in un file, usando un formato semplificato. Per ogni riga, il file riporta:

    tipoGate nomeGate netOutput netInput1 netInput2 ...

Notare che la terza stringa si riferisce sempre alla net collegata all'uscita del gate, mentre dalla quarta stringa in poi vi sono le net collegate ai vari input (il numero di tali net dipende dal tipo di gate). Ad esempio:

    and U1 net1 net2 net3 
    not U2 net4 net3
    not U3 net5 net1
    or U4 net7 net4 net5 net6

Implementare un programma Python in grado di leggere un file formattato come il precedente esempio e riportare tre tipi di informazioni:

1.    eventuali errori presenti nel file
2.    la lista degli input ed output del circuito
3.    statistiche relative a gate e net.

Il nome del file da processare viene fornito in input dall'utente.

## Punto 1: report errori

Il programma dovrà effettuare alcune verifiche sulle interconnessioni e riportare, per ogni errore rilevato, il **numero di riga** e il relativo **tipo d'errore**. Gli errori da riportare sono i seguenti:

-    **Gate sconosciuto**: se il tipo di gate è diverso da quelli noti (*and*, *or*, ...).
-    **Nome già utilizzato**: ogni gate deve avere un nome diverso all'interno del circuito.
-    **Numero di net non valido**: ogni gate deve avere un numero corretto di net in ingresso e in uscita (esempio: una and con un solo input rappresenta un errore).
-    **Net collegata a più output**: ogni net può essere collegata al massimo ad un output di un solo gate nel circuito.

Il programma deve riportare inoltre il **numero totale** di errori rilevati.

## Punto 2: input/output globali

Il programma deve riportare il numero e la lista degli input/output globali del circuito, definiti come segue:

-    **input del circuito**: corrispondono alle net collegate in input ad uno o più gate, ma a nessun output dei gate.
-    **output del circuito**: le net collegate all'output di uno dei gate, ma a nessun input dei gate.

*Nota*: le righe contenenti errori non devono essere considerate.

## Punto 3: statistiche

Il programma deve riportare le seguenti statistiche:

-    Il numero totale di gate.
-    Per ogni tipo di gate (*and*, *or*, ...), il numero di gate a 2 ingressi, a 3 ingressi, ecc. (cioè: numero di *and* a 2 ingressi, a 3 ingressi, 4 ingressi, ..., stessa cosa per *or*, ecc.).

*Nota*: le righe contenenti errori non devono essere considerate.

## Esempio file "c5315.txt" (prime 20 righe)

    buf U1 net144 net141
    buf U2 net298 net293
    and2 U3 net4114 net135 net4115
    not U4 
    buffer U5 net973 net3173
    not U6 net3547 net3546
    not U7 net3549 net3548
    not U10 net3551 net3550
    not U9 net3553 net3552
    not U10 net594 net545
    not U11 net599 net348
    not U12 net600 net366
    and U13 net601 net552 net562
    not U14 net602 net549
    not U15 net603 net545
    not U16 net3551 net545
    not U17 net611 net338
    not U18 net612 net358
    nand U19 net633 net373 net1
    and U20 net810 net141 net145

## Esempio di esecuzione (alcune parti sono troncate)

    Inserisci il nome del file: c5315.txt

    Rilevamento errori:
    Riga 3: Gate sconosciuto (and2)
    Riga 4: Numero di net non valido (0)
    Riga 5: Gate sconosciuto (buffer)
    Riga 10: Nome già utilizzato (U10)
    Riga 16 : Net collegata a più output (net3551)
    5 errori

    Input globali: 176
    net49
    net64
    net3550
    net128
    net87
    net248
    ...

    Output globali: 122
    net664
    net602
    net685
    net762
    net752
    net696
    ...

    Numero di gate: 2302
    318 and con 2 input
    359 and con 3 input
    27 and con 4 input
    11 and con 5 input
    2 and con 9 input
    312 buf
    454 nand con 2 input
    19 nor con 2 input
    6 nor con 3 input
    2 nor con 4 input
    578 not
    95 or con 2 input
    50 or con 3 input
    61 or con 4 input
    8 or con 5 input
