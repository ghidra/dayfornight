lines = [line.rstrip('\n') for line in open('rain.txt')]
counter =0
s=""
for l in lines:
	n = []
	for t in l.split():
	    try:
	        n.append(float(t))
	    except ValueError:
	        pass
	if counter == 0:
		s+=str(n[len(n)-1])+"  "
	if counter == 1:
		s+=str(n[0])+":"+str(n[1])+"\n"
	if counter == 2:
		print s
		s=""
	counter=(counter+1)%3