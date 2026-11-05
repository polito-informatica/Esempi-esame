# Risparmio Assicurato

#### (Esame proposto il 26-27/01/2026)

Il sogno di ogni automobilista è sicuramente quello di risparmiare sui costi di mantenimento del proprio veicolo. È per questo che l'Associazione Viaggiatori Automobilisti Risparmiatori Italiani (AVARI) ti ha commissionato lo sviluppo di un programma Python che sia in grado di proporre il contratto assicurativo più economico sul mercato in base a) al veicolo posseduto, b) alla copertura assicurativa richiesta.

I dati dei veicoli supportati sono contenuti nel file `veicoli.txt`, nel formato seguente:

    marca,modello,tipologia_veicolo


dove tipologia_veicolo è un valore, compreso tra 1 e 5. Ogni compagnia assicurativa decide un prezzo diverso in base alla tipologia.

I dati dei contratti assicurativi sono presenti nel file `contratti.txt` nel formato seguente:

    compagnia_assicurativa,id_contratto,tipologia_veicolo,cristalli,prezzo

- Compagnia assicurativa: il nome della compagnia.
- ID Contratto: un valore alfanumerico che identifica univocamente il contratto di assicurazione. Si assuma che, all'interno del file, non esistano ID duplicati.
- Tipologia veicolo: lo stesso campo descritto in `veicoli.txt`
- Cristalli: copertura opzionale che può essere inclusa nel contratto. Può assumere il valore S se inclusa, o N se opzionale.
- Prezzo: il costo finale del contratto, in Euro.

Il file `utente.txt` contiene tre righe:

    marca dell'automobile da assicurare
    modello dell'automobile da assicurare
    copertura cristalli


Nella terza riga è presente il carattere `S` se la copertura cristalli è richiesta, `N` se non è richiesta.

Il programma deve: 

- Stampare a video la tipologia del veicolo corrispondente alla marca e al modello indicati nel file `utente.txt`. Se il veicolo non è presente nel file stampare un messaggio di errore e terminare il programma.

N.B. Gestire correttamente il caso in cui i dati nel file siano indicati usando lettere maiuscole, minuscole o una combinazione di entrambe. Le stringhe `fIaT` e `pANDa` devono restiturie il valore relativo a `Fiat` e `Panda`.

- Stampare a video un elenco completo dei contratti assicurativi che soddisfino le richieste dell'utente.

N.B. Se la copertura cristalli non è richiesta, la ricerca deve considerare sia i contratti con cristalli sia quelli senza cristalli.

- Stampare il contratto assicurativo più conveniente ed il contratto assicurativo meno conveniente.

### Esempio 1

#### File veicoli.txt

    marca,modello,tipologia_veicolo
    Fiat,Panda,1
    Volkswagen,Golf,1
    Toyota,Yaris,1
    Ford,Focus,1
    Renault,Clio,1
    Peugeot,208,1
    Opel,Corsa,1
    Honda,Civic,1
    Nissan,Qashqai,2
    Jeep,Renegade,2
    BMW,X1,2
    Mercedes-Benz,Sprinter,3
    Iveco,Daily,3
    Piaggio,Liberty,4
    Yamaha,MT-07,5
    Ducati,Monster,5
    Kawasaki,Ninja 650,5
    Tesla,Model 3,1
    Volvo,XC40 Recharge,2


#### File contratti.txt (sono mostrate solo le prime righe del file)

    compagnia_assicurativa,id_contratto,tipologia_veicolo,cristalli,prezzo
    Generali,GENFRKGBWN,1,N,778.66
    Generali,GEN6O7CAFW,2,N,840.62
    Generali,GENQBZ9HGG,3,N,1427.03
    Generali,GENMV0Z5ZJ,4,N,441.87
    Generali,GENF3EMUEV,5,N,761.28
    Generali,GEN7E40K7T,1,S,885.00
    Generali,GENM38DEIB,2,N,1178.77
    Generali,GEN0L7B75E,3,S,1453.69
    Generali,GENT0O7LGX,4,N,533.12
    Allianz Direct,ALD2Q0Q0XK,1,S,730.05
    Allianz Direct,ALD4PQ0ZKQ,2,S,1274.69
    Allianz Direct,ALDLZKPRBW,3,S,1656.17
    Allianz Direct,ALD87K8AMZ,4,N,332.03
    Allianz Direct,ALD2HB9KBC,5,S,912.48
    Allianz Direct,ALDORJQ41B,1,N,524.19
    Allianz Direct,ALDUMN7TBT,2,S,1482.80
    Allianz Direct,ALDTCWBL8B,3,N,1260.46
    Allianz Direct,ALD4Q6P5Z2,4,N,245.88


#### File utente.txt

    Honda
    Civic
    S


#### Output

    Veicolo: Honda Civic
    Tipologia veicolo: 1

    Elenco contratti assicurativi che soddisfano le richieste dell'utente:
    ID CONTRATTO    NOME COMPAGNIA         CRISTALLI           COSTO(€)
    GEN7E40K7T      Generali               S                     885.00
    ALD2Q0Q0XK      Allianz Direct         S                     730.05
    AXA7O7V08K      AXA                    S                     840.52
    UNIHABOL3U      UnipolSai              S                    1095.09
    CON0AOHN2B      ConTe.it               S                     706.86
    REA8WB4U2I      Reale Mutua            S                     824.59
    VITL1L3MDS      Vittoria Assicurazioni S                    1063.37
    HELWNGHT4O      Helvetia               S                     479.01
    SAR5FDEG9X      Sara Assicurazioni     S                    1029.09
    LIN9Y3HA78      Linear                 S                     981.22

    Il contratto più costoso è: UNIHABOL3U con €1095.09

### Esempio 2

I file `veicoli.txt` e `contratti.txt` sono uguali all'esempio 1.

#### File utente.txt

    Fiat
    Golf
    N


#### Output

    Errore, nessun veicolo trovato corrispondente a Fiat Golf
