from . import Family
from . import UtilityFunctions
from . import Data

class person(object):
    def __init__(self, id, last_name): #first_name="", last_name="", gender="", iq=0, beauty=0, leadership=0
        #Setting up the variables with attributes of the characters
        self.id = id
        self.last_name = last_name 
        if last_name in Data.last_name_list:
            Data.last_name_list.remove(self.last_name)
        self.gender = UtilityFunctions.chooseRandomItemInArray(Data.genders) #genders are needed for reproduction
        self.iq = UtilityFunctions.generateRandomIQ() #will help determine which innovation a character will choose, the smarter he is the smarter choices he'll makee
        self.beauty = UtilityFunctions.generateRandomStatValue(100) #determines the attractivity of a character and how likely they are to find a partner
        self.leadership = UtilityFunctions.generateRandomStatValue(100) #will help determine who's going to the top and how much the character's vote counts
        
        #Set the pronouns to use throughout the game when describing the characters, the pronoun array will be referencesd throughout the game
        self.pronoun = []
        if self.gender == "male":
            self.pronoun = ["he", "his", "him"]
            self.first_name = UtilityFunctions.chooseRandomItemInArray(Data.male_first_name_list) #TODO can't have the same name as the parent
        elif self.gender == "female":
            self.pronoun = ["she", "her", "her"]
            self.first_name = UtilityFunctions.chooseRandomItemInArray(Data.female_first_name_list)
        self.family = Family.family(self.last_name)
        self.family.addMember(self.id)
        #Introduction message with all the basic informations, they will be randomly generated that's why we need this
        print(self.first_name + " " + self.last_name + " is born! " + self.pronoun[1].title() + " stats are " + str(self.iq) + " for IQ, " + str(self.beauty) + " for beauty and " + str(self.leadership) + " for leadership. ")
    
    def reproductionProcess(self, world):#TODO change this to adapt it to couple
        partner = self.findPartner(world) #TODO move the process of finding a partner to another function
        self.childCreation(partner, world)

    def findPartner(self, world):#world is passed through to help us access all entities
        partner = UtilityFunctions.chooseRandomItemInArray(world.entities_members)
        while self.gender == partner.gender: #TODO check if we can change that into a do while
            partner = UtilityFunctions.chooseRandomItemInArray(world.entities_members)
        print("Partner found..." + partner.first_name + " " + partner.last_name + " for " + self.first_name + " " + self.last_name + ".")
        couple_last_name = ""
        #changing last name of the wife and create family
        if self.gender == "female":
            self.last_name = partner.last_name
            couple_last_name = partner.last_name
            partner.family.addMember(self.id)
        else:
            partner.last_name = self.last_name
            couple_last_name = self.last_name
            self.family.addMember(partner.id)
        #TODO delete the wifes family, research how to delete an object
        print("They are married and now called " + self.first_name + " and " + partner.first_name + " " + couple_last_name + ".") #TODO add married status in a person attribute
        return partner

    def childCreation(self, partner, world): #spawns a child and adds it to the family
        if self.gender == "male":
            main_parent = self
            other_parent = partner
        elif partner.gender == "male":
            main_parent = partner
            other_parent = self 
        world.addEntity(main_parent.last_name) #Add a way to append "Jr." to the kid's first name if they have the as their parent
        kid = world.entities_members[len(world.entities_members)-1]
        main_parent.family.addMember(kid.id)
        print(kid.first_name + " is in the " + kid.last_name + " family and " + kid.pronoun[1] + " dad is " + main_parent.first_name + " and " + kid.pronoun[1] + " mom is " + other_parent.first_name + ".")
        main_parent.family.listMembers(world)