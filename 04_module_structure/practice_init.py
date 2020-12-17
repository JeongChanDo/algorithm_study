"""
### __init__.py ###

패키지 : 모듈 + __init__.py가 있는 디렉터리

import 패키지명.모듈명 시

패키지명.py가 아닌 패키지 패키지명에 있는 모듈에 가져오기 위함.

__init__.py에서는 패키지 초기화 코드나 __all__ = ["file1", "file2", ...]변수를 정의

from string import * 시 __init__.py에서 정의한 __all__ 파일들을 읽어들임

"""

from string import string as strs
a = "hello world!"
strs.print_str(a)