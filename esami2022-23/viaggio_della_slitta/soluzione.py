# Soluzione esercizio "Viaggio della slitta"
import csv
import math

RAGGIO = 6731  # km


def leggi_province(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')
    reader = csv.DictReader(f)
    province = dict()
    for item in reader:
        item['latitudine'] = float(item['latitudine'])
        item['longitudine'] = float(item['longitudine'])
        province[item['sigla_automobilistica']] = item
    f.close()
    return province


def leggi_bambini(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')
    reader = csv.DictReader(f)
    bambini = []
    for item in reader:
        bambini.append(item)
    f.close()
    return bambini


def aggiungi_coordinate(bambini, province):
    """
    Per ciascun bambino, aggiungi le coordinate della sua posizione, considerandone la provincia di residenza
    """
    for bambino in bambini:
        provincia = bambino['provincia']
        bambino['latitudine'] = province[provincia]['latitudine']
        bambino['longitudine'] = province[provincia]['longitudine']


def bambino_piu_a_nord(bambini):
    lat_max = -90.00  # polo Sud
    bamb_max = None
    for bambino in bambini:
        if bambino['latitudine'] > lat_max:
            lat_max = bambino['latitudine']
            bamb_max = bambino
    return bamb_max


def bambino_piu_vicino(bambino_corrente, bambini):
    dist_min = 40000
    bamb_min = None
    for bambino in bambini:
        if bamb_min is None or calcola_distanza(bambino_corrente, bambino) < dist_min:
            bamb_min = bambino
            dist_min = calcola_distanza(bambino_corrente, bamb_min)
    return bamb_min, dist_min


def calcola_distanza(A, B):
    lat_A = A['latitudine'] * math.pi / 180.0
    lon_A = A['longitudine'] * math.pi / 180.0
    lat_B = B['latitudine'] * math.pi / 180.0
    lon_B = B['longitudine'] * math.pi / 180.0
    delta_lat = lat_A - lat_B
    delta_lon = lon_A - lon_B
    h = math.sin(delta_lat/2.0)**2+ math.cos(lat_A)*math.cos(lat_B)*math.sin(delta_lon/2)**2
    return 2 * RAGGIO * math.asin(math.sqrt(h))


def main():
    province = leggi_province('province.csv')
    bambini = leggi_bambini('bambini.csv')
    aggiungi_coordinate(bambini, province)

    bambino_corrente = bambino_piu_a_nord(bambini)
    print(f'Consegnato {bambino_corrente["regalo"]} a {bambino_corrente["nome"]} {bambino_corrente["cognome"]} ({bambino_corrente["provincia"]})')

    bambini.remove(bambino_corrente)

    while len(bambini) != 0:
        prossimo, distanza = bambino_piu_vicino(bambino_corrente, bambini)
        bambino_corrente = prossimo
        bambini.remove(prossimo)

        print(f'    Viaggio di {distanza} km')
        print(
            f'Consegnato {bambino_corrente["regalo"]} a {bambino_corrente["nome"]} {bambino_corrente["cognome"]} ({bambino_corrente["provincia"]})')


main()
