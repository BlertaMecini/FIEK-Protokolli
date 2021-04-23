#-------------------SOCKET PROGRAMMING-------------------
#Krijimi i klient aplikacionit 

import socket     #Importojme librarine per socket komunikim ne mes te klientit dhe serverit 
import sys 
import time 

serverName = '127.0.0.1'    #IP
serverPort = 14000          #Porti 
address=(serverName,serverPort)     #Adresa eshte qift i hostit dhe portit 

print("\n------------Mirë se erdhët në FIEK-TCP protokollin------------\n\nAdresa e juaj default është: "+str(address)+"\n")
welcomeMessage = input("1.Shtypni PO për të vazhduar në adresën default\n2.Shtypni JO për të ndërruar adresën\n"
 +"3.Shtypni PERFUNDO për të mbyllur programin\n\n")

 
if welcomeMessage == "P0":
    serverName = '127.0.0.1'    #IP
    serverPort = 14000   
elif welcomeMessage =="J0":
    serverName = str(input('Shkruai IP adresën e re: '))
    serverPort = int(input('Shkruani portin e ri: '))
    address=(serverName,serverPort)     #Adresa eshte qift i hostit dhe portit
elif welcomeMessage == "PERFUNDO":
    print("\nPo mbyllet programi...")
    time.sleep(3)
    sys.exit()  

#Krijimi i soketit. Argumentet e pasuara në socket () specifikojnë familjen e adresave dhe llojin e soketit
#AF_INET është familja e adresave për IPv4. SOCK_STREAM është lloji i soketit për TCP protokollin
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
try:
    clientSocket.connect(address)       #Klienti lidhet me serverin permes metodes connect(), ku si parametra e merr adresen(hosti,porti)
   
except socket.error as err: 
     print("\nKa ndodhur një gabim gjatë lidhjës me serverin!\n")   
     print(str(err))
     time.sleep(3)
     sys.exit()   
    
print("\nJeni lidhur me serverin, mund të zgjedhni njërin nga operacionet e mëposhtme!"
+"\n\nOperacioni (IP,NRPORTIT,NUMERO,ANASJELLTAS,PALINDROM,KOHA,LOJA,GCF,KONVERTO)\n")
print("Shtyp PERFUNDO për ta mbyllur programin.\n")
print("-------------------------------------------------------------------------------")

message=" "
while True: #Unaze e pafundme
    request = input("\nKerkesa juaj? ")
    #dergojme kerkesen tek serveri permes sendall, ku kerkesa duhet te enkodohet (default ne formatin utf-8)
    try:  
        clientSocket.sendall(str.encode(request))
        if request=="PALINDROM" or request=="ANASJELLTAS" or request=="NUMERO":
            request=input("Teksti? ")
            clientSocket.sendall(str.encode(request))
        if request=="GCF":
            request=input("Shkruani dy numra (p.sh.: numri1 numri2): ")
            clientSocket.sendall(str.encode(request))
        if request=="KONVERTO":
            print("\nModet e konvertimit:\n"+
            "1.Për konvertimin cm në inch shtypni cmNeInch\n"+
            "2.Për konvertimin inch në cm shtypni inchNeCm\n"+
            "3.Për konvertimin km në milje shtypni kmNeMiles\n"
            "4.Për konvertimin milje në km shtypni mileNeKm\n")
            request=input("Shtypni modin e konvertimit dhe numrin qe deshironi ta konvertoni\n"+
                          "{Modi}{Hapesirë}{Numri}? ")
            clientSocket.sendall(str.encode(request))
        receivedResponse=clientSocket.recv(1024)
        
    except socket.error as err:
     
        print("Ka ndodhur një gabim gjatë pranimit të përgjigjies së serverit!\n")
        print(str(err))
        break 
    if len(receivedResponse) <= 0:
        break
    message=receivedResponse.decode('utf-8')
    print("\nPërgjigjia nga serveri --> ",message ,"\n")   
    print("-------------------------------------------------------------------------------")
    
clientSocket.close()