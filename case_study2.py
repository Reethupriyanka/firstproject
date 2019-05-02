games=int(input())
li=[]
for i in range(8):
	li.append(input())
player=input()
comand=input()
for i in range(games):
	for j in li:
		if(j=='W' and player=='W'):
			li.index(j)

for i in li:
	print(i)
