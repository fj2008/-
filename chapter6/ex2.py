'''
자료형 set
파이썬 2.3부터 추가된 데이터 타입
리스트,.튜플과 마찬가지로 데이터들을 저장할 수 있는 데이터타입
한글 그대로 집합과 관련된 부분을 쉽게 처리하기 위해 만들어진 데이터 타입

집합에 관하여
원소의 순서는 고려사항이 아니다
원소는 중복될 수 없음
set도 이 특징을 그대로 따라감

변수명 = {값1(요소),값2,값3...}
'''
ㅁ
numberSet = {1,2,3}

stringSet = {"파","이","썬"}

numberSet = {1,2,1,3}

stringSet= {"파","이","이","썬"}

print(numberSet)
print(stringSet)

numberset = {1,2,3}
emptySet = {}
#아무정보를 입력하지 않아도 set에 형태는 출력됨
print(numberSet)
print(emptySet)
#공집합을 만들때는 변수명= set(시퀀스객체)

emptySet =set()
numberset = set([1,2, 3])
stringSet =set("파이썬")

print(emptySet)
print(numberset)
print(stringSet)

#set교집합 : & 또는 intersaction 기능 사용

leftSet = set([1,2,3,4,5,6,7,8,9,])
rightSet = set([2,4,6,8,10,12,14,16,18])

print(leftSet&rightSet)
print(leftSet.intersection(rightSet))
#leftSet을 제공하는 intersection을 사용해서 rightSet의 교집합을 구함

#합집합 : |또는 union

print(leftSet | rightSet)
print(leftSet.union(rightSet))

#leftSet에서 제공하는 union이라는 메서드를 사용해서 rightSet에 합집합을 구함

#차집합: -또는 difference기능

print(leftSet - rightSet)
print(leftSet.difference(rightSet))


'''
set을 어디에 쓸까
문자열을 set화 시켜서 사용할 수 있는데 어떠한 자료를
set화 시켜서 어떠한 자료랑 겹치지는 않았는지 등등을 할때 활용할 수 있음'''

#add라는 메서드를 사용해서 새로운 원소를 추가 할 수있다

numberset = {1,2,3}

numberset.add(4)
numberset.add(7)

numberset.remobe(7)
print(numberset)

#리스트, 튜플 : 인덱스를 지정할 수있다
#셋 :삭제할 데이터를 직접! 지정!

leftSet = set("나는 오늘도 파이썬을 공부한다.")
rightSet = set("나는 내일도 파이썬을 공부한다")

print(leftSet & rightSet)
#차집합과 교집합은 어떤 자료가 먼저 오는지가 중요함
print(leftSet | rightSet)
print(leftSet - rightSet)





