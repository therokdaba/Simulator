from . import Family
from . import UtilityFunctions
from . import Data

class person(object):
    def __init__(self, id): #first_name="", last_name="", gender="", iq=0, beauty=0, leadership=0
        #Setting up the variables with attributes of the characters
        self.id = id
        self.last_name = UtilityFunctions.chooseRandomItemInArray(Data.last_name_list)
        Data.last_name_list.remove(self.last_name)
        self.gender = UtilityFunctions.chooseRandomItemInArray(Data.genders) #genders are needed for reproduction
        self.iq = UtilityFunctions.generateRandomIQ() #will help determine which innovation a character will choose, the smarter he is the smarter choices he'll makee
        self.beauty = UtilityFunctions.generateRandomStatValue(100) #determines the attractivity of a character and how likely they are to find a partner
        self.leadership = UtilityFunctions.generateRandomStatValue(100) #will help determine who's going to the top and how much the character's vote counts
        #TODO create hunger and thirst attributes and a way for characters to eat
        
        #Set the pronouns to use throughout the game when describing the characters, the pronoun array will be referencesd throughout the game
        self.pronoun = []
        if self.gender == "male":
            self.pronoun = ["he", "his", "him"]
            self.first_name = UtilityFunctions.chooseRandomItemInArray(Data.male_first_name_list)
        elif self.gender == "female":
            self.pronoun = ["she", "her", "her"]
            self.first_name = UtilityFunctions.chooseRandomItemInArray(Data.female_first_name_list)
        family = Family.family(self.last_name)
        family.addMember(self.first_name)
        #Introduction message with all the basic informations, they will be randomly generated that's why we need this
        print(self.first_name + " " + self.last_name + " is born! " + self.pronoun[1].title() + " stats are " + str(self.iq) + " for IQ, " + str(self.beauty) + " for beauty and " + str(self.leadership) + " for leadership. ")