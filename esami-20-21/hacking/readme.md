# Testo d'esame "Hacking"

L'azienda XXYYY vuole realizzare un applicativo capace di tracciare le vendite dei suoi prodotti al fine di
indentificare eventuali contraffazioni. L'applicativo deve analizzare il contenuto di due file. Un primo file di
testo `prodotti.txt` è creato dalla casa madre e contiene, per ogni prodotto fabbricato, l'identificativo dell'unico
rivenditore ufficiale che è autorizzato alla vendita del prodotto. Per ogni riga del file sono presenti due
informazioni (stringhe separate da uno spazio):

	id_prodotto id_rivenditore

Ciascun prodotto e ciascun venditore sono identificati tramite un codice alfanumerico univoco.

Un secondo file di testo `acquisti.txt` contiene invece le informazioni sulle vendite che sono state registrate dagli
acquirenti. Il file contiene su ogni riga il codice del prodotto acquistato e il rivenditore che ha gestito la consegna.

Dal momento che un prodotto può essere venduto soltanto dal rivenditore ufficiale autorizzato dalla casa madre,
qualsiasi acquisto di quel prodotto fatto da un acquirente attraverso un rivenditore _non ufficiale_ deve essere segnalato
come sospetto per permettere poi alla casa madre di fare le dovute verifiche.

La casa madre vi chiede pertanto di scrivere un programma Python che, letti i due file in input, stampi su schermo la
lista delle possibili vendite sospette. Nello specifico, per ogni prodotto venduto da uno o più rivenditori non
autorizzati, il programma deve stampare in uscita (nel formato indicato nell'esempio qui sotto) il codice del prodotto
in questione, il rivenditore ufficiale e la lista di tutti i rivenditori presso cui i clienti hanno registrato la
vendita.

***Nota***: non e' previsto alcun ordinamento dei due file in ingresso

## Esempio prodotti.txt:

	P234HF22222 r1011
	P234HF22223 r1112
	P234HF22225 r1114
	P111TG11115 r1015
	P111TG11115 r1216
	P331LS00110 r1017
	P331LS00120 r1318
	P331LS00130 r1019

## Esempio acquisti.txt

    P234HF22223 r1112
    P111TG11115 r1015
    P111TG11115 r1216
    P234HF22222 r1011
    P331LS00110 r1014
    P331LS00120 r1318
    P331LS00130 r1019
    P234HF22225 r1114
    P234HF22223 r1114

## Output del  programma

    Elenco transazioni sospette
    Codice prodotto: P234HF22223
    Rivenditore ufficiale: r1112
    Lista rivenditori:r1112 r1114 
    
    Codice prodotto: P111TG11115
    Rivenditore ufficiale: r1216
    Lista rivenditori:r1015 r1216 
    
    Codice prodotto: P331LS00110
    Rivenditore ufficiale: r1017
    Lista rivenditori:r1014
