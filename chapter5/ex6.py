'''
자료형(리스트)
숫자,문자열과 같은 데이터의 한 종류
변수명 = [데이터,데이터2,데이터3,....]
리스트 내 데이터들을 요소라고 부름
리스트 내 요소의 순서가 있고 데이터의 중복을 허용
'''
EmpyyList = []
print(EmpyyList)

numberList = [1,2,3]
print(numberList)
floatNumberList = [3.14,0.13,4.25]
print(floatNumberList)
duplicateNumber = [1,1,1]
print(duplicateNumber)
stringList = ["나는","지금"]
print(stringList)
variousList = [1,"파이썬을",2,"공부하고 있다"]
print(variousList)
complexList= [[1,2],3,["파","이","썬"]]
print(complexList)
'''
자료형 - 리스트 연산
덧셈
곱셈
인덱싱
슬라이싱
'''
#리스트 문자열 덧셈
oddList = [1,2,3,4,5]
evenList = [2,5,6,7,4]
fullList= oddList+ evenList
print(fullList)

stringList_1 =["나는","지금"]
stringList_2 =["파이썬을","공부하고 있다"]
fullStringList = stringList_1 + stringList_2
print(fullStringList)

#리스트 곱셈

simpleList = [1] *5
print(simpleList)
#해석하자면 []안에 있는 요소를 *n번 반복시켜라는 뜻

#리스트도 문자열 내 각 자리마다 고유하게 인덱스 번호가 부여된다
numberList = [12,34,56,78]
'''
print(numberList[0])
print(numberList[1])
print(numberList[2])
print(numberList[3])
'''
#양수도 되고
print(numberList[-4])
print(numberList[-3])
print(numberList[-2])
print(numberList[-1])
#음수도 됨

'''
리스트 슬라이싱
변수명[시작번효(이상):끝번호(미만)]
'''

numberList1 = [14,34,45,65]

print(numberList1[1:3])
print(numberList1[:3])
print(numberList1[1:])
print(numberList1[:])

#리스트는 요소를 수정할 수 있다

numberList2 = [12,45,62,34]

numberList2 = numberList2[0]*2
numberList2 = numberList2[1]*2
numberList2 = numberList2[2]*2
numberList2 = numberList2[3]*2



