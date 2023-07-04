# Calcolo delle statistiche di un torneo sportivo

#### (Esame proposto il 30/06/2023)

IL gazzettino dello Sport ti chiede di sviluppare un programma in Python per calcolare le statistiche di un torneo di
calcio. Il programma deve ricevere in input un file (`partite.txt`) con i risultati delle partite giocate. Il file in
ingresso ha questo formato:

        squadra1:squadra2:punteggio1:punteggio2

Dove tutti i campi sono separati dal carattere "`:`" (e.g.: `Milan:Inter:2:1`)

Il programma deve generare in output le seguenti informazioni:

1. **Classifica del torneo**:
   - Il programma deve tenere traccia dei punti ottenuti da ciascuna squadra, assegnando 3 punti per una vittoria, 1 punto per un pareggio e 0 punti per una sconfitta.
   - La classifica finale deve essere ordinata in ordine decrescente in base al numero di punti
   - Il programma deve stampare oltre ai punti anche i gol fatti e i gol subiti dalla squadra
5. **Calcolo del miglior attacco**:
   - Il programma deve stampare la squadra che ha segnato più gol durante il torneo insieme al numero di gol segnati (in caso di parità, stampare la prima squadra trovata).
7. **Calcolo della miglior difesa**:
   - Il programma deve stampare la squadra che ha subito meno gol durante il torneo con il numero di gol subiti (in caso di parità, stampare la prima squadra trovata).

### Esempio di input:

        Inter:Milan:2:2
        Juventus:Roma:1:0
        Milan:Juventus:0:1
        Roma:Inter:1:2
        Inter:Juventus:2:1
        Roma:Milan:0:0

### Output generato dal programma:

        Classifica:
        
        1. Inter - Punti: 7, Gol fatti: 6, Gol subiti: 4
        2. Juventus - Punti: 6, Gol fatti: 3, Gol subiti: 2
        3. Milan - Punti: 2, Gol fatti: 2, Gol subiti: 3
        4. Roma - Punti: 1, Gol fatti: 1, Gol subiti: 3
        
        Miglior attacco: Inter - Gol fatti: 6
        Miglior difesa: Juventus - Gol subiti: 2
