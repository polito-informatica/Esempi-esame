# Gestione del prestito PC aziendali

#### (Esame proposto il 30-31/01/2023)

L'ufficio tecnico di una grande azienda dispone di un certo numero di PC da dare in prestito ai dipendenti in caso di
bisogno (ad esempio, quando il loro PC personale è in assistenza oppure sono in attesa di acquistarne uno nuovo).

L'elenco di tutti i PC adibiti a questo scopo è contenuto in un file di testo `parcoPC.txt`, che riporta su ciascuna riga
il codice identificativo univoco di un PC (stringa alfanumerica di 4 caratteri). I PC non sono elencati in un ordine
specifico.

Un secondo file di testo `registrazioni.txt` riporta tutti i prestiti e le restituzioni di PC **ordinati in ordine
cronologico**. In particolare, ciascuna riga del file riporta le seguenti informazioni:

    machineID:personID:data

Dove **machineID** è il codice identificativo del PC, **personID** è la matricola univoca del dipendente (una stringa di 6
cifre) che ha preso in prestito oppure restituito il PC, **data** è la data del prestito o restituzione, in formato
gg/mm/aaaa. Si noti che:

- il file **non distingue in alcun modo** tra prestiti e restituzioni, quindi se la stessa coppia _machineID:personID_ compare
  in due date successive, vuol dire che la prima volta il PC è stato prestato, la seconda volta che è stato restituito.
  Se la coppia _machineID:personID_ compare una volta sola, vuol dire che il PC è attualmente in prestito al dipendente
  _personID_
- un dipendente può avere **più prestiti attivi contemporaneamente** (ovviamente, prestiti di PC diversi)
- **uno stesso PC** può essere **preso in prestito e restituito più volte**, sia dallo stesso dipendente che da dipendenti
  diversi;
- un PC può essere prestato ad un solo dipendente per volta (i.e., non può essere preso in prestito se prima non è stato
  restituito)

Si scriva un programma Python che, una volta lette le informazioni contenute nei due file di input, stampi a monitor:

1. l'**elenco, ordinato per matricola crescente**, dei dipendenti che hanno preso in prestito dei PC che non hanno ancora
   restituito. Per ciascun dipendente, si stampi l'elenco dei codici dei PC che hanno attualmente in prestito, in ordine
   alfabetico.
2. l'**elenco ordinato per matricola crescente** dei PC che sono attualmente disponibili per il prestito.

Nel caso tutti i PC aziendali siano in prestito, il programma deve stampare il messaggio "`Al momento non ci sono PC
disponibili per il prestito`"

## Esempio

### File `parcoPC.txt`

    A021
    A100
    A123
    B015
    B088
    C055
    S100
    S125
    Q034
    Z300
    Z500

### File `registrazioni.txt`

    Q034:100123:31/01/2021
    A123:100123:01/02/2021
    A100:100123:01/02/2021
    B088:123456:10/05/2021
    A123:100123:15/06/2021
    B088:123456:20/06/2021
    A123:123456:21/07/2021
    Z300:135987:22/01/2022
    S100:100012:20/09/2022

### Output del programma (stampato a monitor)

    Elenco dei prestiti in corso: 
    100012: S100
    100123: A100, Q034
    123456: A123
    135987: Z300
    
    PC disponibili per il prestito: A021, B015, B088, C055, S125, Z500
