# Soluzione proposta esempio "Morse"

FILE_MORSE = 'morse.txt'
FILE_COMANDI = 'comandi.txt'


def leggi_testo(nomefile):
    try:
        infile = open(nomefile, 'r')
    except:
        exit('Impossibile aprire il file')

    linea = infile.readline()
    if linea != '':
        linea = linea.rstrip('\n')
    else:
        exit('Il file è vuoto!')

    infile.close()
    return linea


def leggi_morse():
    morsefile = open(FILE_MORSE, 'r')
    conversione = []
    for line in morsefile:
        campi = line.strip().split()
        regola = {
            'testo': campi[0].upper(),
            'morse': campi[1]
        }
        conversione.append(regola)
    return conversione


def codifica(testo, conversione):
    msg = ''
    for ch in testo:
        if ch.upper() in conversione:
            msg = msg + conversione[ch.upper()] + ' '
    return msg


def decodifica(testo, conversione):
    msg = ''
    simboli = testo.strip().split()
    for simbolo in simboli:
        if simbolo in conversione:
            msg = msg + conversione[simbolo]
    return msg


def main():
    conversione = leggi_morse()

    conversione_testo_morse = {}
    conversione_morse_testo = {}
    for regola in conversione:
        conversione_testo_morse[regola['testo']] = regola['morse']
        conversione_morse_testo[regola['morse']] = regola['testo']

    # leggiamo i comandi
    comandi = open(FILE_COMANDI, 'r')
    for riga in comandi:
        op, file_name = riga.strip().split()
        op = op.strip().lower()

        messaggio = leggi_testo(file_name)

        if op == 'c':
            risultato = codifica(messaggio, conversione_testo_morse)
            print(f'Codifica del file {file_name}:')
            print(risultato)
        else:
            risultato = decodifica(messaggio, conversione_morse_testo)
            print(f'Decodifica del file {file_name}:')
            print(risultato)


main()
