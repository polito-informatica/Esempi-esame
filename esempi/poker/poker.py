# Esercizio d'esame "Poker"

from random import shuffle, randint

VALORI = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SEMI = ['C', 'Q', 'F', 'P']
SEMI_UNICODE = {'C': '♥', 'Q': '♦', 'F': '♣', 'P': '♠'}

FILE_NAME = 'mazzo.txt'


def genera_mazzo():
    """
    Crea un mazzo con le 32 carte.

    :return: una lista di 32 record del tipo { 'valore': '7', 'seme': 'P' }
    """
    mazzo = []
    for valore in VALORI:
        for seme in SEMI:
            carta = {
                'valore': valore,
                'seme': seme
            }
            mazzo.append(carta)

    # oppure, usando una list comprehension annidata
    # mazzo = [{'valore': valore, 'seme': seme} for valore in VALORI for seme in SEMI]
    return mazzo


def salva_mazzo(file_name, mazzo):
    """
    Salva su file il contenuto del mazzo specificato

    :param file_name: nome del file da salvare
    :param mazzo: lista di record contenente le carte del mazzo
    """
    try:
        file = open(file_name, 'w')
    except OSError:
        print('Impossibile creare il file')
        return

    for carta in mazzo:
        file.write(f'{carta["valore"]} {carta["seme"]}\n')

    file.close()


def mescola_mazzo(mazzo):
    """
    Dato un mazzo, rimescola in modo casuale il suo contenuto.

    :param mazzo: mazzo da mescolare. Viene modificato direttamente.
    """
    shuffle(mazzo)  # la funzione random.shuffle fa già tutto da sola

    # altrimenti si può realizzare "a mano", come indicato nel blocco commentato di seguito:

    # # sposto tutte le carte in un altro mazzo
    # vecchio_mazzo = list(mazzo)
    # mazzo.clear()  # azzero 'mazzo' e dovrò modificarlo per non perdere l'alias
    #
    # while len(vecchio_mazzo) > 0:
    #     # scelgo una carta a caso
    #     pos = randint(0, len(vecchio_mazzo) - 1)
    #     # la sposto dall'altro mazzo a quello principale
    #     mazzo.append(vecchio_mazzo[pos])
    #     vecchio_mazzo.pop(pos)


def estrai_5_carte(mazzo):
    """
    Estrae le prossime 5 carte dal mazzo (se ve ne sono almeno 5) e le cancella dal mazzo stesso. Se sono meno di 5,
    restituisce una lista vuota.

    :param mazzo: mazzo da cui estrarre le prime 5 carte, verrà modificato eliminando le carte restituite
    :return: lista di 5 carte (le prime 5 del mazzo)
    """
    if len(mazzo) < 5:
        return []

    mano = mazzo[0:5]
    del mazzo[0:5]  # oppure faccio 5 volte mazzo.pop(0) // oppure faccio mazzo[0:5]=[]
    return mano


def trova_combinazione(mano):
    """
    Data una mano composta da 5 carte, determina quale combinazione "vincente" del Poker sia il valore della mano

    :param mano: lista di 5 carte
    :return: la descrizione (stringa) del punto ottenuto, oppure la stringa "Niente..." se non si hanno punti.
    """

    # serie di controlli, in ordine decrescente di valore
    if is_colore(mano) and is_scala(mano):
        return "Scala Reale"
    elif ha_ripetuti(mano, 4):
        return "Poker"
    elif is_colore(mano):
        return "Colore"
    elif ha_ripetuti(mano, 3) and ha_ripetuti(mano, 2):
        return "Full"
    elif is_scala(mano):
        return "Scala"
    elif ha_ripetuti(mano, 3):
        return "Tris"
    elif is_doppia_coppia(mano):
        return "Doppia Coppia"
    elif ha_ripetuti(mano, 2):
        return "Coppia"
    else:
        return "Niente..."


def main():
    mazzo = genera_mazzo()
    mescola_mazzo(mazzo)

    salva_mazzo(FILE_NAME, mazzo)

    mano = estrai_5_carte(mazzo)
    while len(mano) == 5:
        combo = trova_combinazione(mano)
        print(format_mano(mano), combo)
        mano = estrai_5_carte(mazzo)


# Seguono tutte le funzioni ausiliarie utilizzate da trova_combinazione

def is_colore(mano):
    """
    Le 5 carte hanno tutte lo stesso seme?
    """
    for i in range(1, 5):
        if mano[i]['seme'] != mano[0]['seme']:
            return False
    return True


def is_scala(mano):
    """
    I valori delLe 5 carte formano una sequenza crescente?
    """
    valori = set()
    for carta in mano:
        valori.add(carta['valore'])
    # scala -> 5 carte diverse -> il set() avrà 5 elementi (condizione necessaria non sufficiente)
    if len(valori) != 5:
        return False

    if (valori == {'7', '8', '9', '10', 'J'}
            or valori == {'8', '9', '10', 'J', 'Q'}
            or valori == {'9', '10', 'J', 'Q', 'K'}
            or valori == {'10', 'J', 'Q', 'K', 'A'}):
        return True
    # NOTA:  anziché elencare le 4 scale possibili, si potrebbe iterare su degli slice di VALORI
    # così: valori == set( VALORI[i:i+5] ) , al variare di i

    return False


def ha_ripetuti(mano, num):
    """
    determina se ci sono dei valori ripetuti ESATTAMENTE 'num' volte
    """

    valori = []
    for carta in mano:
        valori.append(carta['valore'])

    valori.sort()  # così ho gli elementi uguali tutti di seguito

    while len(valori) > 0:
        # cerco quante volte è ripetuto il primo elemento
        conta = valori.count(valori[0])
        # oppure, se non ricordo il metodo .count():
        # conta = 1
        # while conta < len(valori) and valori[conta] == valori[0]:
        #     conta = conta + 1
        if conta == num:
            return True
        del valori[0:conta]  # li ho già considerati, li posso cancellare (NB sono consecutivi!)

    return False


def is_doppia_coppia(mano):
    """
    Due coppie?
    """

    valori = []
    for carta in mano:
        valori.append(carta['valore'])

    set_valori = set(valori)

    if len(set_valori) != 3:
        return False

    # ho 3 numeri distinti, possono essere solo A A A B C (tris) oppure A A B B C (doppia coppia)
    # verifico se uno degli elementi compare 3 volte -> False
    for v in set_valori:
        if valori.count(v) == 3:
            return False
    return True


def format_mano(mano):
    msg = ""
    for carta in mano:
        msg += f"{carta['valore']:>2}{SEMI_UNICODE[carta['seme']]} "
    return msg


# Chiamata Main
main()
