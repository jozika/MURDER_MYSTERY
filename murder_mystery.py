
import pyfiglet # Här har jag laddad ner pyfiglet libary, där kan vi skapa ASCII texter utan att behöva kopiera de.

ascii_text = pyfiglet.figlet_format("Murder Mystery", font= "big") # Skapad en variabel, stor text på spelets namn, ''.figlet_format'' är en funktion som ändrar texter till ASCII art

print(ascii_text)


#intron
def intro(game):   # Intron visas after man har skrivt in sitt namn, 
    name = input("Skriv in ditt namn: ")
    game_n= "Murdure Mystery" 
    GL_ACSII = pyfiglet.figlet_format("Lycka Till!!!", font= "big") # GL står för Goodluck
    regler = ("""                           
                För att vinna spelet:
              
                    A. Hitta mördaren
                    B. Ingen får lämna huset förrän du hittar mördaren
                    C. Du har tre chanser att gissa vem som är mördaren
                        """) # Regler har ändrats, det är bätter om man har i början av spelet
    print(f"Xx{'_' * 60}xX\nVälkommen till {game_n}, {name}\n{game} \nXx{'_' * 60}xX")  # Dash symbol har det används här, där gångaras det med 60 för att få det antal man behöver
    print(f"{regler}\n {GL_ACSII}")

# The intro is the funktions name, there beholds the argument game, which's now the text 
intro("Du är inbjuden till en hemmafest av dina kollegor.\nMedan alla festade blev någon mördad.\nLös fallet med hjälp av ledtrådar, intervjuer och observationer.")

inventory = []

def starta_spel():
    print("Du vaknar av en skrikande röst, det låter som om den kommer från toan.\nSe vad som pågår? (ja/nej)")
    direction = input("> ").lower()  # Gör att det man skriva med små eller stora posktiver
    
    if direction == "nej":
        print("Jag hallucinera säkert... Jag går och dricker vatten för att glömma det.")
    else:
        print("...")  # Här ska läggas till mer kod senare
    
    return direction  # Returnera direction istället för att använda global

def direction_ja(direction):
    if direction == "ja":
        print("Jäklar! Du ser en död kropp och en kvinna med rosa hår, hon ser medvetslös ut.")

        fortsättning1 = input("""Välj ett av de 3 alternativen:
        A. Väcka kvinnan
        B. Spring och lås ytterdörren
        C. Ropa på hjälp
        > """).upper()  # Gör att det man skriva med små eller stora posktiver
    
        if fortsättning1 == "A":
            print("Hon vaknar inte alls... Hämta kallt vatten.")
        elif fortsättning1 == "B":
            print("Obs... Du behöver en nyckel.")
        elif fortsättning1 == "C":
            print("Du förlorar.")
        else:
            print("Ogiltigt val, försök igen.")

# Starta spelet och skicka direction till nästa funktion
val = starta_spel()
direction_ja(val)



    