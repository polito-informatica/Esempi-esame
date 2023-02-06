# Impact factor

#### (Esame proposto il 30-31/01/2023)

L'_impact factor_ è un indice numerico proposto per valutare l'influenza delle riviste scientifiche. Tiene conto del
numero di articoli pubblicati da una rivista e del numero di citazioni che questi articoli ricevono. Il file "
`journal_IF.csv`" riporta l'impact factor più recente per le riviste scientifiche nell'area di Computer Science.

### Esempio file "`journal_IF.csv`"

    journal name,ISSN,e-ISSN,category,citations,impact factor
    Journal of Computer and System Sciences,0022-0000,1090-2724,Theory & Methods,4964,1.043
    Information Processing Letters,0020-0190,1872-6119,Information Systems,3878,0.851
    ACM Transactions on Computation Theory,1942-3454,1942-3462,Theory & Methods,190,N/A
    ACM Transactions on Parallel Computing,2329-4949,2329-4957,Theory & Methods,171,N/A
    Advances in Human-Computer Interaction,1687-5893,1687-5907,Artificial Intelligence,369,N/A
    ACM Computing Surveys,0360-0300,1557-7341,Theory & Methods,14992,14.324
    Communications of the ACM,0001-0782,1557-7317,Hardware & Architecture,26575,14.065
    Requirements Engineering,0947-3602,1432-010X,Software Engineering,829,2.275
    Journal of the ACM,0004-5411,1557-735X,Software Engineering,7894,2.269
    Distributed Computing,0178-2770,1432-0452,Theory & Methods,868,1.937
    ACM Transactions on Computer Systems,0734-2071,1557-7333,Theory & Methods,1380,1.692

La prima riga del file riporta i nomi dei campi. Ogni rivista ha un titolo, ma possono esserci riviste (di editori
diversi) con lo stesso titolo, quindi le riviste sono identificate univocamente dal codice ISSN. Oltre al codice ISSN (
sempre presente), se la rivista è distribuita in formato elettronico ha anche un codice e-ISSN (opzionale). Per ogni
rivista sono indicati: la categoria (ossia la tipologia di articoli pubblicati dalla rivista), il numero di citazioni
ricevute e l'impact factor. Se l'impact factor di una rivista non è disponibile (ad esempio per le riviste più recenti)
compare la dicitura "N/A".

Il _total impact factor_ (total IF) è un indice proposto per valutare la produzione scientifica dei singoli ricercatori.
E' ottenuto sommando l'impact factor delle riviste su cui sono pubblicati i lavori del ricercatore.

Si scriva un programma che chiede all'utente il cognome di un ricercatore (ad esempio "Goldwasser"). Il programma deve
leggere il file .csv corrispondente al cognome del ricercatore (nell'esempio: "Goldwasser.csv"), segnalando all'utente
se il file non esiste. Il suddetto file contiene l'elenco delle pubblicazioni del ricercatore (la prima riga riporta i
nomi dei campi), con le seguenti informazioni:

- lista degli autori (oltre al ricercatore, altri coautori possono avere contribuito alla pubblicazione). Gli autori
  sono elencati con Cognome e Iniziale del nome e sono separati da una virgola. Data la possibile presenza della
  virgola, questo campo è sempre racchiuso da virgolette;

- titolo della pubblicazione;

- anno di pubblicazione;

- nome della rivista o nome della conferenza in cui appare la pubblicazione;

- codice ISSN (solo per le riviste: per le conferenze questo campo è vuoto)

### Esempio file "Goldwasser.csv"

    Authors,Title,Year,Source title,ISSN
    "Goldwasser S., Kalai Y.T., Rothblum G.N.",Delegating computation: Interactive proofs for muggles,2015,Journal of the ACM,0004-5411
    "Dinur I., Goldwasser S., Lin H.",The computational benefit of correlated instances,2015,ITCS 2015 - Proceedings of the 6th Innovations in Theoretical Computer Science,
    "Chandran N., Chongchitmate W., Garay J.A., Goldwasser S., Ostrovsky R., Zikas V.",The hidden graph model: Communication locality and optimal resiliency with adaptive faults,2015,ITCS 2015 - Proceedings of the 6th Innovations in Theoretical Computer Science,
    "Allender E., Goldwasser S.",Introduction to the special issue on innovations in theoretical computer science 2012 - Part II,2014,ACM Transactions on Computation Theory,1942-3454
    "Boyle E., Goldwasser S., Kalai Y.T.",Leakage-resilient coin tossing,2014,Distributed Computing,0178-2770
    "Goldreich O., Goldwasser S., Ron D.",On the possibilities and limitations of pseudodeterministic algorithms,2013,ITCS 2013 - Proceedings of the 2013 ACM Conference on Innovations in Theoretical Computer Science,
    "Allender E., Goldwasser S.",Introduction to the special issue on innovations in theoretical computer science 2012,2013,ACM Transactions on Computation Theory,1942-3454
    "Akavia A., Goldwasser S., Hazay C.",Distributed public key schemes secure against continual leakage,2012,Proceedings of the Annual ACM Symposium on Principles of Distributed Computing,
    "Goldwasser S.",ITCS 2012 - Innovations in Theoretical Computer Science Conference: Preface,2012,ITCS 2012 - Innovations in Theoretical Computer Science Conference,
    "Goldreich O., Goldwasser S.",On the limits of nonapproximability of lattice problems,2000,Journal of Computer and System Sciences,0022-0000
    "Goldwasser S., Kilian J.",Primality testing using elliptic curves,1999,Journal of the ACM,0004-5411
    "Goldreich O., Goldwasser S., Ron D.",Property Testing and Its Connection to Learning and Approximation,1998,Journal of the ACM,0004-5411
    "Bellare Mihir, Goldwasser S.",Verifiable partial key escrow,1997,Proceedings of the ACM Conference on Computer and Communications Security,
    "Goldwasser S.",Multi-party computations: past and present,1997,Proceedings of the Annual ACM Symposium on Principles of Distributed Computing,
    "Feige U., Goldwasser S., Lovasz L., Safra S., Szegedy M.",Interactive proofs and the hardness of approximating cliques,1996,Journal of the ACM,0004-5411
    "Goldreich O., Goldwasser S., Micali S.",How to construct random functions,1986,Journal of the ACM,0004-5411
    "Goldwasser S., Micali S.",Probabilistic encryption,1984,Journal of Computer and System Sciences,0022-0000

Il programma deve calcolare:

- il total IF del ricercatore. Solo le pubblicazioni a rivista (quelle con codice ISSN) devono essere considerate per il
  conteggio.

- il total IF e il numero di pubblicazioni relativo alle sole pubblicazioni in cui il ricercatore è il primo autore.

- il total IF e il numero di pubblicazioni relativo alle sole pubblicazioni in cui il ricercatore è l'ultimo autore.

**Note importanti:**

- La corrispondenza fra le riviste elencate nei due file in input deve avvenire necessariamente sulla base del codice
  ISSN (il nome della stessa rivista può essere riportato in modo diverso nei due file).

- Nel file delle pubblicazioni, ogni autore è indicato con Cognome e Iniziale del nome, ma l'utente introduce da
  tastiera solo il Cognome. La posizione dell'ultimo autore si può individuare dopo l'ultima virgola (se la virgola è
  presente, ossia se ci sono più autori).

- Se il ricercatore è l'unico autore, è considerato sia primo, sia ultimo autore.

- Se un ricercatore ha scritto più pubblicazioni su una rivista, l'impact factor di quella rivista è sommato più volte.

- Le riviste senza impact factor (ossia "N/A") non contribuiscono al calcolo del total IF.

- Il total IF deve essere stampato con 2 cifre decimali.

- Come ulteriore esempio, nel progetto di PyCharm sono disponibili due file di esempio: "Goldwasser.csv" e "Blum.csv".

### Esempi di esecuzione

    > Inserisci il nome del ricercatore: Goldwasser
    Total IF di Goldwasser: 15.37
    Total IF come primo autore: 5.58 (3 pubblicazioni)
    Total IF come ultimo autore: 1.04 (1 pubblicazione)
    
    > Inserisci il nome del ricercatore: Blum
    Total IF di Blum: 30.89
    Total IF come primo autore: 12.29 (8 pubblicazioni)
    Total IF come ultimo autore: 10.77 (5 pubblicazioni)
    
    > Inserisci il nome del ricercatore: Rivest
    File non trovato per l'autore Rivest
