#!/usr/bin/env python3
from random import random, randint;

if (__name__ == '__main__'):
	dataX = [];
	dataY = [];
	results = [];

	for i in range (0, 100):
		x = randint (1, 200);
		y = randint (1, 200);
		result = randint (1, 500);

		if ( (dataX.count (x) == 0 or dataY.count (y) == 0) and results.count (result) == 0):
			dataX.append (x);
			dataY.append (y);
			results.append (result);

		print (x, y, result);
