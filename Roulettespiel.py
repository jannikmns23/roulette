#Initialisierung
import.random
konto=0
einzahlung=0
x="i"
#Abbruch
while x!="q":
       #Aktion waehlen
       print("Um den Kontostand anzuzeigen, druecken Sie a.")
       print("Um Geld einzuzahlen, druecken Sie die e.")
       print("Um Roulette zu spielen, druecken Sie die s. Ein Spiel kostet 5 Punkte.1")
       print("Um das Programm zu schliessen druecken Sie q.")

       x=input()

       #Geld einzahlen
       if (x=="e"):
              gueltig=0
              while gueltig!=1:
                     print("Bitte Anzahl der Punkte eingeben, welche Sie einzahlen wollen (mind. 5; max. 100)")
                     einzahlung=input()
                     einzahlung=int(einzahlung)
                     if (einzahlung<=5 or einzahlung>=100):
                            print("Ihre Eingabe ist ungueltig!")
                     else:
                            gueltig=1
              #Konto
              konto=konto+einzahlung

       #Kontostandsabfrage
       if (x=="a"):
              print("Ihr Kontostand betraegt:", konto ,".")
       
       #Roulettespiel
       if (x=="s")
              print("Druecken Sie g um auf gerade Zahlen zu setzen")
              print("Druecken Sie u um auf ungerade Zahlen zu setzen")
              print("Druecken Sie r um auf rote Zahlen zu setzen")
              print("Druecken Sie b um auf schwarze zahlen zu setzen")
              
              y=random.randint(1,48)
       
       #gerade Zahlen
       if (x=="g"):
             if  y%2==0
              print("Sie haben gewonnen! +20 Punkte
              konto= konto+10


       #ungerade
       if (x=="u")
              y%1==0
       
       #rot
       if (x=="r")
              y>=1 and y<=24




