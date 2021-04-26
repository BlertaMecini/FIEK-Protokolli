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

#Krijimi i soketit. Argumentet e pasuara ne socket () specifikojne familjen e adresave dhe llojin e soketit
#AF_INET eshte familja e adresave per IPv4. SOCK_DGRAM eshte lloji i soketit per UDP protokollin
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err:  #Nese ndodh gabim, shfaqet gabimi dhe mbyllet sistemi
        print("Soketi nuk ka mundur te krijohet!") 
        print(str(err))
        time.sleep(1)
        sys.exit()

try: #Serveri tenton te lidhet me klientin permes metodes bind(), ku si parameter e merr adresen(hosti,porti)
    serverSocket.bind(address)
    print("\nServeri eshte startuar ne localhost ne portin " + str(serverPort)+".")
    print("\nServeri eshte duke punuar dhe eshte duke pritur per ndonje kerkese!")
except socket.error as err: #Nese ndodh gabim gjate lidhjes, shfaqet gabimi
    print(str(err))
    
def IP(): #Metoda IP kthen IP adresen e klientit
    return "IP adresa e klientit eshte: "+str(addr[0])

def NRPORTIT(): #Metoda NRPORTIT kthen portin e klientit
    return "Klienti eshte duke perdorur portin: "+str(addr[1])

def ANASJELLTAS(x): #Metoda ANASJELLTAS tekstin e dhene e kthen anasjelltas (reverse)
    x=re.sub(r"^\s+|\s+$", "", x)
    if len(x)==1 or len(x)==0:
        return "Keni dhene vetem zbrazetira ose/dhe vetem nje karakter"
    else:
        return "Teksti i kthyer anasjelltas: "+ x[::-1] 
        
def PALINDROM(text): #Metoda PALINDROM tregon nese teksti shkruhet njejt ne te dyja anet, eshte palindrom
    text = re.sub(r'[^a-zA-Z]','',text)
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
    if num1.isnumeric()==False or num2.isnumeric()==False:
        return "Nuk keni dhene vetem dy numra valid!"
    gcdResult=math.gcd(int(num1),int(num2))
    return "Faktori me i madh i perbashket i dy numrave te dhene eshte: "+str(gcdResult)

def KONVERTO(mode,number): #Metoda KONVERTO eshte nje lloj kalkulatori per disa konvertime 
    
    if number.isnumeric()==False:
        return("Nuk keni dhene numer valid!")
    if mode=="cmNeInch":  
        converted=int(number)/2.54
        return "Numri "+str(number)+" cm, i konvertuar ne inch= "+str(round(converted, 3)) 
    elif mode=="inchNeCm":  
        converted=int(number)*2.54
        return "Numri "+str(number)+" inch, i konvertuar ne cm= "+str(round(converted, 3))
    elif mode=="kmNeMiles":  
        converted=int(number)*0.621371
        return "Numri "+str(number)+" km, i konvertuar ne milje= "+str(round(converted, 3))
    elif mode=="mileNeKm":  
        converted=int(number)/0.621371
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
                ,"I raise up my voice�not so that I can shout, but so that those without a voice can be heard. � We cannot all succeed when half of us are held back."
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
    n=re.sub(r"^\s+|\s+$", "", n)
    if n.isnumeric()==False:
        return ("Nuk kemi dhene numer valid, prandaj nuk mund te gjenerohet sekuenca Fibonacci!")
    elif int(n)<=0:
        return ("Keni dhene numer negativ ose 0 prandaj nuk mund te gjenerohet sekuenca Fibonacci!") 
    i=0
    result=""
    while i<int(n):
        result+= (" "+str(fibRecursion(i)))
        i+=1
    return "Sekuenca Fibonacci: "+ result

#Unaze e pafundme. Ketu tentojme te marrim kerkesat e klientit, dhe te kthejme pergjigjien adekuate
while True:  
    print("--------------------------------------------------------------------------------")
    try:
        request,addr = serverSocket.recvfrom(128)
        print("\nJeni lidhur me klientin: "+str(addr))
    except socket.error as err:
        print("Ka ndodhur gabim gjate pranimit te kerkeses se klientit!")
        print(str(err))
        continue
            
    if len(request)<=0: 
        print("Klienti nuk ka dhene kerkese prandaj lidhja eshte mbyllur.")    
        continue

    request=str(request.decode('utf-8'))  #Dekodimi i kerkeses 
    print("\nKerkesa nga klienti: "+ request+"\n")
    
    #Ne baze te kerkesave  thirrim metodat perkatese
    response = ''
    if request== 'KOHA':
        response = str(KOHA())

    elif request == 'IP':
        response= str(IP())

    elif request == 'NRPORTIT':
        response= str(NRPORTIT())

    elif request=='PALINDROM' or request=='PALINDROM ':
         response="Nuk keni dhene asnje tekst!"
    elif request.split(" ",1)[0] == 'PALINDROM':
         if re.match("^[0-9 ]+$",request.split(" ",1)[1]):
            response="Keni dhene vetem hapesira dhe/ose numra!"
         else:
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
    elif request.split(" ",1)[0] == 'GCF':
         numbers=request.split(" ",1)[1]   
         num1=numbers.split(' ',1)[0]
         
         if len(numbers)<len(num1+" "):
            response="Keni dhene vetem nje numer!"
         else:
            num2=numbers.split(' ',1)[1]
            response=str(GCF(num1,num2))

    elif request == 'NUMERO' or request == 'NUMERO ' :
         response="Nuk keni dhene asnje tekst!"
    elif request.split(" ",1)[0] == 'NUMERO':
         if re.match("^[0-9 ]+$",request.split(" ",1)[1]):
             response="Keni dhene vetem hapesira dhe/ose numra!"
         else:
             response=str(NUMERO(request.split(" ",1)[1]))

    elif request == 'KONVERTO':
         response=("\nModet e konvertimit:\n"+
                "1.Per konvertimin cm ne inch shtypni cmaNeInch\n"+
                "2.Per konvertimin inch ne cm shtypni inchNeCm\n"+
                "3.Per konvertimin km ne milje shtypni kmNeMiles\n"+
                "4.Per konvertimin milje ne km shtypni mileNeKm\n\n"+
                "Duhet ta shtypni modin e konvertimit dhe numrin qe deshironi ta konvertoni si: "+
                "KONVERTO{Hapesire}{Modi}{Hapesire}{Numri}")
            
    elif request.split(' ',1)[0] == 'KONVERTO':
         parameters=request.split(" ",1)[1]   
         mode=parameters.split(' ',1)[0]
         if len(parameters)<len(mode+" "):
            response="Keni dhene vetem modin e konvertimit!"
         else:
            num=parameters.split(' ',1)[1]
            response=str(KONVERTO(mode,num))
       
    elif request == 'THENJA':
        response= str(THENJA())

    elif request== 'FIBONACCI' or request== 'FIBONACCI ':
        response="Duhet te jepni numrin e termave te serise"
    elif request.split(' ',1)[0] == 'FIBONACCI':
        n=request.split(' ',1)[1]
        response= str(FIBONACCI(n))

    else: 
        response ="Kjo eshte nje kerkese jo valide!"
        
    print('Pergjigjja nga serveri --> '+str(response)+"\n")
    serverSocket.sendto(str.encode(response),addr)
        
serverSocket.close()  #Mbyllja e soket serverit 
