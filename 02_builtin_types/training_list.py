q = [2, 3]
p = [1, q, 4]
print(p)


p[1].append("banana")
print(p)
print(q)

"""
list.insert(index, value)
- insert value into index of list
"""

people = ["jone", "homes"]
people.insert(1, "smith")
print(people)


"""
list.remove(value)
- remove value from list
"""
people.remove("jone")
print(people)


"""
list.pop(index=-1)
- remove and return index value of list 
"""
people = ["jone", "homes", "smith"]
print(people)
print(people.pop(1))
print(people.pop())


"""
del
- delete values of list by indexing
"""
a = [-1, 4, 5, 6, 10]
del a[0]
print(a)

del a[2:3]
print(a)

"""
del variable : delete variable

del a
print(a)
"""


"""
list.index(value)
- find index of value
"""
people = ["jone", "smith", "homes"]
print(people.index("jone"))



"""
list comprehension
- list iterable expression
"""
print("\n### list comprehension ###")
a = [y for y in range(1900, 1940) if y%4 == 0]
print(a)

b = [2**i for i in range(13)]
print(b)

c = [x for x in a if x % 2 ==0]
print(c)

d = [str(round(355/133.0, i)) for i in range(1, 6)]
print(d)

