# Soluzione proposta esempio "Morse"

FILE_MORSE = 'morse.txt'
FILE_COMANDI = 'comandi.txt'


def leggi_testo(nome_file):
    """
    Legge e restituisce il contenuto della prima riga del file.

    :param nome_file: Nome del file da leggere
    :return: Stringa contenente la prima riga del file (senza \n finale)
    """
    try:
        in_file = open(nome_file, 'r')
    except OSError:
        exit('Impossibile aprire il file')

    linea = in_file.readline()
    if linea != '':
        linea = linea.rstrip('\n')
    else:
        exit('Il file è vuoto!')

    in_file.close()
    return linea


def leggi_codifica_morse():
    """
    Acquisisce dal file MORSE_FILE le regole di conversione tra alfabeto e codice Morse

    :return: una lista di dizionari { 'testo': lettera maiuscola, 'morse': stringa con la codifica Morse }
    """
    file_morse = open(FILE_MORSE, 'r')
    conversione = []
    for line in file_morse:
        campi = line.strip().split()
        regola = {
            'testo': campi[0].upper(),
            'morse': campi[1]
        }
        conversione.append(regola)
    return conversione


def codifica(testo, conversione):
    """
    Converte una stringa alfabetica in codice Morse. I caratteri non alfabetici vengono ignorati.

    :param testo: la stringa alfabetica da convertire
    :param conversione: la tabella di conversione, come dizionario { ascii: morse }
    :return: la stringa contenente la rappresentazione Morse di 'testo'
    """
    msg = ''
    for ch in testo:
        if ch.upper() in conversione:
            msg = msg + conversione[ch.upper()] + ' '
    return msg


def decodifica(testo, conversione):
    """
    Converte una stringa in codice Morse nel corrispondente alfabetico. I codici non riconosciuti vengono ignorati.

    :param testo: la stringa contenente un messaggio in codice Morse
    :param conversione: la tabella di conversione, come dizionario { morse: ascii }
    :return: la stringa contenente la rappresentazione alfabetica convertita
    """
    msg = ''
    simboli = testo.strip().split()
    for simbolo in simboli:
        if simbolo in conversione:
            msg = msg + conversione[simbolo]
    return msg


def main():
    conversione = leggi_codifica_morse()
    # 'conversione' contiene una lista di regole, nella forma
    # [ {'testo': 'A', 'morse': '.-}, { 'testo': 'B', 'morse': '-...'}, ...]

    conversione_testo_morse = {}  # dizionario contenente l'array associativo ascii -> morse, per la codifica
    conversione_morse_testo = {}  # dizionario contenente l'array associativo morse -> ascii, per la decodifica
    for regola in conversione:
        conversione_testo_morse[regola['testo']] = regola['morse']  # conversione_testo_morse['A'] = '.-'
        conversione_morse_testo[regola['morse']] = regola['testo']  # conversione_morse_testo['.-'] = 'A'

    # leggiamo i comandi
    comandi = open(FILE_COMANDI, 'r')
    for riga in comandi:
        op, file_name = riga.strip().split()  # legge i 2 campi e li salva, rispettivamente, nelle 2 variabili
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
