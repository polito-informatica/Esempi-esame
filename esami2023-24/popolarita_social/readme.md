# Popolarità sui social

#### (Esame proposto il 17/09/2024)


Si realizzi un programma per classificare i 100 account Instagram più seguiti per professione.

Un file di testo denominato "instagram.csv" contiene le informazioni sugli account Instagram più seguiti (fonte: List of most-followed Instagram accounts). In questo file, ogni riga rappresenta un account e contiene le seguenti informazioni, separate da virgole: il nome dell'account, il numero di follower (**in milioni**), e la professione.

Esempio di formato del file:

```
nome_account1;nome_persona1;followers1;professione1
nome_account2;nome_persona2;followers2;professione2
```

Il programma dovrà leggere il file "`instagram.csv`" e sommare il numero totale di follower per ciascuna professione. Successivamente, il programma dovrà creare un istogramma del numero di follower totali per ciascuna professione e stamparlo a video. L'istogramma dovrà mostrare, per ogni professione, il nome della professione ed il numero totale di follower in ordine **decrescente** di follower totali.

### Esempio di Input:

```
@instagram;Instagram;672;Social media platform
@cristiano;Cristiano Ronaldo;630;Footballer
@leomessi;Lionel Messi;503;Footballer
@selenagomez;Selena Gomez;427;Musician and actress
@kyliejenner;Kylie Jenner;399;Media personality
@therock;Dwayne Johnson;397;Actor and professional wrestler
@arianagrande;Ariana Grande;379;Musician and actress
@kimkardashian;Kim Kardashian;362;Media personality
@beyonce;Beyoncé;318;Musician and actress
@khloekardashian;Khloé Kardashian;309;Media personality
@nike;Nike;306;Sportswear multinational
@kendalljenner;Kendall Jenner;293;Media personality
@justinbieber;Justin Bieber;293;Musician
@taylorswift;Taylor Swift;283;Musician
@natgeo;National Geographic;283;Magazine
@virat.kohli;Virat Kohli;269;Cricketer
@jlo;Jennifer Lopez;252;Musician and actress
@nickiminaj;Nicki Minaj;229;Musician
@kourtneykardash;Kourtney Kardashian;223;Media personality
@neymarjr;Neymar;221;Footballer
...
```

### Esempio di Output:

```
Musician:               2024.6M
Musician and actress:   1915.0M
Media personality:      1586.0M
Footballer:             1468.0M
Social media platform:  672.0M
...
```