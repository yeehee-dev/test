import re # 정규표현식을 사용하기 위한 모듈

data = """
park 808095-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-******",data))