import pygame
from entity import Entity
from player import Player
from command import Command


class Game:

    def __init__(self, title, width, height, scale, fps):
        # Initialize pygame
        pygame.init()
        
        self.display = pygame.display.set_mode((width * scale, height * scale))
        # self.display.set_caption(title)
        print((width * scale, height * scale))
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.player = Player(self.display)
        self.objs = [self.player]

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == pygame.KEYDOWN:
                if event.key in self.player.commands:
                    self.player.commands[event.key].execute()

    def logic_loop(self):
        self.player.horizontal_state_machine.update()
        # self.player.vertical_state_machine.update()
        # print(self.objs)
        
    def render_loop(self):
        self.display.fill("gray")
        
    
    def run(self): # Game loop
        while True:
            # Temporary
            # print(f"Game inputs: {Game.INPUTS_EVENT}")
            # pygame.event.post(self.inputs_ev)
            # pygame.event.post(self.graphics_ev)

            # Handle events test
            self.event_loop()                
            self.logic_loop()
            self.render_loop()
            # update window
            pygame.display.flip()
            self.clock.tick(self.fps)
        
    