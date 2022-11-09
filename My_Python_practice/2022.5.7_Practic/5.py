foods = {
    '떡볶이' : "오뎅",
    '짜장면' : "단무지",
    '라면' : "김치",
    '피자' : "피클",
    '맥주' : "땅콩",
    '치킨' : "치킨무",
    '삼겹살' : "상추",
    
}

while (True):
    
    print(str(list(foods.keys())))
    myFood = input("당신이 좋아하는 음식은? : ")
    
    if (myFood in foods):
        print("")
        print("=> {}의 궁합 음식은 '{}'입니다.".format(myFood, foods.get(myFood)))
        print("")
        
    elif (myFood == "끝"):
        print("이용해주셔서 감사힙니다!")
        break 
    
    else:
        print("그런 음식은 없습니다. 다시 확인해보세요.")
