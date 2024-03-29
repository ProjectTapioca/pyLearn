#Create a function called greet()
#Write 3 print statements inside the function
#Call the greet() function and run your code

def greet():
    print("This is the first line")
    print("This is out to be the second")
    print("Finally the last")

greet()

#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Tom")

#Positional arguments for more than one input
def greet_with_inputs(name, location):
    print(f"Hello {name}")
    print(f"What is the temperature like in {location}?")

greet_with_inputs("Tom Shelby","Peaky")

#Keyword Arguments
greet_with_inputs(name = "Jerry", location = "NoWhere")
#For clean code you may want to take a moment to determine if the value is worth a keyword argument