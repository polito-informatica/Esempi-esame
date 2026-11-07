# Estrazione di stringhe

#### (Esame proposto il 09-10/02/2026)


Scrivere un programma Python che legga un file sorgente `codice.py` ed estragga **tutte le stringhe** presenti nel testo, ignorando correttamente i commenti.

## Regole e semplificazioni

- Le stringhe sono solo su una riga (non sono presenti stringhe multiriga né triple virgolette).
- Una stringa è **delimitata** da **apici singoli** (`'`) oppure **doppi apici** (`"`).
- Non sono presenti sequenze di escape: **il carattere backslash `"\"` non compare mai all’interno del file**.
- È possibile che esistano stringhe iniziate da un tipo di virgolette che contengono virgolette dell'altro tipo; queste vanno gestite ignorando la virgolette "piu' interne" (es. nella stringa `"Ho detto 'no'"` la stringa `'no'` va considerata parte della stringa delimitata dalle `""`)
- **Una stringa termina quando si incontra lo stesso delimitatore di apertura**.
- **Il carattere `"#"` indica l’inizio di un commento solo se non si trova all’interno di una stringa**; il commento termina a fine riga.
- Occorre ignorare le stringhe vuote.

## Cosa deve fare il programma
1. Scorrere il file `codice.py` riga per riga ed estrarre tutte le stringhe presenti (tenendo conto delle regole sopra).
2. Salvare il contenuto delle stringhe, senza i delimitatori in una struttura dati opportuna.
3. Eliminare le stringhe duplicate.
4. Ordinare le stringhe rimanenti per lunghezza crescente;
5. Salvare le stringhe ordinate nel file `strings.txt` (una per riga).

## Suggerimento

Si può usare un flag per distinguere se il programma si trova dentro o fuori da una stringa mentre si esamina il testo:


- Se si **è fuori da una stringa**, l’incontro di `'` o `"` indica **l’inizio di una stringa** (quindi il **delimitatore di apertura** della stringa stessa), mentre `#` indica l’inizio di un commento (riga da ignorare).

- Se si **è dentro una stringa**, l'incontro **dello stesso delimitatore di apertura** (che va memorizzato da qualche parte!) determina la **fine della stringa**.

### Esempio


Dato il seguente file `codice.py`:

    print("a", "", "b", "a", 'c', 'c')   # contiene una stringa vuota e duplicati
    print("riga1", "riga1")        # duplicato
    x = "it's ok"
    y = "# non è commento"
    z = "fine"  # "ignorato"

Stringhe salvate in `strings.txt` dopo l’esecuzione del programma:

    a
    b
    c
    fine
    riga1
    it's ok
    # non è commento