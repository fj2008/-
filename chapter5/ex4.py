'''
인덱스 번호는 한자리 한자리 마다 부여하는것임
그래서 각각에 자리에 번호부여할 수 있음

파이썬에서는 문자열 안에 들어가있는 문자를 문자라 하지않고 '요소'라고 한다

'''
text = "Life is too short, You need Python"


monja1 = text[6]
monja2 = text[13]
monja3 = text[10]
monja4 = text[15]
monja5 = text[16]

print(monja1)
print(monja2)
print(monja3)
print(monja4)
print(monja5)

'''
      RAM
--------------------
#1             "Life is too short, You need Python"
#2             "L"
#3             "i"
#4             "o"

위와같이 #1변수에서의 값을 때오는게 아닌 가리키는 값을 복사를 해서
새로운 공간에 그 값을 표현함


파이썬은 인덱스 번호를 역순으로도 부여 할  수 있음
뒤에서 부터 세도 된다는 말      -n을 붙이면됨

'''
'''
text = "python is easy"
#양수 인덱스 번호와 음수 인덱스 번호를 적절히 상요해서
#아래와 같이 출력하세요
#python
#is
#easy

monja1 = text[0] +text[1] +text[2] +text[3] +text[4] +text[5]
monja2 = text[7] +text[8]

monja3 = text[-4] +text[-3]+ text[-2]+ text[-1]



print(monja1)
print(monja2)
print(monja3)
'''
'''위와 같이 하면 되지만 
존나 불편함
그래서 나온게 슬라이싱임
내일함 ㅅㄱ'''


