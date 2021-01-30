from Entities import Entities

if __name__ == "__main__":
    world = Entities.entities()
    first_entity = world.addEntity()
    second_entity = world.addEntity()
    world.listEntities()