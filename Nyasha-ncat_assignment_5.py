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

# Step 3: Multiplication Table Grid

# Display the title 
print("Multiplication Table:")

# Header Row
print("    ", end="") 
for col_header in range(1, 11):
    # Each header number gets 4 spaces of width
    print(f"{col_header:4}", end="")
print() 

# The outer loop represents each row (1-10)
for row in range(1, 11):
    
    # Print the row number at the start, formatted to take 2 spaces
    print(f"{row:2}", end=" ")
    
    # The inner loop represents each column (1-10)
    for col in range(1, 11):
        product = row * col
        # Print the product with 4 spaces of width to keep columns straight
        print(f"{product:4}", end="")
    
    # After finishing all columns in a row, use print() to move to the next line
    print()

print() 

# Statistics Dashboard
print("=== Statistics Dashboard ===")
print("Enter positive numbers (enter -1 to finish):")

# Initialize variables for tracking statistics
numbers_list = []
total_sum = 0
count = 0
minimum = None
maximum = None

# Part A: Data Collection (While Loop)
# Use a while loop because we don't know how many numbers the user will enter
while True:
    user_input = int(input("Enter number: "))
    
    # Check for the sentinel value to break the loop
    if user_input == -1:
        break
    
    # Process valid positive numbers
    numbers_list.append(user_input)
    total_sum += user_input
    count += 1
    
    if count == 1:
        minimum = user_input
        maximum = user_input
    else:
        if user_input < minimum:
            minimum = user_input
        if user_input > maximum:
            maximum = user_input

#  Statistics Display
if count > 0:
    average = total_sum / count
    
    print("\n=== Statistics ===")
    print(f"Count: {count} numbers")
    print(f"Sum: {total_sum}")
    # Show average with one decimal place using :.1f
    print(f"Average: {average:.1f}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

    # Part C: Bar Chart (Nested Loops)
    print("\n=== Bar Chart ===")
    # The outer loop goes through each number stored in our list
    for num in numbers_list:
        # Display the number with spacing
        print(f"{num:2}: ", end="")
        
        # The inner loop prints asterisks equal to the value of the number
        for i in range(num):
            print("*", end="")
        
        # Move to the next line after the inner loop finishes the stars
        print()
else:
    print("No numbers were entered.")
