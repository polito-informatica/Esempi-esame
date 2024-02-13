# Emissioni di CO2

#### (Esame proposto il 05-06/02/2024)

Il Global Carbon Project (GCP) pubblica stime delle emissioni fossili di CO2. Scrivere un programma Python che elabora l'ultimo report rilasciato dal GCP e consente all'utente di estrarre alcune informazioni. Il file in input è di tipo CSV e usa come **separatore** il punto e virgola (`';'`). Il contenuto riporta i valori di CO2 per un certo numero di paesi e per una finestra di 10 anni. Il numero di paesi **non è noto a priori**.

La prima riga contiene l'intestazione delle colonne (e il numero di colonne presenti non è noto a priori). La prima colonna indica sempre il paese, il secondo sempre l'anno, le altre le variabili misurate.

Ciascuna delle righe successive contiene: - il paese e l'anno a cui si riferiscono i rilevamenti riportati (indicato con la sigla internazionale, ad esempio ITA per Italia) - i valori di CO2, espressi in milioni di tonnellate, emessi in totale e le rispettive quote legate ai combustibili fossili (ad esempio, carbone, petrolio e gas).

Le righe sono ordinate in modo da riportare consecutivamente le misurazioni relative a ciascun paese, ordinate tra loro per anno. Il programma deve caricare i dati del file e riportare a schermo:

-    il nome del file caricato
-    il primo e l'ultimo anno monitorati
-    i codici dei paesi monitorati
-    le grandezze monitorate (totale, carbone, petrolio, ecc).

Il programma deve poi elaborare una serie di interrogazioni definite dall'utente e memorizzate all'interno di un file di testo che contiene (una per riga) le operazioni richieste. Ogni operazione ha nel file il seguente formato:

    <operazione> <parametro1> <parametro2>

Le operazioni possibili sono due:

-    'paese', in questo caso `parametro1` indica il paese da monitorare e `parametro2` il valore di interesse (ad esempio, petrolio, totale, ecc); il programma mostra a video i relativi valori anno per anno e calcola l'aumento (o la diminuzione) percentuale di tale valore nell'ultimo anno rispetto al primo anno monitorato;

-   'massimo', in questo caso `parametro1` indica un anno di riferimento e `parametro2` il valore di interesse (ad esempio, petrolio, totale, ecc); il programma deve riportare il paese con le emissioni massime rispetto a quel valore nell'anno indicato, assieme al relativo valore e all'aumento percentuale rispetto al paese con le emissioni minime nello stesso anno.

## Esempio di Esecuzione

supponendo di avere come input il file `"GCB2023.csv"`

    Paese;Anno;Totale;Carbone;Petrolio;Gas
    AUS;2013;399288;176363;137311;69870
    AUS;2014;393049;168146;137683;70771
    AUS;2015;401378;174204;137710;71500
    AUS;2016;410253;179561;137439;73935
    AUS;2017;413655;176932;139481;75430
    AUS;2018;415350;169393;143690;78468
    AUS;2019;415811;164947;143064;80661
    AUS;2020;396685;156681;135379;83479
    AUS;2021;386606;151542;134686;80159
    AUS;2022;392279;144105;144456;83499
    BRA;2013;532418;65604;342338;74703
    BRA;2014;557901;69033;356753;81285
    BRA;2015;529353;69451;330358;80464
    BRA;2016;492748;63831;312939;69665
    BRA;2017;497121;66689;316132;70185
    BRA;2018;477998;65736;300804;67066
    BRA;2019;473464;61925;299527;67066
    BRA;2020;444504;56209;282283;58747
    BRA;2021;497206;67642;305275;75904
    BRA;2022;483477;56209;319964;59787
    ITA;2013;370253;57781;159757;137700
    ITA;2014;350126;55837;158481;121589
    ...

E come file dei comandi il file `queries.txt`:

    paese AUS Gas
    paese ITA Petrolio
    massimo 2021 Petrolio
    massimo 2016 Gas

L'output generato dal programma sarà il seguente:

    Nome file: GCB2023.csv
    Anni monitorati: da 2013 a 2022
    Paesi monitorati: AUS BRA GBR ITA MEX
    Quantita monitorate: Totale Carbone Petrolio Gas

    Paese: AUS - Valore: Gas
        2013    2014    2015    2016    2017    2018    2019    2020    2021    2022
       69870   70771   71500   73935   75430   78468   80661   83479   80159   83499
    Differenza: +19.51%

    Paese: ITA - Valore: Petrolio
        2013    2014    2015    2016    2017    2018    2019    2020    2021    2022
      159757  158481  162217  156806  149602  153616  149355  128330  147624  155162
    Differenza: -2.88%

    Anno: 2021 - Valore: Petrolio
    Paese massimo: BRA (305275, +126.66% rispetto al minimo)

    Anno: 2016 - Valore: Gas
    Paese massimo: GBR (165742, +137.91% rispetto al minimo)
