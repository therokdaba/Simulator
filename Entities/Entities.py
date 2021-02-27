from Entities.PersonEntity import Person
from Entities.PersonEntity import UtilityFunctions
from Entities.PersonEntity import Data

class entities(object):
    def __init__(self):
        self.entities_members = []

    def addEntity(self, last_name=""):
        if last_name == "":
            last_name = UtilityFunctions.chooseRandomItemInArray(Data.last_name_list)
        self.entities_members.append(Person.person(len(self.entities_members), last_name))
    
    def listEntities(self):
        print("Current member list:")
        for i in range(len(self.entities_members)):
            print(str(i + 1) + ". " + self.entities_members[i].first_name + " " + self.entities_members[i].last_name)