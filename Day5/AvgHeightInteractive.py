# 🚨 Don't change the code below 👇
from typing import Counter


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

height_total = 0
counter = 0

for x in student_heights:
    height_total += x
    counter += 1
    
avg_height = height_total/counter

print(round(avg_height))