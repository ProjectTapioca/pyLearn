#Menu and greeting
print("Welcome to Python Pizza Deliveries!")
print("Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\nPepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3\nExtra cheese for any size pizza: +$1")

# 🚨 Don't change the code below 👇
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Creating variables
total_price = 0.00
s_pizza = 15.00
m_pizza = 20.00
l_pizza = 25.00

s_pepperoni = 2.00
ml_pepperoni = 3.00

ex_cheese = 1.00

if size == "S":
    total_price += s_pizza
    if add_pepperoni == "Y":
        total_price += s_pepperoni
    elif add_pepperoni == "N":
        total_price
    if extra_cheese == "Y":
        total_price += ex_cheese
        print(f"Your final bill is: ${total_price}")
    elif add_pepperoni == "N":
        total_price
    #Keep in mind this is outside of the elif block so it can be executed 
    print(f"Your final bill is: ${total_price}")
    
elif size == "M":
    total_price += m_pizza
    if add_pepperoni == "Y":
        total_price += ml_pepperoni
    elif add_pepperoni == "N":
        total_price
    if extra_cheese == "Y":
        total_price += ex_cheese
        print(f"Your final bill is: ${total_price}")
    elif add_pepperoni == "N":
        total_price
        
    print(f"Your final bill is: ${total_price}")
    
elif size == "L":
    total_price += l_pizza
    if add_pepperoni == "Y":
        total_price += ml_pepperoni
    elif add_pepperoni == "N":
        total_price
    if extra_cheese == "Y":
        total_price += ex_cheese
        print(f"Your final bill is: ${total_price}")
    elif add_pepperoni == "N":
        total_price
        
    print(f"Your final bill is: ${total_price}")

#Dr. Angela Solution
# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
    
# if extra_cheese == "Y":
#   bill += 1
  
# print(f"Your final bill is: ${bill}.")




