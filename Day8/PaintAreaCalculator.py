# Write your code below this line 👇

import math

def paint_calc(height, width, cover):
    paint_area = (height * width) / cover
    print(f"You will need {math.ceil(paint_area)} cans")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   



# 🚨 Don't change the code below 👇
test_h = int(input("Please input the height ")) # Height of wall (m)
test_w = int(input("Please input the width")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)