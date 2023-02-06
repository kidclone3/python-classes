# source: https://www.geeksforgeeks.org/converting-epsilon-nfa-to-dfa-using-python-and-graphviz/

import json
from typing import KeysView, List, Dict

from graphviz import Digraph
from prettytable import PrettyTable


class DFA:
    def __init__(
        self, states: List, alphabets: List, start: str, finals: List, transitions: Dict
    ) -> None:
        self.states = sorted(states)

        self.alphabets = sorted(alphabets)
        # Add epsilon as alphabet.
        # self.alphabets.append("e")

        self.start = start

        assert start in states, "Start state is not in the states"
        self.start_index = self.states.index(start)

        self.finals = finals

        self.transitions = transitions

        self.graph = Digraph()

        self.check()


    def check(self):
        # Check if the DFA is valid

        # Check if the final states are in the states
        for final in self.finals:
            assert final in self.finals, f"Final state {final} is not in the states"

        # Check if the transition table is valid
        for state in self.transitions:
            assert state in self.states, f"State {state} is not in the states"
            for alphabet in self.alphabets:
                assert alphabet in self.alphabets, f"Alphabet {alphabet} is not in the alphabets"
                assert self.transitions[state][alphabet] in self.states, f"Transition [{state}][{alphabet}] -> {transitions[state][alphabet]} is not in the states"
    # Method to represent quintuple
    def __repr__(self):
        return (
            "S : "
            + str(self.states)
            + "\nΣ : "
            + str(self.alphabets)
            + "\nS0 : "
            + str(self.start)
            + "\nδ : \n"
            + str(self.transitions)
            + "\nF : "
            + str(self.finals)
        )

    def state_list_to_string(self, state_list):
        # Convert list of states to string
        # Example: [1, 2, 3] -> {1,2,3}
        if type(state_list) != list:
            state_list = [state_list]
        return "{"+",".join(state_list)+"}"

    def table(self):
        header = ["", "States"] + self.alphabets
        self.dfa_table = PrettyTable(header)
        for state in self.states:
            row = list()
            if self.start == state:
                row.append("->")
            elif state in self.finals:
                row.append("*")
            else:
                row.append("")
            row.append(state)
            for alphabet in self.alphabets:
                row.append(self.transitions[state][alphabet])
            self.dfa_table.add_row(row)
        print(self.dfa_table)

    def draw_graph(self):
        for state in self.states:
        # If state is not a final state, then border shape is single circle
        # Else it is double circle
            if state not in self.finals:
                self.graph.attr("node", shape="circle")
            else:
                self.graph.attr("node", shape="doublecircle")
            self.graph.node(state)

        # Adding start state arrow in DFA diagram
        self.graph.attr("node", shape="none")
        self.graph.node("")
        self.graph.edge("", self.start)

        # Adding edge between states in DFA from transitions
        for state in self.transitions:
            for alphabet in self.transitions[state]:
                tmp = self.transitions[state][alphabet]
                self.graph.edge(state, tmp, label=("ε", alphabet)[alphabet != "e"])
    
    def minimize(self):
        table = {}
        for i, row in enumerate(self.states):
            table[row] = {}
            for j, col in enumerate(self.states[:i]):
                if (row in self.finals) != (col in self.finals):
                    table[row][col] = 1
                else:
                    table[row][col] = 0
        

        flag = True
        while flag:
            flag = False
            for i, row in enumerate(self.states):
                for j, col in enumerate(self.states[:i]):
                    if table[row][col] == 1:
                        continue
                    for alpha in self.alphabets:
                        tmp_row = self.transitions[row][alpha]
                        tmp_col = self.transitions[col][alpha]

                        if (tmp_row != tmp_col) and (tmp_row in table) and (tmp_col in table[tmp_row]) and (table[tmp_row][tmp_col] == 1):
                            table[row][col] = 1
                            flag = True

                        if (tmp_col != tmp_row) and (tmp_col in table) and (tmp_row in table[tmp_col]) and (table[tmp_col][tmp_row] == 1):
                            table[row][col] = 1
                            flag = True
        

        new_states = list(self.states)
        index = {}
        
        # Indexing states in same group.
        for i in new_states:
            index[i] = 0
        
        for i, row in enumerate(self.states):
            for j, col in enumerate(self.states[:i]):
                if table[row][col] == 0:
                    if index[row] == 0 and index[col] == 0:
                        new_states.append(sorted([row, col]))
                        index[row] = i
                        index[col] = i
                        new_states.remove(row)
                        new_states.remove(col)
                    elif index[row] != 0 and index[col] == 0:
                        tmp = []
                        for tmp_index in index:
                            if index[tmp_index] == index[row]:
                                tmp.append(tmp_index)
                        new_states.remove(col)
                        new_states.remove(sorted(tmp))
                        tmp.append(col)
                        new_states.append(sorted(tmp))
                        for t in tmp:
                            index[t] = i
                    elif index[row] == 0 and index[col] != 0:
                        tmp = []
                        for tmp_index in index:
                            if index[tmp_index] == index[col]:
                                tmp.append(tmp_index)
                        new_states.remove(row)
                        new_states.remove(sorted(tmp))
                        tmp.append(row)
                        new_states.append(sorted(tmp))
                        for t in tmp:
                            index[t] = i

        new_transitions = {}
        for n_state in new_states:
            for alpha in self.alphabets:
                new_states_transitions = self.state_list_to_string(n_state)
                if new_states_transitions not in new_transitions:
                    new_transitions[new_states_transitions] = {}
                
                if (type(n_state) == str):
                    n_state = [n_state]
                tmp_state = self.transitions[n_state[0]][alpha]
                for tmp_new_state in new_states:
                    if tmp_state in tmp_new_state:
                        new_transitions[new_states_transitions][alpha] = self.state_list_to_string(tmp_new_state)
                        break


        new_finals = []
        new_states_string = []

        new_start = "" 
        # The original start state in new_states => new_start
        # The original final state in new_states => new_finals
        for n_state in new_states:
            state = self.state_list_to_string(n_state)
            new_states_string.append(state)
            if type(n_state) != list:
                n_state = [n_state]
            for s in n_state:
                if s == self.start:
                    new_start = state
                if s in self.finals and state not in new_finals:
                    new_finals.append(state)
        
        return DFA(new_states_string, self.alphabets, new_start, new_finals, new_transitions)
    def to_json(self):
        return {
            "states": self.states,
            "alphabets": self.alphabets,
            "start": self.start,
            "finals": self.finals,
            "transitions": self.transitions
        }

if __name__ == "__main__":
    f = open("input.json", "r")
    data = json.load(f)
    assert data["states"], "States is missing!"
    assert data["alphabets"], "Alphabets is missing!"
    assert data["start"], "Start state is missing!"
    assert data["finals"], "Final states are missing!"
    assert data["transitions"], "Transitions are missing!"

    states = data["states"]
    alphabets = data["alphabets"]
    start = data["start"]
    finals = data["finals"]
    transitions = data["transitions"]
    # print(transitions)
    dfa = DFA(states, alphabets, start, finals, transitions)

    print(dfa.__repr__)

    # dfa.render('dfa', view=True)
    print("DFA Table:")
    dfa.table()

    dfa.draw_graph()
    dfa.graph.render("dfa_input", view=True)


    DFA_output = dfa.minimize()

    print(DFA_output.__repr__())
    print("DFA OUTPUT Table:")
    
    DFA_output.table()
    DFA_output.draw_graph()
    DFA_output.graph.render("dfa_output", view=True)
    with open("output.json", "w") as f:
        json.dump(DFA_output.to_json(), f, indent=4)
