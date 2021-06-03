#generatore del file delle domande
domande=open("domande.txt","w")
domande.writelines([
                "Solitamente di che colore ha la pelle un globlin? A=Rossa\tB=verde\n","B\n",
                "Quante zampe ha un drago? A=4\tB=2\n","A\n",
                "Quante zampe ha una viverna? A=4\tB=2\n","B\n",
                "I paladini in che magia sono specializzati? A=Sacra\tB=Acqua\n","A\n",
                "Quale razza vive più a lungo? A=Orchi\tB=Elfi\n","B\n",
                "Come si definisce un ibrido umano-ragno? A=Aracne\tB=Arciragno\n","A\n",
                "Quale creatura è un non morto? A=Lich\tB=Forgiato\n","A\n",
                "I Druidi possono trasformarsi in animali? A=Vero\tB=Falso\n","A\n",
                "Come si definisce il libro di un mago? A=Bestiario\tB=Grimorio\n","B\n",
                "Solitamente gli elfi oscuri vivono sottoterra? A=Vero\tB=Falso\n","A\n",
                "Chi appartiene alla classe barbaro usa prevalentemente la magia? A=Vero\tB=Falso\n","B\n",
                "Quale potere è caratteristico dei gorgoni? A=Avvelenamento\tB=Pietrificazione\n","B\n",
                "Cosa usi per allontanare un vampiro? A=Pomodoro\tB=Aglio\n","B\n"
                    ])
domande.close()

#generatore del file delle situazioni
situazioni=open("situazioni.txt","w")
#situazione,opzione1,opzione2,opzione3,testo_trabocchetto,testo_domanda
situazioni.writelines(["Ti trovi davanti a 3 porte magiche, quale scegli?\n","Porta rossa\n","Porta blu\n","Porta gialla\n","La porta ti conduce sopra un lago di lava!\n","La porta ti conduce a un albero interrogativo\n",
                    "Davanti a te ci sono 3 sentieri, quale decidi di percorrere?\n","Sentiero centrale\n","Sentiero di destra\n","Sentiero di sinistra\n","Mentre percorri il sentiero inciampi e cadi in una trappola letale!\n","Il sentiero termina davanti a un albero interrogativo\n",
                    "Hai davanti a te 3 forzieri e una chiave, quale forziere vuoi aprire?\n","Forziere grande\n","Forziere storto\n","Forziere brutto\n","Il forziere contiene un gatto esplosivo!\n","Il forziere contiene le indicazioni per un albero interrogativo\n",
                    "Ti trovi a un bivio, quale strada scegli?\n","Strada lastricata\n","Strada dissestata\n","Strada ghiaiosa\n","La strada scelta è di proprietà dell'orco Klaustron che decide di mangiarti!\n","A lato della strada trovi un albero interrogativo \n",
                    "Incontri uno gnomo bipolare che ti chiede come gli sta il suo berretto, cosa rispondi?\n","Bene\n","Male\n","Non saprei dire\n","Lo gnomo si offende e ti spezza le gambe!\n","Lo gnomo è soddisfatto della tua risposta e ti teletrasporta davanti a un albero interrogativo\n",
                    "Incontri un Drago raffinato che ti saluta, come rispondi?\n","Buongiorno signor Drago\n","Salve messer Drago\n","-Ruggisci-\n","Non hai rispettato il galateo draconico, e il Drago non la prende bene!\n","Il drago si sposta e dietro di lui vi è un albero interrogativo\n",
                    "Hai fame, ti guardi inorno per cercare del cibo, cosa mangi?\n","Fungo viola\n","Bacche nere\n","Frutto spinoso\n","Inizi a sentirti male e ti accasci al suolo!\n","Mentre raccogli il cibo noti un albero interrogativo nascosto alla vista\n",
                    "Vedi un coniglio tricefalo che sta venendo verso di te, dove ti nascondi?\n","Nel fitto della foresta\n","Sopra un albero\n","Dietro una roccia\n","Il coniglio riesce a individuarti, purtroppo per te hai un buon sapore.\n","Il coniglio perde le tue tracce e noti un albero interrogativo davanti a te\n",
                    "Sei nel territorio dei ragni giganti, come vuoi procedere?\n","Avanzo senza timore\n","Tento di aggirarla\n","Provo a tornare indietro\n","Mentre ti muovi spezzi accidentalmente un ramo e vieni notato dai residenti.\n","Riesci a uscire dalla zona e a trovare un albero interrogativo\n",
                    "Incontri il mago Rapynus che decide di offrirti un dono a tua scelta, quale prendi?\n","Dono grande\n","Dono medio\n","Dono piccolo\n","Apri il dono: contiene dei serpenti velenosi che ti mordono in tutto il corpo.\n","Apri il dono: contiene dei pomodori e le indicazioni per un albero interrogativo\n",
                    ])
situazioni.close()
