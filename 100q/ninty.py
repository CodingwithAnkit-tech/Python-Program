#Q19. Write a program to print the factorial of a number accepted from user.num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial:", fact)
