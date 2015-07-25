#!/usr/bin/env python3
from random import randint, random;

def euclid (dataPoint, queryPoint):
	x = pow (dataPoint [0] - queryPoint [0], 2);
	y = pow (dataPoint [1] - queryPoint [1], 2);

	out = pow (x + y, 1 / 2);
	return (out);

if (__name__ == '__main__'):
	lines = open ('examples_regression', 'r').readlines ();
	examples = [];
	distances = [];
	queryPoint = (randint (1, 200), randint (1, 200));

	print ("Running 1-NN Algorithm for Query Point: ", queryPoint);
	for line in lines:
		example = [float (i) for i in line.split ()];
		examples.append (example);
	
	for x in examples:
		distances.append (euclid ( (x [0], x [1]), queryPoint));

	pos = distances.index (min (distances));
	print ( "Closest to point: ", examples [pos] [0], examples [pos] [1], " Result: ", examples [pos] [2] );
