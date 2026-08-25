# outdoor-bosun
sistema software di supporto decisionale personalizzato per il trekking

A partire da una traccia gpx e dal profilo fisico dell'utente (età, altezza, peso, allenamento), il sistema fornisce dettagli e consigliper l'utente su 5 sezioni differenti, ma comunicanti tra loro:

- **dati tecnici percorso**: distanza, dislivello totale e parziale, profilo altimetrico, possibilità di dormire in tenda (comunica eventuali restrizioni a causa di aree protette dove è vietato il campeggio e il bivacco)
  
- **gestione acqua**: fonti di acqua disponibile durante il percorso, calcola il fabbisogno min/max per l'utente e suggerisce un range di capacità di acqua da portare
  
- **gestione cibo**: calcola kcal da assumere (in base a una stima del consumo giornaliero), divide le kcal totali tra i pasti e snack fuori pasto.
  { Suggerisce ricette per il fabbisogno calorico calcolato (tramite AI) }
  
- **gestione energia**: calcola che tipo di powerbank o caricatore portare in base ai dispositivi utilizzati e all frequenza d'uso.
  
- **gestione attrezatura**: in base alle sezioni precedenti, al meteo e altipo di pernotto (tenda, rifugio) fornisce una lista di attrezzatura utile al trekking, la suddivide nelle categorie essenziali (notte/shelter; cucina; primo soccorso; beautycase; abbigliamento; acqua; cibo; elettronica) e fornisce un range di peso adatto per ogni categoria, oltre al peso complessivo dello zaino.
  { Deve essere possibile inserire il proprio peso reale in modo tale da far confrontare il modello generato con lo zaino reale fatto per poter ricevere consigli su come alleggerire lo zaino o aumentare la comodità o altro (tramite AI) }

