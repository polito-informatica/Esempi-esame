# prova QDV
from operator import itemgetter

FILE_NAME = '20201214_QDV2020_001.csv'
FILE_INDICATORE = 'indicatore.txt'


def leggi_dati(nome_file):
    try:
        file = open(FILE_NAME, 'r', encoding='utf-8')
    except IOError:
        exit('Impossibile aprire il file')

    dati = []

    file.readline()  # ignora la linea di intestazione

    for line in file:
        campi = line.rstrip().split(',')
        provincia = campi[3].strip('"')
        indicatore = campi[5].strip('"')
        valore = float(campi[4])

        record = {
            'provincia': provincia,
            'indicatore': indicatore,
            'valore': valore
        }

        dati.append(record)

    file.close()
    return dati


def trova_indicatori(dati):
    indicatori = []
    for record in dati:
        if record['indicatore'] not in indicatori:
            indicatori.append(record['indicatore'])
    indicatori.sort()
    return indicatori


def calcola_classifica(dati, indicatore_scelto):
    # faccio una copia dei dati che mi interessano
    classifica = []
    for record in dati:
        if record['indicatore'] == indicatore_scelto:
            classifica.append(record)

    # ordina per indicatore
    classifica.sort(key=itemgetter('valore'), reverse=True)

    return classifica

def main():
    dati = leggi_dati(FILE_NAME)
    indicatori = trova_indicatori(dati)

    # Stampa il menu per scegliere gli indicatori
    print('Indicatori della qualità della vita:')
    for i in range(len(indicatori)):
        print(f'{i + 1:2d}. {indicatori[i]}')

    # Acquisisci l'indicatore scelto dal file
    try:
        ind_file = open(FILE_INDICATORE, 'r')
        indicatore = ind_file.readline().rstrip()
        ind_file.close()
    except IOError:
        print('Impossibile leggere l\'indicatore dal file')
        exit()

    if indicatore not in indicatori:
        print(f"L'indicatore {indicatore} non è definito nel file")
    else:
        classifica = calcola_classifica(dati, indicatore)
        print(f"Classifica secondo l'indicatore '{indicatore}': ")
        for record in classifica:
            print(f"{record['provincia']:22} : {record['valore']}")



main()
