from Entities import Entities
from Entities.PersonEntity import UtilityFunctions

if __name__ == "__main__":
    world = Entities.entities()
    for i in range(7):
        world.addEntity()
    world.listEntities()
    for i in range(100):
        UtilityFunctions.chooseRandomItemInArray(world.entities_members).reproductionProcess(world)
        world.newYear()
    percentage = (world.deaths / world.births) * 100
    world.listEntities()
    print("Percentage of death: " + str(percentage))
    #TODO add more space and clean up the output processf