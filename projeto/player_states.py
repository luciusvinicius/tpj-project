from state import State

class IdleState(State):
    def __init__(self, state_name):
        super().__init__(state_name)
        
    def enter(self):
        print("Entering Idle State")
        
    def update(self):
        print("Updating Idle State")
        
    def exit(self):
        print("Exiting Idle State")

class RunningState(State):
    def __init__(self, state_name):
        super().__init__(state_name)
        
    def enter(self):
        print("Entering Running State")
        
    def update(self):
        print("Updating Running State")
        
    def exit(self):
        print("Exiting Running State")
        
class JumpingState(State):
    def __init__(self, state_name):
        super().__init__(state_name)
    
    def enter(self):
        return super().enter()
    
    def update(self):
        return super().update()
    
    def exit(self):
        return super().exit()