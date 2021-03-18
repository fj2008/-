'''
시퀀스 (문자열,리스트,튜플은 시퀀서의 객채들(어머니격))
문자열,리스트,튜플과 같이 값이 연속적으로 이어진 자료형을 시퀀스 자료형(Sequence Typese)라고함
시퀀스 자료형 공통기능
가장큰 특징은 공통된동작과 기능을 제공
시퀀스 자료형을 갖고 있는 변수를 시퀀스 객체라고함
시퀀스 객체에 들어있는 각 값을 요소 라고 부르는거심
시퀀스 객체(리스트 문자열 튜플 등등)간에는 서로 변환할수 있음
시퀀스 자료형의 덧셈 연산은 같은 자료형 끼리만 할 수 있다(문자열은 문자열끼리만등등등,,,)

'''
'''
simpleString = "문자열"
simpleList = ["무","야","호"]
simpleTuple = ("무","야")

strToList = list(simpleList)
listToTuple = tuple(simpleList)
tupletostr = str(simpleTuple)

print("str -> list", strToList)
print("list -> tuple =" ,listToTuple)
print("tuple -> str", tupletostr)
#len이라는 기능을 이용하면 각 변수에 들어있는 요소의 갯수를 파악할 수 있음
print(len(simpleString))
print(len(simpleList))
print(len(simpleTuple)) 
'''
'''
in 과 not in
위 기능들은 list안에 들어있는 요소인지 아닌지 확인해 주는 기능
in 들어있다
not in 없다
'''
simpleText = "apple, banana, pineapple"

print ("apple" in simpleText)
print ("apsdfe" in simpleText)

print ("apple" not in simpleText)
print ("apple" not in simpleText)

simpelString = '문자열'
simpleList =["무","야","호"]
simpleTuple = ("무","한")

simpelString[0] ="1"
simpleList[0] = 1
simpleTuple[0] =1
#이렇게 입력하면 47번줄에서 막힘
'''
시퀀서에는 크게 두가지 타입의 데이터가 있다
-수정 가능한 데이터타입
읽고 쓸수 있는 데이터 타입
mutable 데이터 타입
리스트,세트,딕셔너리

-수정불가능한 데이터 타입
읽기만 가능한 데이터 타입
immutable 데이터 타입
정수,실수,문자열, 튜플
'''