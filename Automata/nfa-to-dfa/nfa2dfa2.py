# source: https://www.geeksforgeeks.org/converting-epsilon-nfa-to-dfa-using-python-and-graphviz/

import json
from typing import KeysView, List, Dict

from graphviz import Digraph
from prettytable import PrettyTable


class NFA:
    def __init__(self, json_file):
        states = json_file["states"]
        alphabets = json_file["alphabets"]
        start = json_file["start"]
        finals = json_file["finals"]
        transitions = json_file["transitions"]
        self.setup(
            states=states,
            alphabets=alphabets,
            start=start,
            finals=finals,
            transitions=transitions,
        )

    def setup(
        self, states: List, alphabets: List, start: str, finals: List, transitions: List
    ) -> None:
        self.states = states
        self.no_state = len(states)

        self.alphabets = alphabets
        # Add epsilon as alphabet.
        self.alphabets.append("e")
        self.no_alphabet = len(alphabets)

        self.start = self.states.index(start)
        self.start_name = start

        self.finals = finals
        self.no_final = len(finals)

        self.transitions = transitions
        self.no_transition = len(transitions)

        self.graph = Digraph()

        # Use dict to get index of states
        self.states_dict = dict()
        # Indexing for each state
        for i, state in enumerate(self.states):
            self.states_dict[state] = i

        # Use dict to get index of alphabets
        self.alphabets_dict = dict()
        # Indexing for each alphabet
        for i, alphabet in enumerate(self.alphabets):
            self.alphabets_dict[alphabet] = i

        # transition table is of the form:
        # [From state + Alphabet] -> [Set of To States]
        self.transition_table: Dict[int, list] = dict()
        for i in range(self.no_state):
            for j in range(self.no_alphabet):
                self.transition_table[self.hashing(i, j)] = list()
        print(self.transition_table)
        # Just combine state with alphabet -> new state (instead of using 2d table)
        for i in range(self.no_transition):

            print(self.transitions[i])
            hashed = self.hashing(
                self.states_dict[self.transitions[i][0]],
                self.alphabets_dict[self.transitions[i][1]],
            )
            print(hashed)
            self.transition_table[hashed].append(
                self.states_dict[self.transitions[i][2]]
            )

    def hashing(self, state: int, alphabet: int) -> int:
        """
        From_state + alphabet = to_state
        """
        # Use rolling hash
        return (1 + state) * len(self.alphabets) + alphabet

    # Method to represent quintuple
    def __repr__(self):
        return (
            "S : "
            + str(self.states)
            + "\nΣ : "
            + str(self.alphabets)
            + "\nS0 : "
            + str(self.start_name)
            + "\nδ : \n"
            + str(self.transition_table)
            + "\nF : "
            + str(self.finals)
        )

    def get_epsilon_closure(self, state) -> KeysView:
        """
            Method to get Epsilon Closure of a state of NFA.
            Make a dictionary to track if state is visited or not
            And an array as stack to get the state to visit next
            Return:
                List of closure state indexes 
        """
        closure = dict()
        closure[self.states_dict[state]] = 0
        closure_stack = [self.states_dict[state]]

        while len(closure_stack) > 0:

            # Get the top of stack.
            current = closure_stack.pop(0)

            # For the epsilon transition of that state,
            # if not present in closure array then add to dict
            # and add to stack
            for x in self.transition_table[
                self.hashing(current, self.alphabets_dict["e"])
            ]:
                if x not in closure.keys():  # if not visited
                    closure[x] = 0
                    closure_stack.append(x)
            closure[current] = 1  # Mark as visited
        return closure.keys()

    def get_state_name(self, state_list) -> str:
        """
            Get name from set of states to display in graph
        """

        name = ""
        for x in state_list:
            name += self.states[x]
        return name

    def is_final_DFA(self, state_list):
        """
            Check if the set of state is final state in DFA
            just by checking if any of the set is final state in NFA
        """
        for x in state_list:
            for y in self.finals:
                if x == self.states_dict[y]:
                    return True
        return False

    def table(self):
        header = ["States"] + self.alphabets
        self.nfa_table = PrettyTable(header)
        for state in self.states:
            row = list()
            if self.start_name == state:
                row.append("->" + state)
            elif self.is_final_DFA([self.states_dict[state]]):
                row.append("*" + state)
            else:
                row.append(state)
            for j in range(len(self.alphabets)):
                row.append(
                    self.get_state_name(
                        self.transition_table[self.hashing(self.states_dict[state], j)]
                    )
                )
            self.nfa_table.add_row(row)
        print(self.nfa_table)


class DFA:
    def get_state_name(self, states: list) -> str:
        """
        Because one DFA state contains many NFA states, 
        So we need format it in form {S1, S2, ..., Sn}
        or {S1} if only 1 state
        """
        if len(states) <= 1:
            return "{" + self.nfa.get_state_name(states) + "}"
        else:
            return "{" + ",".join([self.nfa.get_state_name([x]) for x in states]) + "}"

    def __init__(self, nfa: NFA = None) -> None:
        if nfa is None:
            return
        self.nfa = nfa

        self.alphabets = nfa.alphabets

        # Transition table just for DFA
        self.transition_table: Dict[str, str] = dict()

        self.graph = Digraph()
        # Get all states and transitions from NFA
        self.epsilon_closure: Dict[str, list] = dict()
        for x in self.nfa.states:
            self.epsilon_closure[x] = list(self.nfa.get_epsilon_closure(x))

        # Because first state of DFA will be epsilon closure of start state of NFA
        # So use stack to maintain till when to evaluate the states
        self.stack = list()
        self.stack.append(self.epsilon_closure[self.nfa.start_name])

        if self.nfa.is_final_DFA(self.stack[0]):
            self.graph.attr("node", shape="doublecircle")
        else:
            self.graph.attr("node", shape="circle")
        self.graph.node(self.get_state_name(self.stack[0]))

        # Adding start state arrow to start state in DFA
        self.graph.attr("node", shape="none")
        self.graph.node("")
        self.graph.edge("", self.get_state_name(self.stack[0]))

        # List of DFA states
        self.states = list()
        self.states.append([self.nfa.start])

        # List of DFA final states
        self.finals = list()
        while len(self.stack) > 0:
            # Get the top of stack
            current_state = self.stack.pop(0)
            # print(current_state)
            # Traverse through all alphabets for evaluating transition
            for id_alphabet in range(len(self.alphabets) - 1):  # -1 for epsilon
                # Set to see if epsilon closure is empty or not
                from_closure = set()
                for x in current_state:
                    from_closure.update(
                        set(self.nfa.transition_table[self.hashing(x, id_alphabet)])
                    )

                if len(from_closure) > 0:
                    # Set the To State set in DFA
                    to_state = set()
                    for x in list(from_closure):
                        to_state.update(set(self.epsilon_closure[nfa.states[x]]))

                    # Check if state already exists in DFA
                    # and if not then add
                    if list(to_state) not in self.states:
                        self.stack.append(list(to_state))
                        self.states.append(list(to_state))

                    # Check if this set contains final state of NFA
                    # to get if this set will be final state in DFA
                    if self.nfa.is_final_DFA(list(to_state)):
                        self.finals.append(to_state)
                        self.graph.attr("node", shape="doublecircle")
                    else:
                        self.graph.attr("node", shape="circle")

                    self.graph.node(self.get_state_name(list(to_state)))

                    # Add edge between from state and to state
                    self.graph.edge(
                        self.get_state_name(current_state),
                        self.get_state_name(list(to_state)),
                        label=self.alphabets[id_alphabet],
                    )

                    # Add [current_state + id_alphabet] = to_state to transition table
                    self.transition_table[
                        self.get_state_name(current_state) + str(id_alphabet)
                    ] = self.get_state_name(list(to_state))
                else:
                    # Check if any dead state was present before this
                    # if not then make a new dead state ϕ
                    if [-1] not in self.states:
                        self.graph.attr("node", shape="circle")
                        self.graph.node("ϕ")

                        # For new dead state, add all transitions to itself
                        # so machine cannot leave the dead state
                        for id_alphabet in range(len(self.alphabets) - 1):
                            self.graph.edge("ϕ", "ϕ", self.alphabets[id_alphabet])
                            self.transition_table["ϕ" + str(id_alphabet)] = "ϕ"

                        # Add -1 to list to mark that the dead state is present
                        self.states.append([-1])

                    # Add transition to dead state
                    self.graph.edge(
                        self.get_state_name(current_state),
                        "ϕ",
                        label=self.alphabets[id_alphabet],
                    )

    def hashing(self, state: int, alphabet: int) -> int:
        return (1 + state) * len(self.alphabets) + alphabet

    def table(self):
        header = ["States"]
        header = header + dfa.alphabets[:-1]
        # print(header)
        table = PrettyTable(header)
        # print(self.states)
        for state in self.states:
            # if state == [-1]:
            #     continue
            tmp = [self.get_state_name(state)]
            for j in range(len(self.alphabets) - 1):
                hash = self.get_state_name(state) + str(j)
                if hash in self.transition_table:
                    tmp.append(self.transition_table[hash])
                else:
                    tmp.append("ϕ")
            table.add_row(tmp)
        print(table)


if __name__ == "__main__":
    f = open("4.json", "r")
    nfa_data = json.load(f)
    nfa = NFA(nfa_data)
    print(nfa.__repr__)

    # Adding states/nodes in NFA diagram
    for x in nfa.states:
        # If state is not a final state, then border shape is single circle
        # Else it is double circle
        if x not in nfa.finals:
            nfa.graph.attr("node", shape="circle")
            nfa.graph.node(x)
        else:
            nfa.graph.attr("node", shape="doublecircle")
            nfa.graph.node(x)

    # Adding start state arrow in NFA diagram
    nfa.graph.attr("node", shape="none")
    nfa.graph.node("")
    nfa.graph.edge("", nfa.start_name)

    # Adding edge between states in NFA from transitions
    for x in nfa.transitions:
        nfa.graph.edge(x[0], x[2], label=("ε", x[1])[x[1] != "e"])

    # dfa.render('dfa', view=True)
    print("NFA Table:")
    nfa.table()

    dfa = DFA(nfa=nfa)
    print("DFA Table:")
    dfa.table()

    nfa.graph.render("nfa", view=True)
    dfa.graph.render("dfa", view=True)
