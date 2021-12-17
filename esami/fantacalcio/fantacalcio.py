# La rosa della squadra è composta da 25 calciatori:
# 3 portieri,
# 8 difensori,
# 8 centrocampisti,
# 6 attaccanti.
NUM_PORTIERI = 3
NUM_DIFENSORI = 8
NUM_CENTROCAMPISTI = 8
NUM_ATTACCANTI = 6

# Il budget complessivo è 260 FantaMilioni; si decide di suddividerlo come segue:
# portieri: 20
# difensori: 40
# centrocampisti: 80
# attaccanti: 120
BUDGET_PORTIERI = 20
BUDGET_DIFENSORI = 40
BUDGET_CENTROCAMPISTI = 80
BUDGET_ATTACCANTI = 120


def main():
    calciatori = leggiFile("fantacalcio.txt")
    print("Portieri ", end="")
    budget = BUDGET_PORTIERI - NUM_PORTIERI + 1
    for i in range(NUM_PORTIERI):
        (nome, spesa) = trovaCalciatore(calciatori, "portiere", budget)
        print(nome, spesa, end=" ")
        budget = budget - spesa + 1

    # L'eventuale budget avanzato nell'acquisto dei portieri è usato per i difensori
    print("\nDifensori: ", end="")
    budget += BUDGET_DIFENSORI - NUM_DIFENSORI
    for i in range(NUM_DIFENSORI):
        (nome, spesa) = trovaCalciatore(calciatori, "difensore", budget)
        print(nome, spesa, end=" ")
        budget = budget - spesa + 1

    print("\nCentrocampisti: ", end="")
    budget += BUDGET_CENTROCAMPISTI - NUM_CENTROCAMPISTI
    for i in range(NUM_CENTROCAMPISTI):
        (nome, spesa) = trovaCalciatore(calciatori, "centrocampista", budget)
        print(nome, spesa, end=" ")
        budget = budget - spesa + 1

    print("\nAttaccanti: ", end="")
    budget += BUDGET_ATTACCANTI - NUM_ATTACCANTI
    for i in range(NUM_ATTACCANTI):
        (nome, spesa) = trovaCalciatore(calciatori, "attaccante", budget)
        print(nome, spesa, end=" ")
        budget = budget - spesa + 1
    return


## Legge i dati dei calciatori.
#  @param nomeFile nome del file da leggere
#  @return un dizionario: nome, ruolo, quotazione
def leggiFile(nomeFile):
    lista = []  # crea un dizionario vuoto
    try:
        inputFile = open(nomeFile, "r")
    except IOError:
        print("Il file non esiste.")
        return lista

    for riga in inputFile:  # Legge tutti i record presenti nel file.
        campi = riga.split(",")
        lista.append({"nome": campi[0],
                      "ruolo": campi[2].strip(),
                      "quotazione": int(campi[3])})
    inputFile.close()
    return lista


## Restituisce il calciatore con il ruolo indicato e con la più alta quotazione
#  purché inferiore al budget indicato
#  @param calciatori lista di dizionari con i dati dei calciatori
#  @param ruolo ruolo del calciatore
#  @param budget quotazione massima del calciatore
#  @return una tupla: nome del calciatore e quotazione
def trovaCalciatore(lista, ruolo, budget):
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
