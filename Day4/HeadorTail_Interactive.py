import random

coin_choice = int(input("1 for Heads or 2 for tails?\n"))
random_coin = random.randint(1,2)

print(f"It's {random_coin}, you chose {coin_choice}")


#Dr. Angela answer
# import random

# random_side = random.randint(0, 1)
# if random_side == 1:
#   print("Heads")
# else:
#   print("Tails")

