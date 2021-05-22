items = 0

#type 1 - failing testcase
'''
if items!=2:
    raise Exception ("items not matching")
'''
#type 2 - - failing testcase
'''
assert (items == 0)
'''
#type 3 - pass testcase with created exception
'''
try:
    if items == 0:
        print("good")
except:
    print("items not matching")
'''

#type 4 - pass testcase but collect script exception

try:
    if items == 0:
        print("good")
except Exception as e:
    print(e)
finally:
    print("Done")

