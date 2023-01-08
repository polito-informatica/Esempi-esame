# Mezzi Pubblici

#### (Esame proposto il 01/07/2022)

Una società di trasporti ha raccolto una serie di dati relativi all'affluenza di passeggeri sui mezzi pubblici. I dati
registrati in una giornata sulla tratta Aeroporto-Torino (da capolinea a capolinea) sono raccolti in un file di testo (
chiamato `dati_aeroporto_torino.csv`).

I dati riportati su ogni linea, separati da virgola, sono:

- Il **codice autista** (una stringa alfanumerica composta da '`A`' ed un numero su 3 cifre, es. `A001`)
- L'**ora di partenza** dal capolinea (nel formato `hh:mm`)
- Il **numero passeggeri** saliti e/o scesi ad ogni fermata.

**Attenzione**: Il numero di fermate di una tratta (e quindi il numero di campi del file CSV) non è specificato a
priori. Una tratta può essere vista come lista di fermate. La **prima riga** del file riporta un'intestazione con i
campi 'ID', 'Time' e poi **i codici di ogni fermata** (stringhe alfanumeriche composte da '`F`' e numeri su 3 cifre,
es. `F001`). Quindi, il numero totale di fermate della tratta può essere ricavato dall'intestazione.

I passeggeri che salgono o scendono nelle varie fermate sono indicati in uno specifico formato. In particolare, per ogni
fermata, è indicato uno dei quattro valori seguenti:

- `n`: indica che `n` passeggeri sono saliti e nessuno è sceso
- `-n`: indica che `n` passeggeri sono scesi e nessuno è salito
- `n/m`: indica che `n` passeggeri sono saliti ed `m` sono scesi
- `--`: indica che nessuno è salito o sceso

`n` ed `m` sono numeri interi positivi (maggiori di 0).

Un secondo file (denominato `database.txt`) contiene i nomi degli autisti e delle fermate e permette di associarli al
corrispettivo codice. Ogni riga del file presenta il formato `Codice:Nome` (separati dal carattere '`:`'), in cui `Codice`
è il codice di un autista (se inizia con `A`) o di una fermata (se inizia con `F`) e `Nome` è il corrispondente nome
dell'autista o della fermata.

**Attenzione**: notare che il file contiene anche codici relativi ad autisti e fermate _non presenti_ nel primo file.

Scrivere un programma Python che legga i due file e stampi a video:

* Il **nome** della fermata da cui sono saliti il maggior numero di passeggeri (indipendentemente da quanti ne sono scesi).
* Il **nome** della fermata da cui sono scesi il maggior numero di passeggeri (indipendentemente da quanti ne sono saliti).
* La **lista dei nomi** degli autisti, ordinata in modo **decrescente** in base al numero totale di passeggeri **saliti**
sul loro mezzo nel corso dell'intera giornata (N.B.: un autista può percorrere la stessa tratta più volte nel corso di una
giornata, bisogna considerare i passeggeri complessivi).

## Esempio
### Contenuto parziale del file"dati_aeroporto_torino.csv"

**Nota**: gli spazi sono stati aggiunti per migliorarne la visualizzazione, ma non sono presenti nel file.

    ID,   Time,  F042,  F043,  F044,  F039,  F009,  F010,  F011,  F012,  F013
    A012, 06:15,   13,    13,    11,     9,    -1,    -1,    -2,   -16,   -26
    A003, 06:30,   13,    15,    20,     5,    -2,    -2,    -2,   -18,   -29
    A041, 06:45,   16,    18,     1,    17,    -4,    -2,    -2,   -17,   -27
    A240, 07:00,   13,    32,     7,    13,    -2,    -2,    -3,   -22,   -36
    A119, 07:15,    3,    43,    34,    --,    -2,    -3,    -4,   -28,   -43
    A015, 07:30,    4,    25,    29,    22,    -3,    -3,    -3,   -28,   -43
    A154, 07:45,    3,    20,     3,    11,    -1,    -1,    -2,   -13,   -20
    A008, 08:00,   28,  17/1,   5/1,  33/1,    -5,    -3,    -4,   -28,   -40
    A012, 08:15,   29,  18/1,   5/1,  31/1,    -5,    -3,    -4,   -28,   -40
    A003, 08:30,   12,    23,    42,     3,    -3,    -3,    -3,   -28,   -43
    A041, 08:45,   46,  35/1,   1/1,   1/1,    -6,    -2,    -3,   -26,   -43
    [...]

### Contenuto parziale del file"database.txt"

    [...]
    A156:Emperatriz de Albero
    A189:Amico Rusticucci
    A200:Elladio Endrizzi
    A202:Alderano Tiepolo
    A212:Livio Cuda
    A240:Danilo Bazzi
    A250:Matilde Rossi
    F009:Torino 1
    F010:Torino 2
    F011:Torino 3
    F012:Torino P. Susa
    F013:Torino P. Nuova
    F014:Torino Lingotto
    F021:Venaria 1
    [...]

### Esempio di output

    La fermata in cui salgono più passeggeri (1626) è Aeroporto
    
    La fermata in cui scendono più passeggeri (1755) è Torino P. Nuova
    
    Lista di autisti ordinata in base al numero di passeggeri:
    Giacobbe Comboni con 335 passeggeri
    Danilo Bazzi con 316 passeggeri
    Ida Contarini con 301 passeggeri
    Eliana Capuana con 296 passeggeri
    Adele Venditti con 289 passeggeri
    Ivo Cendron con 284 passeggeri
    Fausto Papafava con 257 passeggeri
    Arsenio Sollima con 246 passeggeri
    Adelasia Ceravolo con 163 passeggeri
    Elladio Endrizzi con 149 passeggeri
    Barbara Bush con 140 passeggeri
    Luisa Franscini con 117 passeggeri
    Livio Cuda con 111 passeggeri
    Filippo Gregorio con 107 passeggeri
    Felipe Casal Muñoz con 98 passeggeri
    Silvio Cabibbo con 87 passeggeri


