from collections import defaultdict

epsilon = 'ε'

class CFG:
    def __init__(self, terminals = None, nonterminals = None, start = None):
        self.terminals = set(terminals)
        self.terminals.add(epsilon)
        self.nonterminals = set(nonterminals)
        self.productions = defaultdict(set)
        self.start = start

    def add_production(self, symbol, string):
        self.productions[symbol].update(string)

    def __get_unused_nonterminal__(self, letter):

        if letter != epsilon and letter.upper() not in self.nonterminals:
            self.nonterminals.add(letter.upper())
            return letter.upper()
        for i in range(0, 26):
            L = chr(ord('A') + i)
            if L not in self.nonterminals:
                self.nonterminals.add(L)
                return L

        for i in range(0, 26):
            letter = chr(ord('A') + i)
            for j in range(1,10):
                L = letter + '_' + str(j)
                if L not in self.nonterminals:
                    self.nonterminals.add(L)
                    return L    


    @classmethod
    def __split_into_symbols__(cls, string):

        result = []
        for c in string:
            if c == '_' or c.isnumeric():
                result[-1] = result[-1] + c
            else:
                result.append(c)
        return result

    
    def remove_deleted_nonterminals(self):
        ok = False
        while not ok:                                                   
            ok = True
            newProductions = defaultdict(set)                           
            for k, v in self.productions.items():
                if k not in self.nonterminals:                          
                    continue
                for string in v:                                        
                    string = CFG.__split_into_symbols__(string)                                               
                    newString = [x for x in string if x in self.nonterminals or x in self.terminals]        
                    if string != newString:                                                                 
                        ok = False                                                                          
                    if len(newString):                                                                      
                        newProductions[k].add(''.join(newString))
            self.productions = newProductions
            self.nonterminals = set(newProductions.keys())            


    def remove_redundant_symbols(self):

        # 1. Delete non-terminating symbols

        terminating = set()
        ok = False
        while not ok:
            ok = True
            for k, v in self.productions.items():
                if k in terminating:                                            
                    continue
                for string in v:                                                
                    symbols = CFG.__split_into_symbols__(string)                 
                    isTerminating = True                                        
                    for s in symbols:                                           
                        if s not in terminating and s not in self.terminals:   
                            isTerminating = False
                    
                    if isTerminating:                                           
                        terminating.add(k)
                        ok = False

        self.nonterminals = terminating

        assert self.start in terminating, f'Symbol start {self.start} not terminating!'

        self.remove_deleted_nonterminals()    
        #############################################################################################################################################################################################################
        
        # 2. Delete unreachable symbols 

        reachable = set(self.start)
        stack = [self.start]
        
        while len(stack) > 0:       
            top = stack[-1]
            stack.pop()
            for string in self.productions[top]:
                symbols = [x for x in CFG.__split_into_symbols__(string) if x in self.nonterminals]
                for s in symbols:
                    if s not in reachable:
                        reachable.add(s)
                        stack.append(s)

        self.nonterminals = reachable

        self.remove_deleted_nonterminals()
 
    def __replace_symbol__(self, old, new):
        newProductions = defaultdict(set)
        for k,v in self.productions.items():
            for string in v:
                string = string.replace(old, new)
                newProductions[k].add(string)

        self.nonterminals.remove(old)
        self.productions = newProductions
        self.remove_deleted_nonterminals()

    def __convert_to_CNF__(self):

        self.remove_redundant_symbols()
 
        # 1. if the start symbol is in a production, add a new start symbol
        found = any([self.start in string for strings in self.productions.values() for string in strings])
        if found:
            self.add_production('S_0', [f'{self.start}'])
            self.start = 'S_0'

        #########################################################################################################################################################################
        
        # 2. replace the terminals in each production, 
        # only if it is not of the form A -> a, 
        # with a non-terminal

        terminal_dict = defaultdict(str)

        # find the first non-terminal for each terminal
        for terminal in self.terminals:
            for k, v in self.productions.items():       
                if len(v) == 1 and terminal in v:
                    terminal_dict[terminal] = k
                    break
            else:
                terminal_dict[terminal] = self.__get_unused_nonterminal__(terminal)
            
        
        new_productions = defaultdict(set)
        for key, val in self.productions.items():
            for string in val:
                if len(string) == 1 and string in self.terminals:      
                    new_productions[key].add(string)

                else:
                    # replace terminal with non-terminal
                    for k, v in terminal_dict.items():                  
                        if k in string:                  
                            string = string.replace(k, v)               
                            new_productions[v].add(k)                   

                    new_productions[key].add(string)

        self.productions = new_productions                         

         
        # 3. replace the productions in which more than 2 non-terminals appear with only 2 non-terminals
        
        newNonterminals = dict()
        ok = False
        
        while not ok:
            ok = True
            newProductions = defaultdict(set)
            for k, v in self.productions.items():
                
                for string in v:
                    nonterminals = CFG.__split_into_symbols__(string)                     
                    if len(nonterminals) <= 2:                                          
                        newProductions[k].add(string)
                        continue
                    ok = False

                    newNonterminal = None
                                                
                    # check if the new non-terminal already exists
                    for nonterminal in newNonterminals:    
                        if ''.join(nonterminals[1:]) == newNonterminals.get(nonterminal):
                            newNonterminal = nonterminal
 
                    # Create new non-terminal
                    if newNonterminal is None:                                                  
                        newNonterminal = self.__get_unused_nonterminal__(nonterminals[1][0])     
                        newNonterminals[newNonterminal] = ''.join(nonterminals[1:])             
                        self.nonterminals.add(newNonterminal)  
                        newProductions[newNonterminal].add(''.join(nonterminals[1:]))          

                    newProductions[k].add(nonterminals[0] + newNonterminal)                 
                    
            self.productions = newProductions
            

        #########################################################################################################################################################################
        
        # 4. Delete epsilon productions

        nullables = set()
        ok = False

        # find all nullables
        while not ok:
            ok = True
            for k, v in self.productions.items():
                if k in nullables:
                    continue
                for string in v:
                    if string == epsilon or all([nonterminal in nullables for nonterminal in CFG.__split_into_symbols__(string)]):
                        nullables.add(k)
                        ok = False
        
        # remove epsilon in productions
        newProductions = defaultdict(set)
        for k, v in self.productions.items():
            newProductions[k] = set(v)                                              
            for string in v:
                nonterminals = CFG.__split_into_symbols__(string)                   
                if len(nonterminals) == 1 and nonterminals[0] in nullables:         
                    newProductions[k].add(epsilon)
                elif len(nonterminals) == 2:                                        
                    if nonterminals[0] in nullables:                                
                        newProductions[k].add(nonterminals[1])                      
                    if nonterminals[1] in nullables:                                
                        newProductions[k].add(nonterminals[0])                      
                    if nonterminals[0] in nullables and nonterminals[1] in nullables:
                        newProductions[k].add(epsilon)                                  

        # remove epsilon in set of nonterminals from productions
        newProductions = {k : v.difference([epsilon]) for k,v in newProductions.items() if len(v.difference([epsilon])) > 0}
        print(newProductions)
        self.nonterminals = set(newProductions.keys())
        self.productions = newProductions

        if self.start in nullables:
            self.productions[self.start].add(epsilon)

        self.remove_deleted_nonterminals()

        #########################################################################################################################################################################

        # 5. Delete unit productions

        deletedNonterminals = set()
        ok = False
        while not ok:
            ok = True
            newProductions = defaultdict(set)
            for k, v in self.productions.items():                                         
                for string in v:
                    nonterminals = CFG.__split_into_symbols__(string)                      
                    if len(nonterminals) == 1 and nonterminals[0] in self.nonterminals:    
                        ok = False
                        if nonterminals[0] == k:                                           
                            continue
                        newProductions[k].update(self.productions[nonterminals[0]])        
                    else:
                        newProductions[k].add(string)                                      
        
            self.productions = newProductions
            self.nonterminals = set(newProductions.keys())                                 
            self.remove_deleted_nonterminals()

        #########################################################################################################################################################################

        

    def isCNF(self):
        for k, v in self.productions.items():
            for string in v:
                string = CFG.__split_into_symbols__(string)
                if len(string) != 2 and len(string) != 1:                      
                    return False
                else:
                    if len(string) == 1 and string[0] not in self.terminals:    
                        return False
                    elif len(string) == 2 and (string[0] not in self.nonterminals or string[1] not in self.nonterminals):  
                        return False
        return True


    def convertToCNF(self):
        if not self.isCNF():
            try:
                while not self.isCNF():
                    self.__convert_to_CNF__()
            except ValueError:
                self.start = None
                self.productions.clear()
                self.nonterminals.clear()
                self.terminals.clear()
                print('Start symbol is not terminating!')
                return False

        # delete duplicate productions
        ok = False
        while not ok:
            ok = True
            for k1 in self.productions.keys():
                if k1 == self.start: 
                    continue
                for k2 in self.productions.keys():
                    if k2 == self.start:
                        continue
                    if k1 != k2 and self.productions[k1] == self.productions[k2]:
                        self.__replace_symbol__(k1, k2)
                        ok = False
                        break
                if not ok: 
                    break


    def print(self, file=None):
        if file == None:
            print(f'Start symbol: {self.start}')
            if len(self.productions) == 0:
                return
            
            print(self.start, '->', ' | '.join(self.productions[self.start]))
            
            for key, val in sorted(self.productions.items(),key=lambda x : (-len(x[1]), list(x[1])[0] in self.terminals)):
                if key != self.start:
                    print(key, '->', ' | '.join(val))
        else:
            with open(file, 'w') as f:
                f.write(f'Start symbol: {self.start}\n')
                if len(self.productions) == 0:
                    return
                
                f.write(self.start + ' -> ' + ' | '.join(self.productions[self.start]) + '\n')
                
                for key, val in sorted(self.productions.items(),key=lambda x : (-len(x[1]), list(x[1])[0] in self.terminals)):
                    if key != self.start:
                        f.write(str(key) + ' -> ' + ' | '.join(val) + '\n')
 



if __name__ == '__main__':
    with open('input2.txt', 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        terminals = [x.strip() for x in lines[0].split()]
        non_terminals = [x.strip() for x in lines[1].split()]
        start = lines[2].strip()

        g = CFG(terminals, non_terminals, start)

        for line in lines[3:]:
            line = [x.strip() for x in line.split('->')]
            symbol = line[0]
            strings = [x.strip() for x in line[1].split('|')]

            g.add_production(symbol, strings)
        print(lines)
    print('Input:')
    g.print()

    print('\nChomsky normal form: ')
    g.convertToCNF()


    g.print()
    g.print('output.txt')
