#!/usr/bin/env python3
#
#
#UNDER CONSTRUCTION#
#
#
#
from random import *;

if (__name__ == '__main__'):
	examples = open ('examples', 'r').readlines ();
	query = '17 12 22'.split ();		#the classification should be negative (-)

	classifications = [i [-2] for i in examples];
	pPositive = classifications.count ('+') / len (classifications);	#probability that the new query will be classified as Positive
	pNegative = classifications.count ('-') / len (classifications);	#same as above, for negative
	pClassPositive = 0;
	pClassNegative = 0;
	numOfAP = 0;
	numOfBP = 0;
	numOfCP = 0;
	numOfAN = 0;
	numOfBN = 0;
	numOfCN = 0;

	for i in range (0, len (examples)):
		x = examples [i].split ();
		if (x [3] == '+'):
			for q in query:
				if (not x [0].find (q) == -1):
					numOfAP += 1;
				if (not x [1].find (q) == -1):
	                                numOfBP += 1;
				if (not x [2].find (q) == -1):
	                                numOfCP += 1;
		else:
			for q in query:
                                if (not x [0].find (q) == -1):
                                        numOfAN += 1;
                                if (not x [1].find (q) == -1):
                                        numOfBN += 1;
                                if (not x [2].find (q) == -1):
                                        numOfCN += 1;

	numOfAP /= len (examples);
	numOfBP /= len (examples);
	numOfCP /= len (examples);
	numOfAN /= len (examples);
	numOfBN /= len (examples);
	numOfCN /= len (examples);

	print ( (numOfAP * numOfBP * numOfCP) * pClassPositive);
	print ( (numOfAN * numOfBN * numOfCN) * pClassNegative);
