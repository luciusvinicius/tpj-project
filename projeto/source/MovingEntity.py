from entity import Entity


class MovingEntity(Entity):

    def __init__(self, display_ref, speed_x=1, speed_y=1, gravity=0.5):
        super().__init__(display_ref)
        self.speed = [speed_x, speed_y]
        self.direction = [0, 0]
        self.gravity = gravity

    def update(self):
        super().update()
        self._physics.update(self.pos, self.speed, self.direction, self.gravity)