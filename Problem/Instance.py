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
            warehouses.append([x,y,products])
    
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

    def deliver(idDron, Nitems, product, Ndeliver): # Esto es un deliver
        history.append (str(idDron) + "D" + str(Ndeliver) + str(prodcut) + str(Nitems)) # WTF NAME
        drones[idDron].unload(Nitems, product, instance.orders[Ndeliver])
    
        

    def execute_order(self, iddron,aorder,aw_num):
        dron = drones[iddron]
        (ox,oy,oprod) = aorder
        (wx,wy,wprod) = warehouses[aw_num]
        
        # Carga todos los productos
        for product in products:
            move_dron(aorder)
            load(adron, oprod[product], product, awarehouse)
            deliver(adron,)
        
        coste_de_la_ejecucion = dist((adron.x,adron.y),(ox,oy))+dist((ox,oy),(wx,wy))
        return coste_de_la_ejecucion

    # Instance's constructor.
    def __init__(self, rows, columns, num_drones, deadline, maxload, weights, warehouses, orders):
        self.rows = rows
        self.columns = columns
        self.num_drones = num_drones
        self.deadline = deadline
        self.maxload = maxload
        self.weights = weights
        self.warehouses = warehouses
        self.orders = orders
        
        #Importados de Solution.py
        self.historial = []

        # Initialise drones
        self.drones = []
        for i in range(0,num_drones):
            d = Dron(instance, warehouses[0])
            self.drones.append(d)
            