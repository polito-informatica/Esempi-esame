def creaLegge(text):
    parts = text.strip().split()
    parole = set()
    for i in range(len(parts)):
        token = parts[i].strip(",;.:-_'?^)(!")
        if token != "":
            parole.add(token.lower())

    if len(text) > 50:
        text = text[:50] + "..."

    return {"testo": text, "parole": parole}


def caricaElenco(fileName):
    elenco = {}
    with open(fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()

        i = 0
        title = ""
        text = ""
        while i < len(lines):
            line = lines[i].strip()
            if title != "" and line != "":
                text += line + " "
            elif title == "" and line != "":
                title = line
            elif title != "" and line == "":
                legge = creaLegge(text)
                elenco[title] = legge
                title = ""
                text = ""

            i += 1

    return elenco


CERCA = "male"


def main():
    elenco = caricaElenco("leggi_di_Murphy.txt")
    # print(elenco)
    for (titolo, legge) in elenco.items():
        if CERCA in legge["parole"]:
            print(titolo + " - " + legge["testo"])


main()
