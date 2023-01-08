# Costo Prodotto

#### (Esame proposto il 14/02/2022)

Si realizzi in linguaggio Python un programma per individuare il paese dove un prodotto costa meno.

Il programma legge due file di testo. Il primo file, chiamato `exchange.txt`, contiene i tassi di cambio in Euro di un
certo numero di valute secondo il seguente formato:

    <codice valuta> <euro per unità>  

Si assuma che il formato del file sia corretto.

Un secondo file, il cui nome _deve essere fornito in input_ dall'utente, contiene il prezzo di un certo prodotto in
diversi paesi ed in diverse valute nel seguente formato:

    <nome paese>;<codice valuta>;<prezzo>

Si assuma che in questo secondo file tutti i codici valuta siano anche presenti nel file `exchange.txt`. L'unica
eccezione sono i _prezzi in euro_, in quanto non richiedono di essere convertiti.

Il programma dovrà leggere i due file di testo e stampare a video il paese in cui il prodotto **costa meno** ed il suo
prezzo in Euro con due cifre decimali.

## Esempio:

### Esempio file `exchange.txt`:

    USD 0.8829097484  
    GBP 1.1680390537  
    INR 0.0117073578  
    AUD 0.6325980696   
    CAD 0.6976847548  
    AED 0.2404110955

### Esempio file `iphone13mini.txt`:

    USA;USD;699  
    CANADA;CAD;949  
    AUSTRALIA;AUD;1199  
    INDIA;INR;69900  
    EMIRATI;AED;2999  
    FRANCE;EUR;750

### Esempio esecuzione

L'esecuzione del programma deve produrre il seguente output:

    Il paese dove il prodotto costa meno è: USA  
    Prezzo in Euro: 617,15  


