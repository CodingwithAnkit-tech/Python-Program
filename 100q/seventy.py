#Q17. Write a program to display the number names of the digits of a number entered by 
#user, for example if the number is 231 then output should be Two Three One


num = int(input("Enter a number: "))
num_str = str(num)  # string me convert
i = 0

while i < len(num_str):
    digit = num_str[i]
    if digit == '0':
        print("Zero", end=' ')
    elif digit == '1':
        print("One", end=' ')
    elif digit == '2':
        print("Two", end=' ')
    elif digit == '3':
        print("Three", end=' ')
    elif digit == '4':
        print("Four", end=' ')
    elif digit == '5':
        print("Five", end=' ')
    elif digit == '6':
        print("Six", end=' ')
    elif digit == '7':
        print("Seven", end=' ')
    elif digit == '8':
        print("Eight", end=' ')
    elif digit == '9':
        print("Nine", end=' ')
    i += 1
