class family(object):
    def __init__(self, last_name):
        self.members = []
        self.last_name = last_name 
    
    def addMember(self, first_name):
        self.members.append(first_name)