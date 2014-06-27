def pi(trial):
	import random
	hit = 0
	for i in range(trial):
		a = random.uniform(-1,1)
		b = random.uniform(-1,1)
		if a * a + b * b <= 1:
			hit += 1
	return float(hit)/trial * 4

