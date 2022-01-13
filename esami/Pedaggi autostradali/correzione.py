def main():
  try:
    fileCaselli = open('pedaggi.txt','r')
  except IOError:
    exit('Errore apertura file pedaggi')
  
  # legge i caselli in un dizionario avente il casello di ingresso per chiave
  caselli = leggiCaselli(fileCaselli)
  fileCaselli.close()

  try:
    filePercorsi = open('percorsi.txt','r')
  except IOError:
    exit('Errore apertura file percorsi')

  
  primo = True
  
  for line in filePercorsi :
    campi = line.strip().split(';')
    partenza = campi[0]
    destinazione = campi[1]

    # cerca la tratta (successione di caselli) che parte da partenza e termina con destinazione
    (n_segmenti,costo) = cercaTratta(partenza,destinazione,caselli)

    # se la tratta esiste, n_segmenti > 0
    if n_segmenti > 0 :
      print("Percorso %s-%s: %d caselli, tariffa totale %.2f euro " %(partenza,destinazione,n_segmenti,costo))
      
      # se è il primo percorso valido, è anche quello con tariffa minima
      if primo :
        costoMin = costo
        partenzaMin = partenza
        destinazioneMin = destinazione
        primo = False
      
      # aggiorna il percorso con tariffa minima
      if costo < costoMin :
        costoMin = costo
        partenzaMin = partenza
        destinazioneMin = destinazione    
       
    else :
      print("Percorso %s-%s: non raggiungibile" %(partenza,destinazione))
 
  filePercorsi.close()

  # se primo è False, è stata trovata almeno una tratta valida, quindi si può stampare
  if not primo :
    print('\nIl percorso con la minima tariffa è %s-%s'%(partenzaMin,destinazioneMin))
  else :
    print('\nNon è stato trovato nessun percorso valido!')

# Dato il file dei caselli, già aperto, restituisce un dizionario che ha per chiave il casello di entrata e per valore un dizionario con casello di uscita e tariffa
def leggiCaselli(infile) :
  caselli = {}
  for line in infile :
    campi = line.strip().split(";")
    if campi[0] not in caselli :
      caselli[campi[0]] = {
        'uscita': campi[1],
        'tariffa': float(campi[2])
      }
  return caselli

# Cerca nel dizionario dei caselli la tratta (i.e. la successione di segmenti) che ha come primo ingresso il casello inizio e come ultima uscita il casello fine. Restituisce il numero di segmenti e la tariffa totale della tratta (entrambi 0, se la tratta non esiste)
def cercaTratta(inizio,fine,caselli) :
  nSegmenti = 0
  tariffaTotale = 0
  
  termina = False
  while not termina :
    if inizio in caselli : 
      nSegmenti += 1
      segmento = caselli[inizio]
      tariffaTotale += segmento['tariffa']
      if segmento['uscita'] == fine :
        # la tratta è stata trovata: termina e restituisci i risultati al chiamante
        termina = True 
      else :
        # continua a cercare: il nuovo segmento inizia con l'uscita del passo precedente
        inizio = segmento['uscita'] 
    else :
      # la tratta non è stata trovata: termina mettendo nSegmenti e tariffaTotale a 0
      termina = True 
      nSegmenti = 0 
      tariffaTotale = 0
  
  return(nSegmenti,tariffaTotale)
     
  

main() # inizio esecuzione