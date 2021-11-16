# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Convert input values to float
new_height = float(height)
new_weight = float(weight)

#Provide string values a variable
un_weight = "underweight"
norm_weight = "normal weight"
sl_weight = "slightly overweight"
obese_weight = "obese"
clin_weight = "clinically obese"

#Calculate the BMI
bmi = round((new_weight/(new_height ** 2)))

#Check BMI from underweight to clinically obese
if bmi <= 18.5:
    print(f"Your bmi is {bmi}, you are {un_weight}.")
elif bmi <= 25:
    print(f"Your bmi is {bmi}, you are {norm_weight}.")
elif bmi <= 30:
    print(f"Your bmi is {bmi}, you are {sl_weight}.")
elif bmi <= 35:
        print(f"Your bmi is {bmi}, you are {obese_weight}.")
else:
    print(f"Your bmi is {bmi}, you are {clin_weight}.")

    




