from sys import exit
from operator import itemgetter

NOME_FILE = 'bowling.txt'


def main():
    # Provo ad aprire il file e gestisco l'eccezione
    try:
        infile = open(NOME_FILE, "r", encoding="utf-8")
        partita = leggi_file(infile)  # se posso aprire il file carico i dati
        visualizza(partita)
    except IOError:
        print("Error: file bowling.txt not found.")
        exit(-1)

    infile.close()  # chiudo il file


def leggi_file(fp):
    partita = []
    for line in fp:
        linea = line.rstrip()
        campi = linea.split(";")
        lista = []
        totale = 0
        n_max = 0
        n_min = 0
        for i in range(2, len(campi)):
            lista.append(campi[i])
            totale = totale + int(campi[i])
            if int(campi[i]) == 10:
                n_max = n_max + 1
            if int(campi[i]) == 0:
                n_min = n_min + 1
        record_giocatore = {  # creo un dizionario che contiene i dati di ogni giocatore
            'cognome': campi[0],
            'nome': campi[1],
            'punteggi': lista,
            'totale': totale,
            'massimo': n_max,
            'minimo': n_min
        }
        partita.append(record_giocatore)  # creo una lista di dizionari

    return partita


def visualizza(partita):
    partita_ordinata = list(partita)
    partita_ordinata.sort(key=itemgetter('totale'), reverse=True)
    piu_dieci = 0
    piu_zero = 0
    for i in range(0, len(partita_ordinata)):
        print("%-20s %-20s %-3d" % (
            partita_ordinata[i]["cognome"], partita_ordinata[i]["nome"], partita_ordinata[i]["totale"]))
        if partita_ordinata[i]["minimo"] > partita_ordinata[piu_zero]["minimo"]:
            piu_zero = i
        if partita_ordinata[i]["massimo"] > partita_ordinata[piu_dieci]["massimo"]:
            piu_dieci = i
    print("%s %s ha abbattuto tutti i birilli %d volta/e" % (
        partita_ordinata[piu_dieci]["cognome"], partita_ordinata[piu_dieci]["nome"],
        partita_ordinata[piu_dieci]["massimo"]))
    print("%s %s ha mancato tutti i birilli %d volta/e" % (
        partita_ordinata[piu_zero]["cognome"], partita_ordinata[piu_zero]["nome"], partita_ordinata[piu_zero]["minimo"]))
    return


main()
