import socket
import threading 
import random
import math 
import re
from datetime import datetime


serverName = '127.0.0.1'
serverPort = 14000
address=(serverName,serverPort)

try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(address)
    print("\nServeri �sht� startuar n� localhost n� portin " + str(serverPort)+".")
    serverSocket.listen(50) 
    print("\nServeri �sht� duke punuar dhe �sht� duke pritur p�r ndonj� k�rkes�!")

except socket.error as err: 
    print(str(err))

def handle_connections(clientS,addr): 
    
    def IP(): 
        return "IP adresa e klientit �sht�: "+str(addr[0])

    def NRPORTIT(): 
        return "Klienti �sht� duke p�rdorur portin: "+str(addr[1])

    def ANASJELLTAS(x):
        return "Teksti i kthyer anasjelltas: "+ x[::-1] 

    def PALINDROM(text):
        reversedText=ANASJELLTAS(text)
        if  reversedText==text: 
            return "Teksti i dh�n� �sht� palindrom."
        else: 
            return "Teksti i dh�n� nuk �sht� palindrom."

    def LOJA():
        listOfNumbers = []
        for number in range(0,5):
            number = random.randint(1,35)
            listOfNumbers.append(number) 
            listOfNumbers.sort()
        return "5 numra t� plot� dhe t� sortuar, nga rangu 1-35:\n"+str(listOfNumbers)

    def KOHA():
        currDateTime=datetime.now()
        currDateTimeFormat=currDateTime.strftime("%d/%m/%Y, %H:%M:%S")
        return "Data dhe koha aktuale: "+currdatetimeFormat
    
    def NUMERO(text):
        text = re.sub(r"[^a-zA-Z��]"," ",text)
        vowel=0
        constant=0
        for i in text: 
            if i=="a" or i=="e" or i=="�" or i=="i" or i=="o" or i=="u" or i=="y"or  i=="A" or i=="E"  or i=="�" or i=="I" or i=="O" or i=="U" or i=="Y":
                vowel+=1      
            else: 
                constant+=1
        return "Teksti i dh�n� ka "+ str(vowel)+ " zanore dhe "+str(constant)+" bashk�ting�llore"
    
    def GCF(num1,num2):
        gcdResult=math.gcd(num1,num2)
        return "Faktori m� i madh� i p�rbashk�t i dy numrave t� dh�n� �sht�: "+str(gcdResult)

    def KONVERTO(mode,number):
        converted=0
        if mode=="cmNeInch":  
            converted=number/2.54
            return "Numri "+str(number)+" cm, i konvertuar n� inch= "+str(round(converted, 3)) 
        elif mode=="inchNeCm":  
            converted=number*2.54
            return "Numri "+str(number)+" inch, i konvertuar n� cm= "+str(round(converted, 3))
        elif mode=="kmNeMiles":  
            converted=number*0.621371
            return "Numri "+str(number)+" km, i konvertuar n� milje= "+str(round(converted, 3))
        elif mode=="mileNeKm":  
            converted=number/0.621371
            return "Numri "+str(number)+" milje, i konvertuar n� km= "+str(round(converted, 3))
        else:
            return "Ky konvertim nuk ekziston!"

    while True:
        try:
            request = clientS.recv(1024)
            print("K�rkesa nga klienti: "+ str(request.decode('utf-8'))+"\n") 
            if len(request)<=0:
                break
            response = ''
            if str(request.decode('utf-8')) == 'KOHA':
                response = str(KOHA())

            elif str(request.decode('utf-8')) == 'IP':
                response= str(IP())

            elif str(request.decode('utf-8')) == 'NRPORTIT':
                response= str(NRPORTIT())

            elif str(request.decode('utf-8')) == 'PALINDROM':
                request = clientS.recv(1024)
                response=str(PALINDROM(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'LOJA':
                response= str(LOJA())

            elif str(request.decode('utf-8')) == 'ANASJELLTAS':
                request = clientS.recv(1024)
                response=str(ANASJELLTAS(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'GCF':
                request = clientS.recv(1024).decode('utf-8')
                num1=int(request.split(' ')[0])
                num2=int(request.split(' ')[1])
                response= str(GCF(num1,num2))

            elif str(request.decode('utf-8')) == 'NUMERO':
                request = clientS.recv(1024)
                response=str(NUMERO(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'KONVERTO':
                request = clientS.recv(1024).decode('utf-8')
                mode=str(request.split(' ')[0])
                number=int(request.split(' ')[1])
                response= str(KONVERTO(mode,number))
        
            elif str(request.decode('utf-8')) == 'PERFUNDO':
                print("Lidhja me klientin "+ str(addr)+" �sht� shk�putur!\n")
                break

            else: 
                response ="Kjo �sht� nj� k�rkes� jo valide!"
        
            print('Pergjigjja nga serveri --> '+response+"\n")
            clientS.sendall(str.encode(response))
        
        except socket.error as err: 
            print("Ka ndodhur nj� gabim gjat� pranimit t� k�rkes�s s� klientit\n")
            print(str(err))
            break
        
    clientS.close()
       
  
while True:
    clientS, addr = serverSocket.accept()
    print("\n--------------------------------------------------------------------------------")
    print("Serveri �sht� lidhur me klientin: "+str(addr))
    newThread=threading.Thread(target=handle_connections,args=(clientS,addr))
    newThread.start()
    print("Numri i klient�ve aktiv: " + str(threading.activeCount() - 1))
    print("\n--------------------------------------------------------------------------------")
   
serverSocket.close()

import socket
import threading 
import random
import math 
import re
from datetime import datetime


serverName = '127.0.0.1'
serverPort = 14000
address=(serverName,serverPort)

try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(address)
    print("\nServeri �sht� startuar n� localhost n� portin " + str(serverPort)+".")
    serverSocket.listen(50) 
    print("\nServeri �sht� duke punuar dhe �sht� duke pritur p�r ndonj� k�rkes�!")

except socket.error as err: 
    print(str(err))

def handle_connections(clientS,addr): 
    
    def IP(): 
        return "IP adresa e klientit �sht�: "+str(addr[0])

    def NRPORTIT(): 
        return "Klienti �sht� duke p�rdorur portin: "+str(addr[1])

    def ANASJELLTAS(x):
        return "Teksti i kthyer anasjelltas: "+ x[::-1] 

    def PALINDROM(text):
        reversedText=ANASJELLTAS(text)
        if  reversedText==text: 
            return "Teksti i dh�n� �sht� palindrom."
        else: 
            return "Teksti i dh�n� nuk �sht� palindrom."

    def LOJA():
        listOfNumbers = []
        for number in range(0,5):
            number = random.randint(1,35)
            listOfNumbers.append(number) 
            listOfNumbers.sort()
        return "5 numra t� plot� dhe t� sortuar, nga rangu 1-35:\n"+str(listOfNumbers)

    def KOHA():
        currDateTime=datetime.now()
        currDateTimeFormat=currDateTime.strftime("%d/%m/%Y, %H:%M:%S")
        return "Data dhe koha aktuale: "+currdatetimeFormat
    
    def NUMERO(text):
        text = re.sub(r"[^a-zA-Z��]"," ",text)
        vowel=0
        constant=0
        for i in text: 
            if i=="a" or i=="e" or i=="�" or i=="i" or i=="o" or i=="u" or i=="y"or  i=="A" or i=="E"  or i=="�" or i=="I" or i=="O" or i=="U" or i=="Y":
                vowel+=1      
            else: 
                constant+=1
        return "Teksti i dh�n� ka "+ str(vowel)+ " zanore dhe "+str(constant)+" bashk�ting�llore"
    
    def GCF(num1,num2):
        gcdResult=math.gcd(num1,num2)
        return "Faktori m� i madh� i p�rbashk�t i dy numrave t� dh�n� �sht�: "+str(gcdResult)

    def KONVERTO(mode,number):
        converted=0
        if mode=="cmNeInch":  
            converted=number/2.54
            return "Numri "+str(number)+" cm, i konvertuar n� inch= "+str(round(converted, 3)) 
        elif mode=="inchNeCm":  
            converted=number*2.54
            return "Numri "+str(number)+" inch, i konvertuar n� cm= "+str(round(converted, 3))
        elif mode=="kmNeMiles":  
            converted=number*0.621371
            return "Numri "+str(number)+" km, i konvertuar n� milje= "+str(round(converted, 3))
        elif mode=="mileNeKm":  
            converted=number/0.621371
            return "Numri "+str(number)+" milje, i konvertuar n� km= "+str(round(converted, 3))
        else:
            return "Ky konvertim nuk ekziston!"

    while True:
        try:
            request = clientS.recv(1024)
            print("K�rkesa nga klienti: "+ str(request.decode('utf-8'))+"\n") 
            if len(request)<=0:
                break
            response = ''
            if str(request.decode('utf-8')) == 'KOHA':
                response = str(KOHA())

            elif str(request.decode('utf-8')) == 'IP':
                response= str(IP())

            elif str(request.decode('utf-8')) == 'NRPORTIT':
                response= str(NRPORTIT())

            elif str(request.decode('utf-8')) == 'PALINDROM':
                request = clientS.recv(1024)
                response=str(PALINDROM(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'LOJA':
                response= str(LOJA())

            elif str(request.decode('utf-8')) == 'ANASJELLTAS':
                request = clientS.recv(1024)
                response=str(ANASJELLTAS(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'GCF':
                request = clientS.recv(1024).decode('utf-8')
                num1=int(request.split(' ')[0])
                num2=int(request.split(' ')[1])
                response= str(GCF(num1,num2))

            elif str(request.decode('utf-8')) == 'NUMERO':
                request = clientS.recv(1024)
                response=str(NUMERO(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'KONVERTO':
                request = clientS.recv(1024).decode('utf-8')
                mode=str(request.split(' ')[0])
                number=int(request.split(' ')[1])
                response= str(KONVERTO(mode,number))
        
            elif str(request.decode('utf-8')) == 'PERFUNDO':
                print("Lidhja me klientin "+ str(addr)+" �sht� shk�putur!\n")
                break

            else: 
                response ="Kjo �sht� nj� k�rkes� jo valide!"
        
            print('Pergjigjja nga serveri --> '+response+"\n")
            clientS.sendall(str.encode(response))
        
        except socket.error as err: 
            print("Ka ndodhur nj� gabim gjat� pranimit t� k�rkes�s s� klientit\n")
            print(str(err))
            break
        
    clientS.close()
       
  
while True:
    clientS, addr = serverSocket.accept()
    print("\n--------------------------------------------------------------------------------")
    print("Serveri �sht� lidhur me klientin: "+str(addr))
    newThread=threading.Thread(target=handle_connections,args=(clientS,addr))
    newThread.start()
    print("Numri i klient�ve aktiv: " + str(threading.activeCount() - 1))
    print("\n--------------------------------------------------------------------------------")
   
serverSocket.close()

import socket
import threading 
import random
import math 
import re
from datetime import datetime


serverName = '127.0.0.1'
serverPort = 14000
address=(serverName,serverPort)

try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(address)
    print("\nServeri �sht� startuar n� localhost n� portin " + str(serverPort)+".")
    serverSocket.listen(50) 
    print("\nServeri �sht� duke punuar dhe �sht� duke pritur p�r ndonj� k�rkes�!")

except socket.error as err: 
    print(str(err))

def handle_connections(clientS,addr): 
    
    def IP(): 
        return "IP adresa e klientit �sht�: "+str(addr[0])

    def NRPORTIT(): 
        return "Klienti �sht� duke p�rdorur portin: "+str(addr[1])

    def ANASJELLTAS(x):
        return "Teksti i kthyer anasjelltas: "+ x[::-1] 

    def PALINDROM(text):
        reversedText=ANASJELLTAS(text)
        if  reversedText==text: 
            return "Teksti i dh�n� �sht� palindrom."
        else: 
            return "Teksti i dh�n� nuk �sht� palindrom."

    def LOJA():
        listOfNumbers = []
        for number in range(0,5):
            number = random.randint(1,35)
            listOfNumbers.append(number) 
            listOfNumbers.sort()
        return "5 numra t� plot� dhe t� sortuar, nga rangu 1-35:\n"+str(listOfNumbers)

    def KOHA():
        currDateTime=datetime.now()
        currDateTimeFormat=currDateTime.strftime("%d/%m/%Y, %H:%M:%S")
        return "Data dhe koha aktuale: "+currdatetimeFormat
    
    def NUMERO(text):
        text = re.sub(r"[^a-zA-Z��]"," ",text)
        vowel=0
        constant=0
        for i in text: 
            if i=="a" or i=="e" or i=="�" or i=="i" or i=="o" or i=="u" or i=="y"or  i=="A" or i=="E"  or i=="�" or i=="I" or i=="O" or i=="U" or i=="Y":
                vowel+=1      
            else: 
                constant+=1
        return "Teksti i dh�n� ka "+ str(vowel)+ " zanore dhe "+str(constant)+" bashk�ting�llore"
    
    def GCF(num1,num2):
        gcdResult=math.gcd(num1,num2)
        return "Faktori m� i madh� i p�rbashk�t i dy numrave t� dh�n� �sht�: "+str(gcdResult)

    def KONVERTO(mode,number):
        converted=0
        if mode=="cmNeInch":  
            converted=number/2.54
            return "Numri "+str(number)+" cm, i konvertuar n� inch= "+str(round(converted, 3)) 
        elif mode=="inchNeCm":  
            converted=number*2.54
            return "Numri "+str(number)+" inch, i konvertuar n� cm= "+str(round(converted, 3))
        elif mode=="kmNeMiles":  
            converted=number*0.621371
            return "Numri "+str(number)+" km, i konvertuar n� milje= "+str(round(converted, 3))
        elif mode=="mileNeKm":  
            converted=number/0.621371
            return "Numri "+str(number)+" milje, i konvertuar n� km= "+str(round(converted, 3))
        else:
            return "Ky konvertim nuk ekziston!"

    while True:
        try:
            request = clientS.recv(1024)
            print("K�rkesa nga klienti: "+ str(request.decode('utf-8'))+"\n") 
            if len(request)<=0:
                break
            response = ''
            if str(request.decode('utf-8')) == 'KOHA':
                response = str(KOHA())

            elif str(request.decode('utf-8')) == 'IP':
                response= str(IP())

            elif str(request.decode('utf-8')) == 'NRPORTIT':
                response= str(NRPORTIT())

            elif str(request.decode('utf-8')) == 'PALINDROM':
                request = clientS.recv(1024)
                response=str(PALINDROM(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'LOJA':
                response= str(LOJA())

            elif str(request.decode('utf-8')) == 'ANASJELLTAS':
                request = clientS.recv(1024)
                response=str(ANASJELLTAS(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'GCF':
                request = clientS.recv(1024).decode('utf-8')
                num1=int(request.split(' ')[0])
                num2=int(request.split(' ')[1])
                response= str(GCF(num1,num2))

            elif str(request.decode('utf-8')) == 'NUMERO':
                request = clientS.recv(1024)
                response=str(NUMERO(str(request.decode('utf-8'))))

            elif str(request.decode('utf-8')) == 'KONVERTO':
                request = clientS.recv(1024).decode('utf-8')
                mode=str(request.split(' ')[0])
                number=int(request.split(' ')[1])
                response= str(KONVERTO(mode,number))
        
            elif str(request.decode('utf-8')) == 'PERFUNDO':
                print("Lidhja me klientin "+ str(addr)+" �sht� shk�putur!\n")
                break

            else: 
                response ="Kjo �sht� nj� k�rkes� jo valide!"
        
            print('Pergjigjja nga serveri --> '+response+"\n")
            clientS.sendall(str.encode(response))
        
        except socket.error as err: 
            print("Ka ndodhur nj� gabim gjat� pranimit t� k�rkes�s s� klientit\n")
            print(str(err))
            break
        
    clientS.close()
       
  
while True:
    clientS, addr = serverSocket.accept()
    print("\n--------------------------------------------------------------------------------")
    print("Serveri �sht� lidhur me klientin: "+str(addr))
    newThread=threading.Thread(target=handle_connections,args=(clientS,addr))
    newThread.start()
    print("Numri i klient�ve aktiv: " + str(threading.activeCount() - 1))
    print("\n--------------------------------------------------------------------------------")
   
serverSocket.close()

