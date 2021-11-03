from itertools import product

with open('./files/euler18.def', 'r') as f:
	data = f.readlines()

data = [(x.rstrip()).split(' ') for x in data]
print(data)

p = product(range(2), repeat=len(data)-1)
totals = []
for elem in p:
	s, pos = 75, 0
	
	for cont, line in enumerate(data[1:]):
		
		pos += elem[cont]
		s += int(line[pos])

	totals.append((elem,s))

max_path = max(totals, key=lambda x: x[1])[1]
print(max_path)

