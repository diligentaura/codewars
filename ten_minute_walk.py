def is_valid_walk(walk):
	a = (walk).count('n')
	b = (walk).count('e')
	c = (walk).count('s')
	d = (walk).count('w')
	z = a+b+c+d
	if z == 10:
		if a == c and b == d:
			return True
		else:
			return False
	else:
		return False