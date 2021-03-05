import math
from functools import reduce

class Polygon:

    '''A regular strictly convex polygon is a polygon that has the following characteristics:
      all interior angles are less than 180
      all sides have equal length'''

    def __init__(self, numedges : int, radius : float):

        ''' constructor'''
        
        if not isinstance(numedges, int):
            raise ValueError('Polygon: number of vertices must be integer')
        if numedges < 3:
            raise ValueError('Polygon: number of vertices must be >= 3')
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise ValueError('Polygon: radius must be integer or float')
        if radius <= 0:
            raise ValueError('Polygon: radius must be > 0')

        self._numedges = numedges
        self._radius = radius
        self._interior_angle = (numedges - 2) * 180 / numedges
        self._edge_length = round(2 * radius * math.sin(math.pi / numedges), 4)
        self._apothem = round(radius * math.cos (math.pi / numedges), 4)
        self._area = round(0.5 * numedges * self._edge_length * self._apothem, 4)
        self._perimeter = round(numedges * self._edge_length, 4)
   
    def __repr__(self):
        return f'{self.__class__.__name__}(\nnumedges={self._numedges},\nradius={self._radius},\ninterior_angle={self._interior_angle},\
          \nedge_length={self._edge_length},\napothem={self._apothem},\narea={self._area},\nperimeter={self._perimeter})'

    def __eq__(self, other)-> bool:

        ''' implements equality comparison'''

        if isinstance(other, Polygon):
            return self._numedges == other._numedges and self._radius == other._radius
        else:
            return False

    def __gt__(self, other)-> bool:

        ''' implements > comparison'''

        if isinstance(other, Polygon):
            return self._numedges > other._numedges
        else:
            return False
        
############################

class CustomPolygon:
    
    ''' where initializer takes in:
    number of vertices for largest polygon in the sequence
    common circumradius for all polygons'''


    def __init__(self, numedges : int, radius : float):

        ''' constructor. initializes the sequence. Also find maximum efficient member'''
        
        if not isinstance(numedges, int):
            raise ValueError('CustomPolygon: number of vertices must be integer')
        if numedges < 3:
            raise ValueError('CustomPolygon: number of vertices must be >= 3')
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise ValueError('CustomPolygon: radius must be integer or float')
        if radius <= 0:
            raise ValueError('CustomPolygon: radius must be > 0')
            
        self._polygons=[]       
        for i in range(3,numedges + 1):
            self._polygons.append(Polygon(i, radius))
        
        self._max_efficient = reduce(lambda a, b: a if (a._area/a._perimeter >  b._area/b._perimeter) else b, self._polygons)
        
    def __getitem__(self, key):
        
        ''' key can be index or (numedges) or (numedges, radius)'''
        
        
        if isinstance(key, int) and int(key) <= len(self._polygons) -1:
            return self._polygons[key] 
        else:
            raise ValueError('CustomPolygon: invalid key')
        
                
    def __len__(self):
        
        ''' return len of sequence''' 
        
        return len(self._polygons)
    
    
    def __repr__(self):       
        return f'polygon sequence {self._polygons}'
    
    
    def __max_efficieny__(self):
        return self._max_efficient
      
        
         
        

#######################################

# test #
'''poly1= Polygon(3, 10)
poly2 = Polygon(6, 10)
poly3 = Polygon(8, 7)

print(poly1)
print('\npoly1 == poly2 :',poly1 == poly2)
print('poly3 > poly2 :', poly3 > poly2)'''

############ test 2 #####

#cp1 = CustomPolygon(25,-10)
#print(cp1.__max_efficieny__())