from Entities import Entities

if __name__ == "__main__":
    world = Entities.entities()
    for i in range(6):
        world.addEntity()
    world.listEntities()