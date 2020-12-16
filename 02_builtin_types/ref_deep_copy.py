myList = [1, 2, 3, 4]

newList = myList[:]
newList2 = list(myList)

print(myList)


fruits = {"apple", "banana", "orange"}

eats = fruits.copy()

eats.discard("apple")
print(eats)
print(fruits)


myDict = {"Hello":"World"}
newDict = myDict.copy()

import copy

myObj = "어느 객체"
newObj = copy.copy(myObj)
newObj2 = copy.deepcopy(myObj)