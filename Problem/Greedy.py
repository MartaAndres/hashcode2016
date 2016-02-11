################################################################################
# Authors: Team DGIIM for Google Hash Code
# Date: 11 - February - 2016
################################################################################

from Solution import *
from queue import PriorityQueue

class Greedy:
    
    def __init__(self, instance):
        self.instance = instance
    
    def bestDron():
        min_time = self.instance.timeout
        best_dron = -1
        best_order = -1
        
        for dron in inst.drones:
            for order in inst.orders
                time = dron.cost(order)
                if time < min_time:
                    min_time = time
                    best_dron = dron
                    best_order = order
        
        return (best_dron, best_order)
     
    def solve(inst):
        more_turns = True
        while more_turns:
            mincost = math.inf
            (best_dron,best_order) = bestDron()
            inst.executeOrder(best_dron,best_order)
        
        return solucion
    


    def newSol(self):

        # Initialise problem
        sol = Solution()
        sol.computeCosts()
        more_turns = True

        while more_turns:
            
            # Execute a order
            best_dron = bestDron()
            best_dron.executeBestOrder()
            more_turns = sol.recomputeCosts()

        return sol