################################################################################
# Authors: Team DGIIM for Google Hash Code
# Date: 11 - February - 2016
################################################################################


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
        
        maxOrder = 
            for j in range(len(instance.drones)):
                
        
    
    def bestOrder():
        best=-1
        score=0
        
        for o in range(len(instance.orders)):
            for d in range(len(instance.drones)):
                for p in range(instance.orders[0].products):
                       
                
    
        
        
    
    def load (idDron, Nitems, product, Nwarehouse):
        history.append (str(idDron) + "L" + str(Nwarehouse) + str(prodcut) + str(Nitems))
        drones[idDron].load (Nitems, product, instance.warehouses[Nwarehouse])
        
    def unload(idDron, Nitems, product, Ndeliver):
        history.append (str(idDron) + "D" + str(Ndeliver) + str(prodcut) + str(Nitems))
        drones[idDron].unload(Nitems, product, instance.orders[Ndeliver])