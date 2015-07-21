#!/usr/bin/env python3

#linear combination: 7x + 3y = O
#where <x, y> is the vector of inputs, O is the output and <7, 3> is the weight vector (this weight vector is what we intend to find though the Delta Rule using the 100 training examples. The accuracy of our script will depend on how close we get to the actual weights.
from random import randint;

x = 7;
y = 3;
dataX = [];
dataY = [];
numOfExamples = 100;

while (not len (dataX) == numOfExamples):
	xInput = randint (1, 200);
	yInput = randint (1, 200);

	if (dataX.count (xInput) == 0 and dataY.count (yInput) == 0):
		dataX.append (xInput);
		dataY.append (yInput);

		print (xInput, yInput, ( (x * xInput) + (y * yInput)));
