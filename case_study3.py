n = int(input())
a=[[0 for x in range(n)] for y in range(n)]
for i in range(n):
	for j in range(n):
		while(1):
			a[i][j]=input()
			if(a[i][j]=='Z'):
				break

	print("enter direction")
	d=input()
	for j in range(n):
		if c!=1:
			if(a[i][j]==' '):
				if (d=='l'):
					a[i][j],a[i][j-1] = a[i][j-1],a[i][j]
				elif (d=='r'):
					a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
				elif i==5 or j==5 or i<0 or j<0:
					print("this has no final configaration ")
				elif (d=='d'):
					a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
				elif (d=='u'):
					a[i][j],a[i-1][j] = a[i-1][j],a[i][j]
for i in range(n):
	for j in range(n):
		print(a[i][j])
	print('\n')
