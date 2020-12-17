import cProfile
"""
cProfile
- 호출 시간 세부 사항 분석
- 병목 현상 찾느데 이용
"""
import time


def sleep():
    time.sleep(5)

def hello_world():
    print("Hello world")

def main():
    sleep()
    hello_world()


cProfile.run("main()")