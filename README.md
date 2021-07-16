# Session-10
---
## Sequence Type

In Python programming, sequences are a generic term for an ordered set which means that the order in which we input the items will be the same when we access them.

Python supports six different types of sequences. These are strings, lists, tuples, byte sequences, byte arrays, and range objects. Where as we can create our own type of  sequences. 

In this article, we have created our own sequence called PolygonSequencer.

To make our own sequence type, we need to implement __ get__(), __  len__()  method.

A wonderful article on this sequence type can be found [here](https://blog.teclado.com/creating-a-new-sequence-type-in-python-part-1/)



## Question

###  A regular strictly convex polygon is a polygon that has the following characteristics:

    all interior angles are less than 180
    all sides have equal length

#### 1. Create a Polygon Class

    where initializer takes in:
        number of edges/vertices
        circumradius
    that can provide these properties:
        # edges
        # vertices
        interior angle
        edge length
        apothem
        area
        perimeter
    that has these functionalities:
        a proper __repr__ function
        implements equality (==) based on # vertices and circumradius (__eq__)
        implements > based on number of vertices only (__gt__)

```python
import math

class Polygon:
	'''this  is a polygon class which takes radis and side leangth 
	2 parametersa and calculate few parameters on Polygon'''

	def __init__(self, n, r):

		if isinstance(n, int) and isinstance(r, int):
			if n<3:
				raise IndexError('Minimum 3 vertices Polygon is possible')
			else:
		
				self.num_side = n
				self.radius = r
		else:
			raise TypeError('For a Ploygon, no of Vertices &  Radius has to be a number')

	def edges(self):
		return self.num_side

	def vertices(self):
		return self.num_side

	def interior_anagle(self):
		return f'{(self.num_side-2)*180/self.num_side:.1f}'

	def edge_length(self):
		return f'{2*self.radius*math.sin(math.pi/self.num_side):.2f}'

	def apothem(self):
		return f'{self.radius*math.cos(math.pi/self.num_side):.2f}'

	def area(self):
		return f'{0.5*self.num_side*float(self.apothem())*float(self.edge_length()):.2f}'
	
	def perimiter(self):
		return f'{self.num_side*float(self.edge_length()):.2f}'

	def __eq__(self,other):
		if isinstance(other, Polygon):
			return self.num_side == other.num_side and self.radius == other.radius

		else:
			return "Can't compare different kind of object"
	
	def __gt__(self,other):
		if isinstance(other, Polygon):
			return self.num_side>other.num_side
			



	def __repr__(self):
		return f'Polygon having {self.num_side} sides and circumradius {self.radius} units is created\n'
```

#### 2. Create a Polygon Class
Implement a Custom Polygon sequence type:

    where initializer takes in:
        number of vertices for largest polygon in the sequence
        common circumradius for all polygons
    that can provide these properties:
        max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
    that has these functionalities:
        functions as a sequence type (__getitem__)
        supports the len() function (__len__)
        has a proper representation (__repr__)

```python
from session10 import *

class PolygonSequencer:
	def __init__(self, N):
		

		self.max_vertices  = N
		self.Radius  = 15

	def __len__(self):
		return self.max_vertices-2

	def __getitem__(self,i):
		if isinstance(i, int):
			if i<0 or i >= self.max_vertices-2:
				raise IndexError('passed index is out of range')
			else:
				return Polygon(3+i, self.Radius)
		elif isinstance(i,slice):
			start,stop,step = i.indices(self.max_vertices-2)
			
			rng = range(start,stop,step)
			return [Polygon(3+index, self.Radius) for index in rng]
		else:
			raise TypeError('Index has to be an integer')

	def max_eff_polygon(self):
		max_ratio = 0
		for i in range(3, self.max_vertices+1):
			poly = Polygon(i, self.Radius)
			
			ratio = float(poly.area())/float(poly.perimiter())
			#print(f'{i}:{ratio}')
			if ratio > max_ratio:
				max_side = i
				max_ratio = ratio

		return f'For circumradius {self.Radius},Polygon having {max_side} vertices is max efficiency polygon'




	def __repr__(self):
		return f'polygon sequencer is created having  maximum no of vertices is {self.max_vertices}'

```




 

