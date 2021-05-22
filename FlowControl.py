# If-Else condition
a = 2
b = 4
if a > b:
    print("condition matched")
else:
    print("condition failed")

print("*********************************")
######## For loop #########
Values = [1, 4.3, "hello", 23, "list2", 100.99]
for i in Values:
    print(i)
print("*********************************")
#sum of numbers 1 to 5
summation = 0
for j in range(1, 6): #max index is j-1=5
    summation = summation+j
print(summation)

print("*********************************")
#skipping index
for k in range(1, 6, 2):
    print(k*'*')
print("*********************************")
for m in range(5):
    print(m*'*')

print("*********************************")
###### While Loop ## continue ## break ###

it=6
while it > 1:
    if it == 4:
        it = it - 1
        continue
    if it == 2:
        break
    print(it)
    it = it-1

print("*********************************")
## Function ## It's a group of related statements that perform a specific task

#function declaration
def function1(name):
    print("Hello "+name)

#function call
function1("World")
print("*********************************")


def addint(a, b):
    return a+b


print(addint(2, 3))
