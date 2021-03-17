#format  메서드,
#메서드는 input, print 와 같은 기능을 의미

data = "breakfast is {} and {}". format("spam", "eggs")
#메서드는 어떠한 데이터가 제공하는 기능을 의미
#format을 사용해서 위 데이터의 첫번째 두번째 중괄호에 format의 데이터를 추가하고 마지막으로 data라는 변수에 저장

print(data)

print("My name is {}".format("fames"))
print("My name is {0} and{1}".format("james", 25))
print("My name is {1} and{0}".format("james", 25))

#컴퓨터는 0부터 샌다
#f-string
# f-string은 파이썬 3.6 이후로 나온 새로운 기술
#format 메서드와 비슷하지만
#format 메서드 보다 코드 가독성을 더 높일 수 있음

who = "you"
how = "happy"
print(f"{who} make me {how}")

age = 25
print(f"내년엔 {age+1}살이 됩니다.")