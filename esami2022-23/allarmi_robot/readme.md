# Gestione allarmi robot

#### (Esame proposto il 13-14/02/2023)

I guasti che si verificano su una linea robotizzata sono salvati nel file `allarmi.csv`.
Le informazioni sono separate da punto e virgola:

    fk_id_robot; severity; alarm_text

In particolare, `fk_id_robot` è un codice numerico univoco che identifica i robot sulla linea,
`severity` è un valore intero che classifica la gravità dell'allarme (valore maggiore
significa allarme più grave) e `alarm_text` è la descrizione testuale dell'allarme.

In base alle informazioni contenute in `allarmi.csv` il programma deve:

1. Stampare a video l'identificativo di ogni robot e il numero di allarmi corrispondenti (si ordini per numero di allarmi decrescenti)
2. Identificare il livello massimo di severità raggiunto e stampare tutti i codici identificati dei robot per i quali si è verificato tale livello di severità.

Si supponga che il formato del file sia corretto.

### Esempio

#### File `allarmi.csv`

    fk_id_robot;severity;alarm_text
    2213487;4;Timer  1 Alarm: (162)
    2213885;2;TP reconnection successfully completed (3s)
    2213369;4;Power Source 1 not ready for start riveting, waiting for $IN[103] = True
    2212111;4;PWS1 Fault 374 Alimentatore master: La slitta caricatore1 non ha ragg
    2213369;4;PWS1 Fault 476 Alimentatore master: Sensore di prossimit… _Ricevitore
    2212111;4;PWS1 Fault 210 DDC: La curva di rivettatura giace al di sopra della c
    2213487;10;Power Contactor Status Fault
    2213369;4;PWS1 Fault 374 Alimentatore master: La slitta caricatore1 non ha ragg
    2214565;2;MISURA OXFORD RETURNS ERROR
    2213885;4;ALARM code received from system 1 ERROR 1 from $FMI[95]
    2213885;2;RS - Joint Space Limiting SET 1 activation: TRUE
    2213885;2;RS - Joint Space Limiting SET 1 activation: FALSE
    2213885;4;Vision system in alarm $IN[389] = ON
    2214565;10;Axis 8 Arm 1 I2T triggered

#### Output a video

    Per il robot 2213885 si sono verificati 5 allarmi
    Per il robot 2213369 si sono verificati 3 allarmi
    Per il robot 2213487 si sono verificati 2 allarmi
    Per il robot 2212111 si sono verificati 2 allarmi
    Per il robot 2214565 si sono verificati 2 allarmi
    
    Il livello massimo di severità 10 è stato raggiunto dai seguenti robot:
    2213487
    2214565
