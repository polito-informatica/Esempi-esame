# Componenti software

#### (Esame proposto il 29/04/2025)


Scrivere un programma in Python per gestire una collezione di **componenti software**, ognuno dei quali può essere composto da diversi **moduli funzionali**. Ogni modulo è descritto da alcune informazioni ed è salvato singolarmente nella libreria.

Il programma deve essere in grado di:

- Leggere i dati da un file CSV `componenti.csv`
- Eseguire richieste specificate in un file `richieste.txt`
- Stampare in output un riepilogo strutturato delle informazioni richieste

### File `componenti.csv`

Il file contiene informazioni sui moduli, con i seguenti campi (separati da virgole):

| Campo | Descrizione |
|-------|-------------|
| id | ID univoco del modulo |
| developer | Nome dello sviluppatore |
| component | Nome del componente software |
| module | Nome specifico del modulo (es. file o funzione) |
| language | Linguaggio di programmazione usato
| version | Codice versione del componente |
| size_kb | Dimensione del modulo in KB |

#### Esempio:

```
id,developer,component,module,language,version,size_kb
101,Mario Rossi,UserManager,LoginHandler,Python,v1.0,120
102,Mario Rossi,UserManager,RegisterHandler,Python,v1.0,135
103,Mario Rossi,UserManager,PasswordReset,Python,v1.0,110
201,Luca Verdi,AnalyticsTool,Tracker,Java,v2.3,200
202,Luca Verdi,AnalyticsTool,Reporter,Java,v2.3,180
203,Luca Verdi,AnalyticsTool,Filter,C++,v2.3,170
301,Anna Bianchi,ShopCart,AddToCart,JavaScript,v1.5,90
302,Anna Bianchi,ShopCart,RemoveFromCart,JavaScript,v1.5,95
401,Mario Rossi,AuthLib,TokenGen,Go,v2.0,80
402,Mario Rossi,AuthLib,TokenVerify,Go,v2.0,75
501,Sara Neri,ReportGen,CSVExporter,Python,v1.1,130
502,Sara Neri,ReportGen,PDFExporter,Python,v1.1,150
503,Sara Neri,ReportGen,HTMLExporter,Python,v1.1,120
```

### File `richieste.txt`

Contiene una richiesta per riga. Le richieste possono essere di due tipi:

- `d`: per ottenere informazioni sui componenti realizzati dallo sviluppatore indicato
- `l`: per ottenere informazioni sui componenti interamente realizzati nel linguaggio indicato

#### Esempio:

```
d:Mario Rossi
d:Sara Neri
d:Marco Bianchi
l:Python
l:Go
l:Rust
````

#### 1. Interrogazione per sviluppatore (`d`)

Dato uno sviluppatore, stampare per ogni suo componente:

- Codice versione del componente
- Nome del componente
- Dimensione totale in KB (somma dei moduli)
- Numero di moduli
- Dimensione media dei moduli

Se lo sviluppatore non è presente, indicarlo chiaramente ("Sviluppatore non presente nella libreria").

#### 2. Interrogazione per linguaggio di programmazione (`l`)

Dato un linguaggio, stampare i componenti interamente scritti in quel linguaggio, con:
- Nome dello sviluppatore
- Codice versione del componente

Se nessun componente è interamente scritto in quel linguaggio ma esistono moduli sparsi, stampare un messaggio di avviso.

Se il linguaggio non compare affatto nella libreria, indicarlo chiaramente ("Linguaggio non presente nella libreria").

### Esempio di output

```
Componenti sviluppati da Mario Rossi
- v1.0: UserManager, 365.00 KB
        3 moduli, in media 121.67 KB
- v2.0: AuthLib, 155.00 KB
        2 moduli, in media 77.50 KB

Componenti sviluppati da Sara Neri
- v1.1: ReportGen, 400.00 KB
        3 moduli, in media 133.33 KB

Componenti sviluppati da Marco Bianchi
Sviluppatore non presente nella libreria

Componenti scritti completamente in Python
- Mario Rossi, componente v1.0
- Sara Neri, componente v1.1

Componenti scritti completamente in Go
- Mario Rossi, componente v2.0

Componenti scritti completamente in Rust
Linguaggio non presente nella libreria
```