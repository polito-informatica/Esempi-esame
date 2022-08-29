# Soluzione proposta 'Indovina Chi'

FILE_PERSONAGGI = 'personaggi.txt'
FILE_DOMANDE = 'domande1.txt'


def main():
    personaggi = leggi_personaggi(FILE_PERSONAGGI)
    print(personaggi)

    gioca_partita(FILE_DOMANDE, personaggi)


def leggi_personaggi(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')

    proprieta = f.readline().rstrip().split(';')

    personaggi = []

    for line in f:
        valori = line.rstrip().split(';')
        personaggio = {}
        for i in range(len(proprieta)):
            personaggio[proprieta[i]] = valori[i]
        personaggi.append(personaggio)
    return personaggi


def gioca_partita(nome_file_partita, personaggi):
    personaggi_in_gioco = list(personaggi)  # faccio una copia per non modificare l'elenco completo

    f = open(nome_file_partita, 'r', encoding='utf-8')
    mosse = 0
    for line in f:
        proprieta, valore = line.rstrip().split('=')
        mosse += 1
        print(f'Mossa {mosse} - Domanda: {proprieta} = {valore} ?')

        personaggi_in_gioco = [p for p in personaggi_in_gioco if p[proprieta] == valore]
        print('Personaggi selezionati:')
        for personaggio in personaggi_in_gioco:
            for proprieta in personaggio:
                print(f'{proprieta}={personaggio[proprieta]}', end='  ')
            print()

    # alla fine del file quanti ne rimangono?
    if len(personaggi_in_gioco) == 1:
        print("Hai vinto!")
    else:
        print("Hai perso...")


main()
