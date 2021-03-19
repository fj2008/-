'''
자료형 -문자열 연산
덧셈
곱셈
이 두연산으로 문자열 생성에 활용할수있음
or
인덱싱
슬라이싱
문자열을 활용할때 사용함


문자포배팅
'''

text1 = "Life is too short ."
text2 = "You need Python"

fullText = text1+text2
#새로운 문자열이 합쳐져서 fulltext에 저장됨
print(fullText)

""" RAM
----------------
주소          값
#1           Life is too short,
#2           You need Python
#3           life is too short, You need Python
덧셈 연산은 이런식을로 새로운 문자열을 생산 하는 것이다
"""
'''
text1_1 = "어제는 비가 내려"
text1_2 = "시원했습니다"
fulltext1 = text1_1 + text1_2
print(fulltext1)

text2_1 = "지금은 문자열에 대해서"
text2_2 = "배우고 있습니다."
fulltext2 = text2_1+text2_2
print(fulltext2)
"--------------------------------------"

'''
text3 ="안녕\n"
text4 = "하세요"

print(text3)
print(text4)
fulltext= text3+text4
print(fulltext)


'''
    RAM
----------------------
#1              안녕\n
#2              하세요
#3              안녕\n하세요
이렇게 출력물과는 다르게 한공간에 저장돼 있는데 \n때문에 줄이 나눠져서 우리눈에 출력된느거임
'''
