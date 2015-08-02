#!/usr/bin/env python3
from random import *;

if (__name__ == '__main__'):
	concept = {
		'a1' : ',1,7,4,10,11,19,22,25,16,15,12,',
		'a2' : '?',
		'a3' : '1,3,5,7,9,11,13,15,17,19,21,24,22'
	};
	attrClass = [];
	attrList = [];

	while (not len (attrList) == 10000):
		attributes = str (randint (1, 25)) + ' ' + str (randint (1, 25)) + ' ' + str (randint (1, 25));
		if (attrList.count (attributes) == 0):
			attrList.append (attributes);
			terms = attributes.split ();

			if (not (concept ['a1'].find (',' + terms [0] + ',') == -1) and not (concept ['a3'].find (',' + terms [2] + ',') == -1)):
				attrClass.append ('+');
			else:
				attrClass.append ('-');

	for i in range (0, len (attrList)):
		print (attrList [i], attrClass [i]);
