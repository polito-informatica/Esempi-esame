# Superenalotto

#### (Esame proposto il 05-06/02/2024)

I partecipanti al gioco del Superenalotto pagano una cifra variabile per giocare una schedina da 6 numeri (da 1 a 90). Dopo un certo lasso di tempo, gli organizzatori estraggono 6 numeri, detti numeri vincenti. I partecipanti vincono premi a seconda di quanti numeri estratti sono sulla loro schedina.

Scrivere un programma in python che si occupi di assegnare i premi ai vincitori dell'estrazione del supernealotto. Nello specifico, vengono forniti 3 file di testo, `"schedine.txt"`, `"vincente.txt"` e `"premi.txt"`. Il primo, `"schedine.txt"` contiene tutte le schedine valide giocate con il seguente formato:

    id_schedina,numero1,numero2,numero3,numero4,numero5,numero6,costo_schedina

dove `numero1`/`2`.../`6` e' un intero da 1 a 90 oppure un carattere `"*"`, cioe' un numero bonus (chiamato wildcard nel seguito) che puo' prendere il valore di un qualsiasi numero vincente. La wildcard puo' essere solo una nella schedina e se presente puo' essere in qualsiasi posizione. `costo_schedina` e' un float.

Il secondo file contiene i 6 numeri della sequenza vincente con il seguente formato:

    numero1 numero2 numero3 numero4 numero5 numero6

in questo caso, `numero1`-`6` sono interi da 1 90 (nessun asterisco presente), L'ultimo file contiene una lista di categorie di premi con l'ammontare delle vincite, con il seguente formato:

    6   premio1
    5   premio2
    4   premio3
    3   premio4
    2   premio5 
    1   premio6

dove `premio1`-`6` e' un intero che riporta il valore della vincita per una schedina che ha `N` dei numeri esatti (dove `N` e' il numero nella prima colonna). Il premio per 1 o 2 numeri indovinati e' sempre zero (vedi file di esempio).

I premi vengono assegnati come segue: alla schedina che indovina `N` dei numeri viene assegnato solo il premio per `N` numeri indovinati e non anche quello da `N-1`, `N-2`, etc.

Il programma deve:

1. Calcolare per ogni schedina la vincita ottenuta.
2. Stampare la vincita in euro di ogni schedina, con il seguente formato:

    ```
    Schedine Vincenti:
    ID_SCHEDINA: ...  -- NUMERI_INDOVINATI: ....  VINCITA: ....
    ...
    ```

    Attenzione: 
    - Le schedine che danno una vincita di 0 (1 o 2 numeri indovinati nell'esempio) non vanno stampate 
    - Le schedine devono essere stampate in ordine decrescente di vincita 
    - Il campo NUMERI_INDOVINATI: riporta i numeri vincenti che ci sono nella schedina, compreso l'asterisco 
    - Il campo VINCITA deve riportare l'importo finale inviato alle persone.

3. Stampare il guadagno degli organizzatori, dato dal guadagno totale della vendita delle schedine meno i premi assegnati.

## Esempio di esecuzione

Dati i seguenti premi (`premi.txt`)

    6   180
    5   40
    4   30
    3   20  
    2   0
    1   0

La seguente serie di schedine (`schedine.txt`)

    1,11,22,87,42,28,63,1.5
    2,23,34,49,39,31,1,1.5
    3,41,2,14,13,19,73,1.5
    4,34,71,80,*,29,42,135.0
    5,69,34,88,59,22,12,1.5
    6,26,4,2,22,63,89,1.5
    7,84,59,66,52,19,81,1.5
    8,34,*,18,86,59,22,135.0

e la serie di numeri vincenti (file `vincente.txt`)

    11 63 22 28 34 59

Il programma deve produrre il seguente output

    Schedine Vincenti:
    ID_SCHEDINA: 1 NUMERI_INDOVINATI: 11 63 22 28 VINCITA: 30  TIPO PREMIO: 4
    ID_SCHEDINA: 8 NUMERI_INDOVINATI: * 22 34 59 VINCITA: 30  TIPO PREMIO: 4
    ID_SCHEDINA: 5 NUMERI_INDOVINATI: 22 34 59 VINCITA: 20  TIPO PREMIO: 3

    Guadagno netto degli organizzatori: 229.0 euro
