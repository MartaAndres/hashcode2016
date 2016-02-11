################################################################################
# Authors: Team DGIIM for Google Hash Code
# Date: 11 - February - 2016
################################################################################

from Solution import *
from queue import PriorityQueue

class Greedy:
    
    def bestDron():
        min_time = self.instance.timeout
        best_dron = None
        best_order = None
        best_warehouse = None
        
        for dron in inst.drones:
            for order in inst.orders:
                time, warehouse = dron.cost(order)
                if time < min_time:
                    min_time = time
                    best_dron = dron
                    best_order = order
                    best_warehouse = warehouse
        
        return (best_dron, best_order, best_warehouse)
     
    def solve(inst):
        (best_dron, best_order, best_warehouse) = Greedy.bestDron()
        more_turns = best_drone != None
        while more_turns:
            inst.executeOrder(best_dron, best_order, best_warehouse)
            (best_dron, best_order, best_warehouse) = Greedy.bestDron()
            more_turns = best_drone != None
        
        return instance.historial


## MAIN

inst = Instance.readInstance()
solve(inst)