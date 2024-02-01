"""
Risoluzione tema d'esame "Tempesta"

La tempesta viene rappresentata da una matrice (lista di
liste) di numeri interi.
"""


def leggi_tempesta(nome_file):
    f = open(nome_file, "r", encoding="utf-8")
    righe = f.readlines()  # liste di stringhe (riga del file con \n)
    f.close()
    matrice = []
    for riga in righe:
        valori = []
        for carattere in riga.rstrip("\n"):
            if carattere == "_":
                valori.append(0)
            elif carattere.isnumeric():
                valori.append(int(carattere))
            else:
                print("Errore nel formato del file")
        matrice.append(valori)
    return matrice


def ombelico(mappa):
    # calcolo una lista che contiene, per ciascuna riga, la somma degli elementi
    somma_riga = []
    for r in range(len(mappa)):
        somma = sum(mappa[r])
        somma_riga.append(somma)

    # trova la posizione del valore massimo
    max_riga = max(somma_riga)
    pos_max_riga = somma_riga.index(max_riga)

    # calcola una lista che contiene la somma per ogni colonna
    somma_col = []
    for c in range(len(mappa[0])):
        somma = 0
        for r in range(len(mappa)):
            somma = somma + mappa[r][c]
        somma_col.append(somma)

    # trova la posizione del valore massimo
    max_col = max(somma_col)
    pos_max_col = somma_col.index(max_col)

    # restituisce le coordinate riga,colonna dell'ombelico
    return pos_max_riga, pos_max_col


def sposta_tempesta(mappa):
    # costruisice una nuova matrice, con i numeri aggiornati,
    # senza modificare mappa[r][c]
    nuova = []
    for riga in mappa:
        # fai una copia della riga per non modificare la mappa originale
        riga2 = list(riga)
        # trova l'elemnto più a destra !=0 (se esiste, considerando il caso che potrebbero essere tutti 0)
        pos = len(riga2) - 1
        while riga2[pos] == 0 and pos >= 0:
            pos = pos - 1
        # decrementa di 1 l'ultimo elemento, se ho scoperto che esiste
        if riga2[pos] != 0:
            riga2[pos] = riga2[pos] - 1
        # costruisci una nuova riga contenenete i valori della precedente, spostati a destra di 1 posizione
        nuova_riga = [0] + riga2[:-1]
        nuova.append(nuova_riga)
    return nuova


def stampa_tempesta(mappa):
    for riga in mappa:
        stringa = ""
        for num in riga:
            if num == 0:
                stringa = stringa + "_"
            else:
                stringa = stringa + str(num)
        print(stringa)
    print()


def tempesta_esaurita(mappa):
    # la tempesta è esaurita se i numeri sono tutti zeri... cioè la loro somma è uguale a zero
    somma = 0
    for riga in mappa:
        somma = somma + sum(riga)
    return somma == 0


mappa = leggi_tempesta("mappa.txt")
r, c = ombelico(mappa)
print(f"L'ombelico è in posizione {r},{c} e vale {mappa[r][c]}")
stampa_tempesta(mappa)
while not tempesta_esaurita(mappa):
    nuova = sposta_tempesta(mappa)
    mappa = nuova
    stampa_tempesta(mappa)
