# s = '51900;83000;158000;367500;250000;59200;128500;1304000'

# ss = s.split(';')

# for i in ss[::-1]:
# 	print(i, end="\n")


# a, b = map(str, input().split())
# a, b = list(a), list(b)
# A_, B_ = "", ""

# for i in a:
#     A_ = i + A_
# for j in b:
#     B_ = j + B_

# print(A_ if A_>B_ else B_)


S = input().upper()
print(S)
S_set = list(set(S))
print(S_set)
cnt = []
for i in S_set:
    cnt.append(S.count(i))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(S_set[cnt.index(max(cnt))])