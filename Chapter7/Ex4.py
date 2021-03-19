'''
조건문 - if else
if 조건 :
    코드1
    코드2
    ,,,
    else :
        코드1
        코드2
이렇게 하면 둘중에 하나만 참이어도 실행이 된다.
else에는 조건이 없어서 else를 만나면 무조건 else코드를 무적권 실행함
'''
'''
print("미세먼지 농도 :", end="")

fineDust = int(input())

if fineDust >= 5:
    print("집에 있는다.")
else:
    print("밖에 나간다.")
#주의할점 else는 조건이 없어서 5이하에 모든수가 적용됨 음수,실수 같은
'''

'''
print("님 돈 얼마있음? :" , end="")

money = int(input())

if money >=10000:
    print("세상은 돈이 곧힘 ㅎ")
else:
    print("돈없으면 버스타야지 ㅋㅋㅋㅋ")
'''
'''
print("수 입력 :", end="")

su = int(input())

if su %2 == 0 :
    print(2*1)
    print(2 * 2)
    print(2 * 3)
    print(2 * 4)
    print(2 * 5)
    print(2 * 6)
    print(2 * 7)
    print(2 * 8)
    print(2 * 9)
else:
    print(3*1)
    print(3 * 2)
    print(3 * 3)
    print(3 * 4)
    print(3 * 5)
    print(3 * 6)
    print(3 * 7)
    print(3 * 8)
    print(3 * 9)

print("1.숫자 쓰샘 :" ,end= "")

su2 = int(input())

print("2.숫자 쓰샘 :" ,end= "")

su3 = int(input())

print("3.숫자 쓰샘 :" ,end= "")

su4 = int(input())

if su2 <su3 <su4:
    print(su4)
else :
    print(su2)
'''
#멤버연산자


