from Entities import Entities
from Entities.PersonEntity import UtilityFunctions

if __name__ == "__main__":
    world = Entities.entities()
    for i in range(6):
        world.addEntity()
    world.listEntities()
    UtilityFunctions.chooseRandomItemInArray(world.entities_members).reproductionProcess(world)
    world.listEntities()
    #TODO add more space and clean up the output process