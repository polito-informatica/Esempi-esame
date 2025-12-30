# Scuola di magia

#### (Esame proposto il 10/09/2025)

Il Ministero della Magia ha chiesto una relazione dettagliata sui risultati dell’esame di fine anno degli studenti della scuola di magia di Hogwarts, in modo da identificare le eccellenze e le difficoltà nelle diverse casate e materie. I risultati sono contenuti in un file `risultati.csv` in cui ogni riga rappresenta un voto ottenuto da uno studente in una determinata materia, con i seguenti campi:

```
nome,cognome,casata,materia,punti
````

dove casata è la casata di appartenenza dello studente, e i punti sono un valore intero tra 0 e 100. Si assuma, per semplicità, che non ci siano studenti con lo stesso nome e cognome, e che il file non sia vuoto e non contenga errori di formato. I dati sono riportati senza un ordine particolare, e la prima riga del file contiene il nome dei campi. Si scriva un programma Python che:

1. Legga i dati dal file CSV, salvandoli come una lista di dizionari. È richiesto gestire opportunamente l’eccezione generata dall’apertura del file.
2. Calcoli e stampi a monitor la media dei punti per ciascuna casata, riportando le casate in ordine alfabetico e le medie con due cifre decimali.
3. Identifichi e stampi a monitor lo studente con la media più alta
4. Identifichi e stampi a monitor la materia più facile e quella più difficile (rispettivamente, quelle con la media più alta e più bassa)

Per i punti 3 e 4, si assuma per semplicità che non esistano casi di parimerito.

## Esempio

#### `risultati.csv`:

```
nome,cognome,casata,materia,punti
Harry,Potter,Grifondoro,Difesa contro le Arti Oscure,95
Draco,Malfoy,Serpeverde,Pozioni,90
Hermione,Granger,Grifondoro,Pozioni,99
Hermione,Granger,Grifondoro,Aritmanzia,100
Luna,Lovegood,Corvonero,Erbologia,85
Ron,Weasley,Grifondoro,Difesa contro le Arti Oscure,75
Harry,Potter,Grifondoro,Trasfigurazione,85
Ron,Weasley,Grifondoro,Pozioni,70
Draco,Malfoy,Serpeverde,Trasfigurazione,76
Hermione,Granger,Grifondoro,Erbologia,88
Draco,Malfoy,Serpeverde,Difesa contro le Arti Oscure,82
Luna,Lovegood,Corvonero,Aritmanzia,92
Neville,Paciock,Grifondoro,Erbologia,95
Neville,Paciock,Grifondoro,Pozioni,60
Harry,Potter,Grifondoro,Pozioni,78
````

#### Output a schermo:

```
Media dei punti per casata:
- Corvonero: 88.50
- Grifondoro: 84.50
- Serpeverde: 82.67

Studente con la media più alta: Hermione Granger (95.67)

Materia più facile: Aritmanzia (96.00)

Materia più difficile: Pozioni (79.40)
```