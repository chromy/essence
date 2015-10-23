import essence

class Position(essence.Component):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PhysicsSystem(essence.System):
    def __init__(self, gravity):
        self.gravity = gravity

    def update(self, world):
        for e in world.entites:
            e.get(Position).y -= self.gravity

class RenderSystem(essence.System):
    def update(self, world):
        for e in world.entites:
            # Render entity...

if __name__ == '__main__':
    world = essence.World()
    world.systems.append(PhysicsSystem(2))
    world.systems.append(RenderSystem(2))

    player = world.create_entity()
    player.add(Position(10, 10))

    while True:
        world.update()

