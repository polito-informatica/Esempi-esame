# Analisi degli Avvistamenti di UFO

#### (Esame proposto il 20/02/2024)

Si scriva un programma Python per analizzare i dati relativi agli avvistamenti di UFO. Le informazioni degli avvistamenti cono contenute nel file `ufo_sightings.csv`. Ogni riga del file rappresenta un avvistamento, con le seguenti informazioni separate da virgole:

    data - data dell'avvistamento (formato YYYY-MM-DD)
    ora - ora dell'avvistamento (formato HH:MM:SS)
    paese - paese dell'avvistamento
    forma - forma dell'UFO osservato (ad esempio, disco, sfera, luce)
    durata - durata dell'avvistamento in secondi
    descrizione - breve descrizione dell'avvistamento

Il file **non ha** una riga di intestazione con i nomi dei campi.

Il programma deve stampare su schermo le seguenti informazioni:

-    Il paese con il maggior numero di avvistamenti.
-    L'avvistamento di durata più lunga con la relativa durata e forma.

**NOTA: non saranno considerate sufficienti soluzioni che possano esclusivamente funzionare con i file di esempio allegati al compito (e.g., che possono analizzare esclusivamente i contenuti di quei file, o che usano per le operazioni valori costanti persi dal file...)**

#### File `ufo_sightings.csv`

    2023-06-01,22:30:00,Italia,disco,120,Un disco volante luminoso sopra la città
    2023-06-02,23:15:00,USA,sfera,180,Luci sferiche che si muovono rapidamente nel cielo
    2023-06-03,20:45:00,Francia,luce,600,Fasci di luce intensa che attraversano il cielo
    2023-06-04,21:30:00,USA,disco,90,Disco luminoso che segue un aereo
    2023-06-05,22:00:00,Canada,triangolo,300,Triangolo luminoso fermo nel cielo
    2023-06-06,23:00:00,Messico,sfera,150,Sfere di luce che cambiano colore
    2023-06-07,19:45:00,Germania,cilindro,240,Cilindro metallico che si muove lentamente
    2023-06-08,20:30:00,Brasile,luce,420,Luce intensa che si muove in modo irregolare
    2023-06-09,21:45:00,Giappone,disco,180,Disco che emette luci multicolori
    2023-06-10,22:30:00,Italia,sfera,200,Sfere luminose in formazione
    2023-06-11,23:15:00,USA,luce,500,Luce che si divide in più sfere più piccole
    2023-06-12,20:45:00,Russia,disco,360,Disco volante che emette suoni bassi
    2023-06-13,21:30:00,USA,triangolo,480,Triangolo che si muove a grande velocità

#### Stampa in output

    Paese con il maggior numero di avvistamenti: USA
    Avvistamento di durata più lunga: Fasci di luce intensa che attraversano il cielo (Durata: 600 secondi, Forma: luce)
