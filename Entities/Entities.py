from Entities.PersonEntity import Person
from Entities.PersonEntity import UtilityFunctions
from Entities.PersonEntity import Data

class entities(object):
    def __init__(self):
        self.entities_members = []
        self.year = 2021
        self.births = 0
        self.deaths = 0

    def addEntity(self, last_name="", age=0):
        if last_name == "":
            last_name = UtilityFunctions.chooseRandomItemInArray(Data.last_name_list)
            age = 25
        self.entities_members.append(Person.person(len(self.entities_members), last_name, age))
        self.births += 1
    
    def listEntities(self):
        print("Current member list:")
        for i in range(len(self.entities_members)):
            print(str(i + 1) + ". " + self.entities_members[i].first_name + " " + self.entities_members[i].last_name)

    def newYear(self):
        self.year += 1
        for entity in self.entities_members:
            entity.addYear(self)
        print("Happy New Year! We are now in " + str(self.year) + "!")