from csp import *
import time

def read_var_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        var_count = int(lines[0].strip())
        var_data = [list(map(int, line.strip().split())) for line in lines[1:]]
    return var_count, var_data

def read_dom_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        dom_count = int(lines[0].strip())
        dom_data = [list(map(int, line.strip().split()[1:])) for line in lines[1:]]
    return dom_count, dom_data

def read_ctr_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        ctr_count = int(lines[0].strip())
        ctr_data = []

        for line in lines[1:]:
            parts = line.strip().split()
            operator = parts[2]
            k = int(parts[3])
            ctr_data.append((int(parts[0]), int(parts[1]), operator, k))

    return ctr_count, ctr_data


def main():

    var_count, var_data = read_var_file('var11.txt')
    # print(f"Variable count: {var_count}")
    # print("Variables:")
    # for var in var_data:
    #     print(var)
  

    dom_count, dom_data = read_dom_file('dom11.txt')
    # print(f"Domain number: {dom_count}")
    # print("Domain data: ")
    # for dom in dom_data:
    #     print(dom)

    ctr_count, ctr_data = read_ctr_file('ctr6-w2.txt')
    # print(f"Constraint number: {ctr_count}")
    # print("Constraints: ")
    # for ctr in ctr_data:
    #     print(ctr)

    variables = list(range(var_count))
    domains = {var: list(range(dom_count)) for var in variables}

    neighbors = {var: [v for v in variables if v != var] for var in variables}

    def constraints(A, a, B, b):
        for x, y, relation, value in constraints:
            if (A == x and B == y) or (A == y and B == x):
                return f(a, b, relation, value)
        return True
    
    csp_instance = CSP(variables, domains, neighbors, constraints)

    begin = time.time()
    temp1 = backtracking_search(csp_instance)
    end = time.time()
    print("Results are: ", temp1)
    print(end-begin)

if __name__ == "__main__":
    main()



    # try:
    #     read_instance_file(file_path)
    #     print("Variables:", variables)
    #     print("Structs:", structures)
    #     print("Constraints:", constraints)
    # except FileNotFoundError:
    #     print(f"File {file_path} not found.")
    # except Exception as e:
    #     print(f"Error: {e}")


    #temp1 = backtracking_search(,,,forward_checking)

