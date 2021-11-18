# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
new_name1 = input("What is your name? \n")
new_name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Hints
# lower() function
# count() function      true love

#Write your code below this line 👇

#initializing variables
new_name1 = str.lower(new_name1)
new_name2 = str.lower(new_name2)

#Letter count for words true and love
letter_true = 0
letter_love = 0

#Creating if statements to count for letters true and love in first name
if new_name1.count("t"):
    letter_true += new_name1.count("t")
if new_name1.count("r"):
    letter_true += new_name1.count("r")  
if new_name1.count("u"):
    letter_true += new_name1.count("u")
if new_name1.count("e"):
    letter_true += new_name1.count("e")
if new_name1.count("l"):
    letter_love += new_name1.count("l")
if new_name1.count("o"):
    letter_love += new_name1.count("o")
if new_name1.count("v"):
    letter_love += new_name1.count("v")
if new_name1.count("e"):
    letter_love += new_name1.count("e")
    
#Creating if statements to count for letters true and love in second name
if new_name2.count("t"):
    letter_true += new_name2.count("t")
if new_name2.count("r"):
    letter_true += new_name2.count("r")  
if new_name2.count("u"):
    letter_true += new_name2.count("u")
if new_name2.count("e"):
    letter_true += new_name2.count("e")
if new_name2.count("l"):
    letter_love += new_name2.count("l")
if new_name2.count("o"):
    letter_love += new_name2.count("o")
if new_name2.count("v"):
    letter_love += new_name2.count("v")
if new_name2.count("e"):
    letter_love += new_name2.count("e")
    
#Combining the numbers as a string to concatenate temporarily
letter_combine = str(letter_love) + str(letter_true)
    
#Recast into int to check the love score
if int(letter_combine) < 10 or int(letter_combine) < 90:
    print(f"Your score is {letter_true}{letter_love}, you go together like coke and mentos.")
elif int(letter_combine) > 40 and int(letter_combine) < 50:
    print(f"Your score is {letter_true}{letter_love}, you are alright together.")
else:
    print(f"Your score is {letter_true}{letter_love} ...fin")
