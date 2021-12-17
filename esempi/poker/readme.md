# Esempio d'esame "Poker"

Si consideri un mazzo di carte da poker (contenente 32 carte: valore 7, 8, 9, 10, J, Q, K, A nei quattro semi ♥, ♦, ♣,
♠, rappresentati dalle lettere C, Q, F, P).

Il programma deve generare tutte le carte del mazzo, memorizzandole in opportuna struttura dati, ed eseguire le seguenti
operazioni:

1. mescolare il mazzo, ottenendo le 32 carte in un ordine casuale
2. salvare sul file *mazzo.txt* il contenuto del mazzo mescolato. Ciascuna carta deve essere salvata su una riga
   separata, in due campi separati da spazio: il primo campo è il valore, ed il secondo è il seme (esempio: '10 C', per
   il 10 di cuori).
3. estrarre le carte dal mazzo a gruppi di 5 (ignorando il resto). Per ciascun gruppo di 5, occorre stampare a video:
    - le 5 carte estratte (in un formato a piacere)
    - la combinazione del Poker corrispondente alle 5 carte estratte.

## Nota

Le combinazioni da riconoscere sono le seguenti (
fonte: [Wikipedia "Poker tradizionale"](https://it.wikipedia.org/wiki/Poker_tradizionale)):

| Combinazione | Definizione | Esempio |
|--------------|-------------|---------|
| Scala reale  | Scala con cinque carte dello stesso seme | K♠ Q♠ J♠ 10♠ 9♠  |
| Poker        | Quattro carte dello stesso valore. | Q♥ Q♦ Q♣ Q♠ 7♣ |
| Colore       | Cinque carte dello stesso seme, non in scala | A♦ K♦ J♦ 9♦ 8♦ |
| Full         | Combinazione di un tris e una coppia | J♥ J♦ J♣ 6♠ 6♣ |
| Scala        | Sequenza di carte in ordine di valore (Es: 7,8,9,10,J oppure 10,J,Q,K,A) e appartenenti a diversi semi | K♣ Q♥ J♠ 10♦ 9♥ |
| Tris         | Tre carte dello stesso valore. | A♦ J♥ J♣ J♠ 8♠ |
| Doppia coppia | Due coppie | Q♣ Q♠ 9♦ 9♣ 8♥  |
| Coppia       | Due carte dello stesso valore | K♣ J♥ 10♠ 10♥ 7♦ |

## Avvertenza

Verificare tutte le tipologie di combinazioni non è particolarmente arduo, ma farle tutte richiede un tempo decisamente
più lungo di quello disponibile all'esame. In un vero testo di esame sarebbero richieste solo alcune combinazioni.

## Esempio

      KQ 8F KF QC 9F  Coppia
      AC JF AP KP KC  Doppia Coppia
      QQ 9Q 8Q 7C 7P  Coppia
      QF 7Q AQ 10P 10Q  Coppia
      AF 7F 10C 8C 10F  Coppia
      JQ 9C 9P JC JP  Full

oppure...

      K♦ K♠ K♥ 8♣ 10♦  Tris
      9♣ A♦ Q♣ J♥ 8♠  Niente...
      Q♦ A♠ Q♥ 7♠ Q♠  Tris
      J♣ A♥ J♠ 8♥ 9♦  Coppia
      10♥ 7♣ 7♦ 10♣ J♦  Doppia Coppia
      8♦ 7♥ 9♠ 9♥ 10♠  Coppia
