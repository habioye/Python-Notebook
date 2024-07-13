def pprint(string: input):
    if input is None:
        print("nothing added to input")
    else:
        print(input)
    output.call()
    print("----------------------------------------------------------------")
        
# Lists: ordered, mutable, allows duplicate elements
mylist = ["bannana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)
try:
    item = mylist[1]
    item = mylist2[6]
except IndexError:
    print("You should not select out of the index")


# last item
item = mylist[-1]
print(mylist[-1])
# second last
item = mylist[-2]
print(mylist[-2])

for i in mylist:
    print(i)

# or
for x in mylist:
    print(x)

if "banana" in mylist:
    print("yes")
else:
    print("no")

if "lemon" in mylist:
    print("yes")
else:
    print("yes")

# To check the number of lements in the list you can just use len()
mylist.append("lemon")

mylist.insert(1, "blueberry")

print(mylist[1])

# WAe can remove items at the end/last position.
item = mylist.pop()
print(mylist,item)

copy = mylist.copy()
item = mylist.remove("cherry")
print(mylist,item)

item = mylist.clear()
print(mylist,item)

mylist = copy

item = mylist.reverse()
print(item,mylist)


item = mylist.sort()
print(item, mylist)

# Works for numbers
mylist = [4,3,1,-1,-5,10]
print(mylist)

item = mylist.sort()

print(mylist)

item = sorted(mylist)

print(item)

mylist = [0]*5

print(mylist)

mylist2 = [1,2,3,4,5]


new_list = mylist+mylist2

mylist = [1,2,3,4,5,6,7,8,9]

a = mylist[1:5]

print(mylist,a)

b = a[::1]
c = a[::2]
d = a[::-1]

list_org = ["bannana", "cherry", "apple"]
list_cpy = list_org

print(list_cpy)


list_cpy.append("lemon")

print(list_cpy)
print(list_cpy)

a = [i for i in range(1,7)]
b = [i*i for i in a]
print(a,b)
