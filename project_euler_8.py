#!/usr/bin/env python3

def do_product(i, data):
	p = 1
	for x in range(0, 13):
		p = p*int(data[i+x])

	return p

def main():

	with open('./1000_digit_num.txt', 'r') as f:
		data = f.read()

	data = data.replace('\n','')
	length = len(data)
	product = []
	for i in range(length - 12):
		product.append(do_product(i, data))

	print(max(product))

if __name__ == '__main__':
	main()
