#Q20. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number
#  that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)

num = int(input("Enter a number: "))
original = num
sum_of_cubes = 0

while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** 3
    num //= 10

if sum_of_cubes == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
