import tp2, sys

f = open('test.txt','w+')

k = 3

print("Processing...")

for n in ['Euclidean','Manhattan','Sup'] :
	for i in range(0,100) :
		f.write("#"+n+str(tp2.main(k,n)))
		sys.stdout.write("Current norm: "+n+" - Number of iterations: "+str(i)+"\r")
		sys.stdout.flush()


print("Comparing...")


#F = f.read().split('#')

f.close()

