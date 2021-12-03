import os
import time
import random
from math import floor

def create_Game_Stage(): #Create background list for the card values to attached to, like an address

    cards = []
    for count in range(16):
        cards.append([' [] '])
    return cards

def Turned_cards(cards): #Create location for the hidden answers list for the code to input values

    turnedDeck = cards[:] #Copy the cards so we do not modify the original empty list
    possibleCards = {1:"O", 2:"X", 3:"A", 4:"B", 5:"C", 6:"D", 7:"E", 8:"F"} #Value of card

    for count in range(len(turnedDeck)): #Find out got how many cards

        if(turnedDeck[count] == [' [] ']): #If the card at this location is empty, give it a value
            turnedDeck[count] = random.choice(list(possibleCards.values()))

            randomCardPosition = 0 #Search for an empty card location between 0,15 as array starts with 0, we have 16 cards
            while(turnedDeck[randomCardPosition] != [' [] ']):
                randomCardPosition = random.randint(0,15)
            
            turnedDeck[randomCardPosition] = turnedDeck[count] #Assign the same value as the above to the card at this location, forming a pair

            for key in possibleCards.keys(): #Delete away that value from the dictionary so that it will not be used again
                if possibleCards[key] == turnedDeck[count]:
                    possibleCards.pop(key)
                    break
    return turnedDeck

def player_Deck(cards): #Creation of the backbone of the deck that will be shown to player, it will generate a number string and formating it abit

    playerDeck = cards[:] #Copy the cards so we do not modify the original empty list
    count = 0
    for count in range(len(cards)): #Creating a list of numbers in string fomat and adding it to the playerDeck list
        if(count < 9):
            playerDeck[count] = '{} '.format(count+1)
        else:
            playerDeck[count] = '{}'.format(count+1)
    return playerDeck

#Global Variable Dictionary, this are used in multiple functions
EnemyMemory_Dict = {}
Answered_Dict = {}

def EnemyMemory(Choice_First, Choice_Second,AnswerRightWrong,Answer_First,Answer_Second): 
    #The AI will through this function, remember what are the already flipped cards and add it to EnemyMemory_Dict
    if(AnswerRightWrong == False): #If answer was correct, it will add it, if not it will not care
        if(Choice_First not in EnemyMemory_Dict.keys()):
            EnemyMemory_Dict[Choice_First] = Answer_First
        if(Choice_Second not in EnemyMemory_Dict.keys()):
            EnemyMemory_Dict[Choice_Second] = Answer_Second

def Enemy_Choice():
#Through this function, the AI NPC will choose an appropriate response based on the opened cards so far

    Enemy_First_Choice = random.randint(0,15) #It first randomly choose 2 choices
    while(Enemy_First_Choice in Answered_Dict):
        #Ensuring the 1st not an already answered choicce
        Enemy_First_Choice = random.randint(0,15)

    Enemy_Second_Choice = random.randint(0,15)

    while(Enemy_First_Choice == Enemy_Second_Choice or Enemy_Second_Choice in Answered_Dict):
        #Ensuring the 1st and 2nd choice is different and that the 2nd choice is not an already answered choicce
        Enemy_Second_Choice = random.randint(0,15)

    find_Duplicate_Answer_Flipped_Dict = {} #This dictionary will be used to find cards that have already been flipped and matching

    for key,value in EnemyMemory_Dict.items(): #Loop through EnemyMemory_Dict to find duplicates in values and check those keys to a single list.
        if value not in find_Duplicate_Answer_Flipped_Dict:
            find_Duplicate_Answer_Flipped_Dict[value] = [key] #This needs to be list so that we can count how many value in the key for answer
        else:
            find_Duplicate_Answer_Flipped_Dict[value].append(key)

    for key, value in find_Duplicate_Answer_Flipped_Dict.items():
        if(len(value) == 2): #If there is a list with 2 values, then that means that those pair of key have same value
            if(value[0] not in Answered_Dict and value[1] not in Answered_Dict): #Assign those value if it havent been answered before
                Enemy_First_Choice = value[0] #Let the AI NPC choose those vlaue
                Enemy_Second_Choice = value[1]

    return (Enemy_First_Choice,Enemy_Second_Choice) #Return the bot's 1st and 2nd choice
    
def Choose(firstChoice,secondChoice,Player_Number,playerDeck): #Basically the function for both player and AI NPC to choose

    correct_wrong_flag = False #Create a flag to check if an answer chosen is correct later
    if(turned_Deck[firstChoice] == turned_Deck[secondChoice]): #If the choices result in same value, then it is correct

        correct_wrong_flag = True #Set the flag to True
        Answered_Dict[firstChoice] = turned_Deck[firstChoice] #Lock in first correct Answer
        Answered_Dict[secondChoice] = turned_Deck[secondChoice] #Lock in second correct Answer

        os.system('cls')
        if(Player_Number == 'Player_One'): #If it is player that got it, print it in green, if it is AI NPC, print in another colour
            playerDeck[firstChoice] = "\033[1;32;40m" + turned_Deck[firstChoice] + " \033[0;37;40m"
            playerDeck[secondChoice] = "\033[1;32;40m" + turned_Deck[secondChoice] + " \033[0;37;40m"
        else:
            playerDeck[firstChoice] = "\033[1;36;40m" + turned_Deck[firstChoice] + " \033[0;37;40m"
            playerDeck[secondChoice] = "\033[1;36;40m" + turned_Deck[secondChoice] + " \033[0;37;40m"

        EnemyMemory(firstChoice, secondChoice,correct_wrong_flag,turned_Deck[firstChoice],turned_Deck[secondChoice]) #Send the choices to the memory
        Print_Correct_Deck(playerDeck)
        print("{} is correct".format(Player_Number)) #Announce that the choice was correct
        return correct_wrong_flag
    else: #If the choices are wrong
        os.system('cls')
        wrongAnswerDeck = playerDeck[:]

        #Set the val to red
        wrongAnswerDeck[firstChoice] = "\033[1;31;40m" + turned_Deck[firstChoice] + " \033[0;37;40m"
        wrongAnswerDeck[secondChoice] = "\033[1;31;40m" + turned_Deck[secondChoice] + " \033[0;37;40m"

        wrongAnswerDeckString = ''

        #Show the current wrong answers so that it can be memorised
        count = 0
        while count <= (len(wrongAnswerDeck)-4):
            wrongAnswerDeckString += '\u250f\u2501\u2501\u2501\u2501\u2501\u2513' + '\u250f\u2501\u2501\u2501\u2501\u2501\u2513'+ '\u250f\u2501\u2501\u2501\u2501\u2501\u2513' + '\u250f\u2501\u2501\u2501\u2501\u2501\u2513\n'
            wrongAnswerDeckString += '\u2503     \u2503' + '\u2503     \u2503' + '\u2503     \u2503' + '\u2503     \u2503\n'
            wrongAnswerDeckString += '\u2503  {} \u2503'.format(wrongAnswerDeck[count]) + '\u2503  {} \u2503'.format(wrongAnswerDeck[count+1]) + '\u2503  {} \u2503'.format(wrongAnswerDeck[count+2]) + '\u2503  {} \u2503'.format(wrongAnswerDeck[count+3]) + '\n'
            wrongAnswerDeckString += '\u2503     \u2503' + '\u2503     \u2503' + '\u2503     \u2503' + '\u2503     \u2503\n'
            wrongAnswerDeckString += '\u2517\u2501\u2501\u2501\u2501\u2501\u251b' + '\u2517\u2501\u2501\u2501\u2501\u2501\u251b' + '\u2517\u2501\u2501\u2501\u2501\u2501\u251b' + '\u2517\u2501\u2501\u2501\u2501\u2501\u251b\n'
            count += 4

        print(wrongAnswerDeckString)
        EnemyMemory(firstChoice, secondChoice,correct_wrong_flag,turned_Deck[firstChoice],turned_Deck[secondChoice]) #Let the AI NPC remember which card is at where
        return correct_wrong_flag

def Print_Correct_Deck(playerDeck): #Printing formatting
    os.system('cls')
    playerDeckString = ''
    count = 0
    while count <= (len(playerDeck)-4): #Done in unicode
        playerDeckString += '\u250f\u2501\u2501\u2501\u2501\u2501\u2513' + '\u250f\u2501\u2501\u2501\u2501\u2501\u2513'+ '\u250f\u2501\u2501\u2501\u2501\u2501\u2513' + '\u250f\u2501\u2501\u2501\u2501\u2501\u2513\n'
        playerDeckString += '\u2503     \u2503' + '\u2503     \u2503' + '\u2503     \u2503' + '\u2503     \u2503\n'
        playerDeckString += '\u2503  {} \u2503'.format(playerDeck[count]) + '\u2503  {} \u2503'.format(playerDeck[count+1]) + '\u2503  {} \u2503'.format(playerDeck[count+2]) + '\u2503  {} \u2503'.format(playerDeck[count+3]) + '\n'
        playerDeckString += '\u2503     \u2503' + '\u2503     \u2503' + '\u2503     \u2503' + '\u2503     \u2503\n'
        playerDeckString += '\u2517\u2501\u2501\u2501\u2501\u2501\u251b' + '\u2517\u2501\u2501\u2501\u2501\u2501\u251b' + '\u2517\u2501\u2501\u2501\u2501\u2501\u251b' + '\u2517\u2501\u2501\u2501\u2501\u2501\u251b\n'
        count += 4
    print(playerDeckString)

def Game_Main(turned_Deck,playerDeck): #Main game run
    
    print("Welcome to memorise cards game!!!!\n")
    time.sleep(1)

    Lives = 10 # Have as many lives as you want

    while(turned_Deck != playerDeck):
        
        time.sleep(1)
        Print_Correct_Deck(playerDeck)
        #Player 1 Choose Card
        #Player 1 Number is Player_One
        Player_Number = 'Player_One'
        print(EnemyMemory_Dict) #<- Cheat Code (Uncomment to cheat)
        firstChoice = int(input("Choose first card (from 1 to 16):")) - 1 #Input change to int and must be start from 0, but for us normal huumans to see, we "start" it at 1
        secondChoice = int(input("Choose first card (from 1 to 16):")) - 1

        while(firstChoice == secondChoice): # Dont let ppl choose same card
            print("You have to choose two different card!")
            firstChoice = int(input("Choose first card (from 1 to 16):")) - 1
            secondChoice = int(input("Choose first card (from 1 to 16):")) - 1
        
        correct_wrong_flag = Choose(firstChoice,secondChoice,Player_Number,playerDeck) #Call the choose() function

        if(correct_wrong_flag == False): #If wrong, lose a live
            Lives = Lives - 1

            if(Lives > 1):
                print("Wrong Answer! You have {} tries left".format(Lives))
            elif(Lives == 1):
                print("Wrong Answer! Your last life!")
            else:
                print("You Lose")
                break
        
        print(turned_Deck)
        print(playerDeck)

        if(turned_Deck == playerDeck):
            break

        time.sleep(1)
        os.system('cls')
        
        #AI turn
        Enemy_First_Choices = Enemy_Choice()
        Player_Number = 'Enemy'
        Choose(Enemy_First_Choices[0],Enemy_First_Choices[1],Player_Number,playerDeck)
        if(Player_Number == 'Enemy'):
            print("It is now {} turn and he choose card {} and card {}".format(Player_Number,Enemy_First_Choices[0],Enemy_First_Choices[1]))
            time.sleep(1)
        
        if(turned_Deck == playerDeck):
            break
    
    print("Congrats you have won") #To do add score

cards = create_Game_Stage()
turned_Deck = Turned_cards(cards)
playerDeck = player_Deck(cards)
Game_Main(turned_Deck,playerDeck)