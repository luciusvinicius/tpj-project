from image_loader import*

class GraphicsComponent:
    def __init__(self, image_path):
        self.actor_ref = None
        self.is_setted_up = False
        self.sprite_sheet_image = ImageLoader.get_instance().image_dict[image_path]

    def set_up(self, actor):
        self.actor_ref = actor
        self.is_setted_up = True
    
    def render(self):
        if self.is_setted_up:
            self.actor_ref.engine_ref.display.blit(self.sprite_sheet_image, (self.actor_ref.pos[0], -self.actor_ref.pos[1]))