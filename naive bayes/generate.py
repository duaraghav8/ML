#!/usr/bin/env python3
from random import *;

if (__name__ == '__main__'):
	concept = {
		'a1' : ',1,3,5,6,7,4,10,11,14,19,22,25,16,15,12,23,',
		'a2' : ',1,2,4,5,8,9,10,11,12,13,14,15,16,18,19,21,22,23,24,25,',
		'a3' : ',1,2,3,4,5,6,7,9,10,11,13,14,15,16,17,19,20,21,24,22,23,'
	};
	attrClass = [];
	attrList = [];
	positiveCount = 0;

	while (not len (attrList) == 10000):
		attributes = str (randint (1, 25)) + ' ' + str (randint (1, 25)) + ' ' + str (randint (1, 25));
		if (attrList.count (attributes) == 0):
			attrList.append (attributes);
			terms = attributes.split ();

			if (not (concept ['a1'].find (',' + terms [0] + ',') == -1) and not (concept ['a2'].find (',' + terms [1] + ',') == -1) and not (concept ['a3'].find (',' + terms [2] + ',') == -1)):
				attrClass.append ('+');
			else:
				attrClass.append ('-');

	for i in range (0, len (attrList)):
		print (attrList [i], attrClass [i]);
