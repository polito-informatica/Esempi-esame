# Gestione risultati di una gara podistica

#### (Esame proposto il 13-14/02/2023)

Si realizzi un programma strutturato in Python che gestisca in maniera automatica i
risultati di una gara podistica di 10 km. Le informazioni relative alla gara
sono registrate nel file `risultati_gara.txt`.

Il file contiene, in ogni riga, i seguenti dati relativi ai partecipanti 
(separate da punto e virgola):

    <Nome>;<Cognome>;<Età>;<Categoria (M/F)>;<Tempo (min)>;<ID_Atleta>

I partecipanti sono elencati in ordine di arrivo.

In un secondo file, `database_atleti.txt`, sono contenuti i record personali 
(espressi come passo, in min/km) di ogni atleta, in questo formato:

    <ID_Atleta>;<Record Personale>

Il record personale è indicato con un numero a virgola mobile, dove la cifra intera indica i minuti e le cifre decimali i secondi.

Si facciano le seguenti assunzioni:
* Il numero di atleti non è noto a priori 
* L'ID di ogni atleta è univoco 
* Il formato del file è corretto

Il programma deve:

1) Caricare le informazioni contenute nel file `risultati_gara.txt` in una struttura dati opportuna

2) Calcolare il passo di ciascun atleta (min/km), secondo la seguente formula:

    passo = tempo / km

Se la divisione non restituisce un numero esatto di minuti, moltiplicare le cifre decimali per 0.6 per ottenere il passo corretto. Ad esempio:

    tempo = 32 minuti
    distanza = 10 km

    passo_temporaneo = 32/10 = 3.2

    minuti: 3
    secondi: 0.2*0.6 = 0.12

    passo = minuti + secondi = 3.12 min/km

1. Stampare a video l'elenco degli atleti, separati per categoria (M o F), 
riportando nome, cognome, e passo (min/km, con due cifre decimali).

2. Stampare a video l'elenco degli atleti che hanno superato il loro record
personale (un atleta per ogni riga).

### Esempio

#### File: `risultati_gara.txt`

    David;Coq;41;M;33;FR90M1
    Jaxon;Reed;28;M;34;US74M2
    Maximilian;Hofer;40;M;35;AT87M1
    Lena;Bauer;31;F;35;DE90W2
    Giuseppina;Sandberg;25;F;36;SE22W1
    Maria;Gonzalez;28;F;44;SP00W2
    Juan;Rodriguez;35;M;45;SP27M1
    Nadia;Patel;37;F;48;GB59W2

#### File: `database_atleti.txt`

    FR90M1;3.15
    US74M2;3.57
    AT87M1;4.15
    DE90W2;3.25
    SE22W1;3.40
    SP00W2;4.20
    SP27M1;4.28
    GB59W2;4.20

#### Output di stampa

    CLASSIFICA DEI PARTECIPANTI
    
    Categoria: M
    David Coq, 3.18 min/km
    Jaxon Reed, 3.24 min/km
    Maximilian Hofer, 3.30 min/km
    Juan Rodriguez, 4.30 min/km
    
    Categoria: F
    Lena Bauer, 3.30 min/km
    Giuseppina Sandberg, 3.36 min/km
    Maria Gonzalez, 4.24 min/km
    Nadia Patel, 4.48 min/km
    
    ATLETI CHE HANNO SUPERATO IL RECORD PERSONALE
    
    Jaxon Reed
    Maximilian Hofer
    Giuseppina Sandberg

