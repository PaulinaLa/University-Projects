import json
from itertools import combinations

def empty_graph(N):
    G = {}
    for i in range (0,N):
        G[i] = set()
    return G

def fill_in_graph(students, conflicts):
    G = empty_graph(students)
    for e in conflicts:
        G[e['zrzeda']].add(e['nielubiany'])
        G[e['nielubiany']].add(e['zrzeda'])
    return G

def create_variable (tutor_str, ver_num):
    tutor_num = int(tutor_str[1])
    return 4 *ver_num + tutor_num

def vertex_colouring(vertex, tutors):
    variables = [create_variable(tutors[0], vertex),create_variable(tutors[1], vertex), create_variable(tutors[2], vertex), create_variable(tutors[3], vertex)]
    neg_variables = list(map(lambda x: x*(-1), variables))
    clauses = list(map(list, list(combinations(neg_variables, 2))))
    return [variables] + clauses

def graph_compability(graph, tutors):
    cnf = set()
    for vertex in graph.keys():
        for edged in graph[vertex]:
            for tut in tutors:
                variables =(-1 * create_variable(tut, vertex), -1 *create_variable(tut, edged))
                cnf.add(variables)
    res = list(map(list,[tuple(x) for x in set(map(frozenset, cnf))]))
    return res

def whole_clause (graph, tutors):
    var_counter = 0
    clause = graph_compability(graph, tutors)
    for vertex in graph:
        if graph[vertex]:
            var_counter += 4
            clause += vertex_colouring(vertex,tutors)
    return (clause, var_counter, len(clause))

def could_be_easier(G):
    for i in range (0, len(G.keys())):
        if len(G[i]) < 4:
            return True
    return False

def graph_simplification(G):
    removed = set()
    for i in range (0, len(G.keys())):
        if len(G[i]) < 4:
            removed.add(i)
            del G[i]
    for elem in removed:
        for key in G.keys():
            if elem in G[key]:
                G[key].remove(elem)
    vertices = G.keys()
    max_number_of_keys = len(G.keys())
    numerator = 0
    sets = list(G.values())
    for vertex in vertices:
        if vertex == numerator:
            numerator +=1
        else:
            for elem in sets:
                if vertex in elem:
                    elem.remove(vertex)
                    elem.add(numerator)
            numerator +=1
    new_G = empty_graph(max_number_of_keys)
    for i in range(0, max_number_of_keys):
        new_G[i] = sets[i]
    return new_G

def should_I_even_count(G):
    sets = list(filter(lambda x: len(x) > 3,G.values()))
    return len(sets) > 0

def create_answer():
    filename = input()
    tut_colors = ["t1", "t2", "t3", "t4"]
    with open(filename, 'r') as f:
       data_dict = json.load(f)

    studenci = data_dict['studenci']
    konflikty = data_dict['konflikty']

    G = fill_in_graph(studenci,konflikty)

    if not should_I_even_count(G):
        print("p cnf 1 1\n" + "1 0")
    else:
        while could_be_easier(G):
            G = graph_simplification(G)

        if not should_I_even_count(G):
            print("p cnf 1 1\n" + "1 0")
        else:
            res = whole_clause(G, tut_colors)
            clause = res[0]
            print("p cnf " + str(res[1]) + " "  + str(res[2]))
            for disj in clause:
                curr_res = ""
                for var in disj:
                    curr_res += str(var) + " "
                print(curr_res + "0")

create_answer()
