# prova QDV
from operator import itemgetter
import csv

FILE_NAME = '20201214_QDV2020_001.csv'
FILE_INDICATORE = 'indicatore.txt'


def leggi_dati(nome_file):
    try:
        file = open(FILE_NAME, 'r', encoding='utf-8')
    except OSError:
        exit('Impossibile aprire il file')

    reader = csv.DictReader(file)
    dati = []
    for record in reader:
        record['VALORE'] = float(record['VALORE'])
        dati.append(record)

    file.close()
    return dati


def trova_indicatori(dati):
    # crea un set con tutti i valori del campo INDICATORE su tutti i record della lista
    indicatori = {record['INDICATORE'] for record in dati}
    return indicatori


def calcola_classifica(dati, indicatore_scelto):
    # faccio una copia dei soli dati che mi interessano

    classifica = [record for record in dati if record['INDICATORE']==indicatore_scelto]

    # forma "lunga" senza comprehension
    # classifica = []
    # for record in dati:
    #     if record['INDICATORE'] == indicatore_scelto:
    #         classifica.append(record)

    # ordina per valore dell'indicatore
    classifica.sort(key=itemgetter('VALORE'), reverse=True)

    return classifica


def main():
    dati = leggi_dati(FILE_NAME)
    indicatori = trova_indicatori(dati)

    # Stampa il menu per scegliere gli indicatori
    print('Indicatori della qualità della vita:')
    for i, indicatore in enumerate(sorted(indicatori)):
        print(f'{i + 1:2d}. {indicatore}')

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
            print(f"{record['DENOMINAZIONE CORRENTE']:22} : {record['VALORE']:8.3f}")


main()
