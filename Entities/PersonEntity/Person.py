from . import Family
from . import UtilityFunctions
from . import Data
import copy 
import random

class person(object):
    def __init__(self, id, last_name, age): #first_name="", last_name="", gender="", iq=0, beauty=0, leadership=0
        #Setting up the variables with attributes of the characters
        self.id = id
        self.last_name = last_name 
        self.age = age
        self.age_statuses = ["child", "teenager", "young adult", "middle-aged adult", "older adult", "old adult"]
        self.changeAgeStatus()
        self.health_level = UtilityFunctions.generateRandomHealthLevel()
        self.health_statuses = ["healthy", "a bit ill", "severely ill", "in critical condition"]
        self.changeHealthStatus()
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
        self.family_id = self.family.addMember(self.id)
        #Introduction message with all the basic informations, they will be randomly generated that's why we need this
        print(self.first_name + " " + self.last_name + " just spawned! " + self.pronoun[0].title() + " is " + str(age) + " years old. " + self.pronoun[1].title() + " stats are " + str(self.iq) + " for IQ, " + str(self.beauty) + " for beauty and " + str(self.leadership) + " for leadership. " + self.pronoun[0].title() + " is " + str(self.age) + " years old and is a " + self.age_status + ". " + self.pronoun[1].title() + " health levels are " + str(self.health_level) + " and " + self.pronoun[0] + " is " + self.health_status + ".")
    
    def addYear(self, world):
        self.age += 1
        self.changeAgeStatus()
        alive = self.healthReview(world)
        if alive:
            print("Update: " + self.first_name + " " + self.last_name + " is now " + str(self.age) + " years old and is a " + self.age_status + ". " + self.pronoun[1].title() + " health levels are " + str(self.health_level) + " and " + self.pronoun[0] + " is " + self.health_status + ".")

    def changeAgeStatus(self):
        if self.age >= 0 and self.age < 13:
            self.age_status = self.age_statuses[0]
        elif self.age >= 13 and self.age < 18:
            self.age_status = self.age_statuses[1]
        elif self.age >= 18 and self.age < 30:
            self.age_status = self.age_statuses[2]
        elif self.age >= 30 and self.age < 50:
            self.age_status = self.age_statuses[3]
        elif self.age >= 50 and self.age < 80:
            self.age_status = self.age_statuses[4]
        elif self.age >= 80:
            self.age_status = self.age_statuses[5]
    
    def changeHealthStatus(self):
        if self.health_level >= 80:
            self.health_status = self.health_statuses[0]
        elif self.health_level >=50 and self.health_level < 80:
            self.health_status = self.health_statuses[1]
        elif self.health_level >=20 and self.health_level < 50:
            self.health_status = self.health_statuses[2]
        elif self.health_level >= 0 and self.health_level < 20:
            self.health_status = self.health_statuses[3]

    def healthReview(self, world):
        a = random.random() #first random probability
        b = random.random() #random probability when it comes to health decreasing
        alive = True

        #setting up probabilities of improvement based on age class
        if self.age_status == self.age_statuses[0] or self.age_status == self.age_statuses[1]:
            improv_proba = 0.863
        elif self.age_status == self.age_statuses[2]:
            improv_proba = 0.75
        elif self.age_status == self.age_statuses[3]:
            improv_proba = 0.7
        elif self.age_status == self.age_statuses[4]:
            improv_proba = 0.65
        elif self.age_status == self.age_statuses[5]:
            improv_proba = 0.6

        #setting up probabilities of things worsening based on age class
        if self.age_status == self.age_statuses[0] or self.age_status == self.age_statuses[1]:
            healthy_proba = [0.20, 0.60, 0.80] #20% death 40% small issues 20% bigger issues 20% critical issues
            small_issues_proba = [0.40, 0.70] #40% death 30% bigger issues 30% critical issues
            bigger_issues_proba = [0.60] #60% death 40% critical issues
        elif self.age_status == self.age_statuses[2]:
            healthy_proba = [0.20, 0.55, 0.80] #20% death 35% small issues 25% bigger issues 20% critical issues
            small_issues_proba = [0.40, 0.80] #40% death 40% bigger issues 20% critical issues
            bigger_issues_proba = [0.65] #65% death 35% critical issues
        elif self.age_status == self.age_statuses[3]:
            healthy_proba = [0.25, 0.55, 0.80] #25% death 30% small issues 25% bigger issues 20% critical issues
            small_issues_proba = [0.45, 0.75] #45% death 30% bigger issues 25% critical issues
            bigger_issues_proba = [0.70] #70% death 30% critical issues
        elif self.age_status == self.age_statuses[4]:
            healthy_proba = [0.30, 0.50, 0.75] #30% death 20% small issues 25% bigger issues 25% critical issues
            small_issues_proba = [0.50, 0.70] #50% death 20% bigger issues 30% critical issues
            bigger_issues_proba = [0.75] #75% death 25% critical issues
        elif self.age_status == self.age_statuses[5]:
            healthy_proba = [0.40, 0.55, 0.70] #40% death 15% small issues 15% bigger issues 30% critical issues
            small_issues_proba = [0.55, 0.75] #55% death 20% bigger issues 25% critical issues
            bigger_issues_proba = [0.80] #80% death 20% critical issues

        #improvements for small issues, bigger issues and critical health conditions
        if a <= improv_proba:
            if (self.health_status == self.health_statuses[1]):
                self.health_level = random.randint(80, 100) 
            elif (self.health_status == self.health_statuses[2]):
                self.health_level = random.randint(50, 80)
            elif (self.health_status == self.health_statuses[3]):
                self.health_level = random.randint(20, 50)

        #health levels are getting worse
        elif a > improv_proba:
            if (self.health_status == self.health_statuses[0]):
                if b <= healthy_proba[0]:
                    self.deathProcess(world)
                    alive = False
                elif b > healthy_proba[0] and b <= healthy_proba[1]:
                    self.health_level = random.randint(50, 80)
                elif b > healthy_proba[1] and b <= healthy_proba[2]:
                    self.health_level = random.randint(20, 50)
                elif b > healthy_proba[2]:
                    self.health_level = random.randint(0, 20)
            elif (self.health_status == self.health_statuses[1]):
                if b <= small_issues_proba[0]:
                    self.deathProcess(world)
                    alive = False
                elif b > small_issues_proba[0] and b <= small_issues_proba[1]:
                    self.health_level = random.randint(20, 50)
                elif b > small_issues_proba[1]:
                    self.health_level = random.randint(0,20)
            elif (self.health_status == self.health_statuses[2]):
                if b <= bigger_issues_proba[0]:
                    self.deathProcess(world)
                    alive = False
                elif b > bigger_issues_proba[0]:
                    self.health_level = random.randint(0,20)
            elif (self.health_status == self.health_statuses[3]):
                self.deathProcess(world)
                alive = False
        
        if alive: #updating health status after the changes for all alive people
            self.changeHealthStatus()
        return alive

    def deathProcess(self, world):
        self.chooseCauseOfDeath()
        del(world.entities_members[self.id])
        world.deaths += 1

    def chooseCauseOfDeath(self):
        accidental_causes = [" fell after climbing a tree", " got run over by a truck", "choked on the first bite of a hamburger", "was trapped in " + self.pronoun[1] + " burning house after overcooking pasta", "was knocked over by wind, " + self.pronoun[0] + " fell into a lake"]
        medical_causes = ["cancer", "asthma"]
        if self.health_status == self.health_statuses[3]:
            cause = UtilityFunctions.chooseRandomItemInArray(medical_causes)
            print("Update: " + self.first_name + " " + self.last_name + " died from " + cause + ".")
        else:
            cause = UtilityFunctions.chooseRandomItemInArray(accidental_causes)
            print("Update: " + self.first_name + " " + self.last_name + cause + " and died.")

    def reproductionProcess(self, world):#TODO change this to adapt it to couple
        partner = self.findPartner(world) #TODO move the process of finding a partner to another function
        if partner != False:
            self.childCreation(partner, world)

    def findPartner(self, world):#world is passed through to help us access all entities
        partner_list = copy.deepcopy(world.entities_members)
        partner = UtilityFunctions.chooseRandomItemInArray(partner_list)
        partner_list.remove(partner)
        while (self.gender == partner.gender or not self.partnerCompatibilityTest(partner)) and len(partner_list) > 0: #no need to check that partner is not self because we are making sure that the gender between two partners is different 
            partner = UtilityFunctions.chooseRandomItemInArray(partner_list)
            partner_list.remove(partner)
        if len(partner_list) <= 0:
            print("No partner available!")
            return False
        print("Partner found... " + partner.first_name + " " + partner.last_name + " for " + self.first_name + " " + self.last_name + ".")
        couple_last_name = ""
        #changing last name of the wife and create family
        if self.gender == "female":
            del(world.entities_members[self.id].family)
            print("Family of " + self.first_name + " " + self.last_name + " deleted...")
            world.entities_members[self.id].last_name = partner.last_name
            couple_last_name = partner.last_name
            world.entities_members[self.id].family_id = world.entities_members[partner.id].family.addMember(self.id)
        else:
            del(world.entities_members[partner.id].family)
            print("Family of " + partner.first_name + " " + partner.last_name + " deleted...")
            world.entities_members[partner.id].last_name = self.last_name
            couple_last_name = self.last_name
            world.entities_members[partner.id].family_id = world.entities_members[self.id].family.addMember(partner.id)
        print("They are together and now called " + self.first_name + " and " + partner.first_name + " " + couple_last_name + ".") #TODO add married status in a person attribute
        return partner

    def partnerCompatibilityTest(self, partner):
        compatibility = self.beauty - partner.beauty
        print("Compatibility for " + self.first_name + " " + self.last_name + " and " + partner.first_name + " " + partner.last_name + ": " + str(compatibility))
        if compatibility >= -30 and compatibility <= 30:
            return True 
        else:
            return False

    def childCreation(self, partner, world): #spawns a child and adds it to the family
        if self.gender == "male":
            main_parent = self
            other_parent = partner
        elif partner.gender == "male":
            main_parent = partner
            other_parent = self 
        world.addEntity(main_parent.last_name, 0) #TODO Add a way to append "Jr." to the kid's first name if they have the as their parent
        kid = world.entities_members[len(world.entities_members)-1]
        kid.family_id = world.entities_members[main_parent.id].family.addMember(kid.id)
        print(kid.first_name + " is in the " + kid.last_name + " family and " + kid.pronoun[1] + " dad is " + main_parent.first_name + " and " + kid.pronoun[1] + " mom is " + other_parent.first_name + ".")
        main_parent.family.listMembers(world)