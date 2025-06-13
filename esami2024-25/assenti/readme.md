# Caccia agli assenti

#### (Esame proposto il 10-11/02/2025)


I docenti del corso di Informatica vogliono realizzare un programma in Python che identifichi gli studenti che si sono prenotati a un appello, ma che poi non si sono presentati per sostenere l’esame.

Per ogni appello, sono disponibili due file: 

- un file che riporta l’elenco degli iscritti, nel formato: `MATRICOLA COGNOME NOME`, ad esempio:
```
123456 ROSSI  MASSIMILIANO
263824 VERDI  ELEONORA
262741 GIALLI VERDI   GIOVANNI LUCIANO
343452 BLU    SARA
289374 ARANCIONI  ANDREA CHRISTIAN
```

- un file che riporta l’elenco degli studenti che hanno sostenuto l’esame, nel formato: `ANNO_COGNOME_”S”MATRICOLA_ID-ELABORATO`, ad esempio:
```    
2025_ROSSI_S123456_ex78497276113s326859641280856f8 2025_VERDI_S263824_ex78503276113s29459064128014d38 2025_GIALLIVERDI_S262741_ex78521276113s323676641280ca9b8 2025_BLU_S343452_ex78541276113s325531641280a7a29 2025_VIOLA_S325619_ex78421276113s325619641280e0727
```
Potete aiutare i docenti del corso di Informatica a realizzare il programma descritto?

In particolare, il programma dovrà: 
- leggere l'elenco degli iscritti e di chi si è presentato all’esame da tre coppie di file ("`prenotati_appello1.txt`" e "`consegne_appello1.txt`", "`prenotati_appello2.txt`" e "`consegne_appello2.txt`", "`prenotati_appello3.txt`" e "`consegne_appello3.txt`"); 
- identificare, per ogni appello, gli studenti che non si sono presentati all’esame e riportare il numero di assenti, a quell'appello; 
- dopo aver elaborato i dati dei 3 appelli, identificare le matricole degli studenti che non si sono presentati a nessuno dei 3 appelli, pur essendo prenotati in ciascuno di essi.

### Esempio di output:

```
Assenti al primo appello:
289374  ARANCIONI   ANDREA CHRISTIAN
292018  CAPUTO  EDOARDO
198563  COLLI   GIANLUCA
182637  CORRADO FLAVIA
In totale, ci sono 4 assenti

Assenti al secondo appello:
765849  ZUCCARO PAOLO
292018  CAPUTO  EDOARDO
198563  COLLI   GIANLUCA
In totale, ci sono 3 assenti

Assenti al terzo appello:
325619  VIOLA   FRANCESCO
292018  CAPUTO  EDOARDO
198563  COLLI   GIANLUCA
183927  SANFILIPPO  ANTONIO
In totale, ci sono 4 assenti

Matricole degli studenti che non si sono mai presentati a un appello:
198563
292018
```