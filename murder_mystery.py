
# murder mystery 

print("Välkommen på vart spel murdure mystry..")

def clue1(vem):

    for x in vem:

        if x == "a":
            print ("spelet försätter")
        
        elif x == "b":
            print("Råka spela vin")
        
        elif x == "c":
            print("Va va det för")



ledtrad1 = input(""" 
                    1. Gå ut 
                    2. Frågställa gästen 
                    3. Slå gästen
        """)


if ledtrad1 == "1":
    clue1("a")

if ledtrad1 == "2":
   clue1("b")
   print("Lovar min fru var bredvid mig")

if ledtrad1 == "3":
    clue1("c")


    