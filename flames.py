import math
me1 = input("Your name: ")
crush1 = input("Your crush: ")
me2 = me1.replace(" ", "")
me = me2.replace(".", "")
crush2 = crush1.replace(" ", "")
crush = crush2.replace(".", "")

me_list = list(me)
crush_list = list(crush)

for i in range(len(me_list)):
	for j in range(len(crush_list)):
		if (me_list[i]==crush_list[j]):
			x = me_list[i]
			crush = crush.replace(x, "")
			me = me.replace(x, "")

count = len(list(me)) + len(list(crush))

flames_list = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Soulmates" ]

if count > len(flames_list):
	flames_list = flames_list*(math.ceil(count/6))
	for i in range(len(flames_list)):
		if i==count-1:
			print("Your fate: ", flames_list[i])
else:
	print("Your fate: ", flames_list[count-1])


	

