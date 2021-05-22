Name = "Hello World"
print(Name)
print("*************String********************")

# String
str = "Pallab.com"
str1 = "Debnath"
str3 = "Pal"

print(str[1])   #a
print(str[0:5])  # substring
print(str+" " + str1)   # concatenation
print(str3 in str)  # substring check
var = str.split(".")
print(var)  #return list
print(var[0])
str4 = " great "
print(str4.strip()) # space stripping
print(str4.lstrip())
print(str4.rstrip())

print("************mutiple data types*********************")
a, b, c = 5, 4.3, "Hi"
print(a, b, c)
print ("Value of c is : ", c)
# Concat different data types
print("{} {}".format("Value of b is : ", b))
# find data types
print(type(b))

print("**************List*******************")
# List is a data type which allow multiple different data types
Values = [1, 4.3, "hello", 23, "list2", 100.99]
print(Values[-1])
print(Values[1:3])
Values.insert(2, "Pallab")
Values.append("Debnath")
del Values[1]
print(Values)

print("*************Tuple********************")
#Tuple - Same as list but immutable
TupleValues=(1, 4.3, "hello", 23, "list2", 100.99)
print(TupleValues[2])

print("**************Dictionary*******************")

#Dictionary
dict={1: "First Name", 3: "Last Name", "age": 33}
print(dict[3])
print(dict["age"])
#create dict in run time
dict1={}
dict1["first name"]="rick"
dict1["last name"]="langdon"
dict1["age"]=25
print(dict1)










