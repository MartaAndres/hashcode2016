################################################################################
# Authors: Team DGIIM for Google Hash Code
# Date: 11 - February - 2016
################################################################################

from Instance import *
#from queue import queue
import math

class Dron:

    def __init__(self, instance, warehouse):
        self.instance = instance
        # Position of the dron
        self.x = wharehouse[0]
        self.y = wharehouse[1]
        # Current dron time
        self.time = 0

        # Ocupation of a given dron
        self.load = 0
        # Items that the dron carries
        self.items = []
    
    def cost(order_num):
        min_coste = math.inf
        ware_optima = 0
        inst = self.instance
        (cx,cy,cprods) = inst.orders[order_num]
    
        # Para cada warehouse
        for wn in range(len(warehouses)):
            (wx,wy,wprods) = warehouses[wn]
            
            # Comprueba que aquí esté todo
            for cosa in cprods:
                if cosa not in wprods: 
                    continue
            
            # Calcula el coste
            coste = dist((self.x,self.y), (wx,wy)) + dist((wx,wy), (cx,cy)) + 2 #+1 por el load y el delivery
            if (coste < min_coste):
                ware_optima = wn
                min_coste = coste
    
        return (coste, wn)
    
    
    def dist(u,v):
        (a,b) = u
        (c,d) = v
        return math.sqrt((a-c)**2 + (b-d)**2)
    
    
    
    def load (Nitems, product, warehouse):
        items[product] = Nitems
        
        x = warehouse[0]
        y = warehouse[1]
        
        
        
        
    def unload(Nitems, product, cell):
        items[product] = items[product] - Nitems
        
        x = cell[0]
        y = cell[1]


# Solutions' representation.
class Solution:

    # Solution's constructor.
    def __init__(self, instance):
        # id of a dron is its index in this vector
        self.drones = []
        self.instance = instance
        self.historial = []

        for i in range(0,instance.drones):
            d = Dron(instance.warehouses[0])
            self.drones.append(d)
            


        
    
