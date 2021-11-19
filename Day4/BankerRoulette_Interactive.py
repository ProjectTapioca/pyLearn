#Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#Don't change the above vode

#Write code below this line
import random

#Getting the range of names in thelist
name_range = len(names)

#Using a random function to choose a random index from the range of names
name_index = random.randint(0, name_range - 1)

print(names[name_index] + " is going to buy the meal today!")


 #Dr. Angela Solution
 #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + " is going to buy the meal today!")