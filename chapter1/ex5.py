#print("!! 나이를 입력하면 태어난 연도를 알려드립니다 !!")
#print("나이 (만) :" , end="")
#age = int(input())
#year = 2021 - age
#print(age ,"당신의 태어난 연도는",year,"년 입니다.")
#변수타입을 다른 형태의 데이터라도 기본 데이터 타입을 내가 원하는 데이터로 설정할수 있다

# 문자열, 실수 . 논리를 정수화
#var1 = int("26")
#var2 = int(3.14)
#var3 = int(True)
# 문자열, 실수 . 논리를 실수화
#var4 = float("26")
#var5 = float(3.14)
#var6 = float(True)
# 문자열, 실수 . 논리를 정수화
#var7 = str("26")
#var8 = str(3.14)
#var9 = str(True)
print("어제의 기온 :" , end="")
gion = float(input())
print("오늘의 기온 :" , end="")
today =float(input())

seomday = gion - today


print("어제와 오늘의 기온차는 " ,seomday, "입니다.")
