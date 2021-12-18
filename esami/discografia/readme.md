# Tema d'esame "Discografia"

Si realizzi un programma strutturato in linguaggio Python che gestisca la base dati di una casa discografica. Le
informazioni sono contenute in una serie di file. Il file principale si chiama `artisti.txt` e contiene, uno per riga,
il codice dell'artista, o della band, e il nome del file dove sono contenute tutte le canzoni. Ad esempio, il
file `artisti.txt` potrebbe contenere:

    01023;queen.txt
    02346;kiss.txt
    16750;acdc.txt

Dove:

- il primo campo è un codice numerico su 5 cifre;
- il secondo campo è una stringa che indica il nome del file che contiene i brani dell'artista/della band.
  In tale file sono memorizzati, uno per riga, l’anno di incisione e il titolo del brano (non ordinati
  per data di incisione);
- si assuma che il formato di tutti i file sia corretto.

Ad esempio, nel file `queen.txt` si può trovare:

    1980;Crazy Little Thing Called Love
    1985;It’s a kind of magic
    1978;Under pressure

Nel file `kiss.txt`  potrebbero essere memorizzate le seguenti informazioni:

    1980;Two Sides of the Coin
    1985;King Of The Mountain
    1979;I Was Made for Lovin' You

E nel file `acdc.txt` si può trovare:

    1978;Kicked In The Teeth
    1985;Playing with Girls
    1985;Shake Your Foundations
    1990;Thunderstruck

Il programma deve:

1. caricare le informazioni relative a tutti i brani di tutti gli artisti;
2. stampare in ordine cronologico crescente il titolo di tutte le canzoni di ogni anno, incise da qualunque
   artista/band, affiancate dal codice della band.

## Esempio di output usando i file descritti in precedenza:

    1978:
    Under pressure                 01023
    Kicked In The Teeth            16750
    1979:
    I Was Made for Lovin' You      02346
    1980:
    Crazy Little Thing Called Love 01023
    Two Sides of the Coin          02346
    1985:
    It's a kind of magic           01023
    King Of The Mountain           02346
    Playing with Girls             16750
    Shake Your Foundations         16750
    1990:
    Thunderstruck                  16750
