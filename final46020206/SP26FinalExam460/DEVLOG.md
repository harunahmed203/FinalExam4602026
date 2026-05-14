# Development Log – The Torchbearer

**Student Name:** Harun Ahmed
**Student ID:** 132180465

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [Date]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_What I want to implement is to create a generic dijkstra based alogrithm
The main things I would need to worry about is keeping track of tourch fuel and creating a set of
relic rooms and generate it either using a vector-like data structure or some other way to print it out to keep track.
I will also attempt to keep it randokmly genretaed to make sure my code works through testing ._
._

---

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_My first hurdle when dealing with my code is test my functions for part 2 
the fisrt bug was getting the solve function to work._
my part 2 code was dealing with issues in was with my precompute function
At first i thought it would be good for just calling the dijkstar function above but i forgot that i had to define the dictonary that would store the nodes ad define my key node

I also had a bit of trouble for defining some of my logic lke my 
priority queue can be used for specific order is needed for the correct code or else the grpah testing woulf fail 



---

## Entry 3 – [Date]: [Short description]

_ Another bug I ecnounteed was getting my main explore optimal  fuction to work
I beleive the error come from my recursive case and recursion calling explore
At first i thought it was indentation but it was the order of parameters and what those parametrs where defined as, I searched the rest of my code and saw my lack of attention of this issue and had to retrace my code  in fixing all them 

._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_

I feel that for my chose inplementation was not a vector but arrays, lists sets, prue vectors were to complicated. 
but i beleive i got most of the functions downs
like for select source i mad it a list of varaibles that need to be tracked
the precompute funtcion will run the main dijkstar code multiple times until the the optimal function
solves which path is best sutied for the generated graph
If there is something i would improve if i didnt start so late is my explore function
since that took me the longest to complete espleacialy figuring out  the base/recursive case.
If given mre time I would try have expiremented and trying differnt ways of solving the most imporatnt part of the code  instead i had to rush in completeing so that my test wold pass on randomly generated graphs and not stricly relying on the given tests

._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 15 -30 min|
| Part 2: Precomputation Design |3 hours -> i coded first before part 7 |
| Part 3: Algorithm Correctness |1-2 hours |
| Part 4: Search Design | 2 hours|
| Part 5: State and Search Space | 2 hours |
| Part 6: Pruning | 1-2 hours|
| Part 7: Implementation | 4 hours-> how long ot took to finsh the code affter part 2 time|
| README and DEVLOG writing | 2 hours|
| **Total** |15 hours |
