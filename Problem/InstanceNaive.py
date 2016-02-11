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
            orders.append((x,y,products, i)) # The last element is the original index.    

        return Instance(rows, columns, drones, deadline, maxload, weights, warehouses, orders)
    
    # Instance's constructor.
    def __init__(self, rows, columns, num_drones, deadline, maxload, weights, warehouses, orders):
        self.rows = rows
        self.columns = columns
        self.drones = num_drones
        self.deadline = deadline
        self.maxload = maxload
        self.weights = weights
        self.warehouses = warehouses
        self.orders = orders
