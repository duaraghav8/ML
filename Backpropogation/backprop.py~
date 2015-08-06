#!/usr/bin/env python3
from random import random;
import math;

class Neuron:
	fireWeight = random () % 0.1;
	fireInput = random ();
	weightVector = [];
	inputVector = [];

	def __init__ (self):
		pass;

	def setFireWeight (self, w):
		self.fireWeight = w;

	def setFireInput (self, i):
		self.fireInput = i;

	def feedNextLayer (self, layer):
		for neuron in layer:
			neuron.recvFeed ( (self.fireWeight, self.fireInput) );

	def sigmoid (self, number):
		output = pow (math.e, -number) + 1;
		output = 1 / output;
		return (output);

	def recvFeed (self, firedWeight, firedInput):
		self.weightVector.append (firedWeight);
		self.inputVector.append (firedInput);

	def fireOutput (self):
		output = 0.0;
		for i in range (0, len (weightVector)):
			output += weightVector [i] * inputVector [i];

		return (self.sigmoid (output));

class Network:
	inputs = [];
	outputs = [];
	hiddenLayers = [];

	def __init__ (self, numOfInputs, numOfHiddenLayers, neuronsPerHiddenLayer, numOfOutputs):
		for i in range (0, numOfInputs):
			inputs.append (Neuron ());

		for i in range (0, numOfHiddenLayers):
			temp = [];
			for j in range (0, neuronsPerHiddenLayer):
				temp.append (Neuron ());

			hiddenLayers.append (temp);

		for i in range (0, numOfOutputs):
			outputs.append (Neuron ());

	def feedInputs (self, inputList):
		if (len (inputs) == len (inputList)):
			for i in range (0, len (inputs)):
				inputs [i].setFireInput (inputList [i]);

	def start (self):
		for neuron in inputs:
			neuron.feedNextLayer ();

if (__name__ == '__main__'):
	pass;
