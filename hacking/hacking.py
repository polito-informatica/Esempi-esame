'''
Struttura dati: un dizionario di prodotti

Per ogni prodotto, un dizionario con due campi:
- il rivenditore ufficiale
- la lista di rivenditori segnalata dai clienti

Nota: il rivenditore ufficiale è una lista, in modo da poter controllare
in modo immediato se la lista dei rivenditori ufficiali è diversa dalla
lista dei rivenditori attuali (con gli operatori di uguaglianza tra liste)
'''


def venditori_ufficiali(filename):
    file = open(filename, 'r')

    venditori = {}
    for line in file:
        parti = line.strip().split()
        prodotto = parti[0]
        venditore = parti[1]

        venditori[prodotto] = {'ufficiale': [venditore], 'rivenditori': []}

    file.close()
    return venditori


def leggi_acquisti(venditori, filename):
    file = open(filename, 'r')

    for line in file:
        parti = line.strip().split()
        prodotto = parti[0]
        venditore = parti[1]
        venditori[prodotto]['rivenditori'].append(venditore)

    file.close()


def main():
    venditori = venditori_ufficiali('prodotti.txt')
    leggi_acquisti(venditori, 'acquisti.txt')

    print('Elenco transazioni sospette')
    for prodotto in venditori:
        ufficiale = venditori[prodotto]['ufficiale']
        rivenditori = venditori[prodotto]['rivenditori']

        # i prodotti non acquistati, non vanno considerati
        # quelli che hanno una lista di rivenditori diversi dalla lista ufficiale
        # vanno segnalati
        if len(rivenditori) > 0 and ufficiale != rivenditori:
            print('Codice prodotto:', prodotto)
            print('Rivenditore ufficiale:', ufficiale[0])
            print('Lista rivenditori:', end=' ')
            for rivenditore in rivenditori:
                print(rivenditore, end=' ')
            print('\n')


main()
