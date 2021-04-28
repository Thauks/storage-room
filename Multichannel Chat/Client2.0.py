from socket import *
import sys
from threading import *
import thread
import time

fc = True
nick = ''

serverName = '192.168.1.104'
serverPort = 9999

s = socket(AF_INET, SOCK_STREAM)
s.connect((serverName, 9999))

#funcio usada per enviar


def enviar():
    while True:
        mensaje = raw_input()
        if mensaje != '':
            s.send(mensaje)
        if mensaje == "/fc":
            print 'Attention, you just have closed the connexion with the server.'
            print 'Exiting the client.'
            global fc
            fc = False
            break

#funcio usada per a rebre


def rebre():
    resposta = ''
    while resposta != '/fc':
        resposta = s.recv(1024)
        if (resposta != '') & (resposta != '/fs'):
            print resposta
        time.sleep(0.1)

#funcio que assigna nicknames


def nicknamer():
    global nick
    while nick == '':
        nick = raw_input("Nickname: ")
        if nick == '' or nick[0] == '/':
            print "Not accepted Nickname; try without a starter / or do not send it empty."
            nicknamer()
        s.send(nick)

#main que inicia els threads


def main():
    print "Welcome to the Multichannel chat. Started / or ! nicknames are not going to be accepted."
    while nick == '':
        nicknamer()
    env = Thread(target=enviar)
    env.start()
    thread.start_new_thread(rebre, ())


main()

while fc:
    1 == 1
print 'Have a nice day, Sir/Mme.'

s.close()