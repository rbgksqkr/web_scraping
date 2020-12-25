# regular expression : 정규 표현식. 복잡한 표현들을 간단한 기호로 정의.

import re

# 1. re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")  : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 게 있는지 확인
# 4. list = p.findall("care cafe case cave") # 일치하는 모든 것을 리스트 형태로 변환

# . : 하나의 문자를 의미   ex)ca.e => care, case, cave
# ^ : 문자열의 시작       ex)^de => desk, destination
# $ : 문자열의 끝         ex)se$ => case, base

p = re.compile("ca.e")

def print_match(m):
    if m:
        print("m.group() :", m.group()) # 일치하는 문자열 반환
        print("m.string :", m.string) # 입력받은 문자열
        print("m.start() :", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() :", m.end()) # 일치하는 문자열의 끝 index
        print("m.span() :", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("lesscare")
# print_match(m)

# m = p.search("good care")
# print_match(m)

list = p.findall("care cafe case cave")
print(list)
