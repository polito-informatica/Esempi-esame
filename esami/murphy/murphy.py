FILE_MASSIME = 'leggi_di_Murphy.txt'
FILE_ARGOMENTI = 'argomenti.txt'


def leggi_massime(nomefile):
    massime = []

    murphile = open(nomefile, 'r', encoding='utf-8')

    titolo = murphile.readline().rstrip()
    while titolo != '':  # fino alla fine del file
        enunciato = ''
        riga = murphile.readline().rstrip()
        while riga != '':  # leggo il testo finché non trovo una riga vuota
            enunciato += riga + ' '
            riga = murphile.readline().rstrip()

        massima = {'titolo': titolo, 'enunciato': enunciato}
        massime.append(massima)

        titolo = murphile.readline().rstrip()  # leggo il titolo della successiva

    murphile.close()
    return massime


def leggi_argomenti(nomefile):
    parole = []
    infile = open(nomefile, 'r')
    for line in infile:
        if len(line) > 1:
            parole.append(line.strip().lower())
    infile.close()
    return parole


def ricerca(massime, parole):
    rilevanti = []
    for massima in massime:
        lista_parole = massima['enunciato'].split()  # separa le parole in corrispondenza degli spazi
        for i in range(len(lista_parole)):
            lista_parole[i] = lista_parole[i].strip(',.;:\'\"()').lower()

        if set(parole).intersection(lista_parole) != set():
            rilevanti.append(massima)

    return rilevanti


def main():
    massime = leggi_massime(FILE_MASSIME)
    argomenti = leggi_argomenti(FILE_ARGOMENTI)

    rilevanti = ricerca(massime, argomenti)

    for massima in rilevanti:
        print(f"{massima['titolo']} - ", end='')
        if len(massima['enunciato']) >= 50:
            print(f"{massima['enunciato'][:50]}...")
        else:
            print(f"{massima['enunciato']}")


main()
