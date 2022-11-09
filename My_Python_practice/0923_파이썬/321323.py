# pi = 3.141592
# print(round(pi, 2))

print("본 계산기는 Micro Mini Nasdaq 선물 옵션 레버리지를 SQQQ와 비교하여 계산합니다.")
nasdaqNow = float(input("나스닥의 현재 가를 알려주세요: "))
targetPrice = float(input("포지션 목표 가격을 알려주세요: "))
 
sqqqPercent = (nasdaqNow - targetPrice) / nasdaqNow * 100 * 3
sqqqPercent_round = round(sqqqPercent, 2)

print(sqqqPercent_round)