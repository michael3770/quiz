def threeDoorA(trial):                    #主持人事先知道的情况
	import random
	hit = 0
	doors = ['s','s','c']                   #1，2号门是羊，3号门是车
	for i in range(trial):                                 
		host = [0,1]                          #主持人只会选羊            
		tester = [0,1,2]
		pick = random.choice(tester)          #随机选一个
		if pick in host:                      #如果选到的是羊
			host.remove(pick)                   #主持人就开另外一只羊的门
			tester.remove(host[0])              
			tester.remove(pick)                 #选手换门
		else:                                 #如果选的是车
			hostChoice = random.choice(host)    #主持人随便开一只羊的门
			tester.remove(hostChoice)
			tester.remove(pick)                 #选手换门
		if doors[tester[0]] == 'c':            
			hit += 1
	return hit


def threeDoorB(trial):
	import random 
	doors = ['s','s','c']
	hit = 0
	for i in range(trial):
		choose = [0,1,2]                      #主持人和选手都不知道
		pick = random.choice(choose)
		choose.remove(pick)                   #选手选过的门主持人不能选
		host = random.choice(choose)
		if host == 2:                         #如果主持人选到了车，失败，把此次试验从总数中去掉
			trial -= 1
			continue
		else:
			choose.remove(host)                 #如果主持人开了羊门，选手换门
		if doors[choose[0]] == 'c':
			hit += 1
	return trial,hit

