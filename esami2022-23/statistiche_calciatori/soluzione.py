# Soluzione esercizio "Statistiche Calciatori" (esame del 19/09/2023)

import csv
import operator


def leggi_statistiche():
    """Legge il file CSV con tutte le statistiche

    Returns:
        list(dict): la lista di tutti i giocatori, ciascuno rappresentato da un record (dizionario) contenente i diversi campi. I campi numerici sono
        codificati come int.
    """
    with open("player_stats.csv", "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        stats = list(reader)
        for s in stats:
            for field in [
                "birth_year",
                "minutes",
                "goals",
                "assists",
                "offsides",
                "crosses",
                "interceptions",
                "tackles_won",
                "pens_conceded",
                "ball_recoveries",
                "aerials_won",
                "aerials_lost",
            ]:
                s[field] = int(s[field])
        return stats


def migliori_attaccanti(attaccanti):
    """determina i 3 miglior attaccanti di tutto l'elenco

    Args:
        attaccanti (list(dict)): il sottoinsieme di giocatori che gioca come attaccante

    Returns:
        list(dict): l'elenco degli attaccanti, ciascuno associato al proprio punteggio. La lista contiene un dict con una voce 'score' che
        rappresenta il punteggio, ed una voce 'player' che rappresenta l'intero record rappresentante il giocatore.
    """

    # crea una lista di player, affiancato ciascuno dal proprio punteggio "score"
    # la lista contiene dei dict che rappresentano i due valori (player e score)
    # lo score è calcolato come da testo dell'esercizio
    # la lista è in ordine di apparizione dei giocatori
    scores = [
        {
            "player": a,
            "score": (a["goals"] + a["assists"] - a["offsides"]) / a["minutes"],
        }
        for a in attaccanti
    ]

    # ordina la lista secondo il valore del campo score (decrescente)
    scores.sort(key=operator.itemgetter("score"), reverse=True)

    # stampa in bella i primi 3 elementi
    print("I tre attaccanti più efficaci sono:")
    print("Nome                Squadra              Efficacia")
    for s in scores[:3]:
        print(f'{s["player"]["player"]:20s}{s["player"]["team"]:20s}{s["score"]:10.3f}')
    print()

    # restituisce la lista calcolata, visto che serve nel punto 3
    return scores


def migliori_centrocampisti(centrocampisti):
    """determina i 3 miglior centrocampisti di tutto l'elenco

    Args:
        centrocampisti (list(dict)): il sottoinsieme di giocatori che gioca come centrocampista
    """

    # crea una lista di player, affiancato ciascuno dal proprio punteggio "score"
    # la lista contiene dei dict che rappresentano i due valori (player e score)
    # lo score è calcolato come da testo dell'esercizio
    # in questo caso non usiamo una comprehension, ma un ciclo esplicito (con append) perché il calcolo
    # dello score è più complesso

    # la lista è in ordine di apparizione dei giocatori

    scores = []

    for c in centrocampisti:
        if c["crosses"] == 0:
            score = (c["interceptions"] + c["ball_recoveries"]) / c["minutes"]
        else:
            score = (
                c["interceptions"] + c["ball_recoveries"] + c["assists"] / c["crosses"]
            ) / c["minutes"]
        scores.append({"player": c, "score": score})

    # ordina la lista secondo il valore del campo score (decrescente)
    scores.sort(key=operator.itemgetter("score"), reverse=True)

    # stampa in bella i primi 3 elementi
    print("I tre centrocampisti più efficaci sono:")
    print("Nome                Squadra              Efficacia")
    for s in scores[:3]:
        print(f'{s["player"]["player"]:20s}{s["player"]["team"]:20s}{s["score"]:10.3f}')
    print()


def eta_media_minore(statistiche, squadre):
    """determina le 3 squadre con l'età media minore

    Args:
        statistiche (list(dict)): elenco completo di tutti i giocatori
        squadre (set(str)): nomi unici delle squadre
    """

    # costruisco una lista di coppie (nome squadra, età media)
    eta = []
    for team in squadre:
        eta_team = [2023 - s["birth_year"] for s in statistiche if s["team"] == team]
        media = sum(eta_team) / len(eta_team)
        eta.append((team, media))
    
    # ordino la lista per età media crescente
    eta.sort(key=operator.itemgetter(1))

    # stampo in bella le prime 3
    print("Le tre nazionali più giovani sono:")
    for e in eta[:3]:
        print(f"{e[0]} con {e[1]:.2f} anni")
    print()


def attacco_migliore(efficacia_attaccanti, squadre):
    """Determina la squadra con l'attacco più efficace

    Args:
        efficacia_attaccanti (list(dict)): lista degli attaccanti e dei rispettivi punteggi, come calcolata dalla funzione migliori_attaccanti
        squadre (set(str)): nomi unici delle squadre
    """

    # costruisco una lista di elementi del tipo [nome squadra, somma delle efficacie dei 3 attaccanti migliori, elenco ordinato degli attaccanti migliori]
    eff_squadra = []
    for team in squadre:
        # seleziona gli attaccanti di questo team
        efficacia_attaccanti_team = [
            e for e in efficacia_attaccanti if e["player"]["team"] == team
        ]

        # ordina gli attaccanti per punteggio e prendi i 3 migliori
        efficacia_attaccanti_team.sort(key=operator.itemgetter("score"), reverse=True)
        efficacia_attaccanti_team = efficacia_attaccanti_team[:3]

        # calcola la somma dei punti (dei 3 migliori)
        somma = sum([e["score"] for e in efficacia_attaccanti_team])

        # salva i dati nella lista
        eff_squadra.append([team, somma, efficacia_attaccanti_team])

    # ordina la lista per somma-punti decrescente
    eff_squadra.sort(key=operator.itemgetter(1), reverse=True)

    # la squadra migliore è la prima della lista ordinata
    best = eff_squadra[0]

    # stampa in bella
    print(f"La nazionale con l'attacco più efficace è {best[0]}:")
    for p in best[2][:3]:
        print(f'{p["player"]["player"]} con efficacia {p["score"]:.3f}')


def main():
    # leggi il file CSV
    statistiche = leggi_statistiche()
    # estrai i nomi unici delle squadre
    squadre = {s["team"] for s in statistiche}

    # punto 1
    attaccanti = [s for s in statistiche if s["position"] == "FW"]
    efficacia_attaccanti = migliori_attaccanti(attaccanti)

    centrocampisti = [s for s in statistiche if s["position"] == "MF"]
    migliori_centrocampisti(centrocampisti)

    # punto 2
    eta_media_minore(statistiche, squadre)

    # punto 3
    attacco_migliore(efficacia_attaccanti, squadre)


main()
