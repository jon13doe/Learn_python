setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
setC = setA & setB
print(setC)
print(setA.intersection(setB))
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
setC = setA | setB
print(setC)

print(setA.union(setB))


setC = setA - setB
print(setC)
setC = setB - setA
print(setC)

setC = setA ^ setB
print(setC)