from Entities.PersonEntity import Person

class entities(object):
    def __init__(self, *kwargs):
        self.entities_members = []

    def addEntity(self):
        self.entities_members.append(Person.person(len(self.entities_members)))
    
    def listEntities(self):
        print("Current member list:")
        for i in range(len(self.entities_members)):
            print(str(self.entities_members[i].id + 1) + ". " + self.entities_members[i].first_name + " " + self.entities_members[i].last_name)