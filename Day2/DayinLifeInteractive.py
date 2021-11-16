# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
#Days, weeks, months left
#Write your code below this line 👇

#Converts age into an int and calculates years left to 90
int_age = int(age)
new_age = 90 - int_age

months_left = new_age * 12
weeks_left = new_age * 52
days_left = new_age * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} left.")









