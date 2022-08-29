def main():
    (ingredienti, procedimento) = leggi_file_ricetta("polenta_concia.txt")
    # (ingredienti, procedimento) = leggi_file_ricetta("fusilli_alle_olive.txt")

    print("Ingredienti: ")
    print(stampa_ingredienti(ingredienti))

    print(f"Numero di ingredienti: {len(ingredienti)}")

    cibi = leggi_file_cibi("cibi.txt")

    (costo, calorie) = calcola_costo_calorie(ingredienti, cibi)

    print(f"Costo ricetta: {costo:.2f}")
    print(f"Calorie ricetta: {calorie:.2f}")


def leggi_file_ricetta(nome_file):
    infile_ricetta = open(nome_file, "r")
    line = infile_ricetta.readline()

    ingredienti = []
    procedimento = ""

    while "Procedimento:" not in line:
        if "Ingredienti" not in line and len(line) > 1:
            campi = line.rstrip().split(";")
            ingrediente = {"nome": campi[0], "quantita": float(campi[1])}

            ingredienti.append(ingrediente)

        line = infile_ricetta.readline()

    while line != "":
        if "Procedimento:" not in line:
            procedimento += line.rstrip() + " "
        line = infile_ricetta.readline()

    infile_ricetta.close()

    return ingredienti, procedimento


def stampa_ingredienti(ingredienti):
    risultato = ""
    for ingrediente in ingredienti:
        risultato += f'{ingrediente["nome"]} - {ingrediente["quantita"]}\n'

    return risultato


def leggi_file_cibi(nome_file):
    infile_cibi = open(nome_file, "r")

    cibi = []
    for line in infile_cibi:
        campi = line.rstrip().split(";")
        cibo = {"nome": campi[0], "costo": float(campi[1]), "calorie": float(campi[2])}

        cibi.append(cibo)

    infile_cibi.close()

    return cibi


def calcola_costo_calorie(ingredienti, cibi):
    costo = 0.0
    calorie = 0.0

    for ingrediente in ingredienti:
        for cibo in cibi:
            if ingrediente["nome"] == cibo["nome"]:
                costo += ingrediente["quantita"] / 1000 * cibo["costo"]
                calorie += ingrediente["quantita"] / 1000 * cibo["calorie"]

    return costo, calorie


main()
