from entity import Entity
from command import *
import pygame

COMMANDS = {
    pygame.K_UP: Jump,
    pygame.K_LEFT: MoveLeft,
    pygame.K_RIGHT: MoveRight
}

class Player(Entity):
    
    def __init__(self, display_ref):
        super().__init__(display_ref)
        self.commands = COMMANDS
        
        for command in self.commands:
            self.commands[command] = self.commands[command](self)
        