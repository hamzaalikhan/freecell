#The first class of the assignment
#Designed to create a card
class Card:

    #Constructor
    #Initial method for object creation
    #Intialise the value of the instance attributes
    def __init__(self,face,suit):

        #Instance attributes
        self.card_face = face
        self.card_suit = suit

    #Prints the internal value of the objects in form of a string
    #Prints out a card
    def __str__(self):
        return self.card_face+':'+self.card_suit

    #Accessors
    #To get access to the instance attribute
    #Since instance attributes are local to the class
    #Used to get access to a card face and a card suit.
    def get_face(self):
        return self.card_face

    def get_suit(self):
        return self.card_suit