# def culFunc(fir, sec):
# 	a = fir + sec
# 	b = fir - sec
# 	c = fir * sec
# 	d = fir / sec

# 	return {
# 	print("덧셈:{0}, 뺄셈{1}, 곱셈{2}, 나눗셈{3}"
# 		.format(a,b,c,d))
# 	}

# print(culFunc(10, 20))
# print(culFunc(40, 8))

# ---------------------------------------------------

def score(*args):
	a = min(args)
	b = max(args)

	c_value = 0
	for num in args:
		c_value += num
	
	c = float(c_value/4)

	return {
	print("낮은 점수: {0}, 높은 점수: {1}, 평균 점수: {2}"
		.format(a,b,c))
	}
	
print(score(76,82,89,84))

# ---------------------------------------------------

# import math

# def is_palindrome(word):
# 	word_li = list(word)

# 	for i in range(math.floor(len(word_li)/2)):

# 		if word_li[i] is not word_li[-i-1]:
# 			return False

# 	return True


# print(is_palindrome("hello"))
# print(is_palindrome("level"))

# ---------------------------------------------------

# def fibonacci(v1, v2):
# 	a = v1 + v2

# 	print(v1, v2, end=' ')
# 	b = a + v2
# 	return fibonacci(v2, b)


# print(fibonacci(0, 1))


def fibo(n):
	if n in (0,1): 
		return n
	else: 
		return fibo(n-1) + fibo(n-2)

print(fibo(10))
