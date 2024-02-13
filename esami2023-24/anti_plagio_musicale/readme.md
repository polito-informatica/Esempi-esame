# Anti Plagio Musicale

#### (Esame proposto il 05-06/02/2024)


La Polizia Musicale vuole eradicare il fenomeno del plagio dei motivi musicali presenti in diverse canzoni. A tal fine, decreta che un brano musicale sia illegale se esso è identico o troppo simile ad un brano precedente.

Ciascun brano musicale è rappresentato da una sequenza di note (si assuma che siano tutte della stessa durata), e ciascuna nota è rappresentata da un numero intero compreso tra 0 e 127 (secondo il codice MIDI, in cui ciascun intero rappresenta un semitono, ed il "Do" centrale ha valore 60). Ad esempio, la scala principale DO-RE-MI-FA-SOL-LA-SI-DO sarà rappresentata dai valori 60, 62, 64, 65, 67, 69, 71, 72.

I brani musicali da controllare sono rappresentati in un file di testo (denominato `brani.txt`), che contiene un brano per riga. I brani sono elencati in ordine di pubblicazione. Ciascuna riga è rappresentata nel formato:

`Nome Brano: 60 60 60 60 60 60 60 60 60`

ossia il nome del brano, seguito dal simbolo `:`, seguito dalle note componenti il brano stesso, separate da uno spazio, tutte sulla stessa riga.

Si realizzi un programma Python che, leggendo il file specificato, confronti ciascun brano con tutti quelli **ad esso precedenti**, ed identifichi se si verifica una delle seguenti condizioni:

1. PLAGIO: il brano in oggetto è identico ad un brano precedente
2. COPIATURA: il brano in oggetto contiene almeno 4 note consecutive identiche a quelle di un brano precedente
3. SOSPETTO: il brano in oggetto contiene almeno 4 note consecutive "trasposte" rispetto a quelle di un brano precedente. Si intendono "trasposte" una serie di note che siano state spostate verso l'alto o verso il basso di un numero fisso di semintoni. Ad esempio 60 61 60 62 è una sequenza trasposta di 83 84 83 85 (qui la differenza è sempre 23).

Il programma stampi, per ciascun brano considerato, se esso sia PLAGIO, COPIATURA o SOSPETTO, e rispetto a quali brani precedenti (è possibile che un brano contenga elementi di plagio/copiatura/sospetto da più di un brano).

Si assuma che il file esista ed abbia il formato corretto.

## Esempio

Dato il seguente file `brani.txt`:

    Scala Ascendente: 60 62 64 65 67 69 71 72 60 62 64 65 67 69 71 72
    Noia in Do: 60 60 60 60 60 60 60 60 60
    Scala Discendente: 72 71 69 67 65 64 62 60 72 71 69 67 65 64 62 60
    Ancora Noia in Do: 60 60 60 60 60 60 60 60 60
    Sali e Scendi: 60 62 64 65 67 69 71 72 71 69 67 65 64 62 60
    Alternati Do e Re: 60 60 60 60 60 62 62 62 62 62
    Noia in La: 69 69 69 69 69 69 69 69 69 69 69
    Scala Superiore Ascendente: 72 74 76 77 79 81 83 84
    Di Nuovo Scala Ascendente: 60 62 64 65 67 69 71 72 60 62 64 65 67 69 71 72

il programma produrrà il seguente **output**:

    Ancora Noia in Do è un PLAGIO di Noia in Do
    Sali e Scendi è una COPIATURA di Scala Ascendente
    Sali e Scendi è una COPIATURA di Scala Discendente
    Alternati Do e Re è una COPIATURA di Noia in Do
    Alternati Do e Re è una COPIATURA di Ancora Noia in Do
    Noia in La è un SOSPETTO di Noia in Do
    Noia in La è un SOSPETTO di Ancora Noia in Do
    Noia in La è un SOSPETTO di Alternati Do e Re
    Scala Superiore Ascendente è un SOSPETTO di Scala Ascendente
    Scala Superiore Ascendente è un SOSPETTO di Sali e Scendi
    Di Nuovo Scala Ascendente è un PLAGIO di Scala Ascendente
    Di Nuovo Scala Ascendente è una COPIATURA di Sali e Scendi
    Di Nuovo Scala Ascendente è un SOSPETTO di Scala Superiore Ascendente
