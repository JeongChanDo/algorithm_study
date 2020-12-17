"""
직접 실행하는 경우 __name__ = __main__

임포트 하는 경우 __name__ = 자기 모듈 이름
"""

hello = "hello"

def world():
    return "world"

if __name__ == "__main__":
    print("{0} executed directly".format(__name__))
else:
    print("{0} imported".format(__name__))