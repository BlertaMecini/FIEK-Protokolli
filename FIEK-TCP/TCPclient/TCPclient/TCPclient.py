#-------------------SOCKET PROGRAMMING-------------------
#Krijimi i klient aplikacionit 

import socket     #Importojme librarine per socket komunikim ne mes te klientit dhe serverit 
import sys        #Importojme librarine sys
import time       #Importojme librarine time

serverName = '127.0.0.1'    #IP
serverPort = 14000          #Porti 
address=(serverName,serverPort)     #Adresa eshte qift i hostit dhe portit 

#Krijimi i soketit. Argumentet e pasuara në socket () specifikojne familjen e adresave dhe llojin e soketit
#AF_INET eshte familja e adresave per IPv4. SOCK_STREAM eshte lloji i soketit per TCP protokollin
try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
except socket.error as err:  #Nese ndodh gabim, shfaqet gabimi dhe mbyllet sistemi
    print("Soketi nuk ka mundur te krijohet!") 
    print(str(err))
    time.sleep(1)
    sys.exit()

#Kerkojme nga klienti te jep pergjigjie nese deshiron apo jo ta ndrorroj adresen e serverit
print("-------Mire se erdhet ne FIEK Protokollin!-------\n\nAdresa e serverit eshte:"+str(serverName)+", "+str(serverPort))
answer=input("\nDeshironi ta nderroni adresen e serverit? Shtyp PO ose JO: ")

if answer=="PO":
        serverName=str(input("\nIP? "))   #IP
        serverPort=int(input("\nPORTI? "))    #Porti 

elif answer=="JO":
        serverName = '127.0.0.1'    #IP
        serverPort = 14000          #Porti 
else:
       print("\nNuk keni shtypur as PO as JO,prandaj po vazhdojme me vlera default! ")
       time.sleep(1)
       serverName = '127.0.0.1'    #IP
       serverPort = 14000          #Porti

address=(serverName,serverPort)     #Adresa eshte qift i hostit dhe portit 

try:
    clientSocket.connect(address)       #Klienti tenton te lidhet me serverin permes metodes connect(), ku si parameter e merr adresen(hosti,porti)
      
except socket.error as err:             #Nese ndodh gabim gjate lidhjes me serverin, shfaqet gabimi dhe sistemi behet exit
     print("\nKa ndodhur nje gabim gjate lidhjes me serverin!\n")   
     print(str(err))
     time.sleep(2)
     sys.exit()   
line="--------------------------------------------------------------------------------"
print("\nJeni lidhur me serverin, mund të zgjedhni njerin nga operacionet e meposhtme!\n\n"
      +"Operacionet:\n\n"+line 
      +"1.IP - per ta zgjedhur shtypni IP\n"+line
      +"2.NRPORTIT - per ta zgjedhur shtypni NRPORTIT\n"+line
      +"3.NUMERO- per ta zgjedhur shtypni NUMERO{Hapesire}Teksi Juaj\n"+line
      +"4.ANASJELLTAS- per ta zgjedhur shtypni ANASJELLTAS{Hapesire}Teksi Juaj\n"+line
      +"5.PALINDROM - per ta zgjedhur shtypni PALINDROM{Hapesire}Teksi Juaj\n"+line
      +"6.KOHA - per ta zgjedhur shtypni KOHA\n"+line
      +"7.LOJA - per ta zgjedhur shtypni LOJA\n"+line
      +"8.GCF - per ta zgjedhur shtypni GCF{Hapesire}Numri1{Hapesire}Numri2\n"+line
      +"9.KONVERTO - per ta zgjedhur shtypni {Hapesire}{Modi}{Hapesire}{Numri}\n"+line
      +"10.THENJA - per ta zgjedhur shtypni THENJA\n"+line
      +"11.FIBONACCI - per ta zgjedhur shtypni FIBONACCI{Hapesire}Numri i termave\n"+line
      +"Shtypni PERFUNDO ose vetem tastin ENTER per ta mbyllur programin.\n"+line)

message=" "
while True:    #Unaze e pafundme
    request = input("Kerkesa juaj? ")   #Kerkojme nga klienti te shkruaj kerkesen 

    try:  #Tentojme te dergojme kerkesen tek serveri permes sendall, ku kerkesa duhet te enkodohet (default ne formatin utf-8)
        clientSocket.sendall(str.encode(request))
    except socket.error as err:         #Nese ndodh gabim, shfaqet gabimi dhe mbyllet soketi
        print("Ka ndodhur nje gabim gjate dergimit te kerkeses ne server!\n")
        print(str(err))
        break 

    if not request:                     #Nese klienti nuk jep ndonje kerkese por vetem shtyp enter, soketi mbyllet 
        print("\nNuk keni dhene asnje kerkese prandaj programi po mbyllet...\n")
        time.sleep(1)
        break

    try:  # Tentojme ta marrim pergjigjien nga serveri permes recv   
        receivedResponse=clientSocket.recv(1024)  
    except socket.error as err:        #Nese ndodh gabim, shfaqet gabimi dhe mbyllet soketi
        print("Ka ndodhur nje gabim gjate pranimit te pergjigjies nga serveri!\n")
        print(str(err))
        break 
    
    if len(receivedResponse) <= 0:       
        break
    message=receivedResponse.decode('utf-8')   #Dekodimi i pergjigjies se serverit 
    print("\nPërgjigjia nga serveri --> ",str(message) ,"\n")     #Paraqitja ne ekran e pergjigjies se serverit
    print("-------------------------------------------------------------------------------")
    
clientSocket.close()    #Mbyllja e soketit permes close