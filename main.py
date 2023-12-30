from csp import *
import time


variables = {}
structures = {}
constraints = []

def read_instance_file(file_path):
    # File name only
    file_name = file_path.split("/")[-1]  
    
    # Checking what type of file we're dealing with because there is a function for each one
    if file_name.startswith("var"):
        read_var_file(file_path)
    elif file_name.startswith("dom"):
        read_dom_file(file_path)
    elif file_name.startswith("ctr"):
        read_ctr_file(file_path)

# Function for "var" type file
def read_var_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            var_id, domain_id = map(int, line.split())
            variables[var_id] = domain_id

# Function for "dom" type file
def read_dom_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            domain_id, num_values, *values = map(int, line.split())
            structures[domain_id] = values

# Function for "ctr" type file
def read_ctr_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            constraints.append(line.strip())

def main():
    varName = input("Enter var file name: ")
    ctrName = input("Enter ctr file name: ")
    domName = input("Enter dom file name: ")

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

if __name__ == "__main__":
    main()
