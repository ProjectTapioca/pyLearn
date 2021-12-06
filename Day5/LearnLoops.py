fruits = ["Apple", "Peach", "Pear"]

#fruit is the variable assigned to the items in the list 'fruits'
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

#Loops and range
for number in range(1,10,2):
    print(number)
#This only prints 1 - 9, have to change the 10 to a 11 if want to print from 1 - 10
#The 2 shows how it will skip/step acorss different numbers

total = 0
for number in range(1, 101):
    total += number
print(total)

#While Loops
while something_is_true:
    print("something")
    #Do something repeatedly
    
#For Loops
for item in list_of_items:
    print("Do this")
    #Do something to each item

for number in range(a, b):
    print(number)
    
#When to use for loop and while loop
#For loops are for when wanting to reiterate specific number of times
#   in a range or list

#While loops are for when you don't really care how many times
#   it takes to carry out a functionality, just as long as it
#   does it until the condition is met