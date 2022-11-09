student1 = {                    # 학생 정보
    '학번' : 1000,
    '이름' : "홍길동",
    '학과' : "파이썬",
    '학번' : 2000
    
}

print(type(student1))           # type 확인
print("")
print(student1)
print("")
print(student1['학번'])         # 키 값으로 value 추출
print(student1['이름'])
print(student1['학과'])
print("")
print(str(student1['학과']) + "학과 " + str(student1['학번']) + "학번 " + str(student1['이름']) + " 입니다")    # 완벽한 결과
print("")
print(student1.get('이름'))
print("")
print(student1.keys())
print(student1.values())
print(student1.items())