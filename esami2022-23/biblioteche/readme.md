
# Biblioteche

#### (Esame proposto il 19/09/2023)


Scrivere un programma Python che permetta di gestire i libri di una biblioteca comunale. 

Il contenuto dell'ultimo inventario effettuato in biblioteca è riportato nel file **inventarioOld.csv**, che contiene delle righe formattate come segue:

    codiceCopia;codiceISBN;titolo;autore

dove ***codiceISBN*** è il codice ISBN (International Standard Book Number) che identifica univocamente un determinato prodotto letterario, mentre ***codiceCopia*** è un codice alfanumerico che identifica <u>univocamente</u> ogni copia fisica. Quindi, nel caso in cui nella biblioteca siano presenti diverse copie dello stesso libro, queste saranno riportate in righe diverse, con lo stesso ***codiceISBN*** ma diversi ***codiceCopia***. L’inventario riporta tutti i libri senza un ordine specifico. 

Per semplicità di lettura del file, si supponga che nessuno dei campi contenga il carattere punto e virgola, che è quindi presente nel file solamente come carattere di separazione dei diversi campi.

La biblioteca comunale ha intenzione di selezionare tutti i libri che siano presenti in numero maggiore di 3 copie, in modo da poter regalare le copie in eccesso di questi alla biblioteca di una scuola. 

Scrivete un programma Python che implementi le seguenti operazioni:

- Nel caso in cui ci siano dei libri che superano il numero di 3 copie, generare un file **inventarioScuola.csv**, che contenga l’elenco dei libri da regalare alla scuola. Il numero totale di libri e di copie fisiche regalate alla scuola deve essere anche stampato a schermo.

- Generare un nuovo inventario della biblioteca **inventarioNew.csv**, privato di tutte le copie dei libri che sono state regalate alla scuola.

Entrambi i file **inventarioScuola.csv** e **inventarioNew.csv** devono riportare i libri in una forma più compatta rispetto all’inventario originale. In particolare, i libri devono essere riportati: 

1. ordinati alfabeticamente per ISBN, 
2. ciascun ISBN dovrà comparire una sola volta nel file, e deve essere seguito dalle informazioni del libro (titolo, autore, lista di tutti i codici delle copie del libro rimanenti nella biblioteca) 

Nel dettaglio, il nuovo formato delle righe di questi file è il seguente:

    codiceISBN;titolo;autore;codiceCopia1;codiceCopia2;…;codiceCopiaN

dove **codiceCopia1, codiceCopia2,…codiceCopiaN** rappresentano i codici delle N diverse copie del libro.


## Esempio di contenuto del file inventarioOld.csv in input

    XY128;978-81-7525-766-5;Odissea;Omero
    FZ114;978-88-7775-766-7;Frankenstein o il moderno Prometeo; Mary Shelley
    XY123;978-81-7525-766-5;Odissea;Omero
    AB001;978-23-7525-7546-2;Iliade;Omero
    FZ111;978-88-7775-766-7;Frankenstein o il moderno Prometeo; Mary Shelley
    YY128;978-81-7525-766-5;Odissea;Omero
    XY124;978-81-7525-766-5;Odissea;Omero
    MN214;978-88-3175-866-0;Candido, o l'ottimismo;Voltaire
    XY125;978-81-7525-766-5;Odissea;Omero
    FZ112;978-88-7775-766-7;Frankenstein o il moderno Prometeo; Mary Shelley
    XY126;978-81-7525-766-5;Odissea;Omero
    BA013;999-77-7525-766-5;Il gabbiano Jonathan Livingston;Richard Bach
    FZ115;978-88-7775-766-7;Frankenstein o il moderno Prometeo; Mary Shelley
    FZ113;978-88-7775-766-7;Frankenstein o il moderno Prometeo; Mary Shelley
    FZ116;978-88-7775-766-7;Frankenstein o il moderno Prometeo; Mary Shelley
    XY100;978-81-7525-766-5;Odissea;Omero

In caso il file di input sia come sopra, il programma stamperà a schermo il seguente messaggio:

    Numero libri da regalare: 2, copie totali: 7

Inoltre, genererà i seguenti file:

### inventarioScuola.csv

    978-81-7525-766-5;Omero;Odissea;XY100;XY124;XY125;XY126
    978-88-7775-766-7; Mary Shelley;Frankenstein o il moderno Prometeo;FZ113;FZ115;FZ116

### inventarioNew.csv

    978-23-7525-7546-2;Omero;Iliade;AB001
    978-81-7525-766-5;Omero;Odissea;XY123;XY128;YY128
    978-88-3175-866-0;Voltaire;Candido, o l'ottimismo;MN214
    978-88-7775-766-7; Mary Shelley;Frankenstein o il moderno Prometeo;FZ111;FZ112;FZ114
    999-77-7525-766-5;Richard Bach;Il gabbiano Jonathan Livingston;BA013
