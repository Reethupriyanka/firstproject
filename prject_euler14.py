li=[]
for i in range(1,1000000):
	for j in range(2,i+1):
		while(j!=1):
			if(j%2==0):
				j=j/2
			else:
				j=3*j+1
			li.append(j)
print(li)
