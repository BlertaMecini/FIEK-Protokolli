#-------------------SOCKET PROGRAMMING-------------------
#Krijimi i server aplikacionit 
import socket     #Importojme librarine per socket komunikim ne mes te klientit dhe serverit 
import threading  #Importojme librarine per thread-a
import random     #Importojme librarine per marrjen e vlerave te rastesishme 
import math       #Importojme librarine per funksione matematikore 
import re         #Importojme librarine per regular expression (shprehje te rregullta)
from datetime import datetime  #Klasa datetime per daten dhe kohen 

serverName = '127.0.0.1' #IP 
serverPort = 14000       #Porti
address=(serverName,serverPort)  #Adresa eshte qift i hostit dhe portit 

#Krijimi i soketit. Argumentet e pasuara në socket () specifikojnë familjen e adresave dhe llojin e soketit
#AF_INET është familja e adresave për IPv4. SOCK_STREAM është lloji i soketit për TCP protokollin
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: #Serveri tenton te lidhet me klientin permes metodes bind(), ku si parameter e merr adresen(hosti,porti)
    serverSocket.bind(address)
    print("\nServeri eshte startuar ne localhost ne portin " + str(serverPort)+".")
    serverSocket.listen(50)           #Presim per kerkesa permes listen(), 50 paraqet nr e kerkesave qe mund te rrijne ne rend (queue)
    print("\nServeri eshte duke punuar dhe eshte duke pritur per ndonje kerkese!")

except socket.error as err: #Nese ndodh gabim gjate lidhjes, shfaqet gabimi
    print(str(err))

def handle_connections(clientS,addr): #Metod per trajtimin e kerkesave te klientit
    
    def IP(): #Metoda IP kthen IP adresen e klientit
        return "IP adresa e klientit eshte: "+str(addr[0])

    def NRPORTIT(): #Metoda NRPORTIT kthen portin e klientit
        return "Klienti eshte duke perdorur portin: "+str(addr[1])

    def ANASJELLTAS(x): #Metoda ANASJELLTAS tekstin e dhene e kthen anasjelltas (reverse)
        return "Teksti i kthyer anasjelltas: "+ x[::-1] 
        
    def PALINDROM(text): #Metoda PALINDROM tregon nese teksti shkruhet njejt ne te dyja anet, eshte palindrom
        text = re.sub(r"[^a-zA-Z]","",text)
        reversedText=text[::-1] 
        if  reversedText==text: 
            return "Teksti i dhene eshte palindrom."
        else: 
            return "Teksti i dhene nuk eshte palindrom."

    def LOJA(): #Metoda LOJA kthen 5 numra te rastesishem dhe te sortuar nga 1-35
        listOfNumbers = []
        for number in range(0,5):
            number = random.randint(1,35)
            listOfNumbers.append(number) 
            listOfNumbers.sort()
        return "5 numra te plote dhe te sortuar, nga rangu 1-35:\n"+str(listOfNumbers)

    def KOHA(): #Metoda KOHA kthen daten dhe kohen aktuale te serverit 
        currDateTime=datetime.now()
        currDateTimeFormat=currDateTime.strftime("%d/%m/%Y, %H:%M:%S")
        return "Data dhe koha aktuale: "+currDateTimeFormat
    
    def NUMERO(text): #Metoda NUMERO kthen nr e zanoreve dhe bashketingelloreve te teksit te dhene 
        text = re.sub(r'[^a-zA-Z]','',text)
        vowel=0
        constant=0
        for i in text: 
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="y"or  i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=="Y":
                vowel+=1      
            else: 
                constant+=1
        return "Teksti i dhene ka "+ str(vowel)+ " zanore dhe "+str(constant)+" bashketingellore"
    
    def GCF(num1,num2): #Metoda GCF kthen faktorin me te madh te perbashket te dy numrave 
        gcdResult=math.gcd(num1,num2)
        return "Faktori me i madh i perbashket i dy numrave te dhene eshte: "+str(gcdResult)

    def KONVERTO(mode,number): #Metoda KONVERTO eshte nje lloj kalkulatori per disa konvertime 
        converted=0
        if mode=="cmNeInch":  
            converted=number/2.54
            return "Numri "+str(number)+" cm, i konvertuar ne inch= "+str(round(converted, 3)) 
        elif mode=="inchNeCm":  
            converted=number*2.54
            return "Numri "+str(number)+" inch, i konvertuar ne cm= "+str(round(converted, 3))
        elif mode=="kmNeMiles":  
            converted=number*0.621371
            return "Numri "+str(number)+" km, i konvertuar ne milje= "+str(round(converted, 3))
        elif mode=="mileNeKm":  
            converted=number/0.621371
            return "Numri "+str(number)+" milje, i konvertuar ne km= "+str(round(converted, 3))
        else:
            return "Ky konvertim nuk ekziston!"

    def THENJA():  #Metoda THENJA kthen nje thenje te rastesishme nga nje varg i thenjeve
        quoteArray=["It's not the hours you put in your work that counts, it's the work you put in the hours."
                    ,"No one would have crossed the ocean if he could have gotten off the ship in the storm."
                    ,"Better to get hurt by the truth than comforted with a lie."
                    ,"There is only one sin. and that is theft... when you tell a lie, you steal someones right to the truth."
                    ,"It always hurts more to have and lose than to not have in the first place."
                    ,"A society has no chance of success if its women are uneducated..."
                    ,"People say that eyes are windows to the soul."
                    ,"They say, Find a purpose in your life and live it. But, sometimes, it is only after you have lived that you recognize your life had a purpose, and likely one you never had in mind."
                    ,"A fool thinks himself to be wise, but a wise man knows himself to be a fool."
                    ,"If music be the food of love, play on."
                    ,"I raise up my voice—not so that I can shout, but so that those without a voice can be heard. … We cannot all succeed when half of us are held back."
                    ,"Feminism isn't about making women stronger. Women are already strong, it's about changing the way the world perceives that strength."
                    ,"Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
                    ,"You only live once, but if you do it right, once is enough."]
        return "Nje thenje e rastesishme: "+random.choice(quoteArray)

    def FIBONACCI(n): #Metoda FIBONACCI kthen sekuencen fibonacci per nr e termave te dhene 
        def fibRecursion(n):
            if n==0 or n==1:
                return n 
            else:
                return (fibRecursion(n-1)+fibRecursion(n-2))  
        
        if n<='0':
            return ("Keni dhene numer negativ ose 0 prandaj nuk mund te gjenerohet sekuenca Fibonacci!")
        elif n.isnumeric()==False:
            return ("Nuk kemi dhene numer valid, prandaj nuk mund te gjenerohet sekuenca Fibonacci!")
          
        i=0
        result=""
        while i<n:
            result+= (" "+str(fibRecursion(i)))
            i+=1
        return "Sekuenca Fibonacci: "+ result
       
    while True:  #Unaze e pafundme. Perderisa serveri eshte duke degjuar tentojme te marrim kerkesat e klientit dhe thirrim metodat perkatese
        try:
            request = clientS.recv(128)
        except socket.error as err:
            print(str(err))
            break
            
        request=str(request.decode('utf-8'))
        if len(request)<=0:
            break
        print("Kerkesa nga klienti: "+ request+"\n") 
            
        response = ''
        if request== 'KOHA':
            response = str(KOHA())

        elif request == 'IP':
            response= str(IP())

        elif request == 'NRPORTIT':
            response= str(NRPORTIT())

        elif request=='PALINDROM':
            response="Nuk keni dhene asnje tekst!"
        elif request.split(" ",1)[0] == 'PALINDROM':
            txt=request.split(" ",1)[1]
            response=str(PALINDROM(txt))

        elif request == 'LOJA':
            response= str(LOJA())
        
        elif request=='ANASJELLTAS':
            response="Nuk keni dhene asnje tekst!"
        elif request.split(" ",1)[0] == 'ANASJELLTAS':
            txt=request.split(" ",1)[1]
            print(txt)
            response=str(ANASJELLTAS(txt))

        elif request == 'GCF':
            response="Duhet te jepni 2 numra!"
        elif request.split(" ")[0] == 'GCF':      
            num1=int(request.split(' ')[1])
            num2=int(request.split(' ')[2])
            response= str(GCF(num1,num2))

        elif request == 'NUMERO':
            response="Nuk keni dhene asnje tekst!"
        elif request.split(" ",1)[0] == 'NUMERO':
            response=str(NUMERO(request.split(" ",1)[1]))

        elif request == 'KONVERTO':
            response=("\nModet e konvertimit:\n"+
                "1.Për konvertimin cm në inch shtypni cmNeInch\n"+
                "2.Për konvertimin inch në cm shtypni inchNeCm\n"+
                "3.Për konvertimin km në milje shtypni kmNeMiles\n"+
                "4.Për konvertimin milje në km shtypni mileNeKm\n\n"+
                "Shtypni modin e konvertimit dhe numrin qe deshironi ta konvertoni si: "+
                "KONVERTO{Hapesire}{Modi}{Hapesire}{Numri}")
            
        elif request.split(' ')[0] == 'KONVERTO':
            mode=str(request.split(' ')[1])
            number=int(request.split(' ')[2])
            response= str(KONVERTO(mode,number))
       
        elif request == 'THENJA':
            response= str(THENJA())

        elif request== 'FIBONACCI':
            response="Duhet te jepni numrin e termave te serise"
        elif request.split(' ')[0] == 'FIBONACCI':
            n=request.split(' ')[1]
            response= str(FIBONACCI(n))

        elif request == 'PERFUNDO':
            print("Lidhja me klientin "+ str(addr)+" eshte shkeputur!\n")
            break

        else: 
            response ="Kjo eshte nje kerkese jo valide!"
        
        print('Pergjigjja nga serveri --> '+str(response)+"\n")
        clientS.sendall(str.encode(response))
        
    clientS.close()
       
  #Krijimi i threadit 
while True:  
    try:
        clientS, addr = serverSocket.accept()
        print("\n--------------------------------------------------------------------------------")
        print("Serveri eshte lidhur me klientin: "+str(addr))
        newThread=threading.Thread(target=handle_connections,args=(clientS,addr))
        newThread.start()
        print("Numri i klienteve aktiv: " + str(threading.activeCount() - 1))
        print("\n--------------------------------------------------------------------------------")
    except socket.error as err: 
        print(str(err))

serverSocket.close()  #Mbyllja e soket serverit 

S