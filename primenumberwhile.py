# Python Program to Check Prime Number using While Loop
# Prime number is a number that is greater than 1 and divided by 1 or itself.
# In other words, prime numbers can’t be divided by other numbers than itself or 1.
# For example- 2, 3, 5, 7, 11, 13, 17, 19, 23…. are the prime numbers.

# Take the humber
num = int(input("Enter a number ( greater than 1)"))  
f = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print("The entered number is a PRIME number")
else:
    print("The entered number is not a PRIME number")
