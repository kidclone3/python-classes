from prettytable import PrettyTable


def create_cell(first, second):
    
    res = set()
    if first == set() or second == set():
        return set()
    for f in first:
        for s in second:
            res.add(f+s)
    return res


def read_grammar(filename="./grammar.txt"):
    
    with open(filename) as grammar:
        rules = grammar.readlines()
        v_rules = []
        t_rules = []

        for rule in rules:
            left, right = rule.split(" -> ")

            # for two or more results from a variable
            right = right[:-1].split(" | ")
            for ri in right:

                # it is a terminal
                if str.islower(ri):
                    t_rules.append([left, ri])

                # it is a variable
                else:
                    v_rules.append([left, ri])
        return v_rules, t_rules


def read_input(filename="./input.txt"):
    
    res = []
    with open(filename) as inp:
        inputs = inp.readlines()
        for i in inputs:

            # remove \n
            res.append(i[:-1])
    return res


def cky_algorithm(varies, terms, inp_str):
    

    length = len(inp_str)
    var0 = [va[0] for va in varies]
    var1 = [va[1] for va in varies]

    # table on which we run the algorithm
    table = [[set() for _ in range(length-i)] for i in range(length)]

    # Deal with variables
    for i in range(length):
        for te in terms:
            if inp_str[i] == te[1]:
                table[0][i].add(te[0])

    # Deal with terminals
    # its complexity is O(|G|*n^3)
    for i in range(1, length): # length of string processing
        for j in range(length - i): # starting index of string processing
            for k in range(i): # length of the first string
                row = create_cell(table[k][j], table[i-k-1][j+k+1])
                # check if variable appears in the right of a rule
                for idx, v in enumerate(var1):
                    if v in row:
                        table[i][j].add(var0[idx])

    # if the last element of table contains "S" the input belongs to the grammar
    return table


def show_result(tab, inp):
    
    print(inp)
    header = [""] + [c for c in inp]
    table = PrettyTable()
    table._validate_field_names = lambda *a, **k: None
    table.field_names = header
    for i in range(len(inp)):
        row = list()
        row.append(i+1)
        for c in tab[i]:
            if c == set():
                row.append("_")
            else:
                row.append(c)
        for c in range(len(inp)-len(tab[i])):
            row.append("")
        table.add_row(row)
    print(table)
    if 'S' in tab[len(inp)-1][0]:
        print("The input belongs to this context free grammar!")
    else:
        print("The input does not belong to this context free grammar!")


if __name__ == '__main__':
    v_rules, t_rules = read_grammar()
    inp = read_input()[0]
    table = cky_algorithm(v_rules, t_rules, inp)
    show_result(table, inp)