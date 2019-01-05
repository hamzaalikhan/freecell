#Importing class Card that will be used to make the deck
import random
from card import Card

#The second class of the assignment
#Designed to create deck using 52 card
#The class has the ability to shuffle all cards once they are in the deck
class Deck():

    #Class attribute
    #Global in scope and can be accessed inside or outside the class
    #Constant values
    suitname = ["H", "S", "D", "C"]
    facename = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']

    #Constructor
    #Initial method for object creation
    #Intialise the value of the instance attributes
    #Contains the Instance attributes
    #value_start defines the first card face in the deck
    #value_end defines the last card face in the deck
    #number_of_suit defines how many suits will be available in the deck
    #theDeck defines the consturcted deck using the instance attributes
    def __init__(self,value_start, value_end, number_of_suits):
        self.value_start = value_start
        self.value_end = value_end
        self.number_of_suits = number_of_suits
        self.theDeck = []

    #Prints the internal value of the objects in form of a string
    #Returns the constructed deck
    def __str__(self):
        return str(self.theDeck)

    #Accessors
    #To get access to the instance attribute
    #Since instance attributes are local to the class
    #Used to get access to the deck
    def get_deck(self):
        return self.theDeck


    #function to generate the deck
    #Nested while loop that iterates to add card object to the deck.
    #First while loop iterates according to the suit entry
    #Second while loop iterates according to the start and end value of the card face.
    #The deck obtained contains objects of type card.
    def deck_generator(self):
        i = 0
        while i < self.number_of_suits:
            j = self.value_start - 1
            while j < self.value_end:
                self.theDeck.append(Card(self.facename[j], self.suitname[i]))
                j += 1
            i += 1

    #Function that takes in any list and shuffles the objects inside the list
    #For the sake of this assignment the fucntion will shuffle the cards in the deck
    def deck_shuffle(self,x):
        random.shuffle(x)

    #Fuction that checks if a list has an object, if it does it simply removes it.
    #Otherwise returns false
    def remove_card(self,theList):
        if len(theList)>=0:
            theList.pop()
        else:
            return False

    #Function that simply adds objects to a list
    #For the sake of this assignment it may add a card to a cell, pile or a foundation.
    def addcard(self,theCard,theList):
        theList.append(theCard)


