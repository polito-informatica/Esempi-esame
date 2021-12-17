# Soluzione esercizio "Zodiaco" - tema d'esame 25/06/2021
import operator
from pprint import pprint

FILE_ZODIACO = 'zodiaco.csv'
FILE_SPORTIVI = 'sportivi.csv'


def leggi_zodiaco(nomefile):
    zodiaco = open(nomefile, 'r')
    segni = []
    for line in zodiaco:
        campi = line.rstrip().split(',')
        segni.append({'segno': campi[0], 'inizio': campi[1], 'fine': campi[2]})
    zodiaco.close()
    return segni


def leggi_sportivi(nomefile):
    filesport = open(nomefile, 'r', encoding='UTF-8')
    sportivi = []
    for line in filesport:
        campi = line.rstrip().split(',')
        sportivi.append({'nome': campi[0], 'punti': int(campi[1]), 'nazione': campi[2], 'nato': campi[3]})
    filesport.close()
    return sportivi


def trova_segno(nato, segni):
    '''
    Trova il segno zodiacale, a partire dalla data di nascita
    :param nato: data di nascita, in formato 'gg/mm'
    :param segni: elenco dei segni zodiacali
    :return: il nome del segno zodiacale
    '''

    nascita = nato.split('/')[1] + nato.split('/')[0]  # trasforma '15/03' in '0315'

    for segno in segni:
        # trasforma gg/mm/aaaa in mmgg (es: '25/05/1982' -> '0525')
        gg_inizio = segno['inizio'].split('/')[1] + segno['inizio'].split('/')[0]
        gg_fine = segno['fine'].split('/')[1] + segno['fine'].split('/')[0]

        if (nascita >= gg_inizio) and (nascita <= gg_fine):
            return segno['segno']

    # altrimenti, se non lo strovo, sarà per forza Capricorno, perché è a cavallo dell'anno
    return 'Capricorno'


def calcola_punti(sportivi, segni):
    punti = {}  # dizionario: segno -> punti, inizializzato a tutti 0
    for segno in segni:
        punti[segno['segno']] = 0

    # considero ciascuno sportivo
    for sportivo in sportivi:
        nato = sportivo['nato']
        segno = trova_segno(nato, segni)
        punti[segno] = punti[segno] + sportivo['punti']

    return punti


def calcola_classifica(punti):
    classifica = []
    for (segno, pt) in punti.items():
        classifica.append({'segno': segno, 'punti': pt})

    classifica.sort(key=operator.itemgetter('punti'), reverse=True)

    return classifica


def stampa_istogramma(classifica):
    top = classifica[0]['punti']  # il valore massimo è quello in testa alla classifica

    for voce in classifica:
        segno = voce['segno']
        punti = voce['punti']

        print(f'{segno:10s} ({punti:4d}) ', end='')
        print('*' * int(50 * punti / top))


def main():
    segni = leggi_zodiaco(FILE_ZODIACO)
    # pprint(segni)

    sportivi = leggi_sportivi(FILE_SPORTIVI)
    # pprint(sportivi)

    punti = calcola_punti(sportivi, segni)
    classifica = calcola_classifica(punti)
    stampa_istogramma(classifica)
    # pprint(classifica)


main()
