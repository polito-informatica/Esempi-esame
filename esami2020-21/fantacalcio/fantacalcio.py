"""
Soluzione proposta per il tema d'esame "Fantacalcio"
"""


def leggi_file(nome_file):
    """
    Acquisisci le informazioni sui calciatori
    :param nome_file: Nome del file che contiene le informazioni sui calciatori
    :return: una lista di giocatori; ciascun giocatore è rappresentato da un dizionario
    contenente i 4 campi: nome, squadra, ruolo, costo
    """
    file = open(nome_file, 'r', encoding='utf-8')
    elenco_giocatori = []
    for riga in file:
        campi = riga.split(',')
        record = {
            'nome': campi[0].strip(),
            'squadra': campi[1].strip(),
            'ruolo': campi[2].strip(),
            'costo': int(campi[3])
        }
        elenco_giocatori.append(record)
    file.close()
    return elenco_giocatori


def scegli_rosa(info_ruolo, elenco_giocatori):
    """
    Sceglie in modo "ottimale" i giocatori per un determinato ruolo
    (secondo il criterio specificato nel testo).
    :param info_ruolo: dizionario che contiene la descrizione dei vincoli
    per la scelta dei giocatori: budget, num (numero di giocatori da scegliere), ruolo
    :param elenco_giocatori: lista contenente tutti i giocatori (non viene modificata)
    :return: lista di giocatori contenente quelli selezionati per l'acquisto
    """

    # estraggo i dati per comodità
    budget = info_ruolo['budget']
    num = info_ruolo['num']

    # seleziono solo i giocatori che hanno il ruolo specificato
    giocatori = [g for g in elenco_giocatori if g['ruolo'] == info_ruolo['ruolo']]
    # print(giocatori)

    rosa = []
    for i in range(num):  # ripeto tante volte quanti sono i giocatori desiderati
        costo_max = 0
        # cerco il giocatore di costo massimo
        for g in giocatori:
            # budget - (num - 1 - i) tiene conto del fatto che devo
            # 'riservare' un certo numero di milioni (num-1) la prima volta,
            # (num-2) la seconda volta, ecc... per i futuri giocatori
            if g['costo'] > costo_max and g['costo'] <= budget - (num - 1 - i):
                mio = g  # giocatore scelto
                costo_max = g['costo']
        # print(f'Budget: {budget}  -- Acquisto {mio}')
        rosa.append(mio)
        budget = budget - mio['costo']
        giocatori.remove(mio)  # per evitare di prendere due volte lo stesso
    return rosa


def main():

    # parametri di funzionamento del programma: elenco ruoli e relative cartteristiche
    info_ruoli = [
        {
            'ruolo': 'portiere',
            'num': 3,
            'budget': 20
        },
        {
            'ruolo': 'difensore',
            'num': 8,
            'budget': 40
        },
        {
            'ruolo': 'centrocampista',
            'num': 8,
            'budget': 80
        },
        {
            'ruolo': 'attaccante',
            'num': 6,
            'budget': 120
        }
    ]

    giocatori = leggi_file('fantacalcio.txt')
    # print(giocatori)

    for info_ruolo in info_ruoli:
        rosa = scegli_rosa(info_ruolo, giocatori)

        # Stampa la rosa di giocatori per quel ruolo
        print(f'Ruolo: {info_ruolo["ruolo"]}')
        for g in rosa:
            print(g['nome'], g['costo'], end='  ')
        print()


main()
