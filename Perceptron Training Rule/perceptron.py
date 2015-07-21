#!/usr/bin/env python3
import sys, os;

#Making a few choices is very crucial to your algorithm:
#	1. Threshold
#	2. Learning Rate

def train (x, y, target):
	global threshhold, learn_rate;
	global x_weight, y_weight;
	output = 1 if ( (x_weight * x) + (y_weight * y) >= threshhold) else -1;

	if (not output == target):
		del_x_weight = learn_rate * x * (target - output);
		x_weight += del_x_weight;

		del_y_weight = learn_rate * y * (target - output);
		y_weight += del_y_weight;

if (__name__ == '__main__'):
	t_set = open ('examples', 'r').readlines ();
	learn_rate = 0.0001;
	threshhold = 100;
	x_weight = 0.05;
	y_weight = 0.05;

	while (True):
		for line in t_set:
			line = line.split ();
			train (int (line [0]), int (line [1]), 1 if (not line [2].find ('+') == -1) else -1);
			print (x_weight, y_weight);

#	print (str (x_weight) + "x + " + str (y_weight) + "y");
