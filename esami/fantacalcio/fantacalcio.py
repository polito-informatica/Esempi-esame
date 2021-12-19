# La rosa della squadra è composta da 25 calciatori:
NUM_PORTIERI = 3
NUM_DIFENSORI = 8
NUM_CENTROCAMPISTI = 8
NUM_ATTACCANTI = 6

# Il budget complessivo è 260 FantaMilioni; si decide di suddividerlo come segue:
BUDGET_PORTIERI = 20
BUDGET_DIFENSORI = 40
BUDGET_CENTROCAMPISTI = 80
BUDGET_ATTACCANTI = 120


def main():
    calciatori = leggi_file("fantacalcio.txt")
    print("Portieri: ", end="")
    budget = BUDGET_PORTIERI
    for i in range(NUM_PORTIERI):
        (nome, spesa) = trova_calciatore(calciatori, "portiere", budget - (NUM_PORTIERI - i - 1))
        # devo tenere da parte almeno 1 milione per ciascuno degli ALTRI portieri
        # quando i==0 devo salvare un budget pari a NUM_PORTIERI-1
        # quando i==NUM_PORTIERI-1 (valore max) non devo più salvare budget (infatti NUM_PORTIERI - (NUM_PORTIERI-1)) - 1 == 0)

        print(nome, spesa, end=", ")
        budget = budget - spesa

    # L'eventuale budget avanzato nell'acquisto dei portieri è usato per i difensori
    print("\nDifensori: ", end="")
    budget += BUDGET_DIFENSORI
    for i in range(NUM_DIFENSORI):
        (nome, spesa) = trova_calciatore(calciatori, "difensore", budget - (NUM_DIFENSORI - (i - 1)))
        print(nome, spesa, end=", ")
        budget = budget - spesa

    print("\nCentrocampisti: ", end="")
    budget += BUDGET_CENTROCAMPISTI
    for i in range(NUM_CENTROCAMPISTI):
        (nome, spesa) = trova_calciatore(calciatori, "centrocampista", budget - (NUM_CENTROCAMPISTI - (i - 1)))
        print(nome, spesa, end=", ")
        budget = budget - spesa

    print("\nAttaccanti: ", end="")
    budget += BUDGET_ATTACCANTI
    for i in range(NUM_ATTACCANTI):
        (nome, spesa) = trova_calciatore(calciatori, "attaccante", budget - (NUM_ATTACCANTI - (i - 1)))
        print(nome, spesa, end=", ")
        budget = budget - spesa
    return


def leggi_file(nome_file):
    """
    Legge i dati dei calciatori

    :param nome_file: nome del file da leggere
    :return: una lista di dizionari: nome, ruolo, quotazione
    """
    lista = []  # crea un dizionario vuoto
    try:
        input_file = open(nome_file, "r")
    except IOError:
        print("Il file non esiste.")
        return lista

    for riga in input_file:  # Legge tutti i record presenti nel file.
        campi = riga.split(",")
        lista.append({"nome": campi[0],
                      "ruolo": campi[2].strip(),
                      "quotazione": int(campi[3])})
    input_file.close()
    return lista


def trova_calciatore(lista, ruolo, budget):
    """
    Restituisce il calciatore con il ruolo indicato e con la più alta quotazione
    purché inferiore al budget indicato

    :param lista: lista di dizionari con i dati dei calciatori
    :param ruolo: ruolo del calciatore
    :param budget: quotazione massima del calciatore
    :return: una tupla: nome del calciatore e quotazione
    """
    nome = ""
    quotazione = 0
    indice = 0
    i = 0
    for calciatore in lista:
        if (calciatore["ruolo"] == ruolo and
                quotazione < calciatore["quotazione"] <= budget):
            nome = calciatore["nome"]
            quotazione = calciatore["quotazione"]
            indice = i
        i = i + 1
    lista.pop(indice)
    return nome, quotazione


main()
