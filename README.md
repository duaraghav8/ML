# ML
Code I wrote in order to illustrate Machine Learning Algorithms using input features in mostly 2 dimensional space (could easily be extended to any number of dimensions, its just the visualization that becomes harder which is why I didn't go beyond 2). The code is intended to make developers understand how learners based on Neural Networks, Bayesian learning, Decision Trees and Concept learning algorithms actually work.

ps - Check out Machine Learning by Tom Mitchell. For ML Junkies (like me), it is GOLD!

#Input format:

the file "examples" contains, in each line, first the x input value, second the y input value and finally the output.
For example, in delta rule, examples contains:

**1550 1003 13859**

This follows the equation Ax + By = O. Here, x = 1550, y = 1003, O = 13859. We figure out the values of A and B given the large training set and the Delta Rule (Gradient Descent).

**Spoiler Alert**

The actual weights are provided in generate.py (so that you can compare those to the results our scripts give us).

#Output format:

In the file "calculation", each line contains 2 numbers. The first is the weight (or coefficient) of x and the second of y. If we were computing weights for **n** input features, then we'd have **n** different weights on each line.
