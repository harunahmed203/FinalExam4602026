"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Harun Ahmed
Student ID:   132180465

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq
from json.encoder import INFINITY


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    
    return"""
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.
        
        ## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _Shortest path wont always take in factor the relic rooms only from starting to ending node_

- **What decision remains after all inter-location costs are known:**
  _Its to create the best path by taking into account the relic rooms. It must build its path by
  visitng all relic rooms in the most optimal way before reaching exit_

- **Why this requires a search over orders (one sentence):**
  _because the path taken needs to check all possible nodes before making a decision/based on best choice for our fuel._


       
    
    """
    #return 
#todo


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : start node (S)
    

    relics : list[node]{R1....Rk}
    exit_node : node(T)

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """

    return [spawn] + relics + [exit_node]



    pass


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    #
    """
    #TOD
    #pass

    distance = {node: float('inf') for node in graph} #distance = maps the nodes to each other
    distance[source] = 0 #start node will be defined as zero -> 

    prioity_queue = [(0, source)] #will go in order based on least - most in value
    visited_nodes = set() #will track the nodes we vist in the map/empty until the code runs

    while prioity_queue:
        cost , node = heapq.heappop(prioity_queue) 

        if node in visited_nodes: #this prevents repeat vistis to visted nodes
            continue
        
        visited_nodes.add(node) #if not then add to the visited set

        for next_node , weight in graph[node]: #by looking at the weight of the next node
            cost_updated = cost + weight # your cost will equal the next weight + your orognal cost

            if cost_updated < distance[next_node]: #if the distance is more than our cost
                distance[next_node] = cost_updated #then it will be our new cost
                heapq.heappush(prioity_queue, (cost_updated, next_node)) # then push it in the queue

    return distance









def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    
    """
    #TOD -> placeholder for todo to run my code
    
    sources = select_sources(spawn, relics, exit_node) #our most importantnodes
    dist_table = {} #create an empty dictionary for our nodes

    for start_node in sources:
        dist_table[start_node] = run_dijkstra(graph, start_node)

    return dist_table 

    #pass


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    return"""
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.
        
     
     ## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _finalized node = a node that is visted and put inot the visted set/popped from the queue
  This means its part of the shorest path from start node._

- **For nodes not yet finalized (not in S):**
  _Non-finalized node is unvisited none thats still in the node
  is still being decided wheter to be added to shortest path._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _because no nodes have been added to the path yet so invarant stays valid ._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _ the next node with smallest weight(minimum distance from current node) so its finalized and added to shorest path ._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Algorithm ends when all nodes(relic rooms) are reached/finalized from S to T -> shorest path was reached._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_ It matters because in odre for the algorithm to generate the shorest path it must pick the best node from the options provided between each relic room      ._

---
     
     
    
    """
    #return 
#todo


# =============================================================================
# PART 4
# =============================================================================

def explain_search():

    return"""
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.
        
        ## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _where a greedy algorithm picks the closet node ignoring relic room distances
whihc would reslut in a worse outcome or torch running out _
- **Counter-example setup:** _ if the possible nodes from S is
1.) S -> a(3)
2.) S -> b(6)
3.) S -> c(2) 
the  example will pick c as the next node even if the relic room is now futhure from that choice ._

- **What greedy picks:** _It will alyways pick the next node with shorest path/smallest weight  ._

- **What optimal picks:** _te best next node that will ensure you reach relic room in the shorest path possible towards the neasrest one ._

- **Why greedy loses:** _Because by protitizine the smallest next node it doesnt consider relic rooms
best local choice doesnt guarntee best gobal choice._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _The algortihm must exlpore possible orders of visitng paths to the relic room and pick the best path whihc will guarntee the shorest path._

---

      
      
      
      
      
      
    
    """
    #return
    
#todo


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.    
    """
    
    best_route = [float('inf'), []] # will represent the optimal route to take
    
    #then we recurse call the explore function to find the next node
    
    _explore( dist_table = dist_table, current_loc=spawn, relics_remaining= set(relics),
            relics_visited_order= [], cost_so_far =0, exit_node= exit_node, best = best_route)
    
    #cost so far is set to 0 at the begining
    # nothing stored in relics visiting order
    
    
    
    return(best_route[0], best_route[1])
    
    
    #pass
    #todo


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    
    if(len(relics_remaining)) == 0: #BaseCase = no more relic rooms available
        
        total_cost = cost_so_far + dist_table[current_loc][exit_node]
        # our final cost is out dist table(collection of path taken) with our current location at the end
        #its also added with the the current cost for 
        if dist_table[current_loc][exit_node] == float('inf'):
            return
        
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()
            
        return
    if cost_so_far >= best[0]: #this is where your pruningn happens
        return
    
    for relic_next in list(relics_remaining): # this for loop will be our recursive case
       
        node_travel = dist_table[current_loc][relic_next]
       
        if node_travel == float('inf'):
            continue
        
       
        relics_remaining.remove(relic_next) #where we keep track of visited relic rooms
        relics_visited_order.append(relic_next) #the ist added
        
        
            
        
        _explore( dist_table = dist_table, current_loc= relic_next, 
                 relics_remaining= relics_remaining,
            relics_visited_order=relics_visited_order, 
            cost_so_far=cost_so_far+ node_travel,
            exit_node=exit_node, best = best)
     
        relics_remaining.add(relic_next) #this is for  bactracking from our relic rooms
        relics_visited_order.pop()
    
    
    
    
    
    
    
    
    #Pruning explanation: Since there inst any negative weights(like -2) your'e only left with
    #two options, you either pick a path that will reslut on a higer total cost or a path which
    #remains the shorest path so you can just cut off the firdt option
    
    #pass
    #todo


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    
    """
    
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    #dist_table is the collection of distance chosen to be part of the shorest path from node ot node
    
    return find_optimal_route(dist_table, spawn, relics, exit_node)
    
    #pass
    #todo


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
