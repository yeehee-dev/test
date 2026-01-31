import re # 정규표현식을 사용하기 위한 모듈

data = """
park 808095-1049118
kim 700905-1059119
"""
result = []
for line in data.split("\n"): #enter를 기준으로 나눔
    word_result = []
    for word in line.split(" "): # 공백을 기준으로 나눔
        if len(word) ==14 and word[:6].isdigit() and word[7:].isdigit(): #나눈 것 중 주민등록번호를 찾아서
            word = word[:6]+"-"+"******" # 변경함
        word_result.append(word) # 주민번호를 리스트에 추가
    result.append(" ".join(word_result)) # d이름과 공백과 주민번호를 합쳐서 리스트에 넣음
print("\n".join(result)) # 엔터를 포함하여 프린트 함