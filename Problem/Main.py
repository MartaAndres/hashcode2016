################### INPUT ##########################
# Lee la instancia
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
        

# Almacena una instancia
class Instance:
    def __init__(self, rows, columns, num_drones, deadline, maxload, weights, warehouses, orders):
        self.rows = rows
        self.columns = columns
        self.num_drones = num_drones
        self.deadline = deadline
        self.maxload = maxload
        self.weights = weights
        self.warehouses = warehouses
        self.orders = orders
        
        # Initialise drones
        self.drones = []
        for i in range(0,num_drones):
            d = Dron(instance, warehouses[0])
            self.drones.append(d)
            

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