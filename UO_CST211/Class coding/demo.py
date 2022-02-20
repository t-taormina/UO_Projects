UO CIS 211 Code Demo, Week 6
Created by: Luis Fernando Guzman Nateras
______________________________________________________________________

Define the following python classes:

Vector class
	- Subclass of list
	- Its elements are ints

Methods:
	- __mul__
		- Computes the dot product with another vector
		- Returns int
	- matrix_mult
		- Computes the multiplication of the current Vector by a Matrix
		- Returns a resulting Vector
		- Must check for incompatible dimensions

Matrix class
	- A two-dimensional Matrix

Attributes
	- rows -- A list of Vectors representing the rows of the Matrix
	- cols -- A list of Vectors representing the columns of the Matrix

Methods:
	- __init__
		- Receives a Vector list representing the rows of the Matrix as an argument
		- "cols" must be computed within this method from the contents of rows

Here's an example of a use case of this code:

>>> v = Vector([1,2])
>>> v2 = Vector([3,4])
>>> m = Matrix([v2, Vector([5,6])])
>>> print(v.matrix_mult(m))
[13 16]

Which is basically:

[1 2] * [ [3 4],  = [13 16]
          [5 6] ]


MATH BACKGROUND

VECTOR-MULTIPLICATION

[1 2 3] * [4 5 6] = (1*4) + (2*5) + (3*6) = 4 + 10 + 18 = 32

VECTOR-MATRIX MULTIPLICATION

Requirements: Vector must have the same length as the Matrix has rows.

The elements of the resulting vector are just the dot product of the vector with every column of the Matrix

[1 2] * [ [3 4],  = [ ([1 2] * [3 5]) ([1 2] * [4 6]) ] = [13 16]
          [5 6] ]
