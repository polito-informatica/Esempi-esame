# Analisi degli Hashtag di Tendenza su GigglyGram

#### (Esame proposto il 05-06/02/2024)

GigglyGram è un nuovo social media, e gli sviluppatori vi chiedono di scrivere un programma Python per analizzare le tendenze degli hashtag su GigglyGram. Il file `hashtags.csv` contiene dati estratti da post pubblicati. Ogni riga del file rappresenta un post, con le seguenti informazioni separate da spazi:

    DATA ORA #hashtag1 ... #hashtagN

dove gli hashtag possono essere in numero variabile (e ce n'è sempre almeno uno), e il file contiene solo ed esclusivamente i post di due giornate consecutive.

Il programma deve identificare gli hashtag in tendenza, i.e. che hanno guadagnato popolarità significativa nelle ultime 24 ore. Si considera che un hashtag abbia guadagnato popolarità se la sua frequenza di menzione è aumentata di **almeno il 50%** rispetto al giorno precedente.

Il programma deve visualizzare in uscita un elenco (in ordine di incremento decrescente) dei tag in tendenza e del corrispondente incremento di frequenza (come numero intero).

## File hashtags.csv:

    2023-06-01 08:30 #tech #innovation #social
    2023-06-01 09:15 #health
    2023-06-01 10:00 #environment #sustainability #green
    2023-06-01 11:45 #tech #innovation
    2023-06-01 12:30 #health #wellness #fitness
    2023-06-01 14:00 #environment
    2023-06-01 15:30 #tech #innovation #AI
    2023-06-01 16:45 #wellness
    2023-06-01 18:00 #environment #sustainability
    2023-06-02 09:00 #tech #innovation
    2023-06-02 10:15 #tech #robotics
    2023-06-02 11:30 #health #wellness
    2023-06-02 12:45 #tech #AI #innovation
    2023-06-02 14:00 #environment #climatechange
    2023-06-02 15:15 #tech #innovation
    2023-06-02 16:30 #health #wellness #mentalhealth
    2023-06-02 17:45 #environment #sustainability #eco
    2023-06-02 19:00 #tech #innovation #futurism
    2023-06-02 20:15 #health #wellness #lifestyle

## Stampa in output:

    Hashtag in tendenza:
    #tech con un incremento del 67%
    #health con un incremento del 50%
    #wellness con un incremento del 50%
