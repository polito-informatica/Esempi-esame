# Eldoria

#### (Esame proposto il 10-11/02/2025)


Nel regno di Eldoria, un'antica profezia narra di un imminente scontro tra le forze della luce e dell'oscurità. Maghi, fate, draghi e altre creature fantastiche, un tempo alleati, ora si trovano divisi da antiche rivalità e oscure macchinazioni. Per studiare le dinamiche di potere tra queste creature magiche, l'Arcimago ha commissionato un'analisi dettagliata delle loro abilità e dei loro incantesimi. Due file contengono le informazioni raccolte dai suoi emissari.

Il file `creature.csv` contiene l'ID della creatura, il nome, il tipo e il livello di potere (un intero che rappresenta la loro forza magica), separati da virgole.

Il file `incantesimi.csv` contiene l'ID dell'incantesimo, il nome, il tipo (*attacco*, *difesa*, *supporto*), l'ID della creatura che lo usa e la potenza dell'incantesimo (un intero che rappresenta l'efficacia dell'incantesimo), anch'essi separati da virgole.

Scrivi un programma Python che legga i dati da questi due file e stampi su schermo le informazioni che aiuteranno l'Arcimago a comprendere meglio la situazione.

In particolare il programma deve stampare delle informazioni relative alle creature, cioè gli incantesimi di tipo attacco e difesa, in questo formato (**vedi esempio!**):

```
Nome creatura (tipo, potenza)
 Attacco:
   Nome incantesimo: potenza
   Nome incantesimo: potenza
   ...
 Difesa:
   Nome incantesimo: potenza
   Nome incantesimo: potenza
   ...
```

Se non si trovano incantesimi (di attacco o difesa), l'output deve riportare la stringa "`Nessun incantesimo`".

È importante rispettare degli ordinamenti quando si stampano le informazioni:

1. Innanzitutto, le creature devono essere  **ordinate per tipo in ordine alfabetico crescente** (esempio: prima tutti i draghi, poi fate, ecc.)
2. A parità di tipo, il nome delle creature deve essere ordinato in ordine alfabetico crescente
3. Gli incantesimi di attacco e difesa devono essere ordinati per potenza decrescente
4. A parità di potenza, gli incantesimi devono essere ordinati in ordine alfabetico crescente.

### Esempio

#### `creature.csv`:
```
1,Merlino,mago,10
2,Viviana,fata,8
3,Fafnir,drago,15
4,Gandalf,mago,12
5,Morgana,fata,9
6,Smaug,drago,18
7,Oberon,fata,7
8,Radagast,mago,11
9,Ariel,fata,6
10,Drago Bianco,drago,16
11,Elrond,mago,13
12,Titania,fata,10
13,Bolla,drago,14
14,Saruman,mago,9
15,Ninfea,fata,8
16,Vermithor,drago,17
17,Silente,mago,14
18,Fata Madrina,fata,11
19,Scaglia di Ferro,drago,19
20,Merlin Ambrosius,mago,15
```

#### `incantesimi.csv`:

```
101,Fulmine,attacco,1,5
102,Scudo,difesa,1,7
103,Palla di fuoco,attacco,3,10
104,Cura,supporto,2,4
105,Tempesta di ghiaccio,attacco,6,12
106,Invisibilità,supporto,5,3
107,Protezione,difesa,4,6
108,Dardo incantato,attacco,1,3
109,Ali di fata,supporto,9,2
110,Soffio di fuoco,attacco,3,8
111,Terremoto,attacco,6,15
112,Muro di pietra,difesa,8,9
113,Illusione,supporto,7,5
114,Pioggia di meteoriti,attacco,10,18
115,Benedizione,supporto,12,6
116,Armatura magica,difesa,11,8
117,Disintegrazione,attacco,16,20
118,Parola del potere,supporto,17,7
119,Volo,supporto,19,4
120,Onda d'urto,attacco,14,11
121,Pietrificazione,attacco,20,16
122,Teletrasporto,supporto,18,9
123,Evocazione elementale,attacco,4,7
124,Raggio di luce,attacco,8,6
125,Trasformazione,supporto,15,8
126,Fulmine oscuro,attacco,13,9
127,Controllo mentale,supporto,20,10
128,Barriera magica,difesa,16,12
129,Esplosione arcana,attacco,17,14
130,Resurrezione,supporto,1,15
```

#### Output (rispetto a questi files):

```
Bolla (drago, potenza = 14):
  Attacco:
    Fulmine oscuro:9
  Difesa:
    Nessun incantesimo
Drago Bianco (drago, potenza = 16):
  Attacco:
    Pioggia di meteoriti:18
  Difesa:
    Nessun incantesimo
Fafnir (drago, potenza = 15):
  Attacco:
    Palla di fuoco:10
    Soffio di fuoco:8
  Difesa:
    Nessun incantesimo
Scaglia di Ferro (drago, potenza = 19):
  Attacco:
    Nessun incantesimo
  Difesa:
    Nessun incantesimo
Smaug (drago, potenza = 18):
  Attacco:
    Terremoto:15
    Tempesta di ghiaccio:12
  Difesa:
    Nessun incantesimo
Vermithor (drago, potenza = 17):
  Attacco:
    Disintegrazione:20
  Difesa:
    Barriera magica:12
Ariel (fata, potenza = 6):
  Attacco:
    Nessun incantesimo
  Difesa:
    Nessun incantesimo
Fata Madrina (fata, potenza = 11):
  Attacco:
    Nessun incantesimo
  Difesa:
    Nessun incantesimo
Morgana (fata, potenza = 9):
  Attacco:
    Nessun incantesimo
  Difesa:
    Nessun incantesimo
Ninfea (fata, potenza = 8):
  Attacco:
    Nessun incantesimo
  Difesa:
    Nessun incantesimo
Oberon (fata, potenza = 7):
  Attacco:
    Nessun incantesimo
  Difesa:
    Nessun incantesimo
Titania (fata, potenza = 10):
  Attacco:
    Nessun incantesimo
  Difesa:
    Nessun incantesimo
Viviana (fata, potenza = 8):
  Attacco:
    Nessun incantesimo
  Difesa:
    Nessun incantesimo
Elrond (mago, potenza = 13):
  Attacco:
    Nessun incantesimo
  Difesa:
    Armatura magica:8
Gandalf (mago, potenza = 12):
  Attacco:
    Evocazione elementale:7
  Difesa:
    Protezione:6
Merlin Ambrosius (mago, potenza = 15):
  Attacco:
    Pietrificazione:16
  Difesa:
    Nessun incantesimo
Merlino (mago, potenza = 10):
  Attacco:
    Fulmine:5
    Dardo incantato:3
  Difesa:
    Scudo:7
Radagast (mago, potenza = 11):
  Attacco:
    Raggio di luce:6
  Difesa:
    Muro di pietra:9
Saruman (mago, potenza = 9):
  Attacco:
    Onda d'urto:11
  Difesa:
    Nessun incantesimo
Silente (mago, potenza = 14):
  Attacco:
    Esplosione arcana:14
  Difesa:
    Nessun incantesimo
```