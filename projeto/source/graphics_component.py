from image_loader import*
import pygame as pg

class GraphicsComponent:
    def __init__(self, engine_ref, image_path, scale=[1, 1], speed=40, layer=0):
        self.engine_ref = engine_ref
        self.actor_ref = None
        self.scale = scale
        self.is_set_up = False
        self.flip_X = False
        self.flip_Y = False
        self.layer = layer

        # Image vars 
        self.sprite_sheet_image = ImageLoader.get_instance().image_dict[image_path]
        self.img_size = [self.sprite_sheet_image.get_width(), self.sprite_sheet_image.get_height()]
        self.sprite_sheet_image = self.scale_images(self.sprite_sheet_image, self.img_size, self.scale, True)

        # Animation vars
        self.is_animated = False
        self.all_animations = {}
        self.current_anim = None
        self.anim_frame = 0
        self.anim_speed = speed  # Overall speed. +anim_speed -> slower anim. Speed<=17 -> 1 anim frame per game frame. 1000ms/60fps ~= 17.
        self.anim_counter = 0

    def set_up(self, actor):
        self.actor_ref = actor
        self.is_set_up = True

    # "animations" parameter example: [["idle", [0, 5], true, 10], [...]]. Order is: "name, frame numbers, is_loopable, speed"
    def set_up_animations(self, animations: list[list[str, list[int, int], bool, int]], frame_size: list[int, int],
                          sheet_size: list[int, int]):
        self.is_animated = True

        # Scale back in case the image was "inited" with a non 1 scale value
        temp_img_size = [self.sprite_sheet_image.get_width(), self.sprite_sheet_image.get_height()] 
        self.sprite_sheet_image = self.scale_images(self.sprite_sheet_image, temp_img_size, self.scale, False)

        temp_spritesheet = SpriteSheet(self.sprite_sheet_image)

        for animation in animations:
            temp_img_list = []

            # Range does not include the last element, hence the +1
            for frame_nmbr in range(animation[1][0], animation[1][1] + 1):
                # print(frame_nmbr)
                pos = self.get_pos(sheet_size, frame_nmbr)
                temp_img_list.append(temp_spritesheet.get_image(pos, frame_size, self.scale))

            self.all_animations[animation[0]] = Animation(animation[0], temp_img_list, animation[2], animation[3])

        # After "all_animations" is set up, access the first element using string as a key. [0][0] is the name of the first animation
        self.current_anim = self.all_animations[animations[0][0]]
        
    def change_animation(self, anim_string):
        if anim_string in self.all_animations.keys():
            self.current_anim = self.all_animations[anim_string]
            self.anim_frame = 0
            self.anim_counter = 0

    def render(self):
        if self.is_set_up:

            img_to_render = self.sprite_sheet_image

            if self.is_animated:
                # Animations will play at the set rate independent of frame rate
                self.anim_counter += self.engine_ref.clock.get_time()
                if self.anim_counter >= self.anim_speed + self.current_anim.speed:
                    self.anim_frame +=1
                    self.anim_counter = 0

                    # Setting up loop animation     
                    if self.anim_frame >= len(self.current_anim.frames):
                        if self.current_anim.loopable:
                            self.anim_frame = 0
                        else:
                            self.anim_frame -=1
                        
                img_to_render = self.current_anim.frames[self.anim_frame]

            img_to_render = pg.transform.flip(img_to_render, self.flip_X, self.flip_Y)
            img_to_render.set_colorkey(pg.Color(0, 0, 0)) # Need to colorkey once again the returned flipped image
            self.actor_ref.engine_ref.display.blit(img_to_render, (self.actor_ref.pos[0], -self.actor_ref.pos[1]))
  
    def scale_images(self, img, size, scale_ref, scale_up):
        # Scale up or down using the same positive values
        if scale_up:
            scale = scale_ref
        else:
            scale = [1 / scale_ref[0], 1 / scale_ref[1]]
        
        image = pg.transform.scale(img, (size[0] * scale[0], size[1] * scale[1]))
        return image

    def get_pos(self, size, frame_nmbr):

        y, x = divmod(frame_nmbr, size[0])

        if y >= size[1]:
            raise ValueError("Animation y coordinates are outside of range!")

        #print([x, y])
        return [x, y]

        
class SpriteSheet():
    def __init__(self, image):
        self.image_ref = image
        
    def get_image(self, pos, size, scale):
        image = pg.Surface((size[0], size[1])).convert_alpha()
        image.blit(self.image_ref, (0, 0), ((pos[0] * size[0]), (pos[1] * size[1]), size[0], size[1]))
        image = pg.transform.scale(image, (size[0] * scale[0], size[1] * scale[1]))
        image.set_colorkey(pg.Color(0, 0, 0))

        return image
        

class Animation():
    def __init__(self, name, frames, loopable, speed):
        self.name = name
        self.frames = frames
        self.loopable = loopable
        self.speed = speed # Modifier to overall speed of component
        