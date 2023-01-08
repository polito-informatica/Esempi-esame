# Soluzione proposta al Tema d'Esame "Bowling"

from operator import itemgetter

FILENAME = 'bowling.txt'


def leggi_bowling(file_name):
    classifica = []
    bowling_file = open(file_name, 'r')
    for line in bowling_file:
        campi = line.rstrip().split(';')
        cognome = campi[0]
        nome = campi[1]
        punti = campi[2:]
        for i in range(0, len(punti)):
            punti[i] = int(punti[i])
        classifica.append({'cognome': cognome, 'nome': nome, 'punti': punti})
    return classifica


def calcola_totali(classifica):
    for atleta in classifica:
        atleta['totale'] = sum(atleta['punti'])

        num_0 = 0
        num_10 = 0
        for pt in atleta['punti']:
            if pt == 0:
                num_0 = num_0 + 1
            if pt == 10:
                num_10 = num_10 + 1
        atleta['num_0'] = num_0
        atleta['num_10'] = num_10


def main():
    classifica = leggi_bowling(FILENAME)
    calcola_totali(classifica)
    classifica.sort(key=itemgetter('totale'), reverse=True)

    for atleta in classifica:
        print(f"{atleta['cognome']:20} {atleta['nome']:20} {atleta['totale']}")

    max_zeri = max([a['num_0'] for a in classifica])
    # pprint(max_zeri)
    max_dieci = max([a['num_10'] for a in classifica])
    # pprint(max_dieci)

    if max_dieci != 0:
        for atleta in classifica:
            if atleta['num_10'] == max_dieci:
                print(
                    f"{atleta['cognome']:20} {atleta['nome']:20} ha abbattuto tutti i birilli {max_dieci} volte"
                )

    if max_zeri != 0:
        for atleta in classifica:
            if atleta['num_0'] == max_zeri:
                print(
                    f"{atleta['cognome']:20} {atleta['nome']:20} ha mancato tutti i birilli {max_zeri} volte"
                )


main()
