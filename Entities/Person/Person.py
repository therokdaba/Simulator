from . import UtilityFunctions
from . import Data

class person(object):
    def __init__(self, first_name="", last_name="", gender="", iq=0, beauty=0, leadership=0):
        #Setting up the variables with attributes of the characters
        self.last_name = last_name 
        last_name = UtilityFunctions.chooseRandomItemInArray(Data.last_name_list)
        self.gender = gender
        gender = UtilityFunctions.chooseRandomItemInArray(Data.genders) #genders are needed for reproduction
        self.iq = iq
        iq = UtilityFunctions.generateRandomIQ() #will help determine which innovation a character will choose, the smarter he is the smarter choices he'll makee
        self.beauty = beauty
        beauty = UtilityFunctions.generateRandomStatValue(100) #determines the attractivity of a character and how likely they are to find a partner
        self.leadership = leadership
        leadership = UtilityFunctions.generateRandomStatValue(100) #will help determine who's going to the top and how much the character's vote counts
        #TODO create hunger and thirst attributes and a way for characters to eat
        
        #Set the pronouns to use throughout the game when describing the characters, the pronoun array will be referencesd throughout the game
        pronoun = []
        if gender == "male":
            pronoun = ["he", "his", "him"]
            first_name = UtilityFunctions.chooseRandomItemInArray(Data.male_first_name_list)
        elif gender == "female":
            pronoun = ["she", "her", "her"]
            first_name = UtilityFunctions.chooseRandomItemInArray(Data.female_first_name_list)
        
        #Introduction message with all the basic informations, they will be randomly generated that's why we need this
        print(first_name + " " + last_name + " is born! " + pronoun[1].title() + " stats are " + str(iq) + " for IQ, " + str(beauty) + " for beauty and " + str(leadership) + " for leadership.")