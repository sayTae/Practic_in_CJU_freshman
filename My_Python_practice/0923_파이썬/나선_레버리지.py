## 나선 레버리지 계산기
 
## 첫 가격 세팅
 
print("본 계산기는 Micro Mini Nasdaq 선물 옵션 레버리지를 SQQQ와 비교하여 계산합니다.")
nasdaqNow = float(input("나스닥의 현재 가를 알려주세요: "))
targetPrice = float(input("포지션 목표 가격을 알려주세요: "))
 
sqqqPercent = (nasdaqNow - targetPrice) / nasdaqNow * 100 * 3

print("\nSQQQ 기준으로 [%f%] 변동한 수치입니다." % round(sqqqPercent))
 
## 계약의 가치 = 현재 가 * 틱당 가치 / 틱 단위
nasdaqFutures = nasdaqNow * 0.5 / 0.25
yeaSugeum = nasdaqFutures / 3
 
print("\n나스닥 선물을 SQQQ 처럼 매매하려면 예수금은 [$%f] 가 필요합니다." % round(yeaSugeum))
 
variancePoint = (nasdaqNow - targetPrice)
varianceDoller = (nasdaqNow - targetPrice) * 2
 
x = varianceDoller / sqqqPercent
 
 
print("\n계약의 가치는 [$%f] 입니다.\n" % round(nasdaqFutures))
