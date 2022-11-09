singer_Input = {}

for key in ['그룹 이름', '구성원 수', '데뷔', '대표곡']:
    print(key,':')
    value = input('값을 입력하세요 : ')
    print("")
    singer_Input[key] = value
    
for i in singer_Input.keys():
    print("{} -> {}".format(i, singer_Input[i]))
