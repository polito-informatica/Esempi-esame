# Controllo compiti copiati

Si scriva un programma per individuare i casi sospetti di compiti copiati fra studenti. Il compito è composto da un
certo numero di domande a scelta multipla. Per ogni domanda, ci sono quattro risposte alternative, indicate con 'A', '
B', 'C', 'D'. Lo studente sceglie al più una sola risposta; può evitare di dare la risposta se non la conosce (ossia,
non seleziona nessuna alternativa). Il file "`risposte.txt`" contiene l'elenco delle risposte date dagli studenti. Ogni
riga è costituita dal nome dello studente e dall'elenco delle risposte; ciascun campo è separato da spazi. Si supponga
che il nome dello studente sia costituito da una sola parola e che non ci siano studenti con lo stesso nome. Il numero
di risposte non è noto a priori, ma è uguale per tutti gli studenti (ogni riga contiene lo stesso numero di risposte).
Una **risposta non data** è indicata con '-'.

### Esempio file `risposte.txt`

    Emma C C C - C D B - C D
    Gabriele - B A C A A B D D -
    Tommaso A - D A A B - - D -
    Riccardo - A B D A D C C - A
    Edoardo - B A - A A B D D -
    Sofia - D B B A B C D A A
    Ginevra C A A B B D A - B C
    Vittoria C C D - A C C D B D
    Beatrice C C C B C D B - C D
    Leonardo B C B A B A D - A B
    Giorgia - A - C - D - D D A
    Greta C C C B C D B - C D
    Francesco A A - D C A A D D B
    Lorenzo - A B D - D C C - A
    Aurora D C B A C A A B - D
    Alessandro C B B - A A C C C D
    Andrea A B C A D D - - A B
    Giulia A B D D A B A - D A
    Mattia C B B - A A C C C D

Durante il compito, gli studenti sono stati collocati in file sufficientemente lontane una dall'altra. Pertanto, si
ritiene che uno studente possa aver copiato solamente dal compagno alla sua sinistra oppure da quello alla sua destra.
Ciascuna riga nel file "`posizioni.txt`" elenca una fila di studenti. Il numero di studenti in ogni fila non è noto a
priori e può variare fra le file.

### Esempio di file `posizioni.txt`

    Sofia Leonardo Alessandro Mattia
    Edoardo Gabriele Aurora
    Vittoria Tommaso Giulia Ginevra Andrea
    Giorgia Francesco Riccardo Lorenzo
    Beatrice Emma Greta

Per ogni studente nel file `posizioni.txt`, il programma deve controllare il corrispondente compito con quello degli
studenti immediatamente a sinistra e a destra. Si noti che se uno studente è all'inizio della fila, il controllo va
effettuato solo con lo studente a destra; se uno studente è all'altra estremità della fila, il controllo deve essere
solo con lo studente a sinistra. Il programma distingue **tre casi** mutuamente esclusivi:

1. le risposte di due studenti vicini sono **esattamente uguali**: sia le risposte date (indicate con 'A', 'B', 'C', '
   D') sia le risposte non date (indicate con '-') sono le stesse. In questo caso non è possibile stabilire chi abbia
   copiato, e il programma stampa il messaggio "Le risposte di studente1 e studente2 sono le stesse" (studente1 e
   studente2 devono essere sostituiti con i nomi reali degli studenti).
2. le risposte date da studente1 (indicate con 'A', 'B', 'C', 'D') sono **identiche** alle risposte di studente2, ma
   studente2 **ha dato almeno una risposta in più** (ovvero, almeno un caso in cui la corrispondente risposta di
   studente1 è '-'). In questo caso si sospetta che studente1 abbia copiato da studente2 e il programma stampa il
   messaggio "studente1 può aver copiato da studente2".
3. le risposte date da studente1 hanno almeno **una differenza** rispetto alle risposte data da studente2 (ovvero, ci
   sono domande a cui entrambi gli studenti hanno risposto e le loro risposte sono diverse). In questo caso **non si
   sospetta copiatura** e il programma non stampa nulla.

Esempio di esecuzione

    Le risposte di Alessandro e Mattia sono le stesse
    Edoardo può aver copiato da Gabriele
    Lorenzo può aver copiato da Riccardo
    Emma può aver copiato da Beatrice
    Emma può aver copiato da Greta


