# Log di un Server Web

#### (Esame proposto il 09-10/02/2026)


Un server web registra tutti gli accessi in un file di log CSV (`web_log.csv`). Ogni riga rappresenta una richiesta HTTP e contiene le seguenti informazioni separate da virgola: 

- timestamp: data e ora della richiesta (formato: YYYY-MM-DD HH:MM:SS) 
- client_ip: indirizzo IP del client 
- resource: risorsa richiesta (es: /index.html, /api/data) 
- response_code: codice di risposta HTTP (es: 200, 404, 500) 
-  response_time: tempo di risposta in millisecondi


Si richiede di scrivere un programma Python che legga il file CSV web_log.csv e calcoli le seguenti statistiche:

1. Per ogni risorsa (resource), determinare:
    - Numero totale di richieste
    - Numero di richieste con codice di risposta diverso da 200

2. Per ogni client (client_ip), identificare:

    - La risorsa più frequentemente richiesta

### Esempio

#### File web_log.csv

    timestamp,client_ip,resource,response_code,response_time
    2024-05-01 10:15:30,192.168.1.100,/index.html,200,45
    2024-05-01 10:15:35,192.168.1.115,/api/data,200,120
    2024-05-01 10:16:10,192.168.1.100,/index.html,404,20
    2024-05-01 10:16:15,192.168.1.100,/api/data,500,200
    2024-05-01 10:34:40,192.168.1.115,/api/users,200,200
    2024-05-01 10:42:15,192.168.1.115,/api/data,500,300
    2024-05-01 10:54:10,192.168.1.115,/api/data,200,125
    2024-05-01 11:23:25,192.168.1.115,/api/products,200,140


#### Output

    === STATISTICHE PER RISORSA ===
    /index.html:
      - Richieste totali: 2
      - Errori (non 200): 1
    /api/data:
      - Richieste totali: 4
      - Errori (non 200): 2
    /api/users:
      - Richieste totali: 1
      - Errori (non 200): 0
    /api/products:
      - Richieste totali: 1
      - Errori (non 200): 0

    === STATISTICHE PER CLIENT ===
    192.168.1.100:
      - Risorsa più richiesta: /index.html (2 volte)
    192.168.1.115:
      - Risorsa più richiesta: /api/data (3 volte)
