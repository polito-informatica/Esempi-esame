def leggi_mappa():
    """
    Legge una tabella di numero interi dal file. Funziona con mappe con qualsiasi numero di righe e colonne. Si assume
    che il numero di colonne sia uguale in tutte le righe.
    :return: una lista di liste di interi
    """
    f = open('mappa.txt', 'r')
    mappa = []

    for line in f:
        campi = line.rstrip().split()
        valori = [int(c) for c in campi]
        mappa.append(valori)

    return mappa


def cerca_cime(mappa):
    """
    Ricerca le coordinate dei punti massimi nella mappa

    :param mappa: la mappa di altezze
    :return: una lista di tuple (altezza, riga, colonna) dei punti massimi locali
    """
    cime = []
    for riga in range(len(mappa)):
        for col in range(len(mappa[riga])):
            adiacenti = trova_adiacenti(mappa, riga, col)
            if mappa[riga][col] > max(adiacenti):
                cime.append((mappa[riga][col], riga, col))
    return cime


def trova_adiacenti(mappa, riga, col):
    """
    Data una casella [riga][col] della mappa, restituisce una lista degli elementi adiacenti (nelle 8 direzioni)
    alla casella data.

    :param mappa: la mappa da analizzare
    :param riga: riga dell'elemento centrale
    :param col: colonna dell'elemento centrale
    :return: lista contenente i valori adiacenti. Possono esserci da 3 (per gli spigoli) a 5 (per i lati) a 8 (per
    le caselle centrali) valori in questa lista.
    """
    adiacenti = []
    for r in [riga - 1, riga, riga + 1]:
        if 0 <= r < len(mappa):
            for c in [col - 1, col, col + 1]:
                if 0 <= c < len(mappa[r]):
                    if (r != riga) or (c != col):
                        adiacenti.append(mappa[r][c])
    return adiacenti


def main():
    mappa = leggi_mappa()
    cime = cerca_cime(mappa)
    if len(cime) == 0:
        print("Non ci sono cime")
    else:
        sum_h = 0
        for cima in cime:
            print(f'{cima[0]} {cima[1]} {cima[2]}')
            sum_h += cima[0]
        print(f'Altezza media: {sum_h / len(cime)}')


main()
