# Personaggi delle favole

#### (Esame proposto il 20/02/2024)

Un file chiamato `personaggi.txt` contiene una lista di nomi di personaggi, riportati uno per riga senza un ordine particolare. I nomi contengono solo caratteri alfabetici maiuscoli, senza spazi. Scrivere un programma Python che:

-    chieda all’utente di inserire da tastiera il nome di un file di testo, contenente una favola;
-    conti il numero di volte che ciascun personaggio contenuto in `personaggi.txt` viene menzionato nella favola.

Il programma deve stampare a monitor un elenco in ordine alfabetico dei nomi di questi personaggi, seguito dal suo numero di occorrenze (vedi esempio di esecuzione). Inoltre, deve produrre un messaggio che riporti il nome del personaggio più ricorrente e di quello meno ricorrente (per semplicità, si assuma che non ci siano situazioni di parità).

Si consideri che:

-    alcuni personaggi del file `personaggi.txt` potrebbero non essere presenti nella favola in questione, e quindi non devono essere riportati nell’elenco, né essere considerati nel calcolo dei più/meno ricorrenti
-    i nomi dei personaggi potrebbero comparire nella favola con caratteri minuscoli o maiuscoli, e/o con uno o più caratteri non alfabetici all’inizio e alla fine. Ad esempio:

    (Biancaneve), 
    sirenetta…
    PolliCIno:

Infine, il programma deve generare un file di testo `personaggi_altri.txt` contenente l’elenco di tutti i personaggi di `personaggi.txt` che non sono contenuti nella favola. Il formato di questo file deve essere analogo a quello di `personaggi.txt`.

NB. il programma deve gestire opportunamente le eventuali eccezioni sollevate in fase di apertura dei file.

### Esempio di Esecuzione

#### Esempio di file `personaggi.txt`

    PIERINO
    REGINA
    RE
    STREGA
    PRINCIPE
    BIANCANEVE
    HANSEL
    LUPO
    SIRENETTA
    PADRE
    MADRE
    GRETEL
    CACCIATORE
    MATRIGNA

#### Esempio di testo della favola, contenuta in `favola.txt`

    C'era una volta una famiglia povera composta da un padre, una matrigna cattiva e due bambini, Hansel e Gretel. La famiglia stava attraversando tempi difficili e la matrigna, preoccupata per la scarsità di cibo, convinse il marito ad abbandonare i bambini nel bosco. La notte dopo, Hansel udì il piano della matrigna e decise di prepararsi. Al mattino, mentre la famiglia si dirigeva nel bosco, Hansel lasciò cadere pezzi di pane lungo il sentiero, sperando di poter seguire le briciole per tornare a casa. Tuttavia, gli uccelli del bosco mangiarono le briciole, lasciando Hansel e Gretel completamente persi. Dopo giorni di vaga erranza, i due fratelli trovarono una strana casa fatta di dolci, caramelle e pane d'avorio. Affamati, iniziarono a mangiare la casa senza sapere che apparteneva a una strega malvagia. La strega uscì e catturò Hansel e Gretel. Li chiuse in una gabbia, nutrendoli per ingrassarli e poi mangiarli. Gretel, però, era astuta e trovò un modo per liberare lei e il fratello. Quando la strega chiese di controllare quanto fosse ingrassato Hansel, Gretel suggerì che la strega avesse bisogno di occhiali. Mentre la strega guardava da vicino, i fratelli la spinsero nel forno ardente. Con la strega sconfitta, Hansel e Gretel trovarono i suoi tesori nella casa e tornarono a casa dal padre. Scoprirono che la matrigna era scomparsa, e la famiglia fu felice e riunita.

Con i file di input sopra indicati, il programma produce il seguente output a video:

    GRETEL: 6 occorrenze
    HANSEL: 7 occorrenze
    MATRIGNA: 4 occorrenze
    PADRE: 2 occorrenze
    STREGA: 6 occorrenze
    Il personaggio più ricorrente è HANSEL, quello meno ricorrente è PADRE

Inoltre, il programma crea un file `personaggi_altri.txt` con il seguente contenuto:

    PIERINO
    RE
    LUPO
    SIRENETTA
    REGINA
    PRINCIPE
    BIANCANEVE
    CACCIATORE
    MADRE
