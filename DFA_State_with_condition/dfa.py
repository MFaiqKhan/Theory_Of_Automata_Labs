class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'} # set of states, this is a dictionary of states
        self.accept_states = {'q3'} # set of accept states, accept means if the string is valid or not
            # defined as 'state' : ('input_character', 'next_state') 
        self.transitions = {
            ('q0', '0'): 'q1', # transition from q0 to q1 with input 0
            ('q0', '1'): 'q2', # transition from q0 to q2 with input 1
            ('q1', '0'): 'q0', # transition from q1 to q0 with input 0
            ('q1', '1'): 'q3', # transition from q1 to q3 with input 1
            ('q2', '0'): 'q3', # transition from q2 to q3 with input 0
            ('q2', '1'): 'q0', # transition from q2 to q0 with input 1
            ('q3', '0'): 'q2', # transition from q3 to q2 with input 0
            ('q3', '1'): 'q1', # transition from q3 to q1 with input 1 
        }

        
        self.start_state = 'q0' # start state

    def process(self, input_string):
        state = self.start_state
        for char in input_string:
            if (state, char) in self.transitions:
                state = self.transitions[(state, char)] 
            else:
                return False
        return state in self.accept_states


dfa = DFA()
input_string = input("Enter a string: ")
if dfa.process(input_string):
    print("String is accepted")
else:
    print("String is not accepted")
    
