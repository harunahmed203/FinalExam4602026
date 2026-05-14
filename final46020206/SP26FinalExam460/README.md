# The Torchbearer

**Student Name:** Harun Ahmed
**Student ID:** 132180465
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _Shortest path wont always take in factor the relic rooms only from starting to ending node_

- **What decision remains after all inter-location costs are known:**
  _Its to create the best path by taking inot account tinerlocations & relic rooms._

- **Why this requires a search over orders (one sentence):**
  _because the path taken needs to check all possible nodes before making a decision/based on best choice for our fuel._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| _ start node(S)_ | _because those nodes represent where the path will start _ |
| _relic nodes{R1....Rk}_ | _will represent where your torch will reset/acts as checkpoint in your path_ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | greedy/shorest path|
|---|---|
| Data structure name |Graph,Priority Queue,Min heap,Visited set,   |
| What the keys represent |Nodes = Start,Relic Rooms,End |
| What the values represent | best distance from S to T|
| Lookup time complexity |visited = O(1), O(nlogn) visited nodes in priotiy queue|
| Why O(1) lookup is possible | because it will only apply to visited nodes|

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _total relic node + S&T_
- **Cost per run:** _O(nlogn)_
- **Total complexity:** _O(nlogn)_
- **Justification (one line):** _The dijkstra is used to find the shorets path from each source node_

---

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

- **Why greedy loses:** _Because by protitizine the smallest next node it doesnt consider relic rooms._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _The algortihm must exlpore possible orders of visitng paths to the relic room and pick the best path whihc will guarntee the shorest path._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location |node | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _the minimum distance from start node + the correct order of relic rooms visted._
- **When it is used:** _When visiting a node/comparing with its neighboors/._
- **What it allows the algorithm to skip:** _paths that cost more/nodes that cnat be reached/visted nodes._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** 
_the next nodes adjacent to the current node + remaining relic rooms + its current fuel cost._
- **What the lower bound accounts for:** 
_the smallest amount of torch fuel needed to vist the next node/relics/exit._
- **Why it never overestimates:** 
_Since its the shorest path, the other choices will be less cost or the same cost._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Because pruning saves the path from picking another choice whic may increase the final cost
Our optimal solution cant make onther shorest path even with lower bound estimation
---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
