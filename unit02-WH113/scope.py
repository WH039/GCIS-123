# scope.py by Weicheng Huang

# Global Variable
int_var = 99
char_var = 'e'
string_var = "help"

# functions
def print_param(a):
    print(a)

def print_local():
    local_variable = "what"
    print(local_variable)

def print_which():
    string_var = 10
    print(string_var)

# main
def main():
    print_param(char_var)
    print_param(int_var)
    print_param(string_var)
    local_variable = ":|"
    print_local()
    print_which()
    print(string_var)

main()