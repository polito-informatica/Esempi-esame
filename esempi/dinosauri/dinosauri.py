# Soluzione proposta esame "Dinosauri"

FILE_NAME = 'mazzo.txt'
NUM_CARTE = 30

# punteggi dei diversi dinosauri. Uso un dizionario come mappa "colore"-->punteggio
PUNTEGGI = {
    'Rosso': 5,
    'Giallo': 3,
    'Verde': 1
}


def leggi_mazzo(file_name):
    try:
        infile = open(file_name, 'r')
    except IOError:
        exit('Impossibile aprire il file')

    mazzo = []
    for dino in infile:
        dino = dino.strip()
        if dino not in PUNTEGGI:
            print(f'Carta {dino} non valida (viene ignorata)')
        else:
            mazzo.append(dino)
    infile.close()

    if len(mazzo) != NUM_CARTE:
        print(f'Il numero di carte {len(mazzo)} non corrisponde a {NUM_CARTE}')
        return []

    return mazzo


def distribuisci_carte(mazzo):
    carte1 = []
    carte2 = []
    for i in range(0, len(mazzo), 2):
        carte1.append(mazzo[i])
        carte2.append(mazzo[i + 1])
    return (carte1, carte2)


def partita(carte1, carte2):
    punti1 = punti2 = 0
    tavolo = 0
    while len(carte1) > 0 and len(carte2) > 0:
        c1 = carte1.pop(0)
        c2 = carte2.pop(0)
        print(f'Giocatore 1: {c1} -- Giocatore 2: {c2}')
        tavolo = tavolo + PUNTEGGI[c1] + PUNTEGGI[c2]
        if c1 == c2:
            print('Pareggio')
        elif PUNTEGGI[c1] > PUNTEGGI[c2]:
            print('Vince Giocatore 1')
            punti1 = punti1 + tavolo
            tavolo = 0
        else:
            print('Vince Giocatore 2')
            punti2 = punti2 + tavolo
            tavolo = 0
        print(f'Punteggio: {punti1} -- {punti2}')
    return (punti1, punti2)


def main():
    mazzo = leggi_mazzo(FILE_NAME)
    (carte1, carte2) = distribuisci_carte(mazzo)
    (punti1, punti2) = partita(carte1, carte2)
    if punti1 > punti2:
        print(f'Ha vinto il Giocatore 1 con {punti1} punti')
    elif punti2 > punti1:
        print(f'Ha vinto il Giocatore 2 con {punti2} punti')
    else:
        print(f'I giocatori hanno pareggiato con {punti1} punti ciascuno')


main()
