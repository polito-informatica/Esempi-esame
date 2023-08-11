# Soluzione proposta al tema d'esame "Paniere dei prezzi in Newfoundland"

# Variante 2: utilizzo di operazioni 'avanzate' sui vettori (comprehension, key)

import csv
import operator


def leggi_prezzi(nome_file):
    prezzi = []

    with open(nome_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(
            f, fieldnames=["date", "place", "store", "food", "essential", "price"]
        )
        next(reader)  # skip 1st line
        prezzi = list(reader)

    for p in prezzi:
        p["essential"] = p["essential"] == "E"  # will be True or False
        p["price"] = float(p["price"])

    return prezzi


def leggi_negozi(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        negozi = f.readlines()

    negozi = [n.strip() for n in negozi]
    return sorted(negozi)


def main():
    prezzi = leggi_prezzi("NLFoodPricing.csv")
    negozi = leggi_negozi("shops.txt")

    # 1. Stampa prodotti essenziali
    essenziali = [p for p in prezzi if p["essential"]]  # filtra gli essenziali
    nomi_essenziali = [p["food"] for p in essenziali]  # estrae solo il nome
    nomi_essenziali = sorted(set(nomi_essenziali))  # elimina duplicati e ordina

    print("Prodotti:")
    for nome in nomi_essenziali:
        print("- " + nome)

    # 2. Prezzo minimo per ciascuna catena e ciascun prodotto essenziale
    for shop in negozi:
        print()
        print(shop)

        prodotti_negozio = [p for p in essenziali if p["store"] == shop]

        for nome in nomi_essenziali:
            prezzi_prodotto_negozio = [
                p["price"] for p in prodotti_negozio if p["food"] == nome
            ]
            prezzo_min = min(prezzi_prodotto_negozio)

            # alternativa
            # prodotti_negozio_nome = [p for p in prodotti_negozio if p['food']==nome]
            # prodotto_prezzo_min = min(prodotti_negozio_nome, key=operator.itemgetter('price'))
            # prezzo_min = prodotto_prezzo_min['price']

            print(f"- {nome}: {prezzo_min} $/kg")

    # 3. Ricerca interattiva
    while True:
        print()
        nome = input("Che cibo vuoi cercare? (q per smettere) ")
        if nome == "q":
            break

        prodotti_nome = [p for p in essenziali if p["food"] == nome]
        if prodotti_nome:
            prodotto_min = min(prodotti_nome, key=operator.itemgetter("price"))
            print(
                f"Prezzo minimo: {prodotto_min['price']} $/kg da {prodotto_min['store']}"
            )
        else:
            print(f"Cibo {nome} non trovato")
    print("Arrivederci")


main()
