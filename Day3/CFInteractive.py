#Create a program that checks if the input number is odd or even
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_reamin = number % 2

if num_reamin == 0:
    print("Number is even.")
else:
    print("Number is odd")