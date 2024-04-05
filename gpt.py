import numpy as np
import random

def compute_cost(matching, graph1, graph2):
    """
    Computes the cost of the current matching.
    This function should be defined based on the specific problem.
    For simplicity, we're just summing the differences in edge weights.
    """
    cost = 0
    for i in range(len(matching)):
        for j in range(len(matching)):
            # Sum the absolute difference in edge weights
            cost += abs(graph1[i, j] - graph2[matching[i], matching[j]])
    return cost

def glauber_dynamics(graph1, graph2, iterations=1000):
    n = graph1.shape[0]
    # Initial random matching
    matching = list(range(n))
    random.shuffle(matching)
    
    for _ in range(iterations):
        # Randomly select two nodes in the first graph to consider swapping
        i, j = random.sample(range(n), 2)
        
        # Compute the cost of the current matching
        current_cost = compute_cost(matching, graph1, graph2)
        
        # Try swapping matches
        matching[i], matching[j] = matching[j], matching[i]
        
        # Compute the cost after swapping
        new_cost = compute_cost(matching, graph1, graph2)
        
        # Decide whether to accept the new matching
        if new_cost > current_cost:
            # Swap back if the new matching is worse, with a certain probability
            # This probability could be adjusted based on temperature or other criteria
            if random.random() > 0.5:
                matching[i], matching[j] = matching[j], matching[i]
                
    return matching

# Example graphs represented as adjacency matrices
graph1 = np.array([[0, 1, 1, 0],
                   [1, 0, 1, 0],
                   [1, 1, 0, 1],
                   [0, 0, 1, 0]])

graph2 = np.array([[0, 1, 0, 1],
                   [1, 0, 1, 1],
                   [0, 1, 0, 1],
                   [1, 1, 1, 0]])

# Run the algorithm
matching = glauber_dynamics(graph1, graph2)
print("Matching:", matching)
