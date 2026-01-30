#Q13. Write a program to check whether a number is prime or not using while loop.

num = int(input("Enter a number: "))
i = 2
is_prime = True

while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if num < 2:
    print("Not Prime")
elif is_prime:
    print("Prime")
else:
    print("Not Prime")
