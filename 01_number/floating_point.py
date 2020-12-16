"""
부동 소수점은 이진수 분수로 표현
2진법으로 구하기 힘든 수가 존재 -> 함부로 사칙연산을 하면 잘못된 결과가 나올 수 있음

"""

print(0.2 * 3 == 0.6)

print(1.2 - 0.2 == 1.0)

print(1.2 - 0.1 == 1.1)

print(0.1 * 0.1 == 0.01)


def eq(x, y, places=7):
    return round(abs(x - y), places) == 0

print("eq test without precision :", ((1.2 -0.1) == 1.1))
print("eq test with precision : ", eq(1.2 - 0.1, 1.1))