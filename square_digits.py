def square_digits(num):
	a=[]
	b=0
	c=0
	a.append(str(num))
	for i in range (0, len(str(num))):
		a.append(a[0][0+b])
		b=b+1
	a.pop(0)
	for i in range (0, len(a)):
		a[i]=str(int(a[i])**2)
	return int("".join(map(str, a)))