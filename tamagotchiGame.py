import pygame, sys
import time
from pygame.locals import *
from random import randint

pygame.init()

#Window dimenisions
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 300

#Color Constants
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128,128,128)

#Declare window variable
display = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
#Window Title
pygame.display.set_caption("Tamagotchi")
#Declare game tick clock
clock = pygame.time.Clock()

#Functions for text
pygame.font.init()
font = pygame.font.SysFont(None,25)

#Button menu variable
#0 = Main display (Food,Game,Meds)
#1 = Food Menu (Snack,Meal,Treat)
#2 = Game Menu (Rock,Paper,Scissors)
#3 = Meds Menu (Medicine)
btnDisplay = 0

#Displays Creature images
frames = 0
creatShow = 0
game = 0

#Creature health variables
health = 100
hunger = 0
fun = 100
sick = 0

#Increment variables
turn = 0
tempTurn = 0

#Mini game variables
# -1=no pick, 0=rock, 1=paper, 2=scissors
userPick = -1
petPick = -1

#Pet image coordinates
x = (75)
y = (5)

#Load in pet images
creature1 =pygame.image.load('gotchi.png').convert_alpha()
creature2 =pygame.image.load('gotchi1.png').convert_alpha()
happy1 = pygame.image.load('gotchihap.png').convert_alpha()
happy2  = pygame.image.load('gotchihap1.png').convert_alpha()
sad1  = pygame.image.load('gotchisad.png').convert_alpha()
sad2  = pygame.image.load('gotchisad1.png').convert_alpha()
sick1  = pygame.image.load('gotchisick.png').convert_alpha()
sick2  = pygame.image.load('gotchisick1.png').convert_alpha()

#Control creature image display
def petDisplay():
    global frames, creatShow, game, tempTurn, btnDisplay
    frames += 1 #Increment frame variable once per frame
    if frames == 30: #Once frames=30, resets frames to 0 and swaps active image for inactive image
        frames = 0

        if sick == 1:#Checks if pet is sick
            if creatShow == 6:#Switches images
                creatShow = 7
            else:
                creatShow = 6
        elif game == 1:#checks if game was played and won
            tempTurn += 1
            if tempTurn == 1 or tempTurn == 3:#Display win images
                creatShow = 2
            elif tempTurn == 2 or tempTurn == 4:
                creatShow = 3
            elif tempTurn == 5:#Resets to main display, tempTurns, sets no game
                creatShow = 0  #has been played, and sets pet to normal
                tempTurn = 0
                game = 0
                btnDisplay = 0
        elif game == 2:#Checks if game was played and lost ot tied
            tempTurn += 1
            if tempTurn == 1 or tempTurn == 3:
                creatShow = 4
            elif tempTurn == 2 or tempTurn == 4:
                creatShow = 5
            elif tempTurn == 5:#Resets to main display, tempTurns, sets no game
                creatShow = 0  #has been played, and sets pet to normal
                tempTurn = 0
                game = 0
                btnDisplay = 0
            
        elif creatShow == 1:#Main pet display change
            creatShow = 0
        else:
            creatShow = 1


    #Blits pet images to screen        
    if creatShow == 0:
        display.blit(creature1,(x,y)) #Places creature1 image on  screen with top-left corner at x,y coordinates
    elif creatShow == 1:
        display.blit(creature2,(x,y)) #Places creature2 image on  screen with top-left corner at x,y coordinates
    elif creatShow == 2:
        display.blit(happy1,(x,y))
    elif creatShow == 3:
        display.blit(happy2,(x,y))
    elif creatShow == 4:
        display.blit(sad1,(x,y))
    elif creatShow == 5:
        display.blit(sad2,(x,y))
    elif creatShow == 6:
        display.blit(sick1,(x,y))
    elif creatShow == 7:
        display.blit(sick2,(x,y))

#Creates button one rectangle
def btnOne(msg,color): #Takes in text and color of text
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [40,250]) #Places text

#Creates button two rectangle
def btnTwo(msg,color): #Takes in text and color of text
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [150,250]) #Places text

#Creates button three rectangle
def btnThree(msg,color): #Takes in text and color of text
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [260,250]) #Places text

#Switches display to food buttons and events
def foodEvent(x,y,w,h,action=None):
    global btnDisplay
    mouse = pygame.mouse.get_pos() #Get position of mouse cursor
    click = pygame.mouse.get_pressed() #Gets which mouse button is clicked
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #Checks if mouse position is within button dimenisions
        if click[0] == 1 and action != None: #Checks if mouse is left clicked and action is being performed
            btnDisplay = 1 #Displays food menu
            pygame.time.delay(100)#prevents clicking on next button
            #The display will change and click before user releases click or tap

#Sub Food Button            
def treat(x,y,w,h,action=None): #Takes in position(x,y), size(w,h), and current action of button
    global hunger, btnDisplay, fun 
    mouse = pygame.mouse.get_pos() #Get position of mouse cursor
    click = pygame.mouse.get_pressed() #Gets which mouse button is clicked
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #Checks if mouse position is within button dimenisions
        if click[0] == 1 and action != None: #Checks if mouse is left clicked and action is being performed
            hunger -= 5
            fun += 5
            btnDisplay = 0
            pygame.time.delay(100)

#Sub Food Button
def snack(x,y,w,h,action=None):
    global hunger, btnDisplay
    mouse = pygame.mouse.get_pos() #Get position of mouse cursor
    click = pygame.mouse.get_pressed() #Gets which mouse button is clicked
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #Checks if mouse position is within button dimenisions
        if click[0] == 1 and action != None: #Checks if mouse is left clicked and action is being performed
            hunger -= 2
            btnDisplay = 0
            pygame.time.delay(100)

#Sub Food Button    
def meal(x,y,w,h,action=None):
    global hunger, btnDisplay
    mouse = pygame.mouse.get_pos() #Get position of mouse cursor
    click = pygame.mouse.get_pressed() #Gets which mouse button is clicked
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #Checks if mouse position is within button dimenisions
        if click[0] == 1 and action != None: #Checks if mouse is left clicked and action is being performed
            hunger -= 10
            btnDisplay = 0
            pygame.time.delay(100)

#Switches to game menu
def funEvent(x,y,w,h,action=None):
    global btnDisplay, game
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            if sick != 1:#Can't play game if pet is sick
                btnDisplay = 2 #Displays game menu
                game = -1 #Prevents pet from getting sick while playing game
                pygame.time.delay(100)#Sickness stops users from choosing game choice
                
#Sub game button
def rock(x,y,w,h,action=None):
    global userPick
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            userPick = 0 #User picks rock
            pygame.time.delay(100)
            playGame()#Calls game function
            
#Sub game button
def paper(x,y,w,h,action=None):
    global userPick
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            userPick = 1 #User picks paper
            pygame.time.delay(100)
            playGame()
            
#Sub game button
def scissors(x,y,w,h,action=None):
    global userPick
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            userPick = 2 #User picks scissors
            pygame.time.delay(100)
            playGame()

#Mini-game Controller
def playGame():
    global userPick, petPick, fun,btnDisplay, game
    petPick = randint(0,2) #Chooses pets pick
    #print(petPick) Random number check
    if userPick == 0 and petPick == 1:#Pet wins
        fun += 15
        game = 1 #Game was played and won
        userPick = -1#Resets user pick
        petPick = -1#Resets pet pick
    elif userPick == 1 and petPick == 2:#Pet wins
        fun += 15
        game = 1
        userPick = -1
        petPick = -1
    elif userPick == 2 and petPick == 0:#Pet wins
        fun += 15
        game = 1
        userPick = -1
        petPick = -1
    elif userPick == petPick:#Tie
        fun += 10
        game = 2 #Game waas played and lost or tied
        userPick = -1
        petPick = -1
    else:#User win
        fun += 10
        game = 2
        userPick = -1
        petPick = -1
        
#Switches to meds menu
def medEvent(x,y,w,h,action=None):
    global btnDisplay
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            btnDisplay = 3 #Displays meds menu
            pygame.time.delay(100)

#Sub meds button
def medicine(x,y,w,h,action=None):
    global sick, health, btnDisplay
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            sick = 0 #Cures sick
            health += 10
            btnDisplay = 0
            pygame.time.delay(100)

#Random event controller+
def events():
    global sick, health, creatShow
    if frames == 29 and game == 0: #Game runs at 30 fps, so checks for event once per second
        if sick == 0:               #Prevents sickness from freezing mini-game
            event = randint(0,200)
            #print(event)
            if(0 < event < 6):#Chance of sickness
                sick = 1
                creatShow = 6
                #print("Im sick")
            elif 194 < event < 200: #Chance of attack and sickness
                sick = 1
                health -= 5
                creatShow = 6
                #print("Im sick")
        
#Attributes Controller           
def attributes(tick):
    global hunger, health, fun, sick, turn
    tempFun = fun #Grabs fun before change
    if tick == 29:
        turn += 1
        if sick == 1:#Decrements health once per seccond if sick
            health -= 1
    if turn == 5:#Makes changes to attributes every 5 seconds
        turn = 0
        if hunger >= 90:#If at or above 90 hunger, pet starts dying of starvation
            hunger += 3
            health -= 1
        elif hunger >= 0 and hunger <= 100:#Normal attribute change
            hunger += 3
        if fun <= 10:#If at or below 10 fun, pet starts dying due mental issues
            fun -= 3
            health -= 1
        elif fun <= 100 and fun >= 0:#Normal attribute change
            fun -= 3
        tempHP = (hunger/18)+((tempFun-fun)/18)#temphealth is calculated by
        #dividing hunger by 18 plus the change in fun attribute divided by 18
        health = health-tempHP #Calculate health

def gameLoop():

    gameExit = False #End game boolean
    
    while not gameExit: #Main Loop
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #Exit game conditions
                gameExit=True
        
        display.fill(WHITE) #Creates white background
        pygame.draw.rect(display, GRAY, (35,250,75,25)) #Draws button one
        pygame.draw.rect(display, GRAY, (145,250,75,25)) #Draws button two
        pygame.draw.rect(display, GRAY, (255,250,75,25)) #Draws button three
        petDisplay()

        if health <= 0:
            gameExit = True

        #print(health)
        attributes(frames)#Changes attributes
        events()#Checks for random event
        if btnDisplay == 0:#Main display
            btnOne("Food",BLACK)
            btnTwo("Game", BLACK)
            btnThree("Meds", BLACK) 
            foodEvent(35,250,75,25,"Food")
            funEvent(145,250,75,25,"Games")
            medEvent(255,250,75,25,"Meds")
        elif btnDisplay == 1:#Food display
            btnOne("Snack",BLACK)
            btnTwo("Meal",BLACK)
            btnThree("Treat",BLACK)
            snack(35,250,75,25,"Snack")
            meal(145,250,75,25,"Meal")
            treat(255,250,75,25,"Treat")
        elif btnDisplay == 2:#Game display
            btnOne("Rock",BLACK)
            btnTwo("Paper",BLACK)
            btnThree("Scissors",BLACK)
            rock(35,250,75,25,"Rock")
            paper(145,250,75,25,"Paper")
            scissors(255,250,75,25,"Scissors")
        elif btnDisplay == 3:#Meds display
            btnOne("Meds", BLACK)
            btnTwo(" ",BLACK)
            btnThree(" ",BLACK)
            medicine(35,250,75,25,"Medicine")
        

        pygame.display.update()#Updates the display screen
        clock.tick(30)#Game clock runs at 30fps(30 loops a second)
        #print("ticked")

gameLoop()#Main game loop function
pygame.quit()
sys.exit()
