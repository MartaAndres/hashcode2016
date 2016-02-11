################################################################################
# Authors: Team DGIIM for Google Hash Code
# Date: 11 - February - 2016
################################################################################

# Instance to work with.
class Instance:

    def readInstance():
        # Parameters of the simulation
        (r,c,d,l,m) = map(int, input().split())
        rows = r
        columns = c
        drones = d
        deadline = l
        maxload = m
    
        # Weights of the products
        p = int(input())
        weights = list(map(int,input().split()))
    
        # Warehouses
        warehouses = []
        w = int(input())
        for i in range(w):
            (x,y) = map(int, input().split())
            products = list(map(int,input().split()))
            warehouses.append((x,y,products))
    
        # Customer orders
        orders = []
        c = int(input())
        for i in range(c):
            (x,y) = map(int, input().split())
            l = int(input())
            products = list(map(int,input().split()))
            orders.append((x,y,products))
    
        return Instance(rows, columns, drones, deadline, maxload, weights, warehouses, orders)
    
    ###
    # Importados de Solution.py (!!!!)
    ###
    def load (idDron, Nitems, product, Nwarehouse):
        history.append (str(idDron) + "L" + str(Nwarehouse) + str(prodcut) + str(Nitems))
        drones[idDron].load (Nitems, product, instance.warehouses[Nwarehouse])

    def unload(idDron, Nitems, product, Ndeliver):
        history.append (str(idDron) + "D" + str(Ndeliver) + str(prodcut) + str(Nitems))
        drones[idDron].unload(Nitems, product, instance.orders[Ndeliver])

    # Best dron is taken from the set of drons with the lowest turn executed.
    # The dron taken is the one with better best_order.
    def bestDron():
        min_time = self.instance.timeout
        for dron in drones:
            if dron.time < min_time:
                min_time = dron.time

    # Instance's constructor.
    def __init__(self, rows, columns, drones, deadline, maxload, weights, warehouses, orders):
        self.rows = rows
        self.columns = columns
        self.drones = drones
        self.deadline = deadline
        self.maxload = maxload
        self.weights = weights
        self.warehouses = warehouses
        self.orders = orders
        
        #Importados de Solution.py
        self.historial = []