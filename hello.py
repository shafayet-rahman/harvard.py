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
