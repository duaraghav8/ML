#!/usr/bin/env python3
from random import *;

#generates 500 Positive examples which do not exist in the training set
if (__name__ == '__main__'):
	examples = open ('examples', 'r').readlines ();
	testSet = [];
	concept = {
                'a1' : ',1,3,5,6,7,4,10,11,14,19,22,25,16,15,12,23,',
                'a2' : ',1,2,4,5,8,9,10,11,12,13,14,15,16,18,19,21,22,23,24,25,',
                'a3' : ',1,2,3,4,5,6,7,9,10,11,13,14,15,16,17,19,20,21,24,22,23,'
        };

	a1 = concept ['a1'].split (',') [1 : -1];
	a2 = concept ['a2'].split (',') [1 : -1];
	a3 = concept ['a3'].split (',') [1 : -1];

	while (not len (testSet) == 500):
		attributes = choice (a1) + ' ' + choice (a2) +  ' ' + choice (a3);
		noExist = True;
		for x in examples:
			if (x == attributes):
				noExist = False;
				break;

		if (noExist):
			testSet.append (attributes);
			print (attributes);
