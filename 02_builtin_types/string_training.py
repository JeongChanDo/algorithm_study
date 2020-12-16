#유니코드 문자열
# \u0020 : escape
u_str = u"bye \u0020world!"
print(u_str)

"""
A.join(B)

리스트 B 요소들을 A로 연결시킴
"""
fruits = ["apple", "banana", "orange"]
sep_bar = " ".join(fruits)

sep_under_bar = "-".join(fruits)

print(sep_bar)
print(sep_under_bar)


"""
A.format()

문자열 A를 형식 지정자에 맞게 출력
"""

print("name : {who}, age : {age}".format(who="james", age=24))
print("name : {who}, age : {0}".format(21, who="amy"))


"""
A.splitlines()

\n줄바꿈 기준으로 문자열 분리
"""
mans = "jimmy\nsmith"
print(mans.splitlines)


"""
A.split(t, n)
t기준으로 n번 만큼 분리
n미지정시 전체 분리
"""
mans = "jimmy-jone=homes"
print(mans.split("-"))



def erase_space_from_string(string):
    s1 = string.split(" ")
    s2 = "".join(s1)
    return s2

print(erase_space_from_string("hello world!!"))


"""
A.strip(B)
문자열 A 앞뒤 문자열 B제거
"""
print("Hello world!!".strip("!!"))

