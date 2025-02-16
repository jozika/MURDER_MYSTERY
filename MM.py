
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
                    D. Varje steg har du val, Om du väljer fel förlorar du spelet.
              
                        """) # Regler har ändrats, det är bätter om man har i början av spelet
    print(f"Xx{'_' * 60}xX\nVälkommen till {game_n}, {name}\n{game} \nXx{'_' * 60}xX")  # Dash symbol har det används här, där gångaras det med 60 för att få det antal man behöver
    print(f"{regler}\n {GL_ACSII}")

# The intro is the funktions name, there beholds the argument game, which's now the text 
intro("Du är inbjuden till en hemmafest av dina kollegor.\nMedan alla festade blev någon mördad.\nLös fallet med hjälp av ledtrådar, intervjuer och observationer.")

while True:

    def starta_spel():
        print(f"""
Xx{'_' * 80}xX\n
Du vaknar av en skrikande röst, det låter som om den kommer från toan.\n
Xx{'_' * 80}xX
                    """)
        direction = input("Se vad som pågår(Ja/Nej): > ").lower()  # Gör svaret skiftlägesokänsligt
        
        if direction == "nej":
            print("Woww..spelet har inte ens börjat och du förlurat (☉_ ☉)!")  
        
        return direction  # Returnera direction istället för att använda global

    def direction_ja(direction):
        
        if direction == "ja":
            print(f"\nJäklar! Du ser en död kropp och en kvinna, hon ser medvetslös ut..\n")

            fortsättning1 = input(f"""
            [Välj ett av de 2 alternativen]:
                                  
                A. Väcka kvinnan
                B. Ropa på hjälp >
Xx{'_' * 80}xX
              """).upper()  # Gör att det går skriva stora och lite pokstiver
        
            if fortsättning1 == "A": # Här är scen direkt after direcktio ja, steg A
                print("Hon vaknar inte alls... Hämta kallt vatten.")
                print("Medan du häller vattnet ser du Diddy som ska hem, ingen annan är vaken.")
                chose1 = input("""Välj ett av de 3 alternativen:              
            A. Ge Diddy en kram ⊂(◉‿◉)つ
            B. Äta chocoloden på bordet 🍫ԅ( ͒ ۝ ͒ )
           
            >>>  """).upper()
                
                if chose1 == "A": # Inne i forsattning1, steg A, 
                    print("Diddy blev glad (͠≖ ͜ʖ͠≖), det verkar som att hans rolex gick sönder..") #har klarat den

                    chose11= input("""Välj ett av de 4 alternativen:             
            A. Fråga Diddy varför hans rolex är sönder?
            B. Säg hejdå till diddy ( ╹◡╹)っ
            C. Välj vem som är mördaren (☉_ ☉)                       
            >>>  """).upper() #Chose111 i chose 1, och välja mördaren
                    
                    if chose11 == "A":
                        print("Oj! Jag märkte inte det, sa Diddy") #behöver försättar
                        fortsättning2 = input("""När du vänder dig om minns du det krossade glaset vid kroppen.
                                                Lås yttredörren och låt Diddy inte gå hem: ja/nej
                                                >>>  """).lower()
                        
                        if fortsättning2 =="ja":
                            print("Nu när du har låst ytterdörren kan ingen lämna....Du börjar väcka alla från deras sömn och ställa frågor.")
                            folk = ("""
                                        - Cendrella och hennes sambo Chepelo, de försker vecka up Raquell som är medvetslös.
                                        - Diddy undrar....-vad är det som händer och varför Annabells har blodfläckar i tröjan...  """)
                            
                            print(f"{folk}\n..Alla ser misstänksamma ut ")
                            print("Du har kommit i slutet av spelet, med andra ord är det dags att bestämma vem som dödade diogo..\nMen innan dess ska du ställa frågor till dem :")

                            fraga_vem = input("""Välj vem du vill fråga...-Du kan ej välja mer än en personer:
                                               
                                                A. Annabell
                                                B. Diddy
                                                C. Raquell
                                                D. Diogo
                                                E. Cendrella
                                                F. Chepelo
                                                >>> """).upper()
                            
                            if fraga_vem =="A":
                                print("""
                                      - Du frågar Annabell varför är det blodfläckar i hennes tröja..
                                       - Hon svarar...-Jag blöder näsan när jag får ont i huvudet 
                                       """)
                                gissa_mördaren()

                            elif fraga_vem =="B":

                                print("""
                                - Diddy säger att han måste gå hem... innan han blir sen till jobbet.
                                - Du frågar igen om hans rolex... han svarar med: "Det är inte din sak.."
                                """)

                                ta_rolex = input("Ta rolexen från honom: Ja/Nej  ").upper()
                                print(f"{ta_rolex}\nShitt,det ser ut som att han blev sur..")

                                gissa_mördaren()
                                
                            elif fraga_vem =="C":
                                print("""
                                        -Raquell har inte vaknat än...
                                      """) 
                                gissa_mördaren()
                                
                            elif fraga_vem =="D":
                                print("""
                                         - He dead..  """) 
                                
                                gissa_mördaren()
                                
                            elif fraga_vem =="E":
                                print("""
                                      -Kan någon hämta kaltt vatten, säger Cendrella
                                       """) 
                                
                                gissa_mördaren()
                                
                            elif fraga_vem =="F":
                                print("""
                                      - Chepelo håller på att hämta vatten.. """) 
                                
                                gissa_mördaren()
                                
                            else:
                                 print("Ogiltigt val, försök igen.")




                    elif chose11 =="B":
                        print(" DU har förlorat igen!!!")
                    
                    elif chose11 =="C":
                        print("Du är halvvägs genom spelet, vilket betyder att du nu får 3 chanser att lista ut vem är mördaren.") # Raquell is medvetlöst, Diogo är död, Diddy rolex sänder, Annabell blodfläckar på tröjan, Cenderella rosa hår sover i vardagsrummet med sin sambo chepelo.
                        gissa_mördaren()
                      
                    else: 
                        print("Ogiltigt val, försök igen.")

                elif chose1 == "B": # Inne i forsattning1, steg B
                    print("UAHg ୧༼ ಠ益ಠ ༽୨!Vilken outur..Du har förlurat") #ändra till font sista delen
                

                else:
                     print("Ogiltigt val, försök igen.")

                
            elif fortsättning1 == "B":
                print("OBS!Du har förlurat..mördaren har rymt\n ( ༎ຶ⌑༎ຶ )") # Det är fortsättning1 C, det sak inte forsättas
                
            else:
                print("Ogiltigt val, försök igen.") # Här är för forsattning1, steg B

       #den här är för direction, 

    def gissa_mördaren():
     chanser = 3  # Spelaren har tre försök
     while chanser > 0:
        print(f"\nDu har {chanser} chanser kvar att gissa vem mördaren är.")
        
        killer_chose1 = input("""Välj en misstänkt:
        A. Annabell
        B. Diddy
        C. Raquell
        D. Diogo
        E. Cendrella
        F. Chepelo
        >>> """).upper()

        rätt_svar = "E"  # Anta att Annabell är mördaren, ändra om det behövs
        
        if killer_chose1 == rätt_svar:
            print("Grattis! Du har gissat rätt och vinner spelet! ")
            return  # Avsluta funktionen eftersom spelaren har vunnit

        else:
            chanser -= 1
            if chanser > 0:
                print("Fel gissning! Försök igen eller gå tillbaka för att samla fler ledtrådar.")
                tillbaka = input("Vill du gå tillbaka? (ja/nej): ").lower()
                if tillbaka == "ja":
                    return  # Avsluta funktionen och låt spelaren fortsätta spelet
            else:
                print("Tyvärr, du har förlorat spelet. Mördaren har rymt!")
                return  # Avsluta spelet  

    # Starta spelet och skicka direction till nästa funktion
    val = starta_spel()
    direction_ja(val)