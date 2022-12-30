
# Description: This file contains the SignalManager class, which is responsible for handling signals from the engine.
# Example of structure:
# {
#   "signal_name": [target1, target2, target3, ...]
# }

from actor import Actor

class SignalManager:
    
    __instance = None
    
    @staticmethod
    def get_instance():
        if SignalManager.__instance is None:
            SignalManager()
        return SignalManager.__instance
    
    def __init__(self):
        if SignalManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SignalManager.__instance = self
            self.signals = {}
    
    def listen_to_signal(self, signal_name, actor: Actor):
        if signal_name not in self.signals:
            self.signals[signal_name] = []
        self.signals[signal_name].append(actor)
    
    def send_signal(self, signal_name, *args):
        if signal_name in self.signals:
            for actor in self.signals[signal_name]:
                actor.on_signal(signal_name, *args)
                
    def unlisten_to_signal(self, signal_name, actor: Actor):
        if signal_name in self.signals:
            for a in self.signals[signal_name]:
                if a.id == actor.id:
                    self.signals[signal_name].remove(a)
                    break
    