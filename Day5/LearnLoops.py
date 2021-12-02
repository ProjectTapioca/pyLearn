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