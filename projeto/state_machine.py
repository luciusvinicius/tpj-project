from state import State

class StateMachine:
    def __init__(self, initial_state: State):
        self.current_state = initial_state
    
    def update(self):
        self.current_state.update()
        
    def change_state(self, new_state: State):
        self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()
        
    