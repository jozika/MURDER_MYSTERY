
#intro funktion, the start of the screen, it's outside of the menyval

def intro(game):   
    name = input("Enter your name ")
    game_n= "Murdure Mystery" 
    print(f"Xx{'_' * 60}xX\nWellcome to {game_n}, {name}\n {game} \nXx{'_' * 60}xX")  # Here is all varibales connected

# The intro is the funktions name, there beholds the argument game, which's now the text 
intro("Your invited to a house party by your coworkers.\n While everyone was partying someone got murdured.\n Solve the case using clues, interviews, and observations.")


# Make the rules, it has to be easy

def g_rules():
    print(f"""
         Xx{'_' * 60}xX
            No one shoukd leave house, untill you find the murdurer
            You ge 3 chanses to guess who's the murdurer
            If you lose all 3, you lose the game and the game will End
            To win the game you just have to find the murdurer 
          Xx{'_' * 60}xX
            """)


#Start the game, now it's hard, make game very simple, no complication. 


def play():
    print("you wake up on someone screaming, the sound looks like it's coming from bedroom")
    print("Go and check what is wrong by typing bedroom, or stay by typing stay ")

    directionuno = input("")

    if directionuno == "bedroom":
        print("Your in the bedroom, but it seems theres no one \n however the bathroom door is open")
        print("If you want to go to the bathroom, just type bathroom \n And if you want to go back to the livingroom  or stay\n just type stay or livingroom ")
        chektoa = input ("")

        if chektoa == "bathroom": 
            print("Gosh.. you see a dead corps and a ledy right beside the body, it seems shes uncoinsas")
        

        elif chektoa == "stay": # jag håller på lägga till några saker, den fungerar inte än, håller på fixa den
            print("The bedroom, seems larger than the livingroom")
            print("chose one of the option listet, to continue")
       
       
        elif chektoa == "livingroom":
            print("Gosh my head hurts")
            print("I must've halusanating")

    else: 
        print("Where is everyone, i need som water")

        quit()
    
def stayoption():
     global option
     option = input("""
                     A. Walk around the house
                     B. Look for the bathroom
                     C. Star eating Pizza 
                                                    
                                """)

     if option == "A":
                    print("It seems everyone is sleep, do i've to wake them up")          
     elif option == "B": 
          print("I need to be")       

     elif option == "C": 
           print("uGH, this pizza taste nasty and hard")

                    
       
while True:

    menyval = input("""
                    1. Rules
                    2. Start the game
                    3. Inventory         
                    4. End the game 

                """)
    


    if menyval == "1": 
        g_rules()

    if menyval == "2": 
        play()
        stayoption()
             
    if menyval == "3": 
        pass

    if menyval == "4": 
        quit("")


    