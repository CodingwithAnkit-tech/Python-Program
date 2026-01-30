# def is_prime(n):
#     i=2
#     is_prime=true
#     while i<=n-1:
#         if n%i==0:
#             is_prime=False
#             break
#         i+=1
#     print(is_prime)
# is_prime(5)


# def is_prime(num):
  
#     for i in range(2,num):
#         if num%i == 0:
#             print("False")
#             break
#     else:
#         print("True")
# is_prime(42)


# def length(a):
#     count = 0
#     if type(a) in [str,list,tuple]:
#         for i in a:
#             count+=1
#     print(count)
# a=eval(input("Enter the data :"))
# length(a)


#--------------------------------------------------------------------
# function with return keyword-----------------------------------------------------
#1) --return keyword is used to return the values from functional space to main space to main space
#2) --  it returns values with flow to the place where it is called 
#3)-- we can return multiple values with the help of reurn keyword in the form of tuple 
#4)-  it will not execute any statement uder the return keyword


# with return keyword

# def main():
#     print('hii')
#     return 10,20,True,4.5
# print(main())

# without return 


# def add(a, b):
#     print(a + b)   # just prints the result

# add(5, 3)

# with return keyword

# def add(a, b):
#     return a + b   # sends the result back

# result = add(5, 3)
# print("The sum is:", result)



# def check_number(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     else:
#         return "Zero"

# print(check_number(5))   # Output: Positive
# print(check_number(-2))  # Output: Negative
# print(check_number(0))   # Output: Zero


# def calculate(a, b):
#     return a + b, a - b, a * b

# add, sub, mul = calculate(10, 5)
# print(add, sub, mul)


# hecking whether a number is a palindrome number
# def is_pr():
#     num = int(input("Enter the number: "))
#     return str(num) == str(num)[::-1]
# print(is_pr())



# s = int(input("Enter the number :"))
# n = int(input("Enter the number :"))
# for i in range(2,n+1):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 break
#             else:
#                 print(i)



# Program to print all prime numbers between 1 and n using nested for loop

# n = int(input("Enter the number: "))
# for num in range(2, n + 1):        
#     for i in range(2, num):        
#         if num % i == 0:           
#             break
#     else:
#         print(num)
                    

# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return  False
#         else:
#             return True
# print("Number is prime :",is_prime(int(input("Enter the value:"))))

# amstrong number series




# Function to check Armstrong number


# def arm(num):
#     original = num
#     result = 0
#     digits = len(str(num))
#     while num > 0:
#         digit = num % 10
#         result += digit ** digits
#         num //= 10
#     return result == original
# n = int(input("Enter the number: "))
# count = 0
# for i in range(1, n + 1):
#     if arm(i) == True:
#         print(i)
#         count += 1

# print("Total Armstrong numbers found:",count)












    


