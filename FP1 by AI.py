import random

# Greeting and getting user's name
print("Hello! Welcome to the Lucky Number Generator.")
varUserName = input("What is your name?\n")

# Greet the user by name
print(f"\nIt's a pleasure to meet you, {varUserName}!")
print("Let's generate your six lucky numbers...")

# Generate the six random numbers
# The first five numbers are between 1 and 69
# The last number is between 1 and 26
ball1 = random.randint(1, 69)
ball2 = random.randint(1, 69)
ball3 = random.randint(1, 69)
ball4 = random.randint(1, 69)
ball5 = random.randint(1, 69)
ball6 = random.randint(1, 26)


print("\nHere are your numbers:")

# Print the numbers with specific spacing
# Two spaces between the first five numbers and four spaces before the last one
print(f"{ball1}  {ball2}  {ball3}  {ball4}  {ball5}    {ball6}")

# Farewell message
print(f"\nGood luck, {varUserName}! Have a wonderful day.")