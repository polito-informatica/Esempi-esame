# Soluzione proposta esercizio d'esame "potenze binomio"

from pprint import pprint


def tartaglia(N):
    """
    Calcola le prime N+1 righe del triangolo di Tartaglia (dal grado 0 al grado N compresi).
    Il triangolo viene calcolato come lista di lista: triangolo[g] contiene i coefficienti relativi
    al grado 'g' (0<=g<=N), e contiene g+1 coefficienti. Ciascun coefficiente triangolo[g][p] è relativo alla
    potenza p-esima di 'y' ed alla potenza (g-p)-esima di 'x'.

    :param N: grado del polinomio, ultima riga calcolata del triangolo
    :return: il triangono corrispondente dalla riga 0 alla riga N
    """

    triangolo = [[1]]  # riga 0 -> (a+b)^0 = 1

    # costruisco le righe del triangolo, dal grado 1 (seconda riga) al grado N
    for grado in range(1, N + 1):
        riga = [1]  # la riga inizia sempre con 1
        # ci sono tanti elementi intermedi quanti "grado-1" (es: grado = 3 -> 1/3/3/1 -> 2 elementi intermedi)
        # quindi range da 0 compreso a grado-2 escluso
        for pos in range(0, grado - 1):
            # faccio la somma dei giusti elementi nella riga precedente (che è già in triangolo[grado-1]
            riga.append(triangolo[grado - 1][pos] + triangolo[grado - 1][pos + 1])
        riga.append(1)  # la riga termina sempre con 1

        triangolo.append(riga)

    # pprint(triangolo)
    return triangolo


def leggi_float(msg):
    """
    Legge un numero reale, controllando gli errori

    :param msg: messaggio di invito da stampare
    :return: numero reale ritornato
    """
    ok = False
    while not ok:
        try:
            x = float(input(msg))
            ok = True
        except ValueError:
            print('Errore di immissione - ripetere')
    return x


def leggi_int(msg):
    """
    Legge un numero intero, controllando gli errori

    :param msg: messaggio di invito da stampare
    :return: numero intero ritornato
    """
    ok = False
    while not ok:
        try:
            x = int(input(msg))
            ok = True
        except ValueError:
            print('Errore di immissione - ripetere')
    return x


# coefficienti del polinomio potenza
def coeff_potenza(a, b, n):
    """
    Calcola i coefficienti del polinomio risultante dall'elevamento a potenza (potenza di grado 'n'). Vi
    saranno n+1 coefficienti, in cui l'i-esimo coefficiente è del tipo: tartaglia[n][i] * a^(n-i) * b^(i).

    :param a: coefficiente di 'x' nel monomio da elevare a potenza
    :param b: coefficiente di 'y' nel monomio da elevare a potenza
    :param n: grado della potenza da calcolare
    :return: lista dei coefficienti
    """
    triangolo = tartaglia(n)

    coeff = []
    # cicliamo sull'esponente di x da 0 a n
    for exp_x in range(0, n + 1):
        c = triangolo[n][exp_x] * a ** (n - exp_x) * b ** (exp_x)
        coeff.append(c)
    return coeff


def formatta_polinomio(grado, coeff):
    """
    Data una serie di coefficienti, "mette in bella" la stampa del polinomio

    :param grado: grado del polinomio
    :param coeff: lista di (grado+1) coefficienti
    :return: una stringa con la rappresentazione del polinomio
    """
    polinomio = ''

    for i in range(0, grado + 1):
        if i != 0:
            polinomio += '+ '

        term = f'{coeff[i]} '

        # x elevato a... grado-i
        if grado - i == 1:
            term += 'x '
        elif grado - i != 0:
            term += f'x^{grado - i} '

        # y elevato a... i
        if i == 1:
            term += 'y '
        elif i != 0:
            term += f'y^{i} '

        polinomio += term
    return polinomio


def main():
    try:
        infile = open('potenze.txt', 'r')
    except IOError:
        print('Impossibile aprire il file')

    coefficienti = infile.readline().strip().split()
    a = float(coefficienti[0])
    b = float(coefficienti[1])

    print(f'Potenze del binomio ({a}x + {b}y)^N')

    for line in infile:
        try:
            n = int(line)
            coeff = coeff_potenza(a, b, n)
            print(f'N = {n}')
            print(formatta_polinomio(n, coeff))
        except ValueError:
            print('Errore nel formato, linea ignorata')


main()
