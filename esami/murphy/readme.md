# Testo d'esame "Leggi di Murphy"

Si consideri un file di testo, denominato `leggi_di_Murphy.txt`, che contiene alcune delle massime derivate dalla famosa *legge di Murphy*.

Nel file di testo, ciascuna massima è composta da _due o più_ righe di testo: sulla prima riga c'è il **titolo** della massima, sulle successive c'è l'**enunciato**. Le diverse massime sono separate tra di loro da una riga vuota.

Ad esempio:

    Principio degli elementi persi
    Il raggio di caduta dal banco di lavoro di piccoli elementi varia inversamente alle loro dimensioni e 
    direttamente alla loro importanza per il completamento del lavoro intrapreso.
    
    Legge di Perussel
    Non c'è lavoro tanto semplice che non possa essere fatto male.
    
    Regola di Ray sulla precisione
    Misura con un micrometro.
    Segna con un gessetto.
    Taglia con un'ascia.
    
    Legge dei semafori
    Se è verde non hai fretta.
    
    Legge di Pudder
    Chi ben comincia, finisce male. Chi comincia male, finisce peggio.
    
    Seconda Legge di Horowitz
    In qualunque momento tu accenda la radio, sentirai le ultime note della tua canzone preferita.
    
    Legge di Vile sul valore
    Più un oggetto costa, più lontano bisognerà spedirlo per farlo riparare.


Un secondo file di testo, denominato `argomenti.txt` contiene una serie di parole (una per riga, prive di spazi o punteggiatura).

Ad esempio:

    male
    fretta
    lavoro


Scrivere un programma Python per identificare le leggi di Murphy che parlano di determinati argomenti. 

Il programma deve identificare tutte le massime in cui almeno una di tali parole compaia
**nell'enunciato** (non è importante se compare o meno nel titolo).
La parola ricercata deve comparire come parola "completa" nel testo, non è ammesso avere corrispondenze parziali.
Ad esempio, se la parola fosse "con", non deve essere selezionata una massima contenente "conti". 
Il confronto deve essere fatto ignorando la differenza tra maiuscole e minuscole, e rimuovendo i caratteri di punteggiatura.

Se una massima contenesse più di una parola tra quelle da ricercare, deve comunque essere stampata una volta sola.
Per le massime corrispondenti al criterio, si stampi il titolo (completo) e l'inizio (primi 50 caratteri)
dell'enunciato. Se l'enunciato fosse più lungo di 50 caratteri, si indichi con '...' il fatto che è stato troncato.

Nel caso di file con il contenuto indicato negli esempi, il programma dovrà  produrre il seguente output:

    Principio degli elementi persi - Il raggio di caduta dal banco di lavoro di piccoli...
    Legge di Perussel - Non c'è lavoro tanto semplice che non possa essere...
    Legge dei semafori - Se è verde non hai fretta.
    Legge di Pudder - Chi ben comincia, finisce male. Chi comincia male,...


(Fonte: http://www.fenice.info/Wisdom/Aforismi/index.asp)
