# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Math for checking leap year

#Every year that is evenly divisible by 4
div_4 = year % 4

#Except every year that is evenly divisible by 100
div_100 = year % 100

#Unless the year is also evenly divisible by 400
div_400 = year % 400

if div_4 == 0:
    if div_100 == 0:
        if div_400 == 0:
            print("Leap Year!")
        else:
            print("Not Leap Year!") 
    else:
        print("Leap Year!")
else:
    print("Not Leap Year!")
    