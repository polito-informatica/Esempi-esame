# Soluzione proposta tema d'esame 'discografia'
from operator import itemgetter

FILE_PRINCIPALE = 'artisti.txt'


def leggi_artisti(nome_file):
    artisti = []
    with open(nome_file, 'r', encoding='utf-8') as f:
        for line in f:
            campi = line.rstrip().split(';')
            artisti.append({
                'codice': campi[0],
                'file': campi[1]
            })
    return artisti


def leggi_brani_artista(artista):
    brani = []
    # leggi i dati dal file il cui nome è nel campo 'file' del record 'artista'
    with open(artista['file'], 'r', encoding='utf-8') as f:
        for line in f:
            campi = line.rstrip().split(';')
            brani.append({
                'codice': artista['codice'],
                'anno': int(campi[0]),
                'brano': campi[1]
            })
    return brani


def stampa_per_anni(brani):
    anno = 0

    for brano in brani:
        if brano['anno'] != anno:  # se cambia anno, stampalo
            anno = brano['anno']
            print(f'Anno {anno}:')
        print(f'{brano["brano"]:30s}{brano["codice"]}')


def main():
    artisti = leggi_artisti(FILE_PRINCIPALE)
    # print(artisti)
    brani = []
    for artista in artisti:
        brani_artista = leggi_brani_artista(artista)
        brani.extend(brani_artista)  # aggiunti tutti i brani dei vari artisti alla stessa lista

    brani.sort(key=itemgetter('anno'))

    stampa_per_anni(brani)


main()
