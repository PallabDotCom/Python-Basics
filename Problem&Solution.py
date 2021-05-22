# If else find odd even and print
from pip._vendor.distlib.compat import raw_input

n= int (input("Enter data:"  ))
if n%2 !=0:
    print("Weird")
if n%2==0 and 2<=n<=5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

    # Arithmetic Operators
    a = int(input("Enter A data:"))
    b = int(input("Enter B data:"))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a / b)

#For loop
    n = int(raw_input())
    for i in range(0,n,1):
        print(i**2)

#function leap year
def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4 == 0):
        if (year % 400 == 0):
            leap = True
        elif (year % 100 == 0):
            leap = False
        else:
            leap = True

    return leap


year = int(raw_input())

#Print function - Avoid printing in new line
if __name__ == '__main__':
    n = int(raw_input())

for i in range (1,n+1,1):
    print(i,end="")
