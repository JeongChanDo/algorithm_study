"""
모듈의 디폴트 값으로 가변 변수 사용해선 안됨
"""

#bad case
def append(number, number_list=[]):
    number_list.append(number)
    return number_list

a = append(5)
print(a)

b = append(7)
print(b)

c = append(2)
print(c)

#good case
def append(number, number_list=None):
    if number_list == None:
        number_list = []
    number_list.append(number)
    return number_list

a = append(5)
print(a)
b = append(7)
print(b)
c = append(2)
print(c)