#!/usr/bin/env python3

#line equation: y = -4x + 100, i.e.,
#an example is classified as positive if y + 4x >= 100, negative otherwise

from random import randint;

def get_negative (x):
	y = (-4 * x) + 100;
	y -= randint (1, 5);

	return (y);

def get_positive (x):
	y = (-4 * x) + 100;
	y += randint (1, 5);

	return (y);

if (__name__ == '__main__'):
	data = [];
	numOfExamples = 100;

	while (not len (data) == numOfExamples):
		x = randint (1, 200);
		if (data.count (x) == 0):
			data.append (x);
			if (randint (1, 2) == 1):
				print (str (x) + ' ' + str (get_positive (x)) + ' +');
			else:
				print (str (x) + ' ' + str (get_negative (x)) + ' -');
			 
