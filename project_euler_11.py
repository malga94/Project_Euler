#!/usr/bin/env python3

with open('./exe_11_input.txt', 'r') as f:
	data = f.read()

matrix = []
cont = 0
for line in data.splitlines():
	matrix.append([])
	for elem in line.split(' '):
		matrix[cont].append(int(elem))

	cont += 1

horiz_prod = []
vert_prod = []
diag_prod = []

for line in matrix:
	for i in range(0, len(matrix) - 3):
		horiz_prod.append(line[i]*line[i+1]*line[i+2]*line[i+3])

for j in range(0, len(matrix)):
	for line in range(0, len(matrix) - 3):
		vert_prod.append(matrix[line][j]*matrix[line+1][j]*matrix[line+2][j]*matrix[line+3][j])

for line in range(0, len(matrix) - 3):
	for i in range(0, len(matrix) - 3):
		diag_prod.append(matrix[line][i]*matrix[line+1][i+1]*matrix[line+2][i+2]*matrix[line+3][i+3])

for line in range(0, len(matrix) - 3):
	for i in range(3, len(matrix)):
		diag_prod.append(matrix[line][i]*matrix[line+1][i-1]*matrix[line+2][i-2]*matrix[line+3][i-3])

products = vert_prod + horiz_prod + diag_prod
print(max(products))

