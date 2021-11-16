#Tip Calculator

print("Welcome to the tip calculator!")

#Input prompts
bill_total = float(input("What was the total bill? $"))
tip_selection = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

#Math
people_pay =round((bill_total/num_people) * (1 + (tip_selection/100)), 2)


#Output
print(f"Each person should pay: ${people_pay}")


#Angela Solution
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)