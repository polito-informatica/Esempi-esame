# Soluzione proposta al tema d'esame "Gestione allarmi robot"


import csv
from operator import itemgetter
from pprint import pprint


def leggi_allarmi(nome_file):
    """
    Legge un file nel formato di allarmi.csv e costruisce una lista
    di dizionari corrispondenti ai dati contenuti nel file.

    Args:
        nome_file (str): nome del file da leggere

    Returns:
        list[dict]: una lista che contiene un elemento per ogni riga del file.
    """
    allarmi = []
    with open(nome_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for item in reader:
            allarmi.append(
                {
                    "id": int(item["fk_id_robot"]),
                    "severity": int(item["severity"]),
                    "text": item["alarm_text"].strip(),
                }
            )
    return allarmi


def statistiche_allarmi(allarmi):
    """
    Costruisce una lista [id robot, numero di allarmi] ordinata
    in modo descrescente per numero di allarmi
    """
    # contiamo quanti allarmi, faccio un dizionario id->numero
    frequenze = dict()
    for allarme in allarmi:
        id = allarme["id"]
        if id in frequenze:
            frequenze[id] = frequenze[id] + 1
        else:
            frequenze[id] = 1

    # convertiamo il dizionario in lista in modo da poterlo ordinare
    statistiche = list(frequenze.items())
    statistiche.sort(key=itemgetter(1), reverse=True)

    return statistiche


def main():
    allarmi = leggi_allarmi("allarmi.csv")
    # pprint(allarmi)

    statistiche = statistiche_allarmi(allarmi)
    for s in statistiche:
        print(f"Per il robot {s[0]} si sono verificati {s[1]} allarmi")

    max_severita = max(allarmi, key=itemgetter("severity"))
    print(
        f'Il livello massimo di severità {max_severita["severity"]} è stato raggiunto dai seguenti robot:'
    )
    for a in allarmi:
        if a["severity"] == max_severita["severity"]:
            print(a["id"])


main()
