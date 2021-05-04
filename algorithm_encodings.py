class SearchAlg:

    def __init__(self, alg_name, length_opt, cost_opt, heuristic, infinite, description, time, space):

        #Algorithm name
        self.name = alg_name

        #Possible values:
        #1: Guaranteed length-optimal solution, 
        #0: Not guaranteed length-optimal solution 
        #-1: parameters can be tuned so that solution is length-optimal
        self.length_optimality = length_opt 
        
        #Possible values:
        #1: Guaranteed cost-optimal solution
        #0: Not guaranteed cost-optimal solution
        #-1: Cost-optimal with an admissible heuristic
        self.cost_optimality = cost_opt

        #Possible Values:
        #1: Algorithm requires search space heuristic
        #0: Heuristic not required
        self.heuristic_req = heuristic

        #Possible Values:
        #1: Algorithm may not find finite length solutions if infinite paths exist
        #2: Algorithm will find finite length solutions regardless of the presence of infinite paths
        self.infinite_paths = infinite
        
        #String description of the search algorithm and its use cases
        self.description = description

        #String representation of algorithm time complexity
        self.time_complexity = time

        #String representation of algorithm space complexity
        self.space_complexity = space

if __name__ == "__main__":

    BFS_description = "The breadth-first search algorithm explores a graph by searching all nodes at its current depth level \
before exploring any nodes at subsequent depths (starting from the search tree's root). \n\nStrengths: Breadth-first search is well-suited to finding solutions \
that are close to the search tree root, and the first solution found is guaranteed to have the shortest path length of any solution.\
\nWeaknesses: Breadth-first search may not be able to find solutions deep within a search tree if the branching factor is high. \
Space complexity is higher than other uninformed search algorithms."

    BFS = SearchAlg("Breadth-first search", 
        1, #Length-optimal solution
        0, #Solution not guaranteed to be cost-optimal
        0, #Heuristic not required
        0, #Can handle infinite length paths
        BFS_description,
        "O(|V| + |E|)  (V: Number of search nodes, E: Number of edges)", #Time complexity
        "O(b^d)    (b: Branching factor, d: Solution depth )" #Space complexity
        )

    DFS_description = "Depth-first search explores a graph by exploring paths as deeply as possible before backtracking and considering other paths.\
\n\nStrengths: Depth-first search is well-suited problems which contain multiple solutions deep within a search tree. Less space requirements than breadth-first search \
\nWeaknesses: Solutions found may not be optimal in terms of length. Infinite paths may cause the algorithm to never terminate. Depth-first search may miss solutions \
very near the search tree's root while exploring deep within the tree."


    DFS = SearchAlg("Depth-first search", 
        0, #Length-optimal solution
        0, #Solution not guaranteed to be cost-optimal
        0, #Heuristic not required
        1, #Cannot handle infinite length paths
        DFS_description,
        "O(|V| + |E|)  (V: Number of search nodes, E: Number of edges)", #Time complexity
        "O(b * h)    (b: Branching factor, h: Maximum depth explored )" #Space complexity
        )

    DLS_description =  "Depth-limited search explores a graph by exploring paths as deeply as possible up to a fixed depth before backtracking and considering other paths.\
\n\nStrengths: Unlike depth-first search, depth-limited search will never get stuck following infinite-length paths. Depth-first search is well-suited problems which contain \
multiple solutions at or just before its depth limit. Less space requirements than breadth-first search. \
\nWeaknesses: Solutions found may not be optimal in terms of length. Depth-limited search will never find a solution that exceeds its maximum depth limit. Depth-first search may miss solutions \
very near the search tree's root while exploring deep within the tree."


    DLS = SearchAlg("Depth-limited search", 
        0, #Solution may not be length-optimal
        0, #Solution not guaranteed to be cost-optimal
        0, #Heuristic not required
        0, #Can handle infinite length paths
        DLS_description,
        "O(|V| + |E|)  (V: Number of search nodes, E: Number of edges)", #Time complexity
        "O(b * h)    (b: Branching factor, h: Maximum depth explored )" #Space complexity
        )

    IDFS_description = "Iterative deepening search explores a graph by performing a depth-first search up to a fixed depth (i.e., exploring paths as deeply as possible up to \
a fixed depth before backtracking). If a solution is not found, the depth limit is increased and the search is restarted. \
\n\nStrengths: If the initial depth limit and depth increment are both set to 1, then found solutions are guaranteed to be optimal in terms of path length. Less space requirements than breadth-first search \
\nWeaknesses: Many of the same node explorations are repeated each time the search restarts with a higher depth limit.  If branching factor is high, \
may take a long time before searching deep within the tree."

    IDFS = SearchAlg("Iterative deepening search", 
        -1, #Algorithm can be tuned to be length-optimal
        0, #Solution not guaranteed to be cost-optimal
        0, #Heuristic not required
        0, #Can handle infinite length paths
        IDFS_description,
        "O(|V| + |E|)  (V: Number of search nodes, E: Number of edges)", #Time complexity
        "O(b * h)    (b: Branching factor, h: Maximum depth explored )" #Space complexity
        )

    candidates = [BFS, DFS, DLS, IDFS]

    remove_set = set()
    heuristics = input("\nDo nodes in the search space have an associated heuristic function? (y, n)\n")

    infinite_paths = input("\nDoes the problem search space contain infinite length paths? (y, n)\n")

    length_optimal = input("\nDoes the problem require finding a solution with shortest length? (y, n)\n")

    optimal_cost = input("\nIf solutions have an associated cost function, does the lowest cost solution need to be found? (y/n)\n")


    for alg in candidates:
        #Prune heuristic search algorithms if necessary
        if heuristics == 'n':
            if alg.heuristic_req == 1:
                remove_set.add(alg)

        #Prune non-length-optimal algorithms if necessary
        if length_optimal == 'y':
            if alg.length_optimality == 0:
                remove_set.add(alg)

        #Prune algorithms that cannot handle infinite paths if necessary
        if infinite_paths == 'y':
            if alg.infinite_paths == 1:
                remove_set.add(alg)

        #Prune non-cost-optimal algorithms if necessary
        if optimal_cost == 'y':
            if alg.cost_optimality == 0:
                remove_set.add(alg)

    if len(remove_set) == len(candidates):
        print("\nNo candidate algorithms can satisfy this problem's requirements.")
    
    else:
        #Prune algorithms that do not satisfy the problem requirements
        for prune_alg in remove_set:
            candidates.remove(prune_alg)

        print("\n-----------------------------------------\n")
        print("\nCandidate algorithms:\n")
        
        #Display information on each algorithm 
        for i in range(len(candidates)):
            print(str(i + 1) + ": " + candidates[i].name + "\n")
            print("TIME COMPLEXITY: " + candidates[i].time_complexity)
            print("SPACE COMPLEXITY: " + candidates[i].space_complexity+ "\n")
            print("DESCRIPTION: " + candidates[i].description + "\n\n")
            








