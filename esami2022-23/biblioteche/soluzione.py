# Soluzione esercizio "Biblioteche" (esame del 19/09/2023)

import csv
from pprint import pprint


NOME_INVENTARIO = "inventarioOld.csv"


def leggi_inventario(nome_file):
    libri = []
    with open(nome_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for record in reader:
            libri.append(record)
    return libri


def crea_dizionario(libri):
    """Crea un dizionario in cui vengono accorpati tutti i libri con lo stesso codice ISBN.
    Restituisce una struttura dati di tipo dizionario, con *chiave* = ISBN, e *valore* un piccolo
    dizionario con i campi titolo, autore, copie. A sua volta, *copie* è una lista dei codici di copia.

    Args:
        libri (list): Lista dei libri presenti nell'inventario

    Returns:
        dict: dizionario con chiave codici ISBN
    """
    titoli = dict()

    for libro in libri:
        # estraggo i campi per comodità
        copia = libro[0]
        isbn = libro[1]
        titolo = libro[2]
        autore = libro[3]

        # nota: potrei anche scrivere
        # [copia, isbn, titolo, autore] = libro

        if isbn in titoli:
            # già visto, devo semplicemente aggiungere il codice copia
            titoli[isbn]["copie"].append(copia)
        else:
            # non ancora visto, devo salvare i suoi dati creando un dizionario
            titoli[isbn] = {
                "titolo": titolo,
                "autore": autore,
                "copie": [
                    copia
                ],  # è una lista perché potranno arrivare altri codici in seguito
            }

    return titoli


def crea_file(titoli, file_scuola, file_inventario):
    """Crea i 2 file di uscita

    Args:
        titoli (dict): elenco dei titoli in inventario (dict con chiave = isbn)
        file_scuola (str): nome file in cui salvare i libri per la scuola
        file_inventario (str): nome file in cui salvare i libri rimasti in inventario
    """
    f_scuola = open(file_scuola, "w", encoding="utf-8")
    f_inventario = open(file_inventario, "w", encoding="utf-8")

    for isbn in titoli:
        # estraggo i campi
        autore = titoli[isbn]["autore"]
        titolo = titoli[isbn]["titolo"]
        copie = titoli[isbn]["copie"]
        # Verifico quante copie ho
        n_copie = len(titoli[isbn]["copie"])

        if n_copie <= 3:
            # ho fino a 3 copie, le tengo tutte in inventario
            scrivi_riga(f_inventario, isbn, titolo, autore, copie)
        else:
            # ho più di 3 copie, mando alla scuola le prime 3, e tengo le restanti in inventario
            scrivi_riga(f_scuola, isbn, titolo, autore, copie[0:3])
            scrivi_riga(f_inventario, isbn, titolo, autore, copie[3:])

    f_scuola.close()
    f_inventario.close()


def scrivi_riga(f, isbn, titolo, autore, copie):
    """scrive una singola riga nei file di uscita

    Args:
        isbn (str): codice isbn del libro (la chiave del dict)
        titolo (str): titolo libro
        autore (str): autore libro
        copie (list[str]): lista con i codici delle stringhe
    """
    print(f"{isbn};{titolo};{autore};", end="", file=f)
    print(";".join(copie), file=f)


def main():
    libri = leggi_inventario(NOME_INVENTARIO)
    # pprint(libri)

    titoli = crea_dizionario(libri)
    # pprint(titoli)

    crea_file(titoli, "inventarioScuola.csv", "inventarioNew.csv")


main()
