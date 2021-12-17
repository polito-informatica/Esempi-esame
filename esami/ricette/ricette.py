def main():
    (ingredienti, procedimento) = leggiFileRicetta("polenta_concia.txt")
    # (ingredienti, procedimento) = leggiFileRicetta("fusilli_alle_olive.txt")

    print("Ingredienti: ")
    print(stampaIngredienti(ingredienti))
    # print("Procedimento: "+procedimento)
    # print()

    print("Numero di ingredienti: %d" % (contaIngredienti(ingredienti)))

    cibi = leggiFileCibi("cibi.txt")

    (costo, calorie) = calcolaCostoCalorie(ingredienti, cibi)

    print("Costo ricetta: %.2f" % (costo))
    print("Calorie ricetta: %.2f" % (calorie))


def leggiFileRicetta(nome_file):
    infile_ricetta = open(nome_file, "r")
    line = infile_ricetta.readline()

    ingredienti = []
    procedimento = ""

    while "Procedimento:" not in line:
        if "Ingredienti" not in line and len(line) > 1:
            campi = line.rstrip().split(";")
            ingrediente = {}
            ingrediente["nome"] = campi[0]
            ingrediente["quantita"] = campi[1]

            ingredienti.append(ingrediente)

        line = infile_ricetta.readline()

    while line != "":
        if "Procedimento:" not in line:
            procedimento += line.rstrip() + " "
        line = infile_ricetta.readline()

    infile_ricetta.close()

    return (ingredienti, procedimento)


def contaIngredienti(ingredienti):
    return len(ingredienti)


def stampaIngredienti(ingredienti):
    risultato = ""
    for ingrediente in ingredienti:
        risultato += ingrediente["nome"] + " - " + ingrediente["quantita"] + "\n"

    return risultato


def leggiFileCibi(nome_file):
    infile_cibi = open(nome_file, "r")

    cibi = []
    for line in infile_cibi:
        campi = line.rstrip().split(";")
        cibo = {}
        cibo["nome"] = campi[0]
        cibo["costo"] = campi[1]
        cibo["calorie"] = campi[2]

        cibi.append(cibo)

    infile_cibi.close()

    return (cibi)


def calcolaCostoCalorie(ingredienti, cibi):
    costo = 0.0
    calorie = 0.0

    for ingrediente in ingredienti:
        for cibo in cibi:
            if ingrediente["nome"] == cibo["nome"]:
                costo += float(ingrediente["quantita"]) / 1000 * float(cibo["costo"])
                calorie += float(ingrediente["quantita"]) / 1000 * float(cibo["calorie"])

    return (costo, calorie)


main()
