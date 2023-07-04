# Analisi dei viaggi dell'USS Enterprise e delle affinità linguistiche

#### (Esame proposto il 30/06/2023)

L'USS Enterprise vi chiede di creare un programma Python per l'analisi dei suoi viaggi su pianeti alieni e delle
affinità linguistiche tra le specie presenti. Il programma deve leggere dati da due file, uno contenente informazioni
sui viaggi e l'altro sulle lingue parlate sui pianeti visitati.

I viaggi sono elencati nel file `viaggi_enterprise.txt`, in cui ogni riga del file rappresenta un viaggio dell'USS
Enterprise su un pianeta e contiene le informazioni separate da virgole nel seguente formato:

        destinazione,durata,passeggeri

Le informazioni sulle lingue sono elencate nel file `lingue_pianeti.txt`, ogni riga del quale rappresenta un pianeta e
le lingue parlate su di esso, con le informazioni separate da virgole nel seguente formato:

        pianeta,lingua1,lingua2,lingua3,...

Il numero di lingue parlate può essere diverso per ogni pianeta.

Il programma deve generare in output le seguenti informazioni:

        Durata media di tutti i viaggi dell'USS Enterprise.
        Numero totale di passeggeri trasportati dall'USS Enterprise.
        Per ciascun pianeta visitato dall'USS Enterprise, l'elenco delle lingue parlate su quel pianeta.
        L’elenco delle tre lingue più ricorrenti tra i pianeti visitati.

### Esempio File:

#### viaggi_enterprise.txt

        Terra,10,150
        Vulcan,7,100
        Kronos,12,200
        Andoria,9,120
        Betazed,6,80

#### lingue_pianeti.txt

        Terra,Inglese,Cinese,Spagnolo
        Vulcan,Vulcaniano,Golic Vulcan
        Kronos,Klingonese,Orioni
        Andoria,Andoriano,Klingonese,Vulcaniano
        Betazed,Betazoid,Lapis
        Romulus,Romulano,Inglese,Klingonese,Vulcaniano
        QonoS,Klingonese,Inglese
        Cardassia,Cardassiano,Inglese,Cinese

l'output del programma dovrà essere il seguente:

        Durata media dei viaggi: 8.8
        Numero totale di passeggeri: 650
        Lingue parlate su ciascun pianeta visitato:
        Terra : ['Inglese', 'Cinese', 'Spagnolo']
        Vulcan : ['Vulcaniano', 'Golic Vulcan']
        Kronos : ['Klingonese', 'Orioni']
        Andoria : ['Andoriano', 'Klingonese', 'Vulcaniano']
        Betazed : ['Betazoid', 'Lapis']
        Tre lingue più ricorrenti tra i pianeti visitati: ['Vulcaniano', 'Klingonese', 'Inglese']
