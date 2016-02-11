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
        
        for dron in inst.drones:
            for order in inst.orders
                time = dron.cost(order)
                if time < min_time:
                    min_time = time
    
    def solve(inst):
        while more_turns:
            mincost = m
            best_dron = 0
            for dron in inst.drones:
        
        return solucion
    
    def newSol(self):

        # Initialise problem
        sol = Solution()
        sol.computeCosts()
        more_turns = True

        while more_turns:
            
            # Execute a order
            best_dron = sol.bestDron()
            best_dron.executeBestOrder()
            more_turns = sol.recomputeCosts()

        return sol