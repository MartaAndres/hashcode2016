################################################################################
# Authors: Team DGIIM for Google Hash Code
# Date: 11 - February - 2016
################################################################################


import math

class Dron:

    def __init__(self, instance):
        self.instance = instance
        # Position of the dron
        self.x = instance.wharehouse[0]
        self.y = instance.wharehouse[1]
        # Current dron time
        self.time = 0


        # Items that the dron carries
        self.items = []
    
    
    def load(Nitems,product,Nwarehouse):
        
        
    
    




# Solutions' representation.
class Solution:

    # Solution's constructor.
    def __init__(self, instance):
        # id of a dron is its index in this vector
        self.drones=[]
        self.instance = instance
        self.history=[]
        
        for i in range(0, instance.drones):
            d = Dron(instance)
            self.drones.append(d)
            
    
    def CalculateSolution():
        TurnsLeft = True
        
        while TurnsLeft:
            # Escogemos el dron con mejor función de evaluación            
            max = 0
            maxIndex = 0
            
            for i in range(0,len(drones)):
                x = drones[i].Evaluate()
                
                if x>max:
                    max = x
                    maxIndex = i
        
        
            drones[i].
                
        
    
    def load (idDron, Nitems, product, Nwarehouse):
        history.append (str(idDron) + "L" + str(Nwarehouse) + str(prodcut) + str(Nitems))
        drones[idDron].load (Nitems, product, instance.warehouses[Nwarehouse])
        
    def unload(idDron, Nitems, product, Ndeliver):
        history.append (str(idDron) + "D" + str(Ndeliver) + str(prodcut) + str(Nitems))
        drones[idDron].unload(Nitems, product, instance.orders[Ndeliver])

    

    # Best dron is taken from the set of drons with the lowest turn executed.
    # The dron taken is the one with better best_order.
    def bestDron():
        
        
        

        
    
