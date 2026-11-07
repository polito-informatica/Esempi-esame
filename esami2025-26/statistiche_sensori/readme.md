# Statistiche Sensori

#### (Esame proposto il 09-10/02/2026)

Un file `readings.txt` contiene una serie di letture di vari sensori, registrate in ordine di tempo. Ogni serie di letture inizia con un’intestazione nel formato:

    #Sensore <nome del sensore>  <tipologia del sensore>


seguita da una serie di letture per quel sensore (un numero float per riga). Le letture per un dato sensore si possono ripetere più volte nel file.

Scrivere un programma Python che:
 - Stampi media e deviazione standard delle letture di ogni sensore, ordinate per numero decrescente di letture
 - Stampi i sensori con numero massimo e minimo di letture.
 - Stampi il sensore con la media più alta e quello con la deviazione standard più alta
 - Stampi, per ogni categoria di sensori, la relativa lista ordinata per nome con il numero di letture.

### Esempio

#### File readings.txt

    #Sensore AB0x1 Temperatura
    1000
    1050
    930
    #Sensore XY034  Temperatura
    4003
    4010
    #Sensore Wn43 Pressione
    102
    103
    101
    #Sensor AB0x1 Temperatura
    1003
    1012
    1025
    #Sensore Wn45 Pressione
    99
    10
    105


#### Output

    AB0x1      (  6 ) Media =  1003.33 Deviazione Standard:    36.77
    Wn43       (  3 ) Media =   102.00 Deviazione Standard:     0.82
    XY034      (  2 ) Media =  4006.50 Deviazione Standard:     3.50
    Wn45       (  2 ) Media =    99.50 Deviazione Standard:     0.50

    Sensore con il numero massimo di letture: AB0x1 (6)
    Sensore con il numero minimo di letture: XY034 (2)

    Sensore con la media più alta: XY034 (4006.50)
    Sensore con la deviazione standard più alta: AB0x1 (36.77)

    Sensori di Pressione:
    Wn43    3
    Wn45    2

    Sensori di Temperatura:
    AB0x1   6
    XY034   2
