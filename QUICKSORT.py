from random import randint

def quicksort(a):
	if len(a) <= 1:
		return a
	smaller, equal, larger = [], [], []
	pivot = a[randint(0, len(a) - 1)]

	for x in a:
		if x < pivot:
			smaller.append(x)
		elif x == pivot:
			equal.append(x)
		else:
			larger.append(x)

	return quicksort(smaller) + equal + quicksort(larger)

num = list()

for i in range(20000):
	num.append(randint(0, 1000))

print(quicksort(num))