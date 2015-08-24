#!/usr/bin/env python3
from random import *;

if (__name__ == '__main__'):
	examples = open ('examples', 'r').readlines ();
	queryString = input ("Input a query string (the format is 3 space seperated numbers pertaining to the 3 attributes, each between 0 and 25 inclusive): ");
	query = queryString.split ();

	classifications = [i [-2] for i in examples];
	pPositive = classifications.count ('+') / len (classifications);	#probability that the new query will be classified as Positive
	pNegative = classifications.count ('-') / len (classifications);	#same as above, for negative
	lenP = int (len (classifications) * pPositive);
	lenN = int (len (classifications) * pNegative);

	pClassPositive = 0;
	pClassNegative = 0;
	numOfAP = 0;
	numOfBP = 0;
	numOfCP = 0;
	numOfAN = 0;
	numOfBN = 0;
	numOfCN = 0;
	priorEstimate = 1 / 26;
	equivSample = 0.3;

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
#			lenP += 1;

		else:
			for q in query:
                                if (not x [0].find (q) == -1):
                                        numOfAN += 1;
                                if (not x [1].find (q) == -1):
                                        numOfBN += 1;
                                if (not x [2].find (q) == -1):
                                        numOfCN += 1;
#			lenN += 1;
#			print (numOfAN, numOfBN, numOfCN);

	pClassifyPositive = ( ( (numOfAP + (equivSample * priorEstimate)) / (lenP + equivSample) ) * ( (numOfBP + (equivSample * priorEstimate)) / (lenP + equivSample) ) * ( (numOfCP + (equivSample * priorEstimate)) / (lenP + equivSample)) ) * pPositive;
	pClassifyNegative = ( ( (numOfAN + (equivSample * priorEstimate)) / (lenN + equivSample)) * ( (numOfBN + (equivSample * priorEstimate)) / (lenN + equivSample)) * (numOfCN + (equivSample * priorEstimate)) / (lenN + equivSample) ) * pNegative;

	print ("Query: " + queryString + " is classified as " + ("Negative" if pClassifyNegative > pClassifyPositive else "Positve"));
	print ("Negative probability = ", pClassifyNegative);
	print ("Positive probability = ", pClassifyPositive);
