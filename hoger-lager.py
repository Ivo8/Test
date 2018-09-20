import random

x= random.randint(0,100) #mogelijkheden

doorgaan = True


while doorgaan == True: #start loop

    getal = int(input(" Raad het getal: ")) #input (int)


    if getal ==x: #precies goed
        print ("Je hebt het graden!")
        doorgaan = False #end loop
        
    if getal <x: #te laag
        print (" Hoger")

    if getal >x: #te hoog
        print ("Lager")
