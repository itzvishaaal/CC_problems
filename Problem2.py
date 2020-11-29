import math

array1 = list(map(int, input().split()))  

array2 = list(map(int, input().split()))   


bread = array1[0]
vada = array1[1]
samosa = array1[2]
    

vadapav_price = array2[0]  
samosapav_price = array2[1]
profit = 0

if(vadapav_price>samosapav_price):
	if(vada*2<bread):
		profit+=(vadapav_price*vada+samosapav_price*math.floor((bread-vada*2)/2))
	
	else:
		profit+=math.floor(bread/2)*vadapav_price
	

else:
	if(samosa*2<bread):
		profit+=(samosapav_price*samosa+vadapav_price*math.floor((bread-samosa*2)/2))
	
	else:
		profit+=math.floor(bread/2)*samosapav_price


print(profit)
