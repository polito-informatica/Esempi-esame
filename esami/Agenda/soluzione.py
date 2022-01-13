GIORNI = 365
ORE = 24

def main():

#Creo l'agenda
    agenda = []
    for i in range(GIORNI):
        row = [0] * ORE
        agenda.append(row)
#Inizializzo a stringa vuota tutte le descrizioni
    for i in range(len(agenda)):
        for j in range(len(agenda[0])):
            agenda[i][j] = ""

#Provo ad aprire il file e gestisco l'eccezione
    try:
        infile = open("agenda.txt", "r", encoding="utf-8")
        leggi_file(infile, agenda) #se posso aprire il file carico l'agenda
    except IOError:
        print("Error: file agenda.txt not found.")
        exit(-1)

    infile.close() #chiudo il file

    try:
        infile = open("comandi.txt", "r", encoding="utf-8")
    except IOError:
        print("Error: file comandi.txt not found.")
        exit(-1)

    for riga in infile:
        if riga[0] == "v" or riga[0]== "V": #se è richiesto visualizzare invoco la procedura visualizza
            campi = riga.split()
            giorno = int(campi[1])
            visualizza(agenda, giorno)
        elif riga[0] == "i" or riga[0] == "I": #altrimenti provo a inserire l'appuntamento
            campi = riga.split(maxsplit=3) #gestisco descrizioni su più parole
            giorno = int(campi[1])
            ora = int(campi[2])
            descrizione = campi[3]
            inserisci(agenda,giorno,ora,descrizione) #invoco la procedura che prova a inserire
        else:
            print("Comando %s errato"%(riga))
    infile.close() #chiudo il file

def leggi_file(fp, agenda):
    for line in fp:
        linea = line.rstrip()
        campi = linea.split(";")
        riga = int(campi[0]) - 1
        colonna = int(campi[1])
        agenda[riga][colonna] = agenda[riga][colonna] + campi[2]

    return

def visualizza(agenda, giorno):

    for i in range(len(agenda)):
        for j in range(len(agenda[0])):
            if i == giorno-1 and agenda[i][j] != "":
                print("%s %d %s %02d: %s"%("giorno",giorno,"ore",j,agenda[i][j]))

    return

def inserisci(agenda, giorno, ora, descrizione):

    if agenda[giorno-1][ora] != "":
        print("Impossibile inserire appuntamento")
    else:
        agenda[giorno-1][ora] = agenda[giorno-1][ora] + descrizione
        print("Appuntamento inserito correttamente")
        visualizza(agenda, giorno)
    return

main()
