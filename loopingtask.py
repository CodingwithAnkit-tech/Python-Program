# 1.Wap to print n natural numbers

# n = eval(input("Enter the number: "))
# if type(n) == int:
#     i=1
#     while i<n:
#         print(i)
#         i=i+1

#----------------------------------------------

# 2.Wap to print n natural numbers in reverse order.

# n = eval(input("Enter the number: "))
# if type(n) == int:
#     while n>0:
#         print(n)
#         n-=1

#--------------------------------------------------

# 3.Wap to print natural numbers in a given range

# start = eval(input("Enter the  start number: "))
# end = eval(input("Enter the  end number: "))
# if type(start) == int and type(end) ==int:
#     while start<=end:
#         print(start) 
#         start+=1


#------------------------------------------------------------------------------
# 4.Wap to print user name 10 times

# user = eval(input("Enter the namme: "))
# if type(user) == str:
#     i=1
#     while i<=10:
#         print(user)
#         i+=1

#-------------------------------------------------------------   

# 5.Wap to print the multiplication table.

# table = int(input("Enter  the number: "))
# if type(table) == int:
#     i=1
#     while i<=10:
#         print(table,'x',i,'=',table*i)
#         i+=1

#------------------------------------------------------------------

# 6.Wap to print n natural even numbers.

# n = eval(input("Enter the number: "))
# if type(n) == int:
#     i=1
#     while i<=n:
#         if i%2==0:
#             print(i,end=" ")   
#         i+=1

        
# n = eval(input("Enter the number: "))
# if type(n) == int:
#     i=1
#     while i<=n:
#         if i%2 == 0:
#             print(i)      
#         i+=1
#-----------------------------------------------------------------------------------------------------


# 7.Wap to print n natural odd numbers.	

# n = eval(input("Enter the number: "))
# if type(n) == int:
#     i=1
#     while i<=n:
#         if i%2!= 0:
#             print(i)      
#         i+=1
#----------------------------------------------------------------------------------------------------------------

# 8.Wap to print n natural palindrome numbers	
# n = eval(input("Enter the number: "))
# if type(n) == int:
#     i=1
#     while n==n-1:
#         print(i)
#         i+=1
#-----------------------------------------------------------------------------------------


# 9.Wap to print the sum of n natural number


# n = eval(input("Enter the number: "))
# i=1
# sum=0

# while i<=n:
#         sum+=i      
#         i+=1
# print("The sum is :". sum)
#--------------------------------------------------------------------------------------------

# 10.Wap to print product of n natural numbers.

#


# 11.Wap to print factorial a number.
# n = int(input("Entewr the number :"))
# fact = 1
# i = 1
# while i<=n:
#     fact = fact*i
#     i+=1
# print("factorial of",n,"is",fact)

# 12.Wap to print the digits of a number




# 13.Wap to find the sum of digits of a number.

# n = int(input("Enter a number: "))
# add=0
# i=1
# while n>0:
#     last_digit =n%10
#     add+=last_digit
#     n//=10
# print(add)

#----------------------------------------------------------

# 14.Wap to find the product of digits of a number.

# n=int(input("Enter the number :"))
# print("The digit of number are:")
# product=1
# while n>0:
#     digits = n %10
#     product*=digits
#     n=n//10
# print("The product of digit is:",product)
#---------------------------------------------------------

# 15.Wap to reverse a number without using slicing

# n=int(input("Enter the number :"))
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n//=10
# print(rev)
#------------------------------------------------------------------------

# 16.Wap to reverse a number without using type casting and slicing.

# n=int(input("Enter the number :"))
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n//=10
# print(rev)


# 17.Wap to count the no. of zeros present in a number

# n=int(input("Enter the number :"))
# count=0
# while n>0:
#     ld=n%10
#     if ld==0:
#         count+=1
#     n//=10
# print("Count :",count)

#-------------------------------------------------------------

# 18.Wap to print the factors of a number.

# n=int(input("Enter the number :"))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1

#-----------------------------------------------------

# 19.Wap check the no. is prime or not

# n=int(input("Enter the number :"))
# if n<=1:
#      print(n,"is not a prime number")
# else:
#      i=2
#      is_prime=True
#      while i<n-1:
          



# 20.Wap to check the no. is Armstrong no. or not. #153,370

# n = int(input("Enter the number :"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print(n,"is not a number")
#             break
#     else:
#         print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")

#------------------------------------------------------------------

# 21.Wap to check the no. disarium no. or not. #89,135,175

# n = int(input("Enter the number :"))
# sum=0
# a=n
# while n>0:
#     ld=n%10
#     p=len(str(n))
#     n//=10
# if sum==a:
#     print(a,"is a disarium number")
# else:
#     print(a,"is not a disarium number")


# 22.Wap to check the given number is a Harshad no. or not #36,18,132

# 23.Check the given no.is spy number or not. #1124,123,22		

# 24.Wap to check the no. is perfect no. or not

# 25.Wap to check the no. is a strong no. or not.

# 26.Wap to check is xylem or phloem no.

# 27.Create a list of n no. values provided by the userś

# 28.Given a list of numbers, count how many are even and how many are odd.





# 29.Wap to print all the values of a collection (str, list, tuple)

# l=eval(input("Enter the list of collection:"))
# i=0
# while i<len(l):
#     print(l[i], end=' ')
#     i+=1


# 30.Wap to print the string values from a given a list

# st=eval(input("Enter the list :"))
# if type(st)==list:
#     i=0
#     while i<len(st):
#         if type(st[i])==str:
#             print(st[i])
#         i+=1

# 31.Wap to extract all the palindrome word from a given list


# &nbsp;	s1 = \[10,404,'hii',4.5,'eye',7-8j,'bye','madam',202]

# &nbsp;	o/p= \['eye', 'madam']

# 32.Wap to print all the characters of a string

# 33.Wap to print all vowels present in a word

# 34.Wap to extract all the strings from a list.

# 35.Wap to  extract all the palindrome no. from a list

# 36.Wap to return a tuple containing n natural odd numbers

# 37.Wap to print all the values of a set

# 38.Wap to extract all the float values from a set and store in a list

# 39.Wap to toggle the string

# 40.Wap to reverse the given word





# Nested loop :-

# ============



# 1. Wap to extract all the prime numbers from a given list
# 2. Wap to extract all the Armstrong number from a given list.
# 3. Wap to extract all the perfect numbers from a tuple
# 4. Wap to extract the xylem numbers from a list





# &nbsp;		


# wap prduct of all the digits of a number

# n=int(input("Enter a number :"))
# pro =1
# while n>0:
#     last_digit = n%10
#     pro = pro*last_digit
#     n = n//10
# print("Product of the digits :",pro)

# find the product odd digits and sum of even digit of a given number
# n=int(input("Enter a number :"))
# sum=0
# pro=1
# while n>0:
#     ld=n%10
#     if ld%2==0:
#         sum+=ld
#     else:
#         pro*=ld
#     n//=10
# print("sum:",sum)
# print("Product:",pro)

# wap to print all the character of a string
# s="Hello"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])




import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


name = input("input your name: ")
age = input("input your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))