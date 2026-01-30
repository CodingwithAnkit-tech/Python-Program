#Q12. Write a program to print all even numbers that falls between two numbers (exclusive 
#both numbers) entered from the user using while loop. 

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
i = start + 1  # exclusive, isliye +1

while i < end:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1