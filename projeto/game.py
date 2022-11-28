import pygame
from entity import Entity

class Game:
    def __init__(self, title, width, height, scale, fps):
        # Initialize pygame
        pygame.init()
        
        self.display = pygame.display.set_mode((width * scale, height * scale))
        # self.display.set_caption(title)
        print((width * scale, height * scale))
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.my_entity = Entity(self.display)
        
    
    def run(self):
        while True:
            # Game loop
            
            # Handle events test
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("Up key pressed")
            
            
            # Display Graphics
            self.display.fill("gray")
        

            self.my_entity.update()

            # update window
            pygame.display.flip()
            self.clock.tick(self.fps)
        
    