get = 1
while(get > 0):
    c = 0       
    l1=[]
    for p in range(5):
        if(get==0):break
        l=[x for x in input()]
        l1.append(l)
        for i in l:
            if(i=='Z'):
                get=0
                c=1
    if(c == 0):
        print('enter direction')
        l2=[x for x in input()]
        for i in range(5):
            for j in range(5):
                for k in l2:
                    if c != 1:
                        if(l1[i][j] == ' '):
                            if(k == 'A'):
                                l1[i-1][j],l1[i][j] = l1[i][j],l1[i-1][j]
                                i,j=i-1,j
                            if(k == 'L'):
                                l1[i][j-1],l1[i][j] = l1[i][j],l1[i][j-1]
                                i,j=i,j-1
                            if(i >= 5 or j >= 5 or i < 0 or j < 0):
                                print("The puzzle has no final configuration")
                                c = 1
                            if(k == 'R'):
                                l1[i][j+1],l1[i][j] = l1[i][j],l1[i][j+1]
                                i,j=i,j+1
                            if(k == 'B'):
                                l1[i+1][j],l1[i][j] = l1[i][j],l1[i+1][j]
                                i,j=i+1,j
                            if(k == '0'):
                                print("puzzle#",get)
                                for i in range(5):
                                    for j in range(5):
                                        print(l1[i][j], end=' ')
                                    print()
                                    c = 1
                                get=get+1
   


   
