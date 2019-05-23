print('1. PHP to USD')
print('2. USD to PHP')
choice = int(input('Enter number of choice: '))
while choice > 2:
	print('pick a number from 1 or 2 only')
	choice = int(input('Enter number of choice: '))
else:	
	rate = float(input('enter conversion rate in peso: '))
	amount = float(input('enter amount to be converted: '))
	if choice == 1:
		result = amount/rate
		print(result,'USD')
	elif choice == 2:
		result = amount*rate
		print(result,'PHP')