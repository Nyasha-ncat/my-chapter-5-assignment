"""
COMP 163 - Introduction to Programming
Assignment: Chapter 5 - Loop Mastery
Name: Nyasha Chimombe
GitHub Username: Nyasha-ncat
Date: 2/20/2025
Description: This program demonstrates mastery of while, for, and nested loops through challanges.
"""


# Collatz Sequence Generator
# get input from user
current_number = int(input("Enter starting number: "))
print(f"Sequence: {current_number}", end=" ")
steps = 0
# use a while loop because we don't know how many steps
while current_number != 1:
    
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = (current_number * 3) + 1
    print(current_number, end=" ")
    
    steps += 1
print() 
print(f"Steps: {steps}")
print() 

# Prime Number Checker

# get input from user
number_to_check = int(input("Enter a number: "))

# tell the user of the range we are testing
print(f"Testing divisors from 2 to {number_to_check - 1}...")

# Use a boolean flag to track if we find a divisor.
is_prime = True

# We use a for loop with range() because we have a known definite number of potential divisors to test 
for divisor in range(2, number_to_check):
    
    if number_to_check % divisor == 0:
        print(f"{number_to_check} is not prime (divisible by {divisor})")
        is_prime = False
        # Exit the loop immediately since we only need to find the first divisor
        break 

# If the loop finishes and our flag is still True, no divisors were found.
if is_prime:
    print(f"{number_to_check} is prime!")
print() 
