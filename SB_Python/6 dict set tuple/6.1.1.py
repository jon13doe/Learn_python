d = {"house": "dom", "car": "mashina",
     "tree": "derevo", "road": "doroga",
     "river": "reka"}
print(*d)
print(d["house"])
a = dict(one=1, two=2, three='3', four='4')
print(a)
lst = [[1, "posredstvenno"], [2, "neudovetworitelno"],
       [3, "udovetworitelno"], [4, "horocho"],
       [5, "otlicho"]]
a = dict(lst)
print(a)
a ={}
print(a)
a = dict()
print(a)
a[True] = 'istina'
a[False] = 'loch'
print(a)
a[False] = 'ololo'
print(a)
a = {True: 1, False: 'loch', 'list': [1, 2, 3], 5: 5}
print(a)
a = dict([[1, 'one'], [2, 'two'], [3, 'three']])
print(a)