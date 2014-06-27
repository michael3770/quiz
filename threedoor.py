def threeDoorA(trial):
	import random
	hit = 0
	doors = ['s','s','c']
	for i in range(trial):
		host = [0,1]
		tester = [0,1,2]
		pick = random.choice(tester)
		if pick in host:
			host.remove(pick)
			tester.remove(host[0])
			tester.remove(pick)
		else:
			hostChoice = random.choice(host)
			tester.remove(hostChoice)
			tester.remove(pick)
		if doors[tester[0]] == 'c':
			hit += 1
	return hit


def threeDoorB(trial):
	import random 
	doors = ['s','s','c']
	hit = 0
	for i in range(trial):
		choose = [0,1,2]
		pick = random.choice(choose)
		choose.remove(pick)
		host = random.choice(choose)
		if host == 2:
			trial -= 1
			continue
		else:
			choose.remove(host)
		if doors[choose[0]] == 'c':
			hit += 1
	return trial,hit

