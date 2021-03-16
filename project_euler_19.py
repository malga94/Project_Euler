#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:40:22 2019

@author: fmalgarini

Solution 1 to Problem 19 of Project Euler
Text of the problem:

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

counter = 1 #Representing days of the week as counter%7. Year 1901 starts on a Tuesday
num_sundays = 0
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1901, 2001):

	for month in days_in_months:
		
		counter = counter + month

		if ((i%4 == 0 and i%100 != 0) or i%400 == 0) and month == 28:
			counter += 1

		if counter%7 == 6:
			num_sundays += 1
			
print(num_sundays)


