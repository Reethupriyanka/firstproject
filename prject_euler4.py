sum = 0
for i in range(100,999):
	for j in range(100,999):
		pro = i * j
		m = pro
		while(pro != 0):
			rem = pro % 10
			sum = sum * 10 + rem
			pro = pro / 10
		if(sum == m):
			max = sum
print(max)
