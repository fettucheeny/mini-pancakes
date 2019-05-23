import random
numbers = random.sample(range(99), 20)
print('random numbers ', numbers)
for i in range(len(numbers)):
	if numbers[i]%2>0:
		continue
	else:
		numbers[i] = numbers[i]+1
print('odd numbers ', numbers)