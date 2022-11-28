
class Command:
    def execute(self):
        raise NotImplementedError("You must implement the execute() method in the derived class!")
    

class Jump(Command):
    def __init__(self, player):
        self.player = player
        
    def execute(self):
        self.player.jump()

class MoveRight(Command):
    def __init__(self, player):
        self.player = player
        
    def execute(self):
        self.player.move((1, 0))

class MoveLeft(Command):
    def __init__(self, player):
        self.player = player
        
    def execute(self):
        self.player.move((-1, 0))