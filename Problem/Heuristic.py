################################################################################
# Authors: Team DGIIM for Google Hash Code
# Date: 11 - February - 2016
################################################################################

import time

# Declaration of an abstract class that is used as an interface for the
# implemented heuristics.

class Heuristic:

    # Initialise the heuristic.
    def init(self, instance):
        self.best_sol = None
        self.instance = instance

    # Init the heuristic.
    # info = Subinterval information
    def __init__(self):
        init()

    # First initial computations.
    # This method should be implemented by the subclasses.
    def initialComputations1(self):
        pass

    # Second initial computations.
    # This method should be implemented by the subclasses.
    def initialComputations2(self):
        pass

    # Iteration of the heuristic.
    # The method should be implemented by the subclasses.
    def iteration(self):
        pass

    # Final computations.
    # This method should be implemented by the subclasses.
    def finalComputations(self):
        pass

    # Generate a solution with the heuristic.
    # @param iterations Number of iterations for the heuristic.
    # @return Tuple with the solution and the execution time in seconds.
    def generateSolution(self, iterations = 0):
        # Start the heuristic
        start = time.time()
        # Initial computations
        initialComputations1()
        initialComputations2()
        # Iterations
        for i in range(0, iterations+1):
            iteration()
        # Final computations
        finalComputations()
        # Get the execution time
        end = time.time()
        return self.best_sol, end-start

    # Generate a list of solutions with the heuristic.
    # @param num_sols Number of solutions that are generated.
    # @param iterations Number of iterations for the heuristic.
    # @return List of tuples. Each tuple has a solution and the corresponding
    #         execution time in seconds.
    def generateSolutions(self, num_sols, iterations = 0):
        return [generateSolution(iterations) for x in range(num_sols)]
