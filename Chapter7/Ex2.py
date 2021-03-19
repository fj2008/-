'''
중첩 if문

if조건 1 :
    코드1
    코드2

    if조건 2:
        코드 2-1
        코드 2-2
        .,,
#if조건 2 가 실행되려면 조건1도 성립되고 2도 성립되면 실행됨
    if조건3 :
        코드 3-1
        코드3-2
        ...
#if조건 3 가 실행되려면 조건1.2도 성립되고 3도 성립되면 실행됨
'''
# 성적 : 0~100

score = 50

#과제 : 0 ~ 10
report = 10

#성적이 80점 이상이면서 과제 점수가 10점이면 A+
#성적이 80점 이상이면서 과제 점수가 10점이 아니면 A
#중첩문은 두가지 조건을 다 만족해야 실행됨
'''
if score >= 80:
    if report == 10:
        print("A+")
    if report != 10:
        print("A")
'''
'''
if score >= 80  and report == 10:
        print("A+")

if score >= 80 and report == 10:
        print("A+")
'''
#이렇게 물리연산자를 사용해서 하나로 묶어서 사용할 수있음
#근데 이렇게하면 코드가 복잡해 지기때문에 적당히 연관된 자료들끼리 묶어야함


