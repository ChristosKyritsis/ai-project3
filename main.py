from csp import *
import math
import time

def var_type_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        var_count = int(lines[0].strip())
        var_data = [list(map(int, line.strip().split())) for line in lines[1:]]
    return var_count, var_data

def dom_type_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        dom_count = int(lines[0].strip())
        dom_data = [list(map(int, line.strip().split()[1:])) for line in lines[1:]]
    return dom_count, dom_data

def ctr_type_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        ctr_count = int(lines[0].strip())
        ctr_data = []

        for line in lines[1:]:
            # Seperating the values of constaints into the two variables, the operator and then the third variable
            vars = line.strip().split()
            # The order is:
            # vars[0] is the first variable
            # vars[1] is the second variable
            # vars[2] is the operator
            # vars[3] is the third variable
            ctr_data.append((int(vars[0]), int(vars[1]), vars[2], vars[3]))

    return ctr_count, ctr_data



def weighted_degree_heuristic(assignment, csp):
    unassigned_vars = [var for var in csp.variables if var not in assignment]
    min = math.inf
    for var in unassigned_vars:
        domain = len(csp.domains[var])
        weight_sum = 0
        for neighbor in csp.neighbors[var]:
            if neighbor in unassigned_vars:
                i = 0
                for con in csp.clist:
                    if((con[0] == var and con[1] == neighbor) or (con[0] == neighbor and con[1] == var)):
                        weight_sum += csp.weights[i]
                    i += 1
        if(domain / weight_sum<min):
            min = domain/weight_sum
            minvar = var
    return minvar




def main():

    # for each function that reads a file, the argument can be changed to a different one

    var_count, var_data = var_type_file('var11.txt')
    # print(f"Variable count: {var_count}")
    # print("Variables:")
    # for var in var_data:
    #     print(var)
  

    dom_count, dom_data = dom_type_file('dom11.txt')
    # print(f"Domain number: {dom_count}")
    # print("Domain data: ")
    # for dom in dom_data:
    #     print(dom)

    ctr_count, ctr_data = ctr_type_file('ctr6-w2.txt')
    # print(f"Constraint number: {ctr_count}")
    # print("Constraints: ")
    # for ctr in ctr_data:
    #     print(ctr)

    variables = list(range(var_count))
    domains = {var: list(range(dom_count)) for var in variables}

    neighbors = {var: [v for v in variables if v != var] for var in variables}

    def constraints(A, a, B, b):
        # for each one of the parameters in a constraint (var1, var2, condition, var3)
        for var1, var2, operator, var3 in ctr_data:
            if (A == var1 and B == var2) or (A == var2 and B == var1):
                if operator  == '=':
                    return abs(var1-var2) == var3
                elif operator == '>':
                    return abs(var1-var2) > var3
        return True
    
    csp_instance = CSP(variables, domains, neighbors, constraints)

    begin = time.time()
    fc = backtracking_search(csp_instance, unordered_domain_values, inference=forward_checking)
    end = time.time()
    print("Results are: ", fc)
    print(end-begin)


    begin = time.time()
    mac_result = backtracking_search(csp_instance, unordered_domain_values, inference=mac)
    end = time.time()
    print("Results are: ", mac_result)
    print(end-begin)


    min_conflicts(CSP)

if __name__ == "__main__":
    main()