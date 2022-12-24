A = {1,2,3,4,5,6,}
B = {3,5,7,9,11,}
print (type(A))
print (type(B))
print (A.union(B))
print (A.intersection(B))
A.add(10)
print (A)
B.add(13)
print (B)

C = {2,3,5,6,8,9,}
A.update(C)
print (A)

print (A.difference(B))
print (A.symmetric_difference(B))

A.remove(1)
print (A)
B.pop()
print (B)
print(max(B))
print(min(B))
print(sorted(B))