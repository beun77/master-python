f = open("gen1551.csv",'r')
f = f.read()
f = f.split('\n')
for l in f :
	print(l)
