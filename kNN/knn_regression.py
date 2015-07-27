#!/usr/bin/env python3
#A more general form of the 1NN: kNN
from random import randint;

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
	neighbours = 5;
	nearest = [];
	mean = 0;

	print ("Running k-NN Algorithm for Query Point: ", queryPoint, "with k = ", neighbours);
	for line in lines:
		example = [int (i) for i in line.split ()];
		examples.append (example);
	
	for x in examples:
		distances.append (euclid ( (x [0], x [1]), queryPoint));

	for i in range (0, neighbours):
		pos = distances.index (min (distances));
		nearest.append (examples [pos]);
		mean += examples [pos] [2];

		examples.remove (examples [pos]);
		distances.remove (distances [pos]);

	mean /= neighbours;

#in case you wish to see which are the nearest neighbours
#	rint (nearest);

	print ( "Query point output: ", mean);
