# SHE SELLS SEA SHELLS BY THE SEA SHORE

#### (Esame proposto il 20/02/2024)

Miss Shelley ha deciso di vendere la sua collezione di conchiglie marine sulla riva del mare. Ogni conchiglia ha un prezzo e ha deciso di tentare potenziali acquirenti con offerte. Ad esempio, chiunque compri due conchiglie *Abalone* riceverà una conchiglia *Drupe* in regalo.

-    Il file `prices.dat` contiene l'elenco delle conchiglie e il loro prezzo unitario. Il file è composto da più righe, il formato di ogni riga è `conchiglia: prezzo`. Il nome della conchiglia non contiene spazi. Il prezzo è in euro e può contenere centesimi di euro.
-    Il file `offers.dat` contiene le offerte. Il file è composto da più righe, il formato di ogni riga è `conchiglia1 conchiglia2 ... conchigliaN: conchiglia`. Ogni riga specifica le conchiglie che devono essere acquistate per ricevere quella in regalo. Ad esempio, se chiunque compri due conchiglie *Abalone* riceve una conchiglia *Drupe* in regalo, il file conterrà la riga `Abalone Abalone: Drupe`. Nota: né le conchiglie che hanno generato un regalo né quelle ricevute possono generare ulteriori regali.
-    Il file `cart.dat` contiene l'elenco delle conchiglie che il cliente desidera acquistare. Il file è composto da più righe, ogni riga contiene il nome di una conchiglia.

Scrivi un programma che calcola il prezzo finale del carrello, senza considerare le conchiglie che il cliente potrebbe ricevere gratuitamente. Il programma dovrebbe visualizzare una riga per ogni offerta corrispondente nel formato `Acquistando conchiglia1, conchiglia2, ..., conchigliaN; hai ricevuto conchigliaX in regalo`, e il prezzo finale nel formato: `Prezzo finale: x.yy EUR`

Ad esempio, con i file di input forniti, se il carrello contiene 6 conchiglie Nautilus, il prezzo finale è solo di 14,95 EUR (cioè 2,99 x 5), perché 1 conchiglia Nautilus è in regalo se un cliente ne acquista 4 ("paghi 4 e ne ottieni 5": `Nautilus_Shell Nautilus_Shell Nautilus_Shell Nautilus_Shell: Nautilus_Shell`).

### Esempio

#### File `prices.dat`

    Abalone: 19.99
    Melo_Melo: 4.99
    Murex: 2.5
    Nautilus_Shell: 2.99
    Oyster_Shell: .5
    Sand_Dollar: 2.5
    Small_Strombus_Gigas: 2500
    Venus_Comb: 75

#### File `offers.dat`

    Abalone Abalone: Drupe
    Conus_Gloriamaris: Cowrie
    Nautilus_Shell Nautilus_Shell Nautilus_Shell Nautilus_Shell: Nautilus_Shell
    Murex Murex Murex: Oyster_Shell

#### File `cart.dat`

    Nautilus_Shell
    Nautilus_Shell
    Nautilus_Shell
    Abalone
    Drupe
    Abalone
    Nautilus_Shell
    Nautilus_Shell
    Nautilus_Shell

#### Output del programma

    Acquistando Abalone, Abalone; hai ricevuto Drupe in regalo
    Acquistando Nautilus_Shell, Nautilus_Shell, Nautilus_Shell, Nautilus_Shell; hai ricevuto Nautilus_Shell in regalo
    Prezzo finale: 58.91 EUR
