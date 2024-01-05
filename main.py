from csp import *
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
            parts = line.strip().split()
            operator = parts[2]
            var3 = int(parts[3])
            ctr_data.append((int(parts[0]), int(parts[1]), operator, var3))

    return ctr_count, ctr_data


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
    fc = backtracking_search(csp_instance)
    end = time.time()
    print("Results are: ", fc)
    print(end-begin)

if __name__ == "__main__":
    main()