from actor import Actor
from signal_manager import SignalManager
from time import time
from sound_loader import SoundLoader

class Pow(Actor):
    
    MAXIMUM_HITS = 3
    MINIMUM_TIME_BETWEEN_HITS = 0.5
    
    def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1]):
        super().__init__(engine, components, init_pos, init_scale)
        
        self.name = "Pow"
        self.n_hits = 0
        self.previous_hit_time = time() # Used to prevent multiple hits in a short time
    
    def hit(self):
        current_time = time()
        if current_time - self.previous_hit_time < Pow.MINIMUM_TIME_BETWEEN_HITS:
            self.previous_hit_time = current_time
            return
        
        
        signal_manager = SignalManager.get_instance()
        signal_manager.send_signal("pow_hit", self)
        
        self.n_hits += 1
        self.previous_hit_time = current_time
        
        if self.n_hits >= Pow.MAXIMUM_HITS:
            self.remove_from_engine()
        
        SoundLoader.get_instance().play_sound("pow.mp3", 0.3)
        
    
    
    