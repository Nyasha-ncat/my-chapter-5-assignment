"""
COMP 163 - Introduction to Programming
Assignment: Chapter 5 - Loop Mastery
Name: Nyasha Chimombe
GitHub Username: Nyasha-ncat
Date: 2/20/2025
Description: This program demonstrates mastery of while, for, and nested loops through challanges.
"""


# Collatz Sequence Generator
current_number = int(input("Enter starting number: "))
print(f"Sequence: {current_number}", end=" ")
steps = 0
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
