#!/usr/bin/env python3
#A Simple Classification problem with 2-dimensional input feature space. A new input vector (Query Point) will be classified as positive or negative using 1-NN and k-NN where k = 5.
#since classification has target functions which are discrete valued, we are going to take a vote of which class amongst the nearest neighbors has the highest frequency of occurence
from random import randint;

if (__name__ == '__main__'):
	for i in range (0, 100):
		x = randint (1, 200);
		y = randint (1, 200);

		print (x, y, randint (0, 1));	#1 = positive classification, #0 = negative
