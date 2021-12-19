"""
Struttura dati: un dizionario di prodotti, la cui chiave è il codice prodotto

Per ogni prodotto, un dizionario con due campi:
- il rivenditore ufficiale
- un insieme dei rivenditori segnalata dai clienti
"""


def venditori_ufficiali(filename):
    """
    Legge l'elenco dei rivenditori ufficiali. Restituisce un dizionario, con chiave uguale al codice prodotto
    e valore pari ad un dizionario { ufficiale : codice venditore, rivenditori: set() }
    Il campo 'rivenditori' sarà utile alla funzione leggi_acquisti, per ora viene inizializzato all'insieme vuoto.

    :param filename: nome del file da leggere
    :return: il dizionario contenente i prodotti ed i rivenditori ufficiali
    """
    file = open(filename, 'r')

    venditori = {}
    for line in file:
        parti = line.strip().split()
        prodotto = parti[0]
        venditore = parti[1]

        venditori[prodotto] = {'ufficiale': venditore, 'rivenditori': set()}

    file.close()
    return venditori


def leggi_acquisti(venditori, filename):
    """
    Arricchisce il dizionario 'venditori' con l'elenco dei rivenditori effettivi, letti dal file.
    Aggiunge dei codici di rivenditori all'insieme 'rivendtitori' del prodotto. Non restisuisce nulla, poiché
    modifica direttamente 'venditori'.

    :param venditori: dizionario con prodotti e rivenditori ufficiali
    :param filename: nome del file contenente gli acquisti
    """
    file = open(filename, 'r')

    for line in file:
        parti = line.strip().split()
        prodotto = parti[0]
        venditore = parti[1]
        venditori[prodotto]['rivenditori'].add(venditore)

    file.close()


def main():
    venditori = venditori_ufficiali('prodotti.txt')
    leggi_acquisti(venditori, 'acquisti.txt')

    print('Elenco transazioni sospette')
    for prodotto in venditori:
        ufficiale = venditori[prodotto]['ufficiale']
        rivenditori = venditori[prodotto]['rivenditori']

        # i prodotti non acquistati, non vanno considerati
        # quelli che hanno dei rivenditori diversi dalla lista ufficiale
        # vanno segnalati
        if len(rivenditori) > 0 and rivenditori != {ufficiale}:
            print('Codice prodotto:', prodotto)
            print('Rivenditore ufficiale:', ufficiale)
            print('Lista rivenditori:', end=' ')
            for rivenditore in rivenditori:
                print(rivenditore, end=' ')
            print('\n')


main()
