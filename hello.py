#use extension easter bunny to study code better
'''name = input("what's your name?").strip().title();#asking user for their name and saving it in a variable named "name"
print(f"hello, {name}");'''#the user input print statement 
#sahira pocha

#print has an auto escape character you can re write it like this
'''
print("gugugaga ", end ="")
print("sahiru") #this will print everything in a single line of code
'''
#python string methods are pretty cool - lower(),upper(),title(),strip(),replace(),etc

#split users name into two variables

'''name = input("whatcha name lil vru? ")
first, last = name.split(" ")
print(first)
print("Oh wait forgot your last name lil vru lemme cook" "\n" + last)'''
#type conversion any input taken from the user comes as text even numbers u have to use int to convert it into num first
'''z = 1000000
print(f"{z:,}")'''#numeric formatting syntax,adds comma after every 3 0
'''x = int(input("what's x? "))
y = int(input("what's y? "))
z = x / y
print(f"{z:.4f}")'''#specifies how many digits you want to print after the dot
'''def main():
    print("hell yea")
main()'''#this is the function syntax and you algo gotta indent stuff like this lmdo or it won't work
#python also has the scope thingy as same as vscode
#return shit to exit functions
#-----------------------------------------------------------
# If statement - Executes a block of code if a specified condition is True
# Basic syntax: if condition: code_block
#x = 5
#if x > 0:
#    print("x is positive")

# Elif (else if) statement - Checks another condition if previous conditions were False
# Used between if and else to check multiple conditions
# Basic syntax: elif condition: code_block
#score = 85
#if score >= 90:
#    print("Grade: A")
#elif score >= 80:
#    print("Grade: B")
#elif score >= 70:
#    print("Grade: C")

# Else statement - Executes when all previous conditions are False
# Provides a default case when no conditions are met
# Basic syntax: else: code_block
#age = 15
#if age >= 18:
#    print("You can vote")
#else:
#    print("Too young to vote")

# Match statement (Python 3.10+) - Similar to switch/case in other languages
# Compares a value against multiple patterns
# Basic syntax: match value: case pattern: code_block
#status = "error"
#match status:
#    case "success":
#        print("Operation completed successfully")
#    case "error":
#        print("An error occurred")
#    case "pending":
#        print("Operation in progress")
#    case _:  # Default case (like else)
#        print("Unknown status")

# Complex if-elif-else with multiple conditions
# Demonstrates using logical operators (and, or, not)
#temperature = 25
#humidity = 60

#if temperature > 30 and humidity > 70:
#    print("Hot and humid")
#elif temperature > 30 and humidity <= 70:
#    print("Hot but dry")
#elif temperature <= 30 and humidity > 70:
#    print("Cool but humid")
#else:
#    print("Pleasant weather")
# Pythonic expressions - Simple examples of Python's elegant syntax

# List comprehension
#numbers = [1, 2, 3, 4, 5]
#squares = [x * x for x in numbers]
#print(squares)  # [1, 4, 9, 16, 25]

# Ternary operator
#age = 20
#status = "adult" if age >= 18 else "minor"
#print(status)

# Multiple assignment
#a, b = 1, 2
#print(a, b)  # 1 2
----------------------------------------------------------------------