def is_prime(num):
	count = 0
	if(num % i == 0 for  i in range(1,num)):
		count += 1
	if(count) == 2:return True
	else : return False
def nth_prime(n):
	count = 0
	for i in range(10000000):
		if is_prime(i):
			count += 1
		if(count == n):
			return(i)
			break
print(nth_prime(600))
