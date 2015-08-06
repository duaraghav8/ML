#!/usr/bin/env python3
from random import randint;

if (__name__ == '__main__'):
	examples = [];
	outputs = [];

	while (not len (examples) == 16):
		newExample = [randint (0, 1), randint (0, 1), randint (0, 1), randint (0, 1)];
		if (examples.count (newExample) == 0):
			examples.append (newExample);
			output = newExample [0] ^ newExample [1] ^ newExample [2] ^ newExample [3];
			outputs.append (output);

			newExampleString = '';
			for i in newExample:
				newExampleString += str (i) + ' ';

			print (newExampleString + str (output));
