products = ["Sensodyne-100,Close Up-150,Colgate-135",
"Safeguard-80,Protex-50,Kojic-135",
"Surf-280,Ariel-350,Tide-635",
"Clover-60,Piattos-20,Chippy-35",
"Jelly bean-60,Hany-20,Starr-35"]

toothpaste=[] 
bathsoap=[]
detergent=[]
chips=[] 
candies=[]

categories = [toothpaste, bathsoap, detergent, chips, candies]

for x in range(len(products)):
	categories[x].append(products[x])
	#categories[x] = products[x].split(",")
	for i in range(len(categories[x])):
		categories[x][i] = categories[x][i].split(",")
		for j in range(len(categories[x][i])):
			categories[x][i][j] = categories[x][i][j].split("-")


toothpaste2=[] 
bathsoap2=[]
detergent2=[]
chips2=[] 
candies2=[]

categories2 = [toothpaste2, bathsoap2, detergent2, chips2, candies2]

item_price=()

for z in range(len(categories)):
	for a in range(len(categories[z])):
		for b in range(len(categories[z][a])):
			item_price = (int(categories[z][a][b][1]), categories[z][a][b][0])
			categories2[z].append(item_price)

toothpaste2.sort()
bathsoap2.sort()
detergent2.sort()
chips2.sort()
candies2.sort()

cheapitems=[]

cheapitems.append(toothpaste2[0])
cheapitems.append(detergent2[0])
cheapitems.append(bathsoap2[0])
cheapitems.append(candies2[0])
cheapitems.append(chips2[0])
print(cheapitems) 

total = toothpaste2[0][0] + bathsoap2[0][0] + detergent2[0][0] + chips2[0][0] + candies2[0][0]
print(total)
