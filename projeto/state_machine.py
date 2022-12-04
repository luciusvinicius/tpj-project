from state import State


class StateMachine:
    def __init__(self, initial_state: str, states: dict[str, tuple[State, list[str]]]):
        # States should be a dictionary with the following structure:
        # {
        #     "state_name": (State, ["possible_state_1", "possible_state_2", ...])
        # }

        self.states = states
        self.current_state = self.states[initial_state][0]

    def update(self):
        self.current_state.update()

    def change_state(self, new_state: str) -> bool:
        if new_state == self.current_state.state_name:
            return False
        self.current_state.exit()
        possible_states = self.states[self.current_state.state_name][1]
        if new_state in possible_states:  # if on possible states
            self.current_state = self.states[new_state][0]
            self.current_state.enter()
            return True
        return False
