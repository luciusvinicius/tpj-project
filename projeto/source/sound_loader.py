import os
import pygame as pg


class SoundLoader:
    __instance = None
    sound_path = None

    @staticmethod
    def get_instance():
        if SoundLoader.__instance is None:
            SoundLoader()
        return SoundLoader.__instance
    
    @staticmethod 
    def has_instance():
        return SoundLoader.__instance is not None

    def __init__(self, sound_path):
        if SoundLoader.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SoundLoader.__instance = self
            SoundLoader.sound_path = sound_path
            self.sound_dict = {}
            self.load_sounds()

    def load_sounds(self):
        for sound in os.listdir(self.sound_path):
            self.sound_dict[sound] = pg.mixer.Sound(os.path.join(self.sound_path, sound))

    def play_sound(self, sound_name, volume=0.5):
        self.sound_dict[sound_name].play()
        self.sound_dict[sound_name].set_volume(volume)
        
    def play_bgm(self, bgm_path, volume=0.5):
        path = SoundLoader.sound_path
        pg.mixer.music.load(os.path.join(path, f"{bgm_path}"))
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(volume)

    def get_path(self):
        return self.sound_path
