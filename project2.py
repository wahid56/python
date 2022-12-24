numberlist=[1,2,3,4,5,6,7,8,9,10 ]
print(numberlist)
print(numberlist[::-1])
print(numberlist[3:6])
numberlist2=['a','b','c','d']
result=numberlist+numberlist2
print(result)
print(result[::-1])
print(result[2:10])

productlist=["happy",['w','t','s']]
print(productlist[0])
print(productlist[1][0])

name=["mango"]
surname=["tree"]
biodata=name+surname
print(biodata)

print(biodata[0][3])
print(biodata[1][3])
print(biodata)

biodata[0]="appple"
print(biodata)

print(biodata*3)

mylist=[12,3,4]
mylist2=[9,6,9]
list = mylist > mylist2
print(list)

no1=[1,2,3]
print(2 in no1)
print(2 not in no1)

numberlist.append(11)
print(numberlist)

numberlist.extend([13,16])
print(numberlist)

numberlist.insert(5,3)
print(numberlist)

numberlist.pop()
print(numberlist)

numberlist.pop(6)
print(numberlist)

numberlist.reverse()
print(numberlist)

print(min(numberlist))

print(max(numberlist))

print(numberlist.count(4))

numberlist.sort()
print(numberlist)

numberlist.clear()
print(numberlist)
