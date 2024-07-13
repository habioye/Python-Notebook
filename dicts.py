# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name":"Max","age":28,"city":"New York"}
print(mydict)

mydict2 = dict(name="Mary",age=27,city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

value = mydict["age"]
print(value)

try:
    value = mydict["lastname"]
except KeyError:
    print("Invalid Key")

mydict["email"] = "asdffasdf@gmail.com"

mydict["phone"] = "234-654-2348"

print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)
mydict.popitem()

print(mydict)

for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)
for value in mydict.values():
    print(value)

mydict_cpy = mydict

mydict_cpy["email"] = "max@xyz.com"

print(mydict_cpy)
print(mydict)

mydict = {"name":"Max","age":28,"city":"New York"}
print(mydict)

mydict2 = dict(name="Mary",age=27,city="Boston")
print(mydict2)
mydict.update(mydict2)
print(mydict)
s = set()


# You want to be careful with the keys
# They are not the same as in lists
my_dict = {3:9, 6: 36, 9:81}
print(my_dict)
try:
    value = mydict[3]
    print("passed")
    value = mydict[0]
except KeyError:
    print("You need to use the actual keys and not just indexes")

mytuple = (8,7)
mydict = {mytuple: 15}

print(mydict)
mylist = [8,7]
try:
    mydict = {mylist: 15}
except TypeError:
    print("lists are unhashable types")


