# Musica classica

#### (Esame proposto il 27-28/01/2025)

Scrivere un programma Python che permetta di gestire una collezione di musica classica che contiene le tracce che compongono le varie opere salvate nella collezione. Si noti che, nella musica classica, **ogni opera** può essere costituita da **più movimenti**, ciascuno dei quali è stato **salvato** nella collezione come una **traccia separata**.

Il programma legge il file `musicnet.csv`, contenente le informazioni relative alla raccolta musicale, in cui la prima riga del file contiene l'intestazione delle colonne ed è costante. Le righe successive contengono le informazioni relative a tutte le **tracce**, separate da virgola ('`,`'), e contengono i seguenti dati:

- **l'identificativo univoco della traccia**, specifico di questa raccolta
- **il nome del compositore**
- **il titolo dell'opera**
- **il titolo del movimento** (cioè della singola traccia)
- **la formazione musicale** (cioè gli strumenti coinvolti, ad esempio quartetto d'archi, pianoforte solista, ecc.)
- **il numero di catalogo** dell'opera, univoco a livello internazionale
- **la durata** della traccia in **secondi**.

Il programma deve leggere i dati della raccolta musicale dal file e permettere all'utente di fare due tipi di interrogazioni (_memorizzate nel file `richieste.txt`, nel formato specificato in seguito_):

1. **Interrogare per compositore**: Dato un compositore, il programma deve stampare **per ogni opera del compositore scelto**:
    - numero di catalogo dell'opera
    - titolo dell'opera
    - durata totale (ottenuta sommando la durata di tutti i movimenti dell'opera)
    - numero di movimenti che costituiscono l'opera
    - durata media dei movimenti.
2. **Interrogare per formazione musicale**: Il programma deve stampare compositore e numero di catalogo di **ciascuna opera** contenuta nella collezione **che prevede esattamente quella formazione musicale**.

In entrambi i casi, se il compositore (o la formazione musicale) non sono contenuti in elenco, bisogna stampare un messaggio su video che esplicita che l'elemento indicato non è presente nel catalogo

**Le interrogazioni da eseguire sono memorizzate nel file `richieste.txt`**, che contiene un comando per riga con il seguente formato:

- `c:compositore` per interrogare su un certo compositore
- `s:formazione musicale` per interrogare su una formazione musicale

quindi i due campi sono separati da '`:`', il primo definisce il comando, il secondo il dato da usare per la ricerca

**NOTA**: si supponga che tutti i file siano presenti, e che il loro formato sia corretto. 

### Esempio di Esecuzione

#### Estratto di file `musicnet.csv`

```
id,composer,composition,movement,ensemble,catalog_name,seconds
1788,Mozart,String Quartet No 19 in C major,1. Adagio - Allegro,String Quartet,K465,513
1789,Mozart,String Quartet No 19 in C major,2. Andante cantabile,String Quartet,K465,461
1790,Mozart,String Quartet No 19 in C major,3. Menuetto. Allegro,String Quartet,K465,323
1791,Mozart,String Quartet No 19 in C major,4. Allegro molto,String Quartet,K465,351
1792,Mozart,String Quartet No 19 in C major,1. Adagio - Allegro,String Quartet,K465,472
1793,Mozart,String Quartet No 19 in C major,2. Andante cantabile,String Quartet,K465,504
2138,Brahms,String Quartet in C minor,2. Romanze: Poco adagio,String Quartet,OP51NO1,429
2140,Brahms,String Quartet in C minor,4. Allegro,String Quartet,OP51NO1,381
2177,Ravel,String Quartet in F,1. Allegro moderato - tres doux,String Quartet,35,490
2178,Ravel,String Quartet in F,2. Assez vif - tres rythme,String Quartet,35,355
2179,Ravel,String Quartet in F,3. Tres lent,String Quartet,35,505
2180,Ravel,String Quartet in F,4. Vif et agite,String Quartet,35,293

...
```

#### Esempio di comandi (`richieste.txt`)

```
c:Ravel
c:Brahms
s:String Quartet
s:Guitar
c:Bob Dylan
```

#### Esempio di output a video:

```
Opere di Ravel
- 35: String Quartet in F, 1643.00 secondi
    4 movimenti, in media 410.75 secondi

Opere di Brahms
- OP38: Cello Sonata No 1 in E minor, 1652.00 secondi
    3 movimenti, in media 550.67 secondi
- OP51NO1: String Quartet in C minor, 810.00 secondi
    2 movimenti, in media 405.00 secondi
- OP25: Piano Quartet No 1 in G minor, 2430.00 secondi
    4 movimenti, in media 607.50 secondi

Opere con formazione musicale: String Quartet
- Mozart, opera K465
- Mozart, opera K387
- Mozart, opera K421
- Mozart, opera K590
- Mozart, opera K464
- Brahms, opera OP51NO1
- Ravel, opera 35

Opere con formazione musicale: Guitar
Formazione musicale non presente in catalogo

Opere di Bob Dylan
Compositore non presente in catalogo
```
