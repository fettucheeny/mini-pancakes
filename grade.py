grade = float(input('enter grade: '))
if grade > 90:
	print('A')
elif grade in range(80, 91):
	print('B')
elif grade in range(70, 80):
	print('C')
elif grade in range(60, 70):
	print('D')
else:
	print('E')