import math

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
        self.timeout = deadline
        self.maxload = maxload
        self.weights = weights
        self.warehouses = warehouses
        self.orders = orders
        
        # Initialise drones
        self.drones = []
        for i in range(0,num_drones):
            self.drones.append(warehouses[0])
        
        # Init history
        self.history = []
            
    ## Movimientos
    def load(idDron,Nwarehouse,prodcut,Nitems):
        history.append (str(dron) + "L" + str(Nwarehouse) + str(prodcut) + str(Nitems))
        
    def deliver(idDron,Nwarehouse,prodcut,Nitems):
        history.append (str(idDron) + "D" + str(Ndeliver) + str(prodcut) + str(Nitems))


################### COMPUTE
# Devuelve lo mejor que puede hacer un dron, la orden que tiene que hacer y el warehouse que use
# (dron,order,warehouse)
def bestDron(inst):
    min_time = inst.timeout
    best_dron = None
    best_order = None
    best_warehouse = None
    
    for dron in range(len(inst.drones)):
        for order in range(len(inst.orders)):
            time, warehouse = cost(inst,dron,order)
            if time < min_time:
                min_time = time
                best_dron = dron
                best_order = order
                best_warehouse = warehouse
    
    return (best_dron, best_order, best_warehouse)
     

# Devuelve la mejor forma de que un dron haga order
# (coste, warehouse)
def cost(inst,dron,order):
    min_coste = float('inf')
    ware_optima = 0
    (cx,cy,cprods) = inst.orders[order]

    # Para cada warehouse
    for wn in range(len(inst.warehouses)):
        (wx,wy,wprods) = inst.warehouses[wn]
        
        # Comprueba que aqui este todo
        for cosa in cprods:
            if cosa not in wprods: 
                continue
        
        # Calcula el coste
        coste = dist((dronx,self.y), (wx,wy)) + dist((wx,wy), (cx,cy)) + 2 #+1 por el load y el delivery
        if (coste < min_coste):
            ware_optima = wn
            min_coste = coste

    return (coste, wn)
           
# Distance 
def dist(u,v):
    (a,b) = u
    (c,d) = v
    return math.sqrt((a-c)**2 + (b-d)**2)            
            
#################### EXECUTE
# Executes the order over the instance
# ()
def executeOrder(inst, dron, order, warehouse):
    (ox,oy,oprod) = inst.orders[order]
    (wx,wy,wprod) = inst.warehouses[warehouse]
        
    # Carga todos los productos
    inst.move(ox,oy) # Mueve al warehouse
    for idprod in range(len(weigths)):
        numprods = oprod[idprod]
        inst.load(adron, numprods, product, awarehouse)
        
    # Entrega
    for idprod in range(len(weigths)):
        inst.deliver(iddron,idorder,product,numprods)



#################### MAIN
inst = readInstance()

(best_dron, best_order, best_warehouse) = bestDron(inst)
more_turns = best_drone != None
while more_turns:
    executeOrder(inst,best_dron, best_order, best_warehouse)
    (best_dron, best_order, best_warehouse) = bestDron(inst)
    more_turns = best_drone != None