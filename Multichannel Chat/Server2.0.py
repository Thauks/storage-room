from socket import *
import sys
from threading import *
import thread

print "Welcome to the Multichannel chat server."
#declaracio de les tres llistes que fan possible
#mantenir clients canals i una relacio de clients
#sockets i adreces.

clients = []
ass = []
channels = []

#Son funcions simples per a
#tal de que la funcio client
#no quedi molt carregada


def joinornc(s):
    option = 0
    if len(s) > 3 and s[0] == 'n' and s[1] == 'c' and s[2] == ' ':
        option = 1
        rep = list(s)
        rep.remove('n')
        rep.remove('c')
        rep.remove(' ')
        if rep:
            s = "".join(rep)
    if len(s) > 5 and s[0] == 'j' and s[1] == 'o' and s[2] == 'i' and s[3] == 'n' and s[4] == ' ':
        option = 2
        rep = list(s)
        rep.remove('j')
        rep.remove('o')
        rep.remove('i')
        rep.remove('n')
        rep.remove(' ')
        if rep:
            s = "".join(rep)
    return option, s


def chanel(s):
    if not channels:
        return False
    for channel in channels:
        temp = str.split(s)
        paraula = ""
        if channel[0] == temp[0]:
            paraula = temp[0]
            break
    print channel[0], paraula
    if channel[0] == paraula:
        return True
    else:
        return False


def kill(sock, adr):
    for x in ass:
        if x[1] == adr:
            for i in channels:
                if i.count(x[0]) != 0:
                    i.remove(x[0])
            clients.remove(x[0])
            ass.remove(x)

#Part troncal del codi, es la
#realment te un pes important.
#Cada vegada que es connecta un client
#s'inicia un nou thread d'aquesta part
#de codi


def client(clientsocket, clientaddr):
    global nik
    cont = 0
    if cont == 0:
        clientNick = clientsocket.recv(512)
        element = clientNick, clientaddr, clientsocket
        ass.append(element)
        clients.append(clientNick)
        cont += 1
    print "Online clients: ", clients
    print "Avaliable channels:", channels
    for i in ass:
        if clientaddr == i[1]:
            nik = i[0]
    print "Accepted connection from: ", clientaddr, "Alias: ", clientNick
    while True:
        recibido = clientsocket.recv(1024)
        if recibido[0] == "/":
            recibido = recibido.replace('/', '')
            if recibido == "fc":
                kill(clientsocket, clientaddr)
                clientsocket.sendto("/fc", clientaddr)
                break
            a = chanel(recibido)
            if a:
                for i in channels:
                    prov = str.split(recibido)
                    if i[0] == prov[0]:
                        can = prov[0]
                        prov.remove(prov[0])
                        recibido = ' '.join(prov)
                        thread.start_new_thread(enviarc, (clientsocket, recibido, can))
            if joinornc(recibido) != (0, recibido):
                option = joinornc(recibido)
                for x in ass:
                    if x[2] == clientsocket:
                        member = x[0]
                if option[0] == 1:
                    recibido = option[1]
                    channel = [recibido, member]
                    if not channels:
                        channels.append(channel)
                    else:
                        # aqui aniria el control de varis canals amb el mateix nom
                        channels.append(channel)
                if option[0] == 2:
                    recibido = option[1]
                    for c in channels:
                        if c[0] == recibido:
                            c.append(member)
        elif recibido == "!channels":
            canals = []
            for i in channels:
                canals.append(i[0])
            trans = ', '.join(canals)
            enviar(clientsocket, trans, clientsocket, "SERVER MSG")
        elif recibido == "!users":
            trans = ', '.join(clients)
            enviar(clientsocket, trans, clientsocket, "SERVER MSG")
        else:
            for x in ass:
                bol = x[2] == clientsocket
                if not bol:
                    enviar(x[2], recibido, clientsocket, "General")

#Com propiament indica es la funcio usada
#per enviar


def enviar(cs, msg, cs2, channel):
    if channel == "SERVER MSG":
        tot = [channel, " >>> ", msg]
        cs.send(''.join(tot))
    else:
        for i in ass:
            if cs2 == i[2]:
                _nick = i[0]
        tot = [channel, " >>> ", _nick, ': ', msg]
        cs.send(''.join(tot))

#subfuncio d'enviar que usa enviar pero
#quan aquest necessita enviar a un canal
#per als usuaris d'aquests


def enviarc(cs, msg, channel):
    print channel
    for i in channels:
        if channel == i[0]:
            channel = i[0]
    for t in ass:
        if cs == t[2]:
            _nick = t[0]
    extra = []
    for x in channels:
        if x[0] == channel:
            for i in range(len(x)):
                if i > 0 and extra != _nick:
                    extra.append(x[i])
        print extra
    for elem in extra:
        for assi in ass:
            if elem == assi[0]:
                thread.start_new_thread(enviar, (assi[2], msg, cs, channel))

#parametres de definicio del servidor
sp = 9999

s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 9999))

s.listen(100)

#part de codi que accepta les connexions i inicia threads

while True:
    sc, addr = s.accept()
    thread.start_new_thread(client, (sc, addr))

print "Thank you for using our service."

sc.close()
s.close()