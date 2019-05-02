n = 600851475143
li=[]
li2=[]
count=0
for i in range(1,n):
	count = 0
	for j in range(1,i+1):
		if(i%j == 0):
			count = count+1
	if count==2:
		li.append(i)
		
for i in li:
	if(n%i==0):
		li2.append(i)
print(max(li2))
