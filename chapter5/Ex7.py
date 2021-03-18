'''
리스트는 요소를 추가 또는 삭제할 수 있다.
-요소 추가 : append(메서드), insert
-요소 삭제 : pop
객체가 재공하는 기능을 메서드라고 함
'''
#4명의 시험 성적
numberList = [12,34,45,64]

#전학온 학생의 성적
'''
numberList.append(77)
print(numberList)
'''
#insert 메서드를 사용할땐 특정 인덱스에 번호를 지정해서 저장할 수있다

numberList.insert(0, 59)
print(numberList)
#0번인덱스에 끼어들기를 하는거임 이 뒤에 인덱스데이터들은 한칸씩 다 밀림



#pop사용법
#맨 뒤 데이터를 꺼낸다
#삭제한데이터를 알려줌
delete = numberList.pop()
print("삭제한 데이터 = %d "% delete)
print(numberList)
#특적 인덱스에 있는데이터를 꺼내올수도 있음
numberList.pop(0)
print(numberList)
'''
append 메서드 또는 pop메서드를 인덱스 번호없이 상용할 때는 조심할 부분이 없음
(리스트의 맨 뒤에 있는 데이터를 추가하거나 삭제하는 동작)

insert 메서드 또는 pop메서드를 인덱스 번호 있게 사용하러 할 때는 조심해야함
(리스트의 중간 또는 맨 앞에 데이터를 추가하거나 삭제하는 동작)
'''



