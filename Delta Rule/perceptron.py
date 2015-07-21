#!/usr/bin/env python3

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

	print (xWeight, yWeight);
	if (delX == 0 and delY == 0):
		stop = True;

	return ( (xWeight, yWeight, stop) );

if (__name__ == '__main__'):
	xWeight = 0.5;
	yWeight = 0.5;
	learnRate = 0.00000000001;
	stop = False;
	lines = open ('examples', 'r').readlines ();
	examples = [];

	for line in lines:
		example = [int (i) for i in line.split ()];
		examples.append (example);

	while (not stop):
		update = train (xWeight, yWeight, examples, learnRate);
		xWeight = update [0];
		yWeight = update [1];
		stop = update [2];

		#break;

	print (xWeight, yWeight);
