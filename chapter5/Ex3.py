'''자료형- 문자열 곱셈
문자열이 가지고 있는 문자열을 n번 출력해주는 방식
파이썬에서만 사용할 수있음
'''
'''
print("=======================")
print("-홈으로")
print("-학원소개")
print("-커리큘럼")
print("-찾아오시는길")
print("-문의사항")
print("=======================")
'''
'''
위와 같이 출력하려면 효율적이지 않음
'''
'''
line = "=" *20
print(line)
print("-홈으로")
print("-학원소개")
print("-커리큘럼")
print("-찾아오시는길")
print("-문의사항")
print(line)'''
'''
파이썬에서는 위와같이 좀더 효율적이게 문자열을 사용할수 있게해줌
'''
la = "<" *5
ra = ">" *5
text = la + "Python Class" + ra
line = "***___" *4
print(text)

print(line)
print("|\t\t\t\t\t\t|")
print("|-홈으로\t\t\t\t\t|")
print("|-집으로 갈레\t\t\t\t|")
print("|-가고싶      갈꺼야\t\t|")
print("|\t\t\t\t\t\t|")
print(line)

