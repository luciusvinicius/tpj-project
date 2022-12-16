class State:
    def __init__(self, state_name, obj):
        self.state_name = state_name
        self.obj = obj
    
    def enter(self):
        pass
    
    def update(self):
        pass
    
    def exit(self):
        pass
    