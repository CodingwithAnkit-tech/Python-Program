#Q21. Write a program to add first n terms of the following series using a while loop: 
#1/1! + 1/2! + 1/3! + …….. + 1/n!

n = int(input("Enter number: "))
i = 1
sumv = 0.0
while i <= n:
    fact = 1
    j = 1
    while j <= i:
        fact *= j
        j += 1
    sumv += 1 / fact
    i += 1
print("Sum =", sumv)
