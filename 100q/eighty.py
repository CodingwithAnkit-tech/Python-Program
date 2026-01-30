#Q18. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.

n = int(input("Enter number of terms: "))
a = 0
b = 1
i = 0

while i < n:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    i += 1
