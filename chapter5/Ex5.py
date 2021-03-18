'''
문자열 슬라이싱
변수명[시작번호(이상):끝번호(미만)] <=문자열번호<끝번호
요소들을 묶어서 표현하고싶을때

'''

text = "Pythen is easy"

#Pythen
print(text[:6])
#시작번호를 생략하면 처음부터 6까지

#is
print(text[7:9])
#위와같이 처음과 끝의 인덱스를 정할 수 도 있음

#easy
print(text[10:])
#끝번호를 생략하면 10부터 끝까지

text1 = "Life is too shotr, You need Pytheon"

print(text1[5:7])

print(text1[8:11])

print(text1[19:])
#19번째부터 끝까지
print(text1[:19])
#처음부터 19번째까지
print(text1[:])
#처음부터 끝까지

#인덱스 번호 하나를 지정해서 접근할 때는 인덱스 범위를 벗어나면 안된다.

