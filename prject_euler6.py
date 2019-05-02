sum = 0
sum1 = 0
for i in range(1,101):
	sum = sum + i * i
	sum1 = sum1 + i
pro = sum1 * sum1
sub = pro - sum
print(sub) 
