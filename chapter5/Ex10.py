'''
시퀀스 자료형 range
시퀀스 자료형 중에서 range 자료형은 +연산자로 객체를 연결 할 수없다
range 자료형 - 특정한 패턴으로 연속되는 숫자를 요소로 갖고 있는 시퀀스 자료형
변수명 = range(시작,끝,패턴)
'''

oddRange = range(1,11,1)
evenRange = range(10,0,-1)
#패턴을빼면 자동적으로 1씩증가해서 가는 패턴을 만들어줌

rangeToList1 = list(oddRange)
rangeToList2 = list(evenRange)

print("range -> list = ",rangeToList1)
print("range -> list = ",rangeToList2)
#range는 덧셈이 안됨
#곱셈도 안됨

