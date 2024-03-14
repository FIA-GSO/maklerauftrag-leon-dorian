        
print ("Hallo, geben Sie die Anzahl der Räume an.")
Anzahl_Raeume = int(input())
#Anzahl der Räume werden Abgefragt
gesamtfläche = float
wohnfläche = 0
listRaumname = []
listRaumfläche = []
#Listen zum zwischenspeichern der Raumnamen und Raumflächen werden erstellt.
p =1
#dem Counter für die while-Schleife wird der Startwert 1 zugeordnet
while p <= Anzahl_Raeume:
    #Die Bedingung für die while-Schleife wird genannt
    print ("Bitte benennen Sie den", p , "Raum.")
    raumname = input();
    #Vergabe für den Raumnamen wird angefordert
    listRaumname.append(raumname)
    #Raumname wird in der Liste für Namen angehangen und gespeichert
    print ("Ist der", p , "Raum rechteckig? Antworten Sie mit Ja oder Nein.")
    rechteck_pruefen = input();
    #Abfrage nach Raumform
    if rechteck_pruefen.lower() == "ja":    #Bedingung für if-Schleife
        print("Geben Sie die Länge des Raumes ein.")
        laenge = float(input())
        print("Geben Sie die Breite des Raumes ein.")
        breite = float(input())
        gesamtfläche = laenge * breite
        """
        Länge und Breite des rechteckigen Raums werden abgefragt und anschließend wir die
        Raumfläche berechnet
        """
        listRaumfläche.append(gesamtfläche) #Die Raumfläche wird in der Liste für Flächen gespeichert
        print("Die Raumfläche beträgt:", gesamtfläche , "Quadratmeter")
        wohnfläche += gesamtfläche  #Ausgabe der Raumfläche
    else:   #für den Fall, dass der Raum nicht rechteckig ist
        print ("In wieviele rechteckige Bereiche lässt sich der Raum unterteilen?")
        AnzahlBereiche = int (input())  #Anzahl der Teilbereiche wird abgefragt
        z =1    #dem Counter für die while-Schleife wird der Startwert 1 zugeordnet
        SummierteFläche = 0 
        while z <= AnzahlBereiche:  #Die Bedingung für die while-Schleife wird genannt
            print ("Geben Sie die Länge des", z ,"Bereiches an")
            laenge = float(input())
            print("Geben sie die Breite des", z ,"Bereiches")
            breite = float(input()) #Länge und Breite eines Bereiches werden abgefragt
            SummierteFläche += laenge * breite  
            #Fläche wir eines Bereiches wird ausgerechnet und auf die Fläche der anderen Bereiche des Raumes addiert
            z +=1   #Counter der while-Schleife erhöht sich um 1
        wohnfläche += SummierteFläche   #gesamtfläche des Raumes wird auf die Wohnfläche gerechnet
        print ("Die Raumfläche beträgt:", SummierteFläche , "Quadratmeter.")
        listRaumfläche.append(SummierteFläche) 
        #die summierte Raumfläche wird ausgegeben und in der Liste für Flächen gepeichert
        
    p +=1   #Counter der while-Schleife erhöht sich um 1
durchRaumgröße = wohnfläche/Anzahl_Raeume   #durchschnittliche Raumgröße wird ausgerechnet
print("Die gesamte Wohnfläche beträgt", wohnfläche , "Quadratmeter und hat eine durchschnittliche Raumgröße von", durchRaumgröße ,"Quadratmeter.")
#Die gesamte Wohnfläche und durchschnittliche Raumgröße wird ausgegeben
n =0
print("Die Wohnung enthält folgende Zimmer:")
while n < Anzahl_Raeume:
    print(listRaumname[n], "mit", listRaumfläche[n], "Quadratmetern")
    n +=1   #Der jeweilige Raumname wird mit der zugehörigen Raumgröße ausgegeben
    
    

            

    

        
        
    
    
