#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:40:22 2019

@author: fmalgarini

Solution to Problem 99 of Project Euler
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

"""

import pandas as pd
import math

def main():

	df = pd.read_csv('p099_base_exp.csv', header=None, sep='\n', names=["Base", "Exponent"])

	#Populating the exponent column with the numbers after the comma
	df['Exponent'] = df['Base'].map(lambda x: x.split(',')[1])
	#Populating the base column
	df['Base'] = df['Base'].map(lambda x: x.split(',')[0])
	#Taking the log and comparing
	df['digitnum'] = df.apply(lambda x: float(math.log10(int(x['Base'])))*int(x['Exponent']), axis=1)
	sorted_df = df.sort_values("digitnum", ascending = False, inplace = False)

	index_of_largest = df.index[df['digitnum'] == sorted_df.iloc[0]["digitnum"]]
	print(index_of_largest, df[['Base', 'Exponent']].iloc[index_of_largest])

if __name__ == '__main__':
	main()