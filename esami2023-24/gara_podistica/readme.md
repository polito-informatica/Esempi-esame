#  Gara podistica

#### (Esame proposto il 05/07/2024)

Si vogliono organizzare 4 gare podistiche della durata di 5km, 10km, 20km e 40km. I partecipanti che desiderano accedere alle competizioni sono registrati in un file di testo, denominato `atleti.txt`, contenente le seguenti informazioni:

```
codice;competizione;tempo1,tempo2,…,tempoN
```

- *codice*: contiene il codice identificativo univoco per ogni atleta;
- *competizione*: contiene un codice 0, 1, 2 e 3 rispettivamente per le competizioni di 5km, 10km, 20km e 40km;
- *tempo1,tempo2,…,tempoN*: rappresenta una sequenza di tempi di allenamento relativa alla competizione selezionata

Le 3 categorie di dati *codice*, *competizione*, *tempo* sono **separate da un punto e virgola** senza spazi, mentre **i dati relativi ai vari tempi di allenamento** sono **separati da una virgola** anche questi senza spazi. Il numero di tempi di allenamento per partecipante risulta essere il medesimo per tutti (ma non è noto a priori).

Si scriva un programma che **calcoli (e stampi a video)** il ***tempo di riferimento*** per ciascuna competizione, corrispondente alla media di tutti i tempi di allenamento di tutti gli atleti su tale competizione.

Per permettere di effettuare una selezione degli atleti in base ai loro tempi di allenamento, si completi il programma in modo che: 

1. per **ogni tipologia** di competizione, **individui (e stampi a video)** il **numero** di atleti con tempo medio di allenamento che si discosta, al massimo, del 10% dal tempo medio di riferimento; 
2. **individui** gli atleti che, **negli ultimi 3 allenamenti** (ovvero, negli ultimi tre valori della loro lista di tempi di allenamento), hanno un **tempo medio** che si discosta, al massimo, del 3% dal tempo medio di riferimento e stampi i loro nomi a video; 
3. stampi a video il **numero totale di partecipanti che hanno superato la selezione** del punto 1 (indipendentemente dalla tipologia di competizione), rispetto al numero totale di atleti iscritti. Inoltre, stampi la rispettiva percentuale visualizzandola con due cifre decimali.

**NOTA 1**: lo scostamento in percentuale tra il tempo `t` e il tempo medio `TM` si calcola come `abs( (t - TM) / TM) * 100.0`

**NOTA 2**: oltre al file di esempio del testo (atleti.txt) il compito contiene anche un secondo file di prova più corto (atleti_short.txt) per accorciare i tempi di test del vostro programma

### Esempio di Esecuzione

Esempio di contenuto del file `atleti.txt` in input

```
AA;0;17.52,32.17,31.19,27.33,40.73,30.04,32.68,6.43,...
AB;1;70.11,46.91,38.49,44.98,59.32,23.56,53.82,65.19,...
AC;1;98.85,81.8,2.85,47.29,111.97,57.0,19.69,76.47,...
AD;3;351.14,272.33,158.32,282.28,218.07,254.72,117.75,...
AE;2;92.86,92.36,135.35,119.79,232.5,226.38,124.05,...
AF;0;24.57,9.99,51.38,20.83,10.85,37.97,23.32,23.34,...
AG;3;192.85,225.87,433.06,128.34,70.81,276.52,342.37,...
AH;2;157.1,214.95,197.84,149.03,233.65,146.34,167.62,...
AI;2;168.41,53.85,155.84,155.99,69.22,121.03,121.6,...
AJ;2;114.54,186.64,56.24,117.43,118.07,105.4,238.83,...
```

Esempio di output in relazione ai dati forniti:

```
Tempi medi di competizione
5 km: tempo medio 26.79
10 km: tempo medio 58.89
20 km: tempo medio 119.75
40 km: tempo medio 260.14

Gli atleti per la gara 5k sono: 100
Gli atleti nel 3% sono ['BN', 'CS', 'FC', 'IP', 'PD', 'SE', 'UL', 'VQ', 'WN', 'WW']

Gli atleti per la gara 10k sono: 108
Gli atleti nel 3% sono ['BD', 'HB', 'MI', 'MK', 'MY', 'NV', 'OG', 'PI', 'QB', 'XU', 'YY', 'ZF']

Gli atleti per la gara 20k sono: 117
Gli atleti nel 3% sono ['BL', 'FS', 'GX', 'HO', 'NE', 'OQ', 'PV', 'UM', 'UP', 'XR']

Gli atleti per la gara 40k sono: 104
Gli atleti nel 3% sono ['AG', 'BF', 'FQ', 'HE', 'MN', 'VA', 'WP', 'XX']

In totale gli atleti selezionati sono 429 su 676 (63.46%)
```