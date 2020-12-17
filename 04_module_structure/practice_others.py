"""
zip(a, b, ...)
두개 이상 시퀀스를 매개변수로 받아
1:1 대응 튜플 시퀀스 생성
"""
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd']

lst = list(zip(a, b))
print(lst)


"""
map(func, list)
list 요소들을 함수 func적용해서 반환
"""
def cube(x):
    return x**3

res = list(map(cube, range(1, 11)))
print(res)


"""
lambda expression
"""
area = lambda x, y : x * y
print(area(5, 4))


import pickle
x = {"name" :"astin", "age" :23}
with open("practice_others.pkl","wb") as f:
    pickle.dump(x, f)

with open("practice_others.pkl","rb") as f:
    read_res = pickle.load(f)

print(read_res)