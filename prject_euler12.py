sum=0
count=0
for i in range(1,12376):
	count=0
	sum=sum+i
	for j in range(1,sum+1):
		if (sum%j==0):
			count=count+1
if(count>500):
	print(sum)
