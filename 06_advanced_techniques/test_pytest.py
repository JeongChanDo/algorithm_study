"""
pytest
- test로 시작하는 함수에서 시작
pytest filename
pytest filename --pdb
"""

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 51