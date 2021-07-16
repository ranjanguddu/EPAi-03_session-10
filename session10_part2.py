from session10 import *

class PolygonSequencer:
	def __init__(self, N):
		'''to instantiate the class'''
		if isinstance(N, int):
			if N<3:
				raise IndexError('Minimum 3 vertices Polygon is possible')
			else:
		
				self.max_vertices  = N
				self.Radius  = 15
		else:
			raise TypeError('For a Ploygon, no of Vertices has to be a number')
		

		

	def __len__(self):
		'''finf the length of this sequence type'''
		return self.max_vertices-2

	def __getitem__(self,i):
		'''this method actually makes this class sequence type'''
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
		''' method to find the polygon having maximum area/perimiter ratio'''
		max_ratio = 0
		for i in range(3, self.max_vertices+1):
			poly = Polygon(i, self.Radius)
			
			ratio = float(poly.area())/float(poly.perimiter())
			#print(f'{i}:{ratio}')
			if ratio > max_ratio:
				max_side = i
				max_ratio = ratio

		return f'For circumradiud {self.Radius},Polygon having {max_side} vertices is max efficiency polygon'




	def __repr__(self):
		'''user helping method to know about the object '''
		return f'polygon sequencer is created having  maximum no of vertices is {self.max_vertices}'


p = PolygonSequencer(5)
print(p)

