def tribonacci(sigma, n):
	p = []
	if n == 0:
		return ([])
	elif n == 1:
		p.append(sigma[0])
	elif n == 2:
		p.append(sigma[0])
		p.append(sigma[1])
	else:
		p.append(sigma[0])
		p.append(sigma[1])
		p.append(sigma[2])
		for i in range (0, n):
			if i == n - 3:
				break
			else:
				d = p[i] + p[i + 1] + p[i + 2]
				p.append(d)
	return (p)