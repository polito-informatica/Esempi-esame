# Asta in busta chiusa

#### (Esame proposto il 10-11/02/2025)

La casa d'aste Sotheby's ha organizzato un'importante vendita di oggetti d'antiquariato. L'asta si svolge in busta chiusa: gli offerenti dispongono le offerte per gli oggetti a cui sono interessati in una busta sigillata e la passano al banditore. Le buste vengono aperte e, per ogni oggetto in vendita, il banditore individua l'offerta più alta. L'offerente che ha disposto l'offerta più alta si aggiudica l'oggetto. Se per un oggetto sono state ricevute offerte di medesimo importo da due o più offerenti, l'oggetto non è assegnato.

Il banditore ha richiesto un programma in Python per determinare le offerte più alte contenute nelle buste. Le offerte ricevute sono elencate nel file `offerte.txt`. E' presente una riga del file per ogni offerente, nel seguente formato:

`nome offerente, nome oggetto 1, offerta 1, nome oggetto 2, offerta 2, ...`

dove **nome offerente** e **nome oggetto** sono stringhe, mentre **offerta** è un intero, rappresentante un valore in k€. Ciascun offerente può cercare di acquistare quanti oggetti desidera, però per ogni oggetto può presentare una sola offerta. Il programma deve stampare in output: 
* l'elenco degli oggetti non assegnati perché sono state ricevute due o più offerte equivalenti. Per ogni oggetto non assegnato, occorre indicare l'ammontare dell'offerta più alta e l'elenco degli offerenti che l'hanno disposta. 
* per ogni offerente, l'elenco degli oggetti acquistati, con il corrispondente importo offerto, e il totale della spesa. Se un offerente non si è aggiudicato nessun oggetto, si deve visualizzare il messaggio "nessun oggetto aggiudicato". 
* Il nome dell'offerente che ha speso di più.

Si supponga che il file esista e non contenga errori. Per il formato di output, si veda l'esempio seguente.

### Esempio

#### `offerte.txt`:

```
Alice Walton, Sedia a dondolo Thonet, 3, Lampadario in cristallo di Boemia, 80, Pendola Boulle in tartaruga e ottone, 60, Tappeto persiano Qashqai, 12, Moneta d'oro romana "Aureo di Traiano", 31, Quadretto sacro fiammingo con cornice in legno dorato, 110
Francois Pinault, Astrolabio in ottone del XVI secolo, 120, Servizio da te in porcellana di Meissen, 40, Scrivania Chippendale in mogano, 120, Set di calici in cristallo Baccarat, 12, Miniatura di ritratto in avorio del periodo georgiano, 9
Leonard Lauder, Lampada Tiffany in vetro colorato, 310, Tavolo da gioco Regency in mogano, 24, Spada giapponese Katana del periodo Edo, 62, Moneta d'oro romana "Aureo di Traiano", 25, Set di piatti Wedgwood in stile neoclassico, 18
Miuccia Prada, Astrolabio in ottone del XVI secolo, 110, Servizio di posate in argento sterling Georg Jensen, 25, Spada giapponese Katana del periodo Edo, 62, Pianoforte a coda Steinway & Sons d'epoca, 100
Bernard Arnault, Tappeto persiano Qashqai, 15, Astrolabio in ottone del XVI secolo, 120, Servizio di posate in argento sterling Georg Jensen, 48, Baionetta napoleonica con impugnatura in avorio, 15, Coppa da libagione in giada cinese, 190
Eli Broad, Tavolo da gioco Regency in mogano, 18, Anello vittoriano con cammeo, 3, Astrolabio in ottone del XVI secolo, 120, Specchio veneziano con cornice dorata del XVIII secolo, 40, Sedia a dondolo Thonet, 7, Set di calici in cristallo Baccarat, 18
Saud bin Muhammed Al Thani, Scrivania Chippendale in mogano, 130, Arazzo francese del XVII secolo, 110, Lampada Tiffany in vetro colorato, 230, Baionetta napoleonica con impugnatura in avorio, 18, Servizio di posate in argento sterling Georg Jensen, 35
Patricia Phelps de Cisneros, Servizio da te in porcellana di Meissen, 45, Pianoforte a coda Steinway & Sons d'epoca, 110, Mappamondo terrestre olandese del XVII secolo, 268, Coppa da libagione in giada cinese, 135
Maja Hoffmann, Set di piatti Wedgwood in stile neoclassico, 19, Lampadario in cristallo di Boemia, 80, Quadretto sacro fiammingo con cornice in legno dorato, 85, Spada giapponese Katana del periodo Edo, 52, Porta sigari in argento Art Nouveau, 8
```

L'output è:

```
Stessa offerta per Lampadario in cristallo di Boemia (80) da parte di: Alice Walton, Maja Hoffmann.
Stessa offerta per Astrolabio in ottone del XVI secolo (120) da parte di: Francois Pinault, Bernard Arnault, Eli Broad.
Stessa offerta per Spada giapponese Katana del periodo Edo (62) da parte di: Leonard Lauder, Miuccia Prada.   

Alice Walton: Pendola Boulle in tartaruga e ottone 60, Moneta d'oro romana "Aureo di Traiano" 31, Quadretto sacro fiammingo con cornice in legno dorato 110, totale 201.
Francois Pinault: Miniatura di ritratto in avorio del periodo georgiano 9, totale 9.
Leonard Lauder: Lampada Tiffany in vetro colorato 310, Tavolo da gioco Regency in mogano 24, totale 334.
Miuccia Prada: nessun oggetto aggiudicato
Bernard Arnault: Tappeto persiano Qashqai 15, Servizio di posate in argento sterling Georg Jensen 48, Coppa da libagione in giada cinese 190, totale 253.
Eli Broad: Sedia a dondolo Thonet 7, Set di calici in cristallo Baccarat 18, Anello vittoriano con cammeo 3, Specchio veneziano con cornice dorata del XVIII secolo 40, totale 68.
Saud bin Muhammed Al Thani: Scrivania Chippendale in mogano 130, Baionetta napoleonica con impugnatura in avorio 18, Arazzo francese del XVII secolo 110, totale 258.
Patricia Phelps de Cisneros: Servizio da te in porcellana di Meissen 45, Pianoforte a coda Steinway & Sons d'epoca 110, Mappamondo terrestre olandese del XVII secolo 268, totale 423.
Maja Hoffmann: Set di piatti Wedgwood in stile neoclassico 19, Porta sigari in argento Art Nouveau 8, totale 27.    

L'offerente che ha speso di più è Patricia Phelps de Cisneros.
```