#딕셔너리
'''
사전이란 뜻처럼 사전과도 같은 역할을 한다
변수명 ={key1:value,key2:value, ~~~}
키는 중복될 수 없으며 값은 중복될 수 있다.
키와 값의 쌍이므로 키는 무작위 순서로 들어간다.
키는 꼭 문자열이 아니어도 상관없음

'''
'''
0-이름
1-생년월일
2-주소
3-연락처
'''
#딕셔너리는 키와 값을 사용해서 데이터를 저장할 수 있다
#위처럼 리스트를 사용할땐 정보를 저장하는 습관을 들이자
'''

personinfo = [   
    "이철수",
    "199년3월18일",
    "부산 부산진구 중앙대로 888",
    "010-2394-2344"]
'''
dic = {"apple": "사과",
       "banana": "바나나",
       "pineaplle": "파인애플"}
print(dic)

#딕셔너리도 key에다가 인덱스자리를 차지한다
#리스트랑 다른건 우리가 직접 key라는 인덱스를 부여한다
#그렇기때문에 key의 이름을 중복하면 안되는것
personlnfon = {"name":"이철수",
               "birth":"1990년 3월 18일",
               "address":"부산 부산진구 중앙대로555",
               "tell": "123-123-3424"}
name = personlnfon["name"]
print(name)
print(personlnfon["address"])
#팁! 개발자끼리 카멜표기법을 사용하면좋다 띄어쓰기없이 단어가 바뀔때 첫음절을 대문자로한다
caffe = {"Americano":4600,
         "latte":5100,
         "cappuccino": 5100,
         "oatmealatte":5400,
         "cold Brew" : 5300
         "Espresso" : 4100}

caffe["cappuccino"] = 5300
caffe.update (dolcelatte = 6500)
caffe.update(Americano = 4700)
caffe.update(oatmealatte = 5300)
#pop을 사용해서 키를 삭제할수도 있따
removedItem = caffe.pop("cappuccino")
removedItem = caffe.pop("cold Brew")
removedItem = caffe.pop("Espresso")

#업데이트 메서드를 사용해서 새로운 key 와 값을 저장 할수 있지만 코드가 헷갈려서 잘 안씀
'''
keys라는 메서드 키만 표현
values라는 메서드는 키에 포함된 값을 표현
items라는 메서드 키와 값을 같이 표현
'''
#딕셔너리는 추가할 수 있음
caffe["new latte"] = 4555
caffe.setdefault("new caffe",5555)
keys = caffe.keys()

print(keys)

values = caffe.values()

print(values)

keyvalue = caffe. items()

print(keyvalue)
