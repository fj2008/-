#미세먼지 농도5이상이면 마스크를 쓰고 돈이 10000원 이상있으면 택시를 타라
'''
print("미세먼지 농도 :", end="" )

fineDust = int(input())

if fineDust >= 5:
    print("마스크를 쓰고 나간다")

    print("현금 : ", end= "")
    money = int(input())
    if money >= 10000:
        print("돈이 최고 ㅎㅎ")
'''

print("중간고사 성적 :", end="")

jonggan = int (input())

print("레포트 성적 :", end="")

lefort = int(input())

if jonggan >= 50 :
    if jonggan >=5 :
        print("PerFect Pass")

if jonggan <= 50 :
    if jonggan <=5 :
        print("Pass")

if jonggan < 50 :
    if jonggan >=5 :
        print("Fail")

if jonggan < 50 :
    if jonggan <5 :
        print("Perfect Fail")
