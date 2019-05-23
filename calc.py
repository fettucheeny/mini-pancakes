print('1. add')
print('2. subtract')
print('3. multiply')
print('4. divide')
choice = int(input('Enter number of choice: '))
while choice > 4:
	print('pick a number from 1 to 4 only')
	choice = int(input('Enter number of choice: '))
else:	
	x = float(input('enter first number: '))
	y = float(input('enter second number: '))
	if choice == 1:
		result = x+y
	elif choice == 2:
		result = x-y
	elif choice == 3:
		result = x*y
	elif choice == 4:
		result = x/y
	print('Result = ', result)
	
