class person(object):
    def __init__(self, first_name, last_name, gender, iq, beauty, leadership):
        #Setting up the variables with attributes of the characters
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender #genders are needed for reproduction
        self.iq = iq #will help determine which innovation a character will choose, the smarter he is the smarter choices he'll makee
        self.beauty = beauty #determines the attractivity of a character and how likely they are to find a partner
        self.leadership = leadership #will help determine who's going to the top and how much the character's vote counts
        #TODO create hunger and thirst attributes and a way for characters to eat

        #Set the pronouns to use throughout the game when describing the characters, the pronoun array will be referencesd throughout the game
        pronoun = []
        if gender == "male":
            pronoun = ["he", "his", "him"]
        elif gender == "female":
            pronoun = ["she", "her", "her"]
        
        #Introduction message with all the basic informations, they will be randomly generated that's why we need this
        print(first_name + " " + last_name + " is born! " + pronoun[1].title() + " stats are " + iq + " for IQ, " + beauty + " for beauty and " + leadership + " for leadership.")