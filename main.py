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
            ctr_data.append((int(vars[0]), int(vars[1]), vars[2], int(vars[3])))

    return ctr_count, ctr_data



def myHeuristic(assignment, csp):
    unassigned_variables = []
    for variable in csp.variables:
        if variable not in assignment:
            unassigned_variables.append(variable)
    
    min_val = math.inf
    result = None
    for var in unassigned_variables:
        domain_size = len(csp.domains[var])
        totalWeight = 0

        for i, constraint in enumerate(csp.listOfConstraints):
            if var in constraint and any(n in unassigned_variables for n in constraint):
                totalWeight += csp.weight[i]

        if totalWeight != 0:
            value = domain_size/totalWeight
        else:
            return math.inf
        
        if value < min_val:
            min_val = value
            result = var
            
    return result



def main():

    # Collecting the data from each file
    var_count, var_data = var_type_file('var6-w2.txt')
    dom_count, dom_data = dom_type_file('dom6-w2.txt')
    ctr_count, ctr_data = ctr_type_file('ctr6-w2.txt')
    # for each function that reads a file, the argument can be changed to a different one


    variables = list(range(var_count))

    domains = {}
    domains = dict((variable, dom_data[dom]) for variable, dom in var_data)

    neighbors = {var: set() for var in range(var_count)}
    for var1, var2, _, _ in ctr_data:
        neighbors[var1].add(var2)
        neighbors[var2].add(var1)


    def constraints(A, a, B, b):
        # for each one of the parameters in a constraint (var1, var2, condition, var3)
        for var1, var2, operator, var3 in ctr_data:
            if (A == var1 and B == var2) or (A == var2 and B == var1):
                if operator  == '=':
                    return abs(a-b) == var3
                elif operator == '>':
                    return abs(a-b) > var3
        return True
    
    csp_instance = CSP(variables, domains, neighbors, constraints, ctr_data)


    # Execution of FC
    begin = time.perf_counter()
    fc = backtracking_search(csp_instance, myHeuristic, unordered_domain_values, forward_checking)
    end = time.perf_counter()
    print("Results for FC are: ", fc)
    print("FC ended in ", end-begin, " seconds")


    #Execution of MAC
    begin = time.perf_counter()
    mac_result = backtracking_search(csp_instance, myHeuristic, unordered_domain_values, mac)
    end = time.perf_counter()
    print("Results for MAC are: ", mac_result)
    print("MAC ended in ", end-begin, " seconds")


    # Execution of min_conflicts
    begin = time.perf_counter()
    min_conflicts_result = min_conflicts(csp_instance)
    end = time.perf_counter()
    print("Results for Min Conflicts are: ", min_conflicts_result)
    print("Min Conflicts ended in ", end - begin, " seconds")

if __name__ == "__main__":
    main()