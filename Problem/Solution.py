################################################################################
# Authors: Team DGIIM for Google Hash Code
# Date: 11 - February - 2016
################################################################################

from instance import *
from queue import queue
import math

class Dron:

    def __init__(self, instance, warehouse):
        self.inst = instance
        # Position of the dron
        self.x = wharehouse[0]
        self.y = wharehouse[1]
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
        for (wx,wy,wprods) in warehouses):
            # Comprueba que aquí esté todo
            for cosa in cprods:
                if (cosa is not in wprods): 
                    continue
            
            # Calcula el coste
            coste = dist((self.x,self.y), (wx,wy)) + dist((wx,wy), (cx,cy)) + 2 #+1 por el load y el delivery
            if (coste < min_coste):
                ware_optima = w
                min_coste = coste
    
        return coste
    
    
    def dist((a,b),(c,d)):
        math.sqrt((a-c)**2 + (b-d)**2)
    
    
    
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
        self.drones=[]
        self.instance = instance
        self.history=[]
        
        for i in range(0,instance.drones):
            d = Dron(instance.warehouses[0])
            self.drones.append(d)
            
            
    def load (idDron, Nitems, product, Nwarehouse):
        history.append (str(idDron) + "L" + str(Nwarehouse) + str(prodcut) + str(Nitems))
        drones[idDron].load (Nitems, product, instance.warehouses[Nwarehouse])
        
    def unload(idDron, Nitems, product, Ndeliver):
        history.append (str(idDron) + "D" + str(Ndeliver) + str(prodcut) + str(Nitems))
        drones[idDron].unload(Nitems, product, instance.orders[Ndeliver])

    def bestron():
        bes

    
