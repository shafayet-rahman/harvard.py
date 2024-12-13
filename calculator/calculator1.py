def main():
    expression = input("What's your arithmetic expression? (x,y,z) ")
    calculator(expression)
    
    
def calculator(exp):
    x,operator,z = exp.split(" ")
    x = int(x)
    z = int(z)
    if operator == "+":
        print(x + z)
    elif operator == "-":
        print(x - z)
    elif operator == "*":
        print(x * z)
    elif operator == "/":
        print(x / z)
    elif operator == "%":
        print(x % z)
    else:
        print("Learn math")
        
        
main()