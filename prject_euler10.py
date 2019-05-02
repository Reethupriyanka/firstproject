count = 0
sum = 0
for i in range(2,10):
	for j in range(1,i+1):
		if(i%j==0):
			count = count+1
		if(count==2):
    			sum = sum + i
print(sum)
