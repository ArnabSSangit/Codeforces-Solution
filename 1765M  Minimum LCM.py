def prime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:return n//i
	return 1
for _ in range(int(input())):
	n=int(input())
	p=prime(n)
	print(p,n-p)
