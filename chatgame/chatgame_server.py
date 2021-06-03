import tkinter as tk
import socket
from time import sleep
import threading
import random


def broadcast(msg, prefisso=""):
    '''funzione per inviare i messaggi a tutti i client associati alla chat'''
    for utente in clients:
        utente.send(bytes(prefisso, "utf8")+msg)

def accept_clients(server, y):
    '''funzione per la gestione dell'accettazione di client da parte del server
    la chat può accettare al massimo 10 client'''
    if gioco_iniziato.get()==True:
        return
    
    try:
        while True:
            if client_counter.get() < 10:
                client, client_addr = server.accept()
                client.send(bytes("~ Salve! Digita il tuo Nome seguito dal tasto Invio!", "utf8"))
                indirizzi[client]=client_addr
                threading._start_new_thread(gestisce_client, (client, client_addr))
                client_counter.set(client_counter.get() + 1)
            else:
                client, client_addr = server.accept()
                client.send(bytes("~ Server pieno, ritenta tra un po'","utf8"))
    except:
        pass


def gestisce_client(client,cilent_addr):
    '''funzione per la gestione dei client'''
    global game_timer
    try:
        nome = client.recv(BUFSIZ).decode("utf8")
        if gioco_iniziato.get()==True:
            return
        nome=nome[4:]
        #assegnazione del ruolo
        ruolo=random.choice(["Cavaliere ","Bardo ","Mago ","Mercante ","Paladino ","Stregone ","Chierico ","Ladro ","Monaco ","Barbaro ","Druido "])
        username = ruolo + nome
        #controllo per verificare che non ci siano utenti con lo stesso nome e lo stesso ruolo
        while ((username, 0) in clients.values()):
            client.send(bytes("~ Nome non valido o già presente", "utf8"))
            nome=client.recv(BUFSIZ).decode("utf8")
            username = ruolo + nome
        nome = username[:25:]
        benvenuto = '~ Benvenuto %s!' % nome 
        client.send(bytes(benvenuto, "utf8"))
        almeno_un_nome.set(True)
        if len(clients.values())!=0:
            print(str(list(clients.values())))
            client.send(bytes("~ I tuoi compagni di avventura sono "+str(list(clients.values())).replace('[','').replace(']','').replace('(','- ').replace("'","").replace(', 0)',''), "utf8"))
        msg = "~ %s si è unito all chat!" % nome
        broadcast(bytes(msg, "utf8"))
        punteggio=0
        clients[client] = (nome,punteggio)
        domanda=""
        pos=0 
        buffer_domande=[]
        buffer_situazioni=[0] #di default la prima domanda è la numero 0
        while True:
            msg = client.recv(BUFSIZ).decode()
            if msg[0:4] == "quit": #gestione dell'uscita
                del clients[client]
                broadcast(bytes("~ %s ha abbandonato la Chat." % nome, "utf8"))
                if(len(clients)==0):
                    game_timer=0
                break             
            elif msg[0:4] == "qstn": #gestione delle domande
                client.send(bytes("~ "+matrice_situa[pos][5],"utf8"))
                #controllo per evitare che una stessa domanda appaia più frequentemente di un'altra
                while True:
                    domanda=random.choice(list(domande.keys()))
                    if domanda not in buffer_domande:
                        buffer_domande.insert(0,domanda)
                        if len(buffer_domande)>4:
                            buffer_domande.pop()
                        break
                sleep(1)
                client.send(bytes(domanda,"utf8"))
            elif msg[0:4] == "answ": #gestione delle risposte
                msg = msg[4:]
                if msg == domande[domanda]:
                    punteggio=punteggio+1
                    client.send(bytes("~ MASTER: Risposta esatta!","utf8"))
                    sleep(1)
                    broadcast(bytes(str(punteggio),"utf8"), "- "+nome+": ")
                else:
                    punteggio=punteggio-1
                    client.send(bytes("~ MASTER: Risposta sbagliata","utf8"))
                    sleep(1)
                    broadcast(bytes(str(punteggio),"utf8"), "- "+nome+": ")
                #controllo per evitare che una stessa situazione appaia più frequentemente di un'altra
                while True:
                    pos=random.randint(0,len(matrice_situa)-1)
                    if pos not in buffer_situazioni:
                        buffer_situazioni.insert(0,pos)
                        if len(buffer_situazioni)>4:
                            buffer_situazioni.pop()
                        break
                client.send(bytes("~ "+matrice_situa[pos][0],"utf8"))
                sleep(1)
                client.send(bytes("_ "+matrice_situa[pos][1].replace("\n", "@")+matrice_situa[pos][2].replace("\n", "@")+matrice_situa[pos][3].replace("\n", "@")+matrice_situa[pos][4],"utf8"))
            else: #gestione dei messaggi dei giocatori
                broadcast(bytes(msg[4:],"utf8"), "~ "+nome+": ")
    except:
        pass

def start_button():
    '''funzione per avviare il gioco e con esso il tempo'''
    if client_counter.get() == 0 or almeno_un_nome.get() == False:
        return
    btnStart['state']=tk.DISABLED
    gioco_iniziato.set(True)
    #introduzione del gioco
    broadcast(bytes("~ MASTER: Benvenuti nel Sottomondo avventurieri!","utf8"))
    sleep(2)
    broadcast(bytes("~ MASTER: Il vostro scopo è sopravvivere a una serie di situazioni fantastiche","utf8"))
    sleep(2)
    broadcast(bytes("~ MASTER: Per ogni situazione superata vi verrà posta una domanda.","utf8"))
    sleep(2)
    broadcast(bytes("~ MASTER: Se risponderete correttamente guadagnerete un punto.","utf8"))
    sleep(2)
    broadcast(bytes("~ MASTER: Se sbaglierete invece perderete un punto.","utf8"))
    sleep(2)
    broadcast(bytes("~ MASTER: Alla fine della partita chi ha più punti vince!","utf8"))
    sleep(2)
    broadcast(bytes("~ MASTER: Ogni partita dura 100 secondi.","utf8"))
    sleep(3)
    broadcast(bytes("~ ~ MASTER: Buon Gioco!!","utf8"))
    broadcast(bytes("~ "+matrice_situa[0][0],"utf8"))
    sleep(1)
    broadcast(bytes("_ "+matrice_situa[0][1].replace("\n", "@")+matrice_situa[0][2].replace("\n", "@")+matrice_situa[0][3].replace("\n", "@")+matrice_situa[0][4],"utf8"))
    time_start()

def time_start():
    '''funzione per avviare il thread che gestisce il tempo'''
    threading._start_new_thread(time_stop,())

def time_stop():
    '''funzione per fermare il tempo alla fine del gioco o all'uscita di tutti i giocatori
    con aggiornamento della grafica'''
    global game_timer, label_counter
    try:
        while(game_timer>0):
            game_timer -= 1
            label_counter.config(text="{}".format(game_timer+1))
            sleep(1)
            if (game_timer % 20 == 0):
                broadcast(bytes("~ MASTER: Mancano ancora "+str(game_timer)+" secondi!","utf8"))
        label_counter.config(text="The End!")
        broadcast(bytes("~ ~ MASTER: FINE DEL GIOCO!","utf8"))
    except:
        pass
#variabili nel main
game_timer=100

def get_ip():
    """estrae l'ip per mostrarlo a video """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


#grafica
window=tk.Tk()
window.title("Server")
window.geometry("400x500")
window.config(bg="slateBlue")
window.resizable(False,False)

gioco_iniziato = tk.BooleanVar(False)
almeno_un_nome = tk.BooleanVar(False)
client_counter = tk.IntVar(0)

btnStart = tk.Button(window, bg="#1e9856", text="START", font=("Elephant",30,"bold"), command=lambda : start_button())
btnStart.place(x=50, y=270, width=300, height=80)

label_counter = tk.Label(window, text="",font=("forte",55,"bold"), bg="medium slate blue", relief="sunken")
label_counter.place(x=20, y=20, width=360, height=200)

label_ip = tk.Label(window, text="Indirizzo IP:",font=("Perpetua",25,"bold"), bg="medium slate blue", relief="groove")
label_ip.place(x=50, y=360, width=300, height=50)
label_ip = tk.Label(window, text=str(get_ip()),font=("Perpetua",30,"bold"), bg="medium slate blue", relief="groove")
label_ip.place(x=50, y=420, width=300, height=70)



#creazione del dizionario con le domande ottenute da un file
domande={}
d=open("domande.txt","r")
while True:
    line=d.readline()
    if (len(line)==0):
        break
    line=line.replace("\n","")
    risp=d.readline().replace("\n", "")
    domande[line]=risp
d.close()

#creazione di una matrice con le varie situazioni
situazioni=open("situazioni.txt","r")
tutto=situazioni.readlines()
matrice_situa=[]
for k in range(len(tutto)//6):
    temp=[]
    for j in range(6):
        temp.append(tutto.pop(0))
    matrice_situa.append(temp)
situazioni.close()

#gestione della connessione
server = None
HOST_ADDR =""
HOST_PORT = 53000
BUFSIZ = 1024
clients = {}
indirizzi = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST_ADDR, HOST_PORT))

server.listen(10)
threading._start_new_thread(accept_clients, (server, " "))
window.mainloop() 
server.close()

