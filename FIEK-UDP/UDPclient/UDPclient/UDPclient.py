#-------------------SOCKET PROGRAMMING-------------------
#Krijimi i klient aplikacionit 

import socket     #Importojme librarine per socket komunikim ne mes te klientit dhe serverit 
import sys        #Importojme librarine sys
import time       #Importojme librarine time

serverName = '127.0.0.1'    #IP
serverPort = 14000          #Porti 

#Krijimi i soketit. Argumentet e pasuara ne socket () specifikojne familjen e adresave dhe llojin e soketit
#AF_INET eshte familja e adresave per IPv4. SOCK_DGRAM eshte lloji i soketit per UDP protokollin
try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
except socket.error as err:  #Nese ndodh gabim, shfaqet gabimi dhe mbyllet sistemi
    print("Soketi nuk ka mundur te krijohet!") 
    print(str(err))
    time.sleep(1)
    sys.exit()

#Kerkojme nga klienti te jep pergjigjie nese deshiron apo jo ta ndrorroj adresen e serverit
print("-------Mire se erdhet ne FIEK Protokollin!-------\n\nAdresa e serverit eshte: "+str(serverName)+", "+str(serverPort))
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

serverAddress=(serverName,serverPort)     #Adresa eshte qift i hostit dhe portit 

line="--------------------------------------------------------------------------------"
print("\nJeni lidhur me serverin, mund te zgjedhni njerin nga operacionet e meposhtme!\n\n"
      +"Operacionet:\n\n"+line 
      +"1.IP - per ta zgjedhur shtypni IP\n"+line
      +"2.NRPORTIT - per ta zgjedhur shtypni NRPORTIT\n"+line
      +"3.NUMERO- per ta zgjedhur shtypni NUMERO{Hapesire}Teksi Juaj\n"+line
      +"4.ANASJELLTAS- per ta zgjedhur shtypni ANASJELLTAS{Hapesire}Teksi Juaj\n"+line
      +"5.PALINDROM - per ta zgjedhur shtypni PALINDROM{Hapesire}Teksi Juaj\n"+line
      +"6.KOHA - per ta zgjedhur shtypni KOHA\n"+line
      +"7.LOJA - per ta zgjedhur shtypni LOJA\n"+line
      +"8.GCF - per ta zgjedhur shtypni GCF{Hapesire}Numri1{Hapesire}Numri2\n"+line
      +"9.KONVERTO - per ta zgjedhur shtypni KONVERTO{Hapesire}{Modi}{Hapesire}{Numri}\n"+line
      +"10.THENJA - per ta zgjedhur shtypni THENJA\n"+line
      +"11.FIBONACCI - per ta zgjedhur shtypni FIBONACCI{Hapesire}Numri i termave\n"+line
      +"Shtypni vetem tastin ENTER per ta mbyllur programin.\n"+line)

connected=True
while connected:
    request = input("Kerkesa juaj? ")   #Kerkojme nga klienti te shkruaj kerkesen 

    if not request:        #Nese klienti nuk jep ndonje kerkese por vetem shtyp enter, programi mbyllet 
        print("\nNuk keni dhene asnje kerkese prandaj programi po mbyllet...\n")
        break
    
    try:  #Tentojme te dergojme kerkesen tek serveri permes sendto, ku kerkesa duhet te enkodohet (default ne formatin utf-8) dhe duhet te shkruhet adresa ku do ta dergojme
        clientSocket.sendto(str.encode(request),serverAddress)
    except socket.error as err:         #Nese ndodh gabim, shfaqet gabimi
        print("Ka ndodhur nje gabim gjate dergimit te kerkeses ne server!\n")
        print(str(err))
        break

    try:          #Tentojme ta marrim pergjigjien nga serveri permes recvfrom   
        receivedResponse,server=clientSocket.recvfrom(1024) 
        message=receivedResponse.decode('utf-8')    #Dekodimi i pergjigjies se serverit 
    except socket.error as err:        #Nese ndodh gabim, shfaqet gabimi 
        print("Ka ndodhur nje gabim gjate pranimit te pergjigjies nga serveri!\n")
        print(str(err))
        break
 
    print("\nPergjigjia nga serveri --> ",str(message) ,"\n")     #Paraqitja ne ekran e pergjigjies se serverit
    print("-------------------------------------------------------------------------------")
    connected==False
    break

clientSocket.close()    #Mbyllja e soketit permes close