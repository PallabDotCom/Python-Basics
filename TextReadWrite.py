#file= open('test.txt', 'r')
# Optimized way to open file is below line. You don't have to close the file at the end.
# with open('test.txt') as file:
#read all lines of file
'''
print(file.read())
'''

#read n number of characters from file
'''
print(file.read(7))
'''
#read one single line at a time
'''
print(file.readline())
'''
#Print line by line using readline
'''
line = file.readline()
while line !="":
    print(line)
    line = file.readline()
'''
#list will be returned in readlines
'''
print(file.readlines())
'''
#Iterate for loop to get all the lines from list
'''
line = file.readlines()
for i in line:
    print(i)
'''
#read the file , reverse list and write it back
'''
line = file.readlines()
file= open('test.txt', 'w')
for i in reversed(line):
    file.write(i)
    print("Done")
'''
#another way to do it -
with open('test.txt', 'r') as reader:
    line = reader.readlines()
    with open('test.txt', 'w') as writer:
        for i in reversed(line):
            writer.write(i)


#file.close()



