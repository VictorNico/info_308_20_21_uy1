import networkx as nx
import matplotlib.pyplot as plt
import os
import sys
import subprocess
from IPython.display import Image
class DFA:
    """ This class represent any type of deterministic finite automaton."""
    def __init__(self, alphabet):
        """ Initialise the finite autaomaton.
            @param the alphabet of the automaton."""

        """ List of string corresponding to states name.
            States are always identificated by name."""
        self.states = []
        """ Dictionary using src state as key and mapping it to a list of
            pair (dest_state, symbol)."""
        self.transitions = {}
        """ The string corresponding to the name of the initial state."""
        self.init = None
        """ A list containing the name of the final states."""
        self.finals = []
        """ A string containing all symbols in the alphabet."""
        self.alphabet = ""
        for s in alphabet:
            if s not in self.alphabet:
                self.alphabet += s
                
    def add_state(self, state, final = False):
        if state in self.states:
            print("error : state '" + state + "' already exists.")
            return
        self.transitions[state] = []
        self.states.append(state)
        if final:
            self.finals.append(state)
    def valid_symbol(self, symbol):
        if symbol not in self.alphabet: return False
        return True
    def dst_state(self, src_state, symbol):
        if src_state not in self.states:
            print("error : the state '" + src_state + "' is not an existing state.")
            return
        for (s, dst_state) in self.transitions[src_state]:
            if s == symbol:
                return dst_state
        return None
 
    def add_transition(self, src_state, symbol, dst_state):
        if not self.valid_symbol(symbol):
            print("error : the symbol '" + symbol + "' is not part of the alphabet.")
            return
        if src_state not in self.states:
            print("error : the state '" + src_state + "' is not an existing state.")
            return
        if dst_state not in self.states:
            print("error : the state '" + dst_state + "' is not an existing state.")
            return
        if self.dst_state(src_state, symbol) != None:
            print("error : the transition (" + src_state + ", " + symbol + ", ...) already exists.")
            return
        self.transitions[src_state].append((symbol, dst_state))
    def __str__(self):
        ret = "FA :\n"
        ret += "-alphabet:'" + self.alphabet + "'\n"
        ret += "-init:" + str(self.init) + "\n"
        ret += "-finals:" + str(self.finals) + "\n"
        ret += "- states (%d) :\n" % (len(self.states))
        for state in self.states:
            ret += "- (%s)" % (state)
            if len(self.transitions[state]) is 0:
                ret += ".\n"
            else:
                ret += ret + ":\n"
                for (sym, dest) in self.transitions[state]:
                    ret += ret + "--(%s)--> (%s)\n" % (sym, dest)
        return ret

def run(dfa, word, verbose = False):
    if dfa.init == None:
        print("error : the automaton does not have any initial symbol.")
        return False
    current_state = dfa.init
    i = 0
    for symbol in word:
        if verbose : print("configuration : (" + current_state + ", " + word[i:] + ")")
        if not dfa.valid_symbol(symbol):
            print("error : the symbol '" + symbol + "' is not part of the alphabet. Abord.")
        next_state = dfa.dst_state(current_state, symbol)
        if next_state is None:
            if verbose: print("no transition available for (" + current_state + ", " + symbol + ").")
            return False;
        current_state = next_state
        i = i+1
        
    if current_state in dfa.finals:
        if verbose: print("ending on final state '" + current_state + "'.")
        return True
    if verbose: print("ending on non accepting state '" + current_state + "'")
    return False
def to_dot(dfa, name="Graph"):
    """ Returns a string corresponding to the specified DFA in DOT format.
        @param dfa  the DFA to be converted in DOT format.
        @param name the name of the automaton for the DOT file ("Graph")
            by default.
        @returns the automaton in DOT format."""
    ret = "digraph " + name + " {\n    rankdir=\"LR\";\n\n"
    ret += "    // States (" + str(len(dfa.states)) + ")\n"
 
    state_name = lambda s : "Q_" + str(dfa.states.index(s))
 
    # States
    ret += "    node [shape = point ];     __Qi__ // Initial state\n" # Initial state
    for state in dfa.states:
        ret += "    "
        if state in dfa.finals:
            ret += "node [shape=doublecircle]; "
        else:
            ret += "node [shape=circle];       "
        ret += state_name(state) + " [label=" + state + "];\n"
 
    # Transitions
    ret += "\n    // Transitions\n"
    ret += "    __Qi__ -> " + state_name(dfa.init) + "; // Initial state arrow\n"
    for state in dfa.states:
        for (symbol, dst_state) in dfa.transitions[state]:
            ret += "    " + state_name(state) + " -> " + state_name(dst_state) + " [label=" + symbol + "];\n"
    ret+="}\n"
    tmp_file ="graph.dot"
    with open(tmp_file, "w") as file:
        file.write(ret)
    return tmp_file
def display(dfa):
    to_dot(dfa)
    subprocess.call("dot -Tpng graph.dot -o test2.png")
    return Image(filename =r'test2.png')