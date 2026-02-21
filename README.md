[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IiqXY2S6)
# Loop Mastery Assignment

**Student Name:** [Nyasha Chimombe]  
**GitHub Username:** [Nyasha=ncat]  
**Date:** [2/20/2026]

## Overview

This assignment demonstrates mastery of while loops, for loops, and nested loops through four programming challenges. Each challenge was selected to showcase the appropriate loop type for different problem scenarios.

---

## Loop Type Analysis

### Step 1: Collatz Sequence - While Loop

**Why while loop?**  
[A while loop is the best choice because the number of iterations needed to reach 1 is unknown at the start. It depends entirely on the path of the starting number.]

**How it works:**  
[I used a "while current_number != 1: "condition. Inside, I used the modulo operator % to check if the number is even or odd, then applied the appropriate Collatz math (dividing by 2 or multiplying by 3 and adding 1).]

**Example:**
```
Enter starting number: 13
Sequence: 13 40 20 10 5 16 8 4 2 1
Steps: 9
```

---

### Step 2: Prime Checker - For Loop

**Why for loop?**  
[A for loop is ideal here because we are testing a specific, known range of numbers. The iteration count is predictable and finite.]

**How it works:**  
[I used range(2, number_to_check) to iterate through all potential divisors. If number % divisor == 0 evaluates to true, the program identifies a factor, marks the number as not prime, and breaks the loop.]

**Example:**
```
Enter a number: 17
Testing divisors from 2 to 16...
17 is prime!
```

---

### Step 3: Multiplication Table - Nested Loops

**Why nested loops?**  
[Nested loops were needed to generate a 2D grid. The outer loop manages the rows (1-10), while the inner loop calculates every column value for that specific row before moving to the next line.]

**Outer vs Inner:**  
[The outer loop handles the rows to ensure we finish one full line of products before moving down. The inner loop handles the columns to print the products side-by-side.]

**How it works:**  
[I used f-string alignment (:4) to ensure all products take up exactly 4 characters of space, keeping the table columns perfectly straight.]

**Example:**
```
Multiplication Table:
    1   2   3   4   5   6   7   8   9  10
 1  1   2   3   4   5   6   7   8   9  10
 2  2   4   6   8  10  12  14  16  18  20
...
```

---

### Step 4: Statistics Dashboard - All Three Loop Types

**Why all three?**  
- **While loop:** [Used for data collection because we don't know how many numbers the user will enter before typing the sentinel value -1.]
- **For loop:** [Used to calculate the statistics and to iterate through the list of stored numbers.]
- **Nested loops:** [Used for the bar chart; the outer loop moves through each number in the list, and the inner loop prints a specific number of asterisks.]

**How it works:**  
[Numbers are collected in a list until the sentinel value -1 is hit. I then used standard logic to find the sum, average, min, and max. Finally, I printed a visual bar chart where the length of each bar matches the value of the number.]

**Example:**
```
=== Statistics Dashboard ===
Enter positive numbers (enter -1 to finish):
Enter number: 5
Enter number: 12
Enter number: 8
Enter number: 15
Enter number: 3
Enter number: -1

=== Statistics ===
Count: 5 numbers
Sum: 43
Average: 8.6
Minimum: 3
Maximum: 15

=== Bar Chart ===
 5: *****
12: ************
 8: ********
15: ***************
 3: ***
```

### Edge Cases Considered

[List any edge cases you thought about or tested:]
- What happens if the user enters 1 immediately?
- Example: What if the user enters -1 as the very first input?

---

## Challenges and Solutions

### Challenge 1: Aligning the Multiplication Table Grid]
**Solution:** [I used Python's f-string formatting with a width specifier (f"{product:4}"). This forces every number to occupy exactly four characters of space, ensuring that the columns align perfectly regardless of how many digits the number has.](AI helped me with this problem)
---

## Key Learnings

[Reflect on what you learned from this assignment:]
- Aligning the Multiplication Table Grid, using the the f string for that, is one thing i learned 
- What was the most challenging part?- for me it was just making sure the logic made sence and the code would actually run and the indenting, cause it still trips me up at times.
- How did this assignment improve your programming skills? It made me aware of my weaknesses and made me more confident in loops. and git too, its still a process to get git to work how I want it.

---

## AI Usage

[Choose one:]

**Option B - AI Used (be specific):**
AI assistance was used for the following:

1. **[Specific concept]:**  
   - What you asked: [How to get my table alligned, how it needs to be. I pasted my code, and what the instructions said needed to be done to pass the test case]
   - What you learned: [i learned how to allocate 4 spaces  ]
   - How you used it: [It honestly taught me how to do it, cause i could not figure it out for the life of me.]

2. **[statistical dashboard ]:**  
   - What you asked: [what am i supposed to do here/ how do i initilize ]
   - What you learned: [i had forgotten about inizilizing for a second, but once i was shown what exactly i was doing, , I was okay]
   - How you used it: [Used  it as aguide ]

**All core logic and implementation were developed independently after understanding the concepts.**


## Commit History

This assignment was developed incrementally with meaningful commits:

---

**Declaration:** I certify that this assignment is my own work and I have not copied code from other students or unauthorized sources. Any AI assistance used has been properly documented above.

**Signature:** [Nyasha Chimombe]  
**Date:** [2/20/2026]
