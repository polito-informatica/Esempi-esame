# Soluzione proposta esercizio "Plotter"

FILE_PLOTTER = 'plotter.txt'
LATO = 5


def crea_riquadro(lato):
    riquadro = []
    for y in range(0, lato):
        riquadro.append(['.'] * lato)
    return riquadro


def stampa_riquadro(riquadro):
    for riga in riquadro[::-1]:  # prendo le righe in ordine inverso perché y=0 è in basso
        print(''.join(riga))


def disegna(riquadro, file):
    for line in file:
        campi = line.strip().split()

        if campi[0] == 'P':
            if len(campi) != 3:
                print('Numero errato di campi - riga ignorata')
            else:
                x = int(campi[1])
                y = int(campi[2])
                if 0 <= x <= len(riquadro[0]) and 0 <= y <= len(riquadro):
                    riquadro[y][x] = '*'
                else:
                    print(f'Coordinate {x} {y} fuori dal riquadro - riga ignorata')
        elif campi[0] == 'H':
            if len(campi) != 4:
                print('Numero errato di campi - riga ignorata')
            else:
                x = int(campi[1])
                y = int(campi[2])
                l = int(campi[3])
                if 0 <= x <= len(riquadro[0]) and 0 <= y <= len(riquadro) and x + l <= len(riquadro[0]):
                    for x1 in range(x, x+l):
                        if riquadro[y][x1] == '|':
                            riquadro[y][x1] = '+'
                        else:
                            riquadro[y][x1] = '-'
                else:
                    print(f'Linea {x} {y} * {l} fuori dal riquadro - riga ignorata')
        elif campi[0] == 'V':
            if len(campi) != 4:
                print('Numero errato di campi - riga ignorata')
            else:
                x = int(campi[1])
                y = int(campi[2])
                l = int(campi[3])
                if 0 <= x <= len(riquadro[0]) and 0 <= y <= len(riquadro) and y + l <= len(riquadro):
                    for y1 in range(y, y+l):
                        if riquadro[y1][x] == '-':
                            riquadro[y1][x] = '+'
                        else:
                            riquadro[y1][x] = '|'
                else:
                    print(f'Linea {x} {y} * {l} fuori dal riquadro - riga ignorata')

        else:
            print(f'Istruzione {campi[0]} non valida - riga ignorata')


def main():
    riquadro = crea_riquadro(LATO)
    # stampa_riquadro(riquadro)

    file = open(FILE_PLOTTER, 'r')
    disegna(riquadro, file)
    file.close()

    stampa_riquadro(riquadro)


main()
