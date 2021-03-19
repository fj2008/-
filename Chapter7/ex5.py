#조건문 - 멤버 연산자
'''
pocket = ['paper','cellphone','money']
money = 'money' in pocket
card = True
if money:
    print("택시를 타라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("그것도 없음 ㅅㄱ")
        '''
'''
조건문 if elif else
if 조건 1:
    코드1
    코드2
    ,,,
elif 조건2:
    코드1
    코드2
    ...
elif 조건3;
    코드1
    코드2
    ...
else 조건4:
    코드1
    코드2
    ,,,
    
elif는 하나의 상황에대한 조건을 더 부여하는것 
여러상황중에서 한상황을 선택해서 코드를 실행해야할때 if elif else를 실행한다

'''
'''
pocket = ['paper','cellphone']

card = True

money = 'money' in pocket
if money:
    print("택시를 타라")
elif card :
    print("택시를 타라")
else:
    print("돈없음 ㅅㄱ")
    '''
'''
1.콜라
2.사이다
3.환타
'''

print("버튼 누르샘",end="")
button = int(input())


if button == 1 :
    print("콜라를 내보냄")

elif button == 2 :
    print("사이다를 내보냄")

elif button == 3 :
    print("환타를 내보냄")

else :
    print("제공하지 않는 메뉴입니다")


x=1
y=2
if x>y :
    print("x가큽니다")
elif x < y :
    print("x가 작습니다")
elif x==y:
    print("둘다 같음")

    #이렇게하면 if문만 쓰는거랑 뭐가다르지?
'''
연산횟수의 차이가 있다
if문만 사용하면 컴퓨터는 if가 참인지 거짓인지 계속 판별하기위해
계산을 계속 하지만
elif를 사용하면 원하는 조건이 나오면 프로그램이 끝나게됨

결론은
최적화를 위해서임
'''
x=1
y=2
if x>y :
    print("x가큽니다")
if x < y :
    print("x가 작습니다")
if x==y:
    print("둘다 같음")

'''

'''




