# Stabilimento balneare

#### (Esame proposto il 13-14/02/2023)

Il gestore di uno stabilimento balneare vuole realizzare un programma per la gestione 
dei posti (sdraio e ombrelloni) del suo stabilimento.

L'area della spiaggia in concessione allo stabilimento è organizzata in file. La 
**prima fila** è quella **più vicina** al mare; l'ultima fila è la più lontana. 
Ogni fila è attrezzata con un certo numero di ombrelloni e sedie a sdraio. 
Il **costo per il noleggio** di ombrelloni e sedie a sdraio <u>dipende</u> dalla fila
in cui si trovano: decresce in base alla lontananza dal mare (ossia, la prima 
fila è la più cara).

L'organizzazione dello stabilimento è memorizzata nel file "`stabilimento.txt`",
in cui **ogni riga** corrisponde ad una fila. La prima riga del file corrisponde alla 
prima fila di ombrelloni (i.e, quella *più vicina* al mare), e così via fino all'ultima.

In ogni riga sono indicati:

- il numero di ombrelloni disponibili in quella fila,
- il costo per il noleggio di un ombrellone in quella fila,
- il numero di sedie a sdraio disponibili in quella fila,
- il costo per il noleggio di una sedia a sdraio in quella fila.

I campi sono separati da virgole. Il file è da considerarsi come sempre corretto.

#### Esempio file '`stabilimento.txt`'

    4, 30, 6, 15
    4, 22, 8, 12
    5, 16, 8, 8
    6, 12, 12, 8

Il programma legge le informazioni sugli ingressi e sulle uscite dei clienti 
dal file "`ingressi-uscite.txt`". Quando un cliente entra nello stabilimento, 
il file riporta una riga con le seguenti informazioni:

    nome (univoco) del cliente, numero di ombrelloni richiesti, numero di sedie a sdraio richieste, budget che è disposto a spendere.

I campi sono separati da virgole. Il programma deve **indicare** in quale fila può andare
il cliente, controllando la disponibilità di ombrelloni e sedie a sdraio e 
cercando di **massimizzare** il costo di prenotazione (ossia, scegliendo la fila 
disponibile più costosa che rientri nel budget del cliente). Il programma **stampa** 
in output la fila assegnata al cliente (**aggiornandone** la disponibilità), oppure 
**segnala l'impossibilità di soddisfare la richiesta**.

Quando un cliente <u>**esce**</u> dallo stabilimento, il file riporta una riga con **solo**
il nome del cliente. Si <u>garantisce</u> che ogni cliente che esce sia precedentemente entrato.
Il programma deve **segnalare** in output l'uscita del cliente e **aggiornare la disponibilità**
della fila in cui si trovava.

#### Esempio file '`ingressi-uscite.txt`'

    Jerry, 2, 3, 100
    Alba, 2, 4, 90
    Teo, 3, 6, 110
    Mauro, 1, 2, 30
    Franco, 3, 4, 75
    Alba
    Eva, 2, 3, 130
    Pier Maria, 2, 5, 100
    Nathalie, 3, 4, 160
    Mauro
    Jerry
    Pier Maria
    Teo
    Eva

Al termine della lettura del file, il programma deve stampare l'incasso giornaliero.

#### Esempio di esecuzione

    Il cliente Jerry è in fila 2
    Il cliente Alba è in fila 3
    Il cliente Teo è in fila 4
    Il cliente Mauro è in fila 4
    Il cliente Franco non ha trovato posto
    Il cliente Alba è uscito
    Il cliente Eva è in fila 1
    Il cliente Pier Maria è in fila 3
    Il cliente Nathalie non ha trovato posto
    Il cliente Mauro è uscito
    Il cliente Jerry è uscito
    Il cliente Pier Maria è uscito
    Il cliente Teo è uscito
    Il cliente Eva è uscito
    L'incasso della giornata è 433
