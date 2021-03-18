'''
자료형 - 튜플
숫자 문자열 리스트와 같은 데이터의  한 종류
변수명 =(요소1,요소2,요소3,...)
튜플 내 요소의 순서가 있고 데이터의 중복을 허용
리스트와 비슷하지만 가장 다른점은 튜플은 요소들의 값을 변경 할 수 없다
'''

emptyTuple = ()

numberTuple = (1,2,3)

floatNumberTuple = (3.21,23.34,23.1)

duplicateNumber = (1, 1, 1)

stringTuple = ("무한","무야호")

variousTuple = (1,"무야호는",2,"신나다는거죠")

complexLTuple = ((1,2),3,("파","이","썬"))

#튜플은 리스트처럼 인덱스데이터를 수정할 수 없다
#수정하면 안되는 공통되는 데이터를 저장할때 튜플을 사용한다
#기준이되는 값을 사용할때 튜플을 사용함

#튜플도 덧셈이 가능함
oddTuple = (1,2,3,4,5)
evenTuple = 6,7,8,9,10
fullTuple = oddTuple+evenTuple
print(fullTuple)
#튜플은 소괄호 없이 표현해도 문제없이 출력됨

#튜플도 곱셈이 가능함
multiTuple = (1,)
print(multiTuple *5)
#요소가 하나인 튜플을 만들떼 (1)이런식으로 사용을하면 컴퓨터가 산술연산자로 오해하기때문에(1,)로 써준다

dashTuple = ("=",)*3
asteriskTuple = ("*",)*3
fullTuple1 = dashTuple + asteriskTuple
print(fullTuple1)

#튜플 인덱싱
#마찬가지로 음수 인덱스 번호도 사용가능함

numberTuple1 = (15,23,53,45)
print(numberTuple1[0])
print(numberTuple1[1])
print(numberTuple1[2])
print(numberTuple1[3])

#튜플 슬라이싱
#변수명[시작번호:끝번호]

numberTuple2 = (15,23,53,45)
print(numberTuple2[1:3])
print(numberTuple2[:3])
print(numberTuple2[1:])
print(numberTuple2[:])
#수정이 안되는데 슬라이싱이 되는 이유는 기존에 있는 인덱스들은 놔둔후 요소가 복사되어 새로운 공간에 슬라이싱이 되는원리

numberTuple3 = (15,23,53,45)

numberTuple3[0] = numberTuple3[0]*2

#이렇게 기존인덱스에 적용된 튜플은 수정되지 않는다
