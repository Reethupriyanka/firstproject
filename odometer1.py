num=int(input())
if num%10 <= num//10:print("invalid number")
li=[int(x) for x in range(12,90) if x%10 > x//10]
if num in li and num<89:print("next number is",li[index(num)+1], "and previous number is",li[index(num)-1])
elif(num==li[i]):print("next number is",li[0] ,"and previous number is",li[i-1])
