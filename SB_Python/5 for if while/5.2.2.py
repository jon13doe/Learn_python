#--------------------------------------------
a = [(i, j)
     for i in range(3) if i % 3 !=0
     for j in range(4) if j % 2 == 0]
print(a)
#--------------------------------------------
a = [f"{i}*{j}={i * j}"
     for i in range(10)
     for j in range(10)]
print(a)
#--------------------------------------------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [x
     for row in matrix
     for x in row]
print(a)
#--------------------------------------------
m, n = 3, 4
k = [[a for a in range(m)] for b in range(n)]
print(k)
#--------------------------------------------
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = [[a ** 2 for a in r] for r in m]
print(k)
#--------------------------------------------
m = [[1, 2, 3, 11], [4, 5, 6, 12], [7, 8, 9, 13]]
k = [[row[i] for row in m] for i in range(len(m[0]))]
print(k)
#--------------------------------------------

g = [u ** 2 for u in [x + 1 for x in range(5)]]
print(g)