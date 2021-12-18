# Soluzione proposta esercizio d'esame "Statistiche Comuni"
from typing import IO

FILE_COMUNI = 'elenco-comuni-italiani.csv'
FILE_REGIONI_SCELTE = 'regioni.txt'


def leggi_file():
    """
    Legge gli interi dati sui comuni, e li salva in una lista di record.
    Ciascun elemento della lista fa riferimento ad un comune, e contiene un dizionario con due chiavi:
    'comune' e 'regione' (gli altri dati non sono rilevanti per questo esercizio)

    :return: L'elenco di tutti i comuni e la relativa regione di appartenenza
    """
    try:
        file = open(FILE_COMUNI)
    except IOError as error:
        print('Impossibile aprire il file:\n' + str(error))
        exit()

    file.readline() # salta la prima riga

    lista = []
    for linea in file:
        try:
            campi = linea.split(';')
            comune = campi[6]
            regione = campi[10]
            # print(comune, regione)
            record = {'comune': comune, 'regione': regione}
            lista.append(record)
        except IndexError:
            print('Riga con numero di campi insufficiente (viene ignorata):\n' + linea)

    file.close()
    return lista


def regione_valida(elenco, regione):
    """
    Verifica se il nome della regione è valido (è presente nella lista?)

    :param elenco: Elenco completo dei dati dei comuni
    :param regione: Nome della regione da controllare
    :return: Booleano che indica se il nome della regione esiste
    """
    valida = False
    for record in elenco:
        if record['regione'] == regione:
            valida = True
            break
    return valida


def comuni_della_regione(elenco, regione):
    """
    Estrae l'elenco di tutti i comuni di una determinata regione

    :param elenco: Elenco completo dei dati dei comuni
    :param regione: Nome della regione di cui estrarre i comuni
    :return: Lista dei nomi dei comuni della regione indicata, restituita in ordine alfabetico
    """
    comuni = []
    for record in elenco:
        if record['regione'] == regione:
            comuni.append(record['comune'])
    comuni.sort()  # così li ho già in ordine alfabetico
    return comuni


def più_corto(nomi):
    """
    Data una lista di stringhe, restituisce la più corta presente nella lista. Qualora ve ne sia più di una
    restituisce la prima.

    :param nomi: Lista di stringhe
    :return: Stringa più breve, o '' se la lista era vuota
    """
    lun = 1000
    corto = ''
    for nome in nomi:
        if len(nome) < lun:
            lun = len(nome)
            corto = nome
    return corto


def più_lungo(nomi):
    """
    Data una lista di stringhe, restituisce la più lunga presente nella lista. Qualora ve ne sia più di una
    restituisce la prima.

    :param nomi: Lista di stringhe
    :return: Stringa più lunga, o '' se la lista era vuota
    """
    lun = 0
    lungo = ''
    for nome in nomi:
        if len(nome) > lun:
            lun = len(nome)
            lungo = nome
    return lungo


def main():
    elenco = leggi_file()

    try:
        regioni_scelte = open(FILE_REGIONI_SCELTE, 'r')
    except IOError as ex:
        print(f"Impossibile aprire il file {FILE_REGIONI_SCELTE}: {ex}")
        exit()

    for riga in regioni_scelte:
        regione = riga.rstrip()
        if regione_valida(elenco, regione):
            comuni = comuni_della_regione(elenco, regione)
            print(f'*** REGIONE {regione} ***')
            print(f'Nella regione {regione} ci sono {len(comuni)} comuni')
            print(f'Il nome più breve è {più_corto(comuni)} e quello più lungo è {più_lungo(comuni)}')
        else:
            print(f'Regione {regione} non valida')

    regioni_scelte.close()


main()
