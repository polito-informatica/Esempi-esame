# e-commerce

#### (Esame proposto il 10-11/02/2025)

Un negozio di e-commerce ti ha assunto per analizzare i dati relativi agli ordini ricevuti nell’ultimo mese. Questi dati sono memorizzati in un file CSV chiamato `ordini.csv`, che contiene i seguenti campi:

- ID ordine: un numero progressivo univoco che identifica l’ordine
- Prodotto: il nome del prodotto
- Quantità: il numero di unità acquistate
- Prezzo unitario: il prezzo in euro di una singola unità del prodotto
- Cliente: il nome del cliente che ha effettuato l’ordine

La prima riga del file riporta il nome dei campi di ciascun ordine d’acquisto, come nell'esempio seguente:

```
ID ordine,Prodotto,Quantità,Prezzo unitario,Cliente
1,Smartphone,2,599.99,Rossi Mario
2,Laptop,1,899.99,Verdi Anna
3,Cuffie,5,49.99,Bianchi Luca
4,Mouse,3,19.99,Rossi Mario
5,Monitor,2,199.99,Neri Sara
6,Mouse,1,19.99,Verdi Anna
```

Ti è richiesto di scrivere un programma Python che stampi a monitor le seguenti informazioni:

1. La lista dei nomi dei clienti riportati in ordine alfabetico uno per riga, con il numero totale di ordini effettuati da ciascuno

2. Il nome del cliente con la spesa totale maggiore e il relativo importo totale speso, visualizzato con due cifre decimali. Si assuma per semplicità che tale cliente sia uno solo, senza parimerito.

3. Il nome del prodotto con meno unità vendute. Si assuma per semplicità che tale prodotto sia uno solo, senza considerare eventuali parimerito.

Assumendo (ad esempio) un file `ordini.csv` come quello riportato sopra, l'output generato dal programma dovrebbe essere il seguente:

```
Numero di ordini di ciascun cliente:
- Bianchi Luca: 1
- Neri Sara: 1
- Rossi Mario: 2
- Verdi Anna: 2
Cliente con la spesa totale maggiore:
- Rossi Mario, con un totale di 1259.95 euro.
Prodotto meno venduto:
- Laptop, con 1 unità vendute.
```

NB. il programma implementato deve gestire opportunamente l'eventuale eccezione sollevata in fase di apertura del file di input. Si assuma che il formato del file sia corretto.