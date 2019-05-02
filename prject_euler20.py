num=100
pro=1
sum=0
for i in range(1,101):
	pro=pro*i
print(pro)
while(pro!=0):
	rem=pro % 10
	sum=sum+rem
	pro=pro//10
print(sum)
