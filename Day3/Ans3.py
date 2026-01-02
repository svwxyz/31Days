mylist = []
mynum = int(input("Enter total number to be inserted::"))
for i in range(0,mynum):
    x = int(input("Enternumber to be inserted::"))
    mylist.append(x)

print(mylist)
print(max(mylist))
print(min(mylist))
print(sum(mylist))
print(sum(mylist)/mynum)