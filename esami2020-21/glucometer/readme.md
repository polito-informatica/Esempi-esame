# Testo d'esame "Glucometer"

I dispositivi indossabili di nuova generazione permettono a pazienti affetti da diabete mellito un monitoraggio continuo
e non invasivo della glicemia. I valori dei singoli dispositivi sono inviati con cadenza giornaliera ad un data-center
che assembla un unico file contenente i dati di tutti i pazienti connessi al servizio di monitoraggio. Si vuole
realizzare un programma in grado di estrarre alcune statistiche. Nello specifico, è richiesto un controllo sui
superamenti del livello massimo 200mg/dL.

Seguono le specifiche tecniche.

Il programma deve gestire un file di input `glucometers.txt` contenente i dati di un'intera giornata di misurazione.
Tale file deve intendersi come un aggregato dei dati raccolti e quindi contenente, in ordine sparso, i dati di tutti i
pazienti.

I dati di un singolo paziente sono in ordine cronologico e possono verificarsi misurazioni mancanti (intervalli in cui
il paziente non indossa il dispositivo).

Tutte le misurazioni sono effettuate a frequenza regolare: un campione ogni 5 minuti.

Ogni riga del file contiene 5 diversi dati separati da singolo spazio e nel seguente ordine:

1. codice identificativo paziente composto di 4 caratteri esadecimali (formato PPPP);
2. orario di acquisizione (formato hh:mm)
3. valore glicemico (g)
4. temperatura corporea (°C)
5. frequenza cardiaca (bpm).

Il programma, dopo aver memorizzato i dati in un'opportuna struttura dati, dovrà stampare su video l'elenco di tutti i
pazienti che hanno registrato almeno un superamento e, per ogni superamento, l'ora ed il livello di glicemia
corrispondente. L'elenco dovrà apparire in ordine di criticità, partendo dal paziente con più superamenti

# Esempio file input:

	1BF0 17:00 160 37.0 68
	1BF0 17:05 168 37.0 68
	1BF0 21:00 180 37.3 66
	1BF0 21:05 210 37.1 67
	0AE1 21:10 187 37.3 69
	0AE1 21:15 192 37.3 70
	0AE1 21:20 195 37.4 70
	0AE1 21:25 201 37.4 75
	BBB3 22:30 108 37.5 73
	BBB3 22:35 200 37.5 73
	0AE1 23:05 203 37.4 73
	0AE1 23:10 210 37.5 71
	1BF0 21:10 213 37.2 68

# Esempio file output:

	0AE1 21:25 201
	0AE1 23:05 203
	0AE1 23:10 210

	1BF0 21:05 210
	1BF0 21:10 213

	BBB3 22:35 200
