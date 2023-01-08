# Classifica di un torneo

#### (Esame proposto il 26/04/2022)

L’organizzatore di un torneo 3 contro 3 di pallacanestro vi ha chiesto di realizzare un programma Python che sia in
grado di elaborarne la classifica in base ai seguenti criteri:

- Ogni partita assegna i seguenti punti:
    * 3 punti alla squadra vincente e 1 punto ai perdenti,
    * 2 punti a squadra in caso di parità;
- In caso una o più squadre abbiano raggiunto lo stesso punteggio in base ai punti partita, si utilizza il quoziente (`Q`)
  tra punti fatti (`PF`) su punti subiti (`PS`) come ulteriore parametro di ordinamento (`Q = PF/PS`).

Il programma riceve in input un file chiamato `torneo.txt` che contiene le partite svolte finora durante il torneo,
distribuite riga per riga. Il formato di ciascuna riga è

    squadra1 – squadra2 : punti1 – punti2.

## Esempio

    La tocco piano - Papauto : 16 - 11
    The king - Aquilazoo : 17 - 12
    Bella Johnny - Tutti in campoo : 16 - 18
    Pro Secco - Cumba : 20 - 15
    The Street Kingz - Aquilazoo : 19 - 17
    I PUGNI NELLE MANI - Papauto : 13 - 19
    I MACULATI - La tocco piano : 19 - 13
    Zero idee innovative - The king : 11 - 18
    Slam drunk - Tutti in campoo : 17 - 18
    Pro Secco - Bella Johnny : 19 - 19
    The Street Kingz - Cumba : 12 - 15
    I PUGNI NELLE MANI - La tocco piano : 20 - 15
    I MACULATI - The king : 12 - 18
    Zero idee innovative - La tocco piano : 20 - 19
    Slam drunk - Papauto : 11 - 14
    Bella Johnny - Aquilazoo : 17 - 16
    I PUGNI NELLE MANI - Cumba : 16 - 17
    I MACULATI - Tutti in campoo : 13 - 14
    Zero idee innovative - Pro Secco : 19 - 11
    Slam drunk - The Street Kingz : 12 - 13
    Zero idee innovative - Bella Johnny : 14 - 12
    Slam drunk - Cumba : 14 - 11

Il risultato dell'elaborazione deve essere mostrato in tabella come mostrato nell'esempio. La classifica deve essere
riportata in ordine di punti partita e quoziente (con massimo 3 cifre decimali) in caso di parità. La tabella deve
riportare anche:

- il numero di partite giocate
- punti fatti e subiti.

## Elaborazione Esempio

    SQUADRA              GIOCATE PUNTI       Q     PF    PS
    -------------------------------------------------------
    Zero idee innovative       4    10    1.07     64    60
    The king                   3     9    1.51     53    35
    Tutti in campoo            3     9    1.09     50    46
    Cumba                      4     8   0.935     58    62
    Papauto                    3     7     1.1     44    40
    The Street Kingz           3     7     1.0     44    44
    Bella Johnny               4     7   0.955     64    67
    Slam drunk                 4     6   0.964     54    56
    Pro Secco                  3     6   0.943     50    53
    La tocco piano             4     6     0.9     63    70
    I MACULATI                 3     5   0.978     44    45
    I PUGNI NELLE MANI         3     5   0.961     49    51
    Aquilazoo                  3     3   0.849     45    53

