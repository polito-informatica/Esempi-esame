from operator import itemgetter


def calcola_punti(p):
    return sum(p) - max(p) - min(p)


def main():
    try:
        filep = open("punteggi.txt", "r")
    except OSError:
        print("file non trovato")
        return 0

    punteggi = {}
    migliore_donna = {'cognome': '', 'nome': '', 'punti': 0}

    for riga in filep:
        dati = riga.split()
        # print(dati)

        nazione = dati[3]
        if nazione not in punteggi:
            punteggi[nazione] = 0

        # prendi i 5 punteggi e salvali in una lista di numeri
        p = [float(d) for d in dati[4:]]

        punteggio = calcola_punti(p)

        punteggi[nazione] += punteggio

        if dati[2] == 'F' and punteggio > migliore_donna['punti']:
            migliore_donna['cognome'] = dati[0]
            migliore_donna['nome'] = dati[1]
            migliore_donna['punti'] = punteggio

    print('La migliore atleta femminile è:', migliore_donna['cognome'], migliore_donna['nome'], "con un punteggio di",
          migliore_donna['punti'])

    nazioni_ordinate = sorted(punteggi.items(), key=itemgetter(1), reverse=True)
    print("Classifica nazioni: ")
    i = 1
    for (nazione, punti) in nazioni_ordinate[:3]:
        print(i, "classificato:", nazione, "punteggio: %.2f" % punti)
        i += 1


main()
