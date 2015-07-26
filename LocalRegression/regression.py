#!/usr/bin/env python3
from random import randint, random;

def train (xWeight, yWeight, examples, learnRate):
	errorSumX = 0;
	errorSumY = 0;
	stop = False;

	for example in examples:
		output = (xWeight * example [0]) + (yWeight * example [1]);
		errorSumX += ( (example [2] - output) * example [0]);
		errorSumY += ( (example [2] - output) * example [1]);

	delX = learnRate * errorSumX;
	delY = learnRate * errorSumY;

	xWeight += delX;
	yWeight += delY;

#	print (xWeight, yWeight);
	if (delX <= 0.00001 and delY <= 0.00001):
		stop = True;

	return ( (xWeight, yWeight, stop) );

def gradientDescent (nearest, queryPoint):
	xWeight = 0.5;
	yWeight = 0.5;
	learnRate = 0.00000000001;
	stop = False;

	while (not stop):
		update = train (xWeight, yWeight, nearest, learnRate);
		xWeight = update [0];
		yWeight = update [1];
		stop = update [2];
	
	return ( (xWeight * queryPoint [0]) + (yWeight * queryPoint [1]) );

def euclid (dataPoint, queryPoint):
	x = pow (dataPoint [0] - queryPoint [0], 2);
	y = pow (dataPoint [1] - queryPoint [1], 2);

	out = pow (x + y, 1 / 2);
	return (out);

if (__name__ == '__main__'):
	lines = open ('examples', 'r').readlines ();
	examples = [];
	distances = [];
	queryPoint = (randint (1, 200), randint (1, 200));
	neighbours = 10;
	nearest = [];
	mean = 0;

	print ("Running Locally Weighted regression for Query Point: ", queryPoint, ", taking nearest ", neighbours, " neighbours.\n\n");
	for line in lines:
		example = [float (i) for i in line.split ()];
		examples.append (example);
	
	for x in examples:
		distances.append (euclid ( (x [0], x [1]), queryPoint));

	for i in range (0, neighbours):
		pos = distances.index (min (distances));
		nearest.append (examples [pos]);
		mean += examples [pos] [2];

		examples.remove (examples [pos]);
		distances.remove (distances [pos]);

	output = gradientDescent (nearest, queryPoint);
	mean /= neighbours;

	print ("Average (mean) output:", mean);
	print ("Gradient Descent output: ", output);
