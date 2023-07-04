# I Viaggi del Capitano Nemo

#### (Esame proposto il 30/06/2023)

Si vuole creare un programma Python per l'analisi dei viaggi del Capitano Nemo su
diversi luoghi subacquei e delle affinità tra i tipi di pietre preziose presenti in quei luoghi.

Occorre leggere due file, uno contenente informazioni sui viaggi e l'altro sui tipi 
di pietre preziose presenti nei luoghi visitati.

Formato del file "viaggi_nemo.txt":
- Ogni riga del file rappresenta un viaggio del Capitano Nemo su un luogo subacqueo e contiene le informazioni separate da virgole nel seguente formato:

        luogo,durata,passeggeri

Formato del file "pietre_preziose_luoghi.txt":
- Ogni riga del file rappresenta un luogo subacqueo e i tipi di pietre preziose presenti in quel luogo, con le informazioni separate da virgole nel seguente formato:

        luogo,pietra1,pietra2,pietra3,...

Risultati desiderati:
1. Durata media di tutti i viaggi del Capitano Nemo. 
2. Numero totale di passeggeri trasportati dal Capitano Nemo.
3. Per ciascun luogo subacqueo visitato dal Capitano Nemo, stampare l'elenco dei tipi di pietre preziose presenti in quel luogo.
4. Stampare i tipi di pietre preziose più comuni tra i luoghi visitati

### Esempio:

#### File `viaggi_nemo.txt`

        Atlantide,7,15
        Grande Barriera Corallina,4,8
        Mariana Trench,10,12

#### File `pietre_preziose_luoghi.txt`

        Atlantide,Pietra dell'Anima,Opale Marino
        Grande Barriera Corallina,Corallo Nero,Pietra di Luna,Perla
        Mariana Trench,Topazio,Quarzo Fumé,Perla,Pietra dell'Anima
        Pacific Rim,Corallo Nero,Pietra di Luna,Opale Marino
        Atlantide,Pietra dell'Anima,Opale Marino,Quarzo Fumé,Perla

#### Output

L'output del programma dovrà essere il seguente:

        Durata media dei viaggi: 7.0
        Numero totale di passeggeri: 35
        Tipi di pietre preziose per luogo visitato:
        - Atlantide: Pietra dell'Anima, Opale Marino, Quarzo Fumé, Perla
        - Grande Barriera Corallina: Corallo Nero, Pietra di Luna, Perla
        - Mariana Trench: Topazio, Quarzo Fumé, Perla, Pietra dell'Anima
        I tre tipi di pietre preziose più comuni: Perla, Pietra dell'Anima, Quarzo Fumé
