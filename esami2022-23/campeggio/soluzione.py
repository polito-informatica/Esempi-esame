# Soluzione proposta tema d'esame `Campeggio` del 30/06/2023
import csv
from pprint import pprint


def leggi_prezzi(nome_file):
    with open(nome_file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter=';')
        prezzi = list(reader)  # crea lista di dict

    # convertiamo in forma numerica
    for prezzo in prezzi:
        prezzo['prezzo_camper'] = float(prezzo['prezzo_camper'])
        prezzo['prezzo_elettricità'] = float(prezzo['prezzo_elettricità'])
        prezzo['prezzo_persona'] = float(prezzo['prezzo_persona'])
        prezzo['prezzo_tenda'] = float(prezzo['prezzo_tenda'])
        del prezzo['']

    return prezzi


def leggi_occupazione(nome_file):
    with open(nome_file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter=';')
        occupazione = list(reader)  # crea lista di dict

    # convertiamo in forma numerica
    for occ in occupazione:
        occ['id_cliente'] = int(occ['id_cliente'])
        occ['numero_adulti'] = int(occ['numero_adulti'])
        occ['numero_bambini'] = int(occ['numero_bambini'])
    return occupazione


def leggi_calendario(nome_file):
    # mappiamo ciascuna data con un numero progressivo, così è comodo calcolare la differenza tra due date
    # costruisco un dizionario con
    # chiave = data (es. '07/05/23', rappresentata come stringa)
    # valore = numero progressivo di quella data nell'anno (es. 127, rappresentato come intero)
    calendario = dict()
    n = 1
    with open(nome_file, 'r', encoding='utf-8') as f:
        for data in f:
            calendario[data.strip()] = n
            n = n + 1
    return calendario


def main():
    prezzi = leggi_prezzi('prezzi.txt')
    # pprint(prezzi)

    occupazione = leggi_occupazione('occupazione.txt')
    # pprint(occupazione)

    calendario = leggi_calendario('calendario.txt')
    # pprint(calendario)

    # Calcola per ogni prenotazione
    for occ in occupazione:
        # giorni di arrivo/partenza rappresentati come numero intero progressivo
        giorno_arrivo = calendario[occ['arrivo']]
        giorno_partenza = calendario[occ['partenza']]

        totale = 0.0

        # Nota: calcola i prezzi giorno per giorno, dal giorno di arrivo al giorno di partenza - 1 (l'ultimo giorno non si conta,
        # e nell'istruzione range() viene appunto escluso l'ultimo elemento.
        # L'iterazione avviene sui numeri interi progressivi delle date
        for giorno in range(giorno_arrivo, giorno_partenza):
            # cerco i prezzi del giorno, considerando i vari intervalli di date
            prezzi_giorno = None
            for prezzo in prezzi:
                # il confranto avviene tra i numeri interi corrispondenti ai giorni indicati nel file
                # (grazie al dizionario che mi traduce le date in numeri progressivi)
                if calendario[prezzo['dal']] <= giorno <= calendario[prezzo['al']]:
                    prezzi_giorno = prezzo

            if prezzi_giorno is None:
                print("Non ho trovato l'intervallo di date")  # non dovrebbe mai succedere
            else:
                costo_giorno = prezzi_giorno['prezzo_persona'] * (occ['numero_adulti'] + occ['numero_bambini'])
                if occ['elettricità'] == 'sì':
                    costo_giorno += prezzi_giorno['prezzo_elettricità']
                if occ['tipo_abitazione'] == 'camper':
                    costo_giorno += prezzi_giorno['prezzo_camper']
                else:
                    costo_giorno += prezzi_giorno['prezzo_tenda']
            totale += costo_giorno

        print(f'cliente: {occ["id_cliente"]}, arrivo: {occ["arrivo"]}, partenza: {occ["partenza"]},  ' +
              f'tipo: {occ["tipo_abitazione"]}, persone: {occ["numero_adulti"] + occ["numero_bambini"]}, ' +
              f'elettricità: {occ["elettricità"]}, ' +
              f'prezzo: {totale}, numero notti: {giorno_partenza - giorno_arrivo}')


main()
