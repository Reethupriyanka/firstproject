n1 = int(input("Enter the number of rows in a matrix"))
n2 = int(input("Enter the number of colums in a matrix"))
a = []
c=0
for i in range (n1):
	a.append(input())
print("Across words")
for i in a:
	i=i.split('*')
	while '' in i:
		i.remove('')
	for k in i:
		print(k)
c=0
print("down words")
sum = a[0][0]
for j in range(0,n2):
	sum=a[0][j]
	for i in range(1,n1):
		sum=sum+a[i][j]
	sum=sum.split('*')
	while '' in sum:
		sum.remove('')
	for k in sum:
		print(k)
