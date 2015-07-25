#!/usr/bin/env python3
#A Simple Regression problem with 2-dimensional input feature space. A new input vector (Query Point) will be assigned the best possible value using 1-NN and k-NN where k = 5.
#since regression has target functions which are continuous valued, we are going to take an average (mean) of the k nearest neighbor-yielded values when k is not 1.
from random import random, randint;

if (__name__ == '__main__'):
	for i in range (0, 100):
		x = randint (1, 200);
		y = randint (1, 200);

		print (x, y, randint (1, 500) * random ());
