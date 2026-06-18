# Day-31-Fibonacci-Sequence
Day 31/100 - Python Program to Find Fibonacci Numbers using Recursion

# Find Fibonacci Sequence (Recursive)
A program to generate and display the Fibonacci sequence up to a specified number of terms utilizing a recursive function.

## 📝 Description

This program calculates the famous **Fibonacci sequence**, a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1.

The script uses a pure **recursive approach**. It features a core recursive function, `fibonacci(n)`, which calls itself to calculate the mathematical value of the sequence at any given index ($F_n = F_{n-1} + F_{n-2}$). A secondary function validates the user's input to ensure it is a positive integer, and then uses a `for` loop to iteratively call the recursive function, printing the sequence line by line on a single continuous output string.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A single integer representing the total number of terms (`count`) to generate in the sequence.

### Output:

* If the input is valid, a prefix text: "Fibonacci sequence:" followed by the generated sequence of numbers separated by spaces.
* If the input is zero or negative, an error message: "Please enter a positive number."

### Rules:

1. The program must accept an integer input from the user representing the number of terms.
2. The program must evaluate if the input is valid (`count > 0`). If not, it must handle the error gracefully.
3. The program must utilize a **recursive function** (`fibonacci(n)`) to calculate the sequence.
4. **Base Case:** If `n <= 1`, the function must return `n` (which naturally sets the first two terms as 0 and 1).
5. **Recursive Step:** For all other values, the function must return `fibonacci(n - 1) + fibonacci(n - 2)`.
6. The sequence must be printed on a single line separated by spaces using the `end=" "` argument.

---

## 💡 Examples

### Example 1 (Standard Sequence)

**Input:**

```
5


```

**Output:**

```
Fibonacci sequence:
0 1 1 2 3 


```

**Explanation:** The program calculates the first 5 terms of the sequence.

* Term 0: 0
* Term 1: 1
* Term 2: 0 + 1 = 1
* Term 3: 1 + 1 = 2
* Term 4: 1 + 2 = 3

### Example 2 (Extended Sequence)

**Input:**

```
8


```

**Output:**

```
Fibonacci sequence:
0 1 1 2 3 5 8 13 


```

**Explanation:** The sequence successfully builds upon the previous sums (e.g., $5 + 8 = 13$).

### Example 3 (Single Term)

**Input:**

```
1


```

**Output:**

```
Fibonacci sequence:
0 


```

**Explanation:** The user asks for exactly 1 term. The loop runs for `i = 0`. The recursive function hits the base case (`0 <= 1`) and returns 0.

### Example 4 (Invalid Input)

**Input:**

```
-3


```

**Output:**

```
Please enter a positive number.


```

**Explanation:** The initial check `if count <= 0:` catches the negative number and prints the prompt without executing the recursive loop.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-31-Fibonacci-Sequence.git
cd fibonacci-sequence


```

2. **Run the program**:

```bash
python main.py


```

Enter the number of terms when prompted to see the recursive Fibonacci sequence generated.
