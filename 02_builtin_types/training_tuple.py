"""
tuple
불변 시퀀스 타입
"""
t1 = 1234, "hello"
print(t1[0])
t2 = t1, (1, 2, 3, 4, 5) #nested tuple
print(t2)

empty = ()
t1 = "hello"
print(len(empty))
print(len(t1))

t2=("hello")
print(t2)

"""
tuple.count(x)

x 갯수 반환
"""
t= 1, 5, 7, 8, 9, 1, 4
print(t.count(1))

"""
tuple.index(x)

x 위치 반환
"""
print(t.index(1))




""""
tuple unpacking

iterable 객체에 시퀀스 언패킹 연산자 *를 붙이면 *가 붙은 변수에 나머지 값들이 할당됨
"""
print("### tuple unpacking ###")
x, *y = (1, 2, 3, 4)
print(x)
print(y)

*x, y = (1, 2, 3, 4)
print(x)
print(y)