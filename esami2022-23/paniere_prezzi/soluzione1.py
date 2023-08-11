# Soluzione proposta al tema d'esame "Paniere dei prezzi in Newfoundland"

# Variante 1: utilizzo di algoritmi "tradizionali" (cicli e scansioni di vettori)

import csv
import sys


def leggi_prezzi(nome_file):
    prezzi = []

    with open(nome_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip 1st line

        for record in reader:
            prezzi.append(
                {
                    "date": record[0],
                    "place": record[1],
                    "store": record[2],
                    "food": record[3],
                    "essential": record[4] == "E",  # will be True or False
                    "price": float(record[5]),
                }
            )

    return prezzi


def leggi_negozi(nome_file):
    negozi = []
    f = open(nome_file, "r", encoding="utf-8")
    for line in f:
        negozi.append(line.strip())
    f.close()
    negozi.sort()
    return negozi


def main():
    prezzi = leggi_prezzi("NLFoodPricing.csv")
    negozi = leggi_negozi("shops.txt")

    # 1. Stampa prodotti essenziali
    essenziali = []
    for prodotto in prezzi:
        nome = prodotto["food"]
        if prodotto["essential"] and (nome not in essenziali):
            essenziali.append(nome)
    essenziali.sort()

    print("Prodotti:")
    for nome in essenziali:
        print("- " + nome)

    # 2. Prezzo minimo per ciascuna catena e ciascun prodotto essenziale
    for shop in negozi:
        print()
        print(shop)
        for nome in essenziali:
            prezzo_min = sys.float_info.max
            for prodotto in prezzi:
                if prodotto["store"] == shop and prodotto["food"] == nome:
                    if prodotto["price"] < prezzo_min:
                        prezzo_min = prodotto["price"]
            print(f"- {nome}: {prezzo_min} $/kg")

    # 3. Ricerca interattiva
    continua = True
    while continua:
        print()
        nome = input("Che cibo vuoi cercare? (q per smettere) ")
        if nome == "q":
            continua = False
        else:
            prezzo_min = sys.float_info.max
            shop_min = None
            for prodotto in prezzi:
                if prodotto["food"] == nome and prodotto["price"] < prezzo_min:
                    prezzo_min = prodotto["price"]
                    shop_min = prodotto["store"]
            if shop_min is None:
                print(f"Cibo {nome} non trovato")
            else:
                print(f"Prezzo minimo: {prezzo_min} $/kg da {shop_min}")
    print("Arrivederci")


main()
