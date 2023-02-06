# Voti

#### (Esame proposto il 30-31/01/2023)

In due file di tipo .csv, aventi nome `primo_appello.csv` e `secondo_appello.csv`, come quelli sotto riportati, sono
presenti i voti dei due appelli della prima sessione di esame di un corso non meglio specificato. I campi sono quelli
riportati nell’header dei file .csv, che come struttura sono identici; tra i due file cambiano naturalmente le persone
riportate, dal momento che non si può superare un esame due volte. Si assuma inoltre che i file contengano dati
corretti (ad esempio voti compresi tra 18 e 31, dove 31 è 30 e lode) e che complessivamente tra i due file vi siano
almeno cinque studenti. Il programma Python deve:

- produrre un file in uscita, sempre di tipo .csv (completo di header), avente nome `sessione.csv`, contenente i dati di
  entrambi i file uniti, ordinati per voto crescente e, a parità di voto, per cognome, sempre crescente (in ordine
  alfabetico). Si ricorda che per ordinare su due chiavi si può utilizzare uno dei seguenti approcci: 1) usare
  itemgetter due volte, prima sulla chiave secondaria e poi su quella primaria in sequenza 2) usare itemgetter una volta
  sola, specificando entrambe le chiavi di ordinamento separate da virgola 3) usare lambda functions.
- dopo aver individuato le cinque persone che hanno ottenuto il voto più elevato (comprendendo entrambi gli appelli
  della sessione), per ciascuna di loro si deve calcolare la differenza tra il voto ricevuto all’esame e la media degli
  esami precedenti. Poi si deve stampare a video la media delle 5 differenze così calcolate, come riportato
  nell’esempio.

## Esempio

Dati i file `primo_appello.csv` e `secondo_appello.csv`:

    nome,cognome,voto,anno_nascita,media_esami_precedenti
    Paola,La Gala,31,2003,27.67
    Giorgio,Vultaggio,26,2002,25.45
    Anna,Marovino,18,2004,20.00
    Alessia,Albano,24,2001,23.80
    Tommaso,Carta,28,2002,28.30
    Michele,Lanza,23,2003,23.00

    nome,cognome,voto,anno_nascita,media_esami_precedenti
    Paola,Landini,27,2003,27.50
    Irene,Lasorsa,30,2003,29.00
    Nicola,Lavagno,23,2002,23.50
    Antonio,Ivaldi,27,2004,24.30
    Luca,Licitra,21,2003,22.00
    Francesca,Leone,31,2003,30.50

Il file `sessione.csv` risultante sarà:

    nome,cognome,voto,anno_nascita,media_esami_precedenti
    Anna,Marovino,18,2004,20.00
    Luca,Licitra,21,2003,22.00
    Michele,Lanza,23,2003,23.00
    Nicola,Lavagno,23,2002,23.50
    Alessia,Albano,24,2001,23.80
    Giorgio,Vultaggio,26,2002,25.45
    Antonio,Ivaldi,27,2004,24.30
    Paola,Landini,27,2003,27.50
    Tommaso,Carta,28,2002,28.30
    Irene,Lasorsa,30,2003,29.00
    Paola,La Gala,31,2003,27.67
    Francesca,Leone,31,2003,30.50

E a video verrà stampato:

    La media tra le differenze tra voto e media pregressa per i cinque studenti con voto maggiore nella sessione è : 0.81