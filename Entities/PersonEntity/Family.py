class family(object):
    def __init__(self, last_name):
        self.members = []
        self.last_name = last_name 
    #create the family based on the last name
    def addMember(self, id):
        self.members.append(id)
        return len(self.members) - 1
    #we will only take the characters id that we can pass in later to the world object
    def listMembers(self, world):
        print("Current " + self.last_name + " family member list:")
        for i in range(len(self.members)):
            print(str(i + 1) + ". " + world.entities_members[self.members[i]].first_name + " " + world.entities_members[self.members[i]].last_name)
    #list characters based on their ids and the world object