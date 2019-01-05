#Importing class deck that will be used to make the freecell game
from deck import Deck

#The last class of the assignment.
#Designed to create the game using class card and deck.
#The class has the ability to create a deck, create the structure of the game
#Validate user inputs and implement the rules of the game
class NotFreecell(Deck):

    #Constructor
    #Initial method for object creation
    #Intialise the value of the instance attributes
    #Contains the Instance attributes
    #The first thing done here was calling the class deck and the functions inside it to create a deck.
    #self.deck defines the deck containing 52 card and 4 different suits
    #self.cpile are all the 8 piles of the game
    #self.cpile defines a list of list that was created from the deck.
    #self.ccascade are the 4 cells of the game which are initially empty.
    #self.cfoundation are the 4 foundations of the game which are intially empty.
    def __init__(self):
        aDeck = Deck(1,13,4)
        aDeck.deck_generator()
        self.deck = aDeck
        self.cpile= []
        self.cfoundation=[[],[],[],[]]
        self.ccascade= ['', '', '', '']

    #Prints the internal value of the objects in form of a string.
    #Returns the freecell heading and empty cell and foundations.
    def __str__(self):

        #Heading of the free cell
        print('Cells'+'\t\t\t\t\t\t\t'+'Foundations')

        #if statements that check if the cell has any elements in it
        newString=""
        if self.ccascade[0]:
            newString += '['+str(self.ccascade[0])+']   '
        else:
            newString += '[   ]   '
        if self.ccascade[1]:
            newString += '[' + str(self.ccascade[1]) + ']   '
        else:
            newString += '[   ]   '
        if self.ccascade[2]:
            newString += '[' + str(self.ccascade[2]) + ']   '
        else:
            newString += '[   ]   '
        if self.ccascade[3]:
            newString += '[' + str(self.ccascade[3]) + ']   '
        else:
            newString += '[   ]   '

        #if statements that check if the foundations has any elements in it
        if len(self.cfoundation[0]) > 0:
            newString += '['+str(self.cfoundation[0][len(self.cfoundation[0])-1])+']   '
        else:
            newString += '[   ]   '
        if len(self.cfoundation[1]) > 0:
            newString += '['+str(self.cfoundation[1][len(self.cfoundation[1])-1])+']   '
        else:
            newString += '[   ]   '
        if len(self.cfoundation[2]) > 0:
            newString += '['+str(self.cfoundation[2][len(self.cfoundation[2])-1])+']   '
        else:
            newString += '[   ]   '
        if len(self.cfoundation[3]) > 0:
            newString += '['+str(self.cfoundation[3][len(self.cfoundation[3])-1])+']   '
        else:
            newString += '[   ]   '
        return newString

    #Accesors
    #To get access to the instance attribute
    #Since instance attributes are local to the class
    #Used to get access to the deck, piles,cells and fondations repectively.
    def get_theDeck(self):
        return self.deck.get_deck()

    def get_cpile(self):
        return self.cpile

    def get_ccascade(self):
        return self.ccascade

    def get_cfoundation(self):
        return self.cfoundation


    #function to get largest list inside a list
    #this function iterates a list of list
    #find the list that is the largest inside the list of lists
    #return back the maximum amount of objects stored inside the largest list
    def get_largest(self,x):
        i = 0
        max = 0
        while i < len(x):
            if len(x[i]) > max:
                max = len(x[i])
            i += 1
        return max



    #function to creates lists inside a list
    #this fucntion creates cpiles from the deck
    #it creates 8 piles with the first 4 holding 7 cards repectively
    #the other 4 piles will hold 6 cards repectively, in total making up 52 cards.
    #the process starts with first storing 28 cards into 4 lists of equal length known as cpile1
    #the next process is to store 24 cards into 4 lists of equal lengths known as cpile2
    #finally cpile1 and cpile2 are combined together to form cpile
    #cpile is a list that holds 8 lists in it, these 8 lists are the 8 piles of the freecell
    def print_deck(self):
        cpile1 = []
        cpile2 = []

        #cards added to cpile1
        i = 0
        while i < 28:
            cpile1.append(self.get_theDeck()[i])
            i += 1

        #cards added to cpile2
        i = 28
        while i < 52:
            cpile2.append(self.get_theDeck()[i])
            i += 1

        #dividing cards in each list by 4
        cpile1 = [cpile1[i:i + 7] for i in range(0, len(cpile1), 7)]
        cpile2 = [cpile2[i:i + 6] for i in range(0, len(cpile2), 6)]

        #adding cpile1 to cpile
        i = 0
        while i < len(cpile1):
            self.cpile.append(cpile1[i])

            i += 1


        #adding cpile2 to cpile
        #this leaves us with cpile a list that hold 8 list or in our game you can call them 8 piles
        i = 0
        while i < len(cpile2):
            self.cpile.append(cpile2[i])
            i += 1



    #funtion to print in freecell format
    #this fuction creates the previously constructed funtion get_largest
    #this fuction takes the created cpile
    #printing the lists inside the cpile into appropriate columns with equal spaces between them
    #it makes use of nested while loops
    #we start first by creating a string known as result_string and calling the get_largest function.
    #the inner loop iterates inside the list's of cpile
    #the outerloop iterates according to the output obtained via get_largest fuction
    def freecell_pile(self):
        x = self.cpile;
        largestPile = self.get_largest(x)
        result_string=""
        i = 0
        while i < largestPile:
            j = 0
            lineString = ' '
            while j < len(x):
                if (len(x[j]) < largestPile) and (len(x[j]) < i + 1):
                    lineString += "        "

                else:
                    lineString += str(x[j][i]) + '     '
                j += 1

            lineString+='\n'
            result_string+=lineString
            i += 1

        return result_string



    #After having all the functions to display the freecell we will now be validating all the moves.
    #Also, implementing the rules of the game.


    #the first fuction returns a true value if each foundation has a length of 13 cards.
    def win_freecell(self):
        if (len(self.get_cfoundation()[0])==13) and (len(self.get_cfoundation()[1])==13):
            if (len(self.get_cfoundation()[2]) == 13) and (len(self.get_cfoundation()[3])==13):
                return True


    #Since the cell can only hold one card at a time
    #The fuction will return true if the cell is empty and return false if otherwise.
    def validateInput_cascade(self,theList):
        if not theList:
            return True
        else:
            return False



    #can cardValue be added to theList?
    #This function take in a card and a pile, checks if a card can be added to a pile
    #face_order shows the sequence of the card faces
    #It first checks for the valid face of the card
    #Then checks for the valid suit
    #Finally if both values return a true value it returns true for the whole fuction
    def validateInput_pile(self,cardValue, theList):

        #Sequence of the card faces
        face_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']

        #to value is the last card of the pile.
        toValue = theList[len(theList) - 1]

        #if statements that check for a valid face.
        validFace = False
        i = 0
        while (i < len(face_order)):
            if toValue.get_face() == face_order[i]:
                if cardValue.get_face() == face_order[i - 1]:
                    validFace = True
                    break;
            i += 1
        if not validFace:
            print("Sorry, the face value needs to be lower than the card present in the pile.")

        #if statements to check for a valid suit.
        validSuit = False
        if toValue.get_suit() == 'C' or toValue.get_suit() == 'S':
            if cardValue.get_suit() == 'H' or cardValue.get_suit() == 'D':
                validSuit = True

        if toValue.get_suit() == 'H' or toValue.get_suit() == 'D':
            if cardValue.get_suit() == 'C' or cardValue.get_suit() == 'S':
                validSuit = True
        if not validSuit:
            print("Sorry,the suit value is not valid.");

        #if statements to check if suit and face are valid or not
        if validSuit and validFace:

            return True
        else:
            return False



    #can cardValue be added to theList?
    #The next function checks for the valid input for foundation
    #it builds on the same concept of the function to add cards to a pile
    #But does validations in a different way.
    def validateInput_foundation(self,cardValue, theList):

        #the if statement first checks if the card's first value entered is 1
        #if so it returns true and if not then it goes and check if cards are of appropriate suit to add
        #to the foundation
        if cardValue.get_face() == "1" and len(theList) == 0:
            return True
        elif len(theList) == 0:
            return False

        #sequence of the cards face
        face_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']

        #Last card present in a foundation
        toValue = theList[len(theList) - 1]

        #Checks if it is a valid face to add to the foundation
        validFace = False
        i = 0
        while (i < len(face_order)):
            if toValue.get_face() == face_order[i]:
                if cardValue.get_face() == face_order[i + 1]:
                    validFace = True
                    break;
            i += 1
        if not validFace:
            print("Sorry, the face value needs to be highter than the card present in the pile.")

        #checks if it is a valid suit to add to the foundation
        validSuit = False
        if toValue.get_suit() == cardValue.get_suit():
            validSuit = True

        if not validSuit:
            print("Sorry,the suit value need to be the same in a foundation.");

        #If the suit and face are found valid it returns a true value
        if validSuit and validFace:

            return True
        else:
            return False



    #The next function checks for the input that the user makes.
    #I have used a dictionary which only specifies the inputs user can make in order to make a move.
    #The function the userinput and checks if that input is specified in the dictionary.
    #It then assigns an empty string a corresponding value according to the dictionary
    #For example if a userinput= P1 it will assign the string empty string to be a "pile"
    #If the input is part of the dictionary it returns it as true.
    #Otherwise it returns it as false.
    def validateInput_userInput(self,x, y):

        #Defining the dictionary of the userinput moves.
        moves = {"P1": "pile", "P2": "pile", "P3": "pile", "P4": "pile", "P5": "pile"
                , "P6": "pile", "P7": "pile", "P8": "pile"
                , "C1": "cell", "C2": "cell", "C3": "cell", "C4": "cell"
                , "F1": "foundation", "F2": "foundation", "F3": "foundation", "F4": "foundation"}

        #Empty strings
        value1 = ""
        value2 = ""

        #Checking if users first input is valid
        validmove1 = False
        for i in moves.keys():
            if str(x) == str(i):

                #If move is valid it assigns the empty string a value from the dictionary
                validmove1 = True
                value1 = moves[x]

                break
        if not validmove1:
            print('Sorry, the first input is invalid')

        #Checking if the second user input is valid
        validmove2 = False
        for j in moves.keys():
            if str(y) == str(j):

                #If move is valid it assigns the empty string a value from the dictionary
                validmove2 = True
                value2 = moves[y]
                break
        if not validmove2:
            print('Sorry, the first input is invalid')

        #if both userinputs are valid it returns the empty string(with a value) that we defined in the start.
        if (validmove1 == True) and (validmove2 == True):
            return value1, value2
        else:
            return False


    #This last function validates all of the moves.
    #Using all of the validations for pile,cell and foundation done above.
    def move_freecell(self, x, y):

        #Calls function to check if user make a valid input
        result= self.validateInput_userInput(x,y)

        if not result:
            print("INVALID INPUT.")
            return

        #Dealing with the first input, that is from where would you like to make the move
        #Defining an empty string to store the from and the to card
        lFromCard = ""
        lFromList = ""
        lToList = ""

        #Checks the first user input, if the move has to be made from a pile
        if result[0] == "pile":

            #lFromCard find the last element of the list inside cpile according to input
            #lFromList find the list where the card needs to be removed
            lFromCard = self.cpile[int(x[1])-1][len(self.cpile[int(x[1])-1])-1]
            lFromList = self.cpile[int(x[1])-1]

        #Checks the first user input, if the move has to be made from a foundation
        if result[0] == "foundation":

            #checks if the foundation is empty
            if len(self.cfoundation[int(x[1])-1]) < 1:
                print("Foundation "+str(int(x[1]))+" is empty.")
                return False

            #lFromCard find the last element of the list inside cfoundation according to input
            #lFromList find the list where the card needs to be removed
            lFromCard = self.cfoundation[int(x[1])-1][len(self.cfoundation[int(x[1])-1])-1]
            lFromList = self.cfoundation[int(x[1])-1]

        #Checks if the cell is empty.
        if result[0] == "cell":
            if not self.ccascade[int(x[1])-1]:
                print("Cell "+str(int(x[1]))+" is empty.")
                return False

            #Finding the element that needs to be removed.
            lFromCard = self.ccascade[int(x[1])-1]
            lFromList = self.ccascade[int(x[1]) - 1]

        #Checking which pile the card needs to be added to, and validates the move
        if result[1] == "pile":
            lToList = self.cpile[int(y[1])-1]
            if self.validateInput_pile(lFromCard, lToList):
                pilePopped = lFromList.pop()
                lToList.append(pilePopped)
                print("Card moved to the pile.")
            else:
                print("No card was moved to the pile.")

        #Checking which foundation the card needs to be added to, and validates the move
        if result[1] == "foundation":
            lToList = self.cfoundation[int(y[1])-1]
            if self.validateInput_foundation(lFromCard, lToList):
                if result[0] == "cell":
                    foundoPopped = lFromList
                    self.ccascade[int(x[1]) - 1] = ''
                else:
                    foundoPopped = lFromList.pop()
                lToList.append(foundoPopped)
                print("Card moved to the foundation.");
            else:
                print("No card was moved to the foundation.")

        #Checking which cell the card needs to be added to, and validates the move
        if result[1] == "cell":
            if self.validateInput_cascade(lToList):
                if result[0] == "cell":
                    cellPopped = lFromList
                    self.ccascade[int(x[1]) - 1] = ''
                else:
                    cellPopped = lFromList.pop()
                self.ccascade[int(y[1]) - 1] = cellPopped
                print("Card moved to the cell.")
            else:
                print("No card was moved to the cell.")

        #asks user for the next input.
        print("Please make the next input.")








def main():

    #Priting welcome note for the user, displaying some of the rules of input.
    print("Welcome to freecell, we are glad that you are here :-)",'\n')
    print("The following rules apply to the freecell input:",'\n')
    print("1) All inputs made by a player are case sensitive,therefore they all need to be in the upper case.")
    print("2) At one instance only one input can be made by the user.")
    print("3) Intially, there will be 8 piles these can be accessed with inputs P1-P8.")
    print("4) Also, there will be 4 cells these can be accessed with inputs C1-C4.")
    print("5) Finally, there will be 4 foundations these can be accessed with inputs F1-F4.")

    #If the user has read the inputs then they can enter into the game.
    ruleInput=" "
    while ruleInput!='Y':
        ruleInput = input('\nHave you read the rules of the game? Press Y for yes, N for no: ')
        print("\n")

        #In case user enters input in the lower case
        if ruleInput == ruleInput.lower():
            print('You need to make inputs in upper case')

        #Once user make all the relavant input the game starts
        if ruleInput=='Y':

            #Initializing the freecell
            a=NotFreecell()

            #Adding cards to the deck
            ans=a.get_theDeck()

            #dShuffling cards inside the deck
            a.deck_shuffle(ans)

            #Calling function to print the deck in a column form
            a.print_deck()

            #Priting the freecell
            print(a)
            print(a.freecell_pile())

            #Taking user input to make a move or to quit the game
            userInput = ''
            while userInput != 'Q':
                userInput=input ('\npress Q to quit,M for move:')
                if userInput=='Q':

                    #If user chooses to quit the game
                    print('See you again, Have a lovely day :-)')

                elif userInput=='M':

                     #If the user decides to make the move.
                     userInput1=str(input('Where would u like to move the card from?'))
                     userInput2=str(input('Where would u like to move the card to?'))
                     print('\n')

                     #Checking if user made input in lower or upper case.
                     if userInput1==userInput1.lower() or userInput2==userInput2.lower():
                         print('You need to make inputs in upper case')

                     #Using fuctions in class to make move to and from location.
                     a.move_freecell(userInput1, userInput2)

                     #Once an input is made and the function is executed, we print the freecell to show the output
                     print(a)
                     print(a.freecell_pile())

                #If user give an invalid input for a move
                else:
                    print("Sorry, that seems to be an invalid input :-(")

        #If user doesn't read the rules.
        elif ruleInput=="N":
            print("Please read the rules")

        #If user makes an invalid input before the game starts.
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()

