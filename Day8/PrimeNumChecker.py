# Write your code below this line 👇

def prime_checker(number):
    max_range = number
    prime_status = 1
    
    while prime_status < max_range:
        for count in range(2, max_range):
            math_result = number % count
            if math_result > 0:
                print(f"{count}")
                print("Is a prime")
                prime_status += 1
                return
            elif math_result == 0:
                print("Is not a prime")
                prime_status += 1
            else:
                print("Not sure")

        #if number has a remainder, it is prime
    
#idea
        # number input to be checked would be the limit of the loop that 
        #calculates for prime

#Flow
        #number is inputted
        #max range to test is the said number
        #goes into a loop, if the counted divisor results in a whole number
            #go into a while loop counter
        #exit and notify the user
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)