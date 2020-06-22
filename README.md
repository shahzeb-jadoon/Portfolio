# Portfolio

## Sieve:
The sieve.py includes the sieve(n) function that implements the Sieve of Eratosthenes algorithm to find Prime numbers up until the number n.

## Multisorter:
The multisorter.py includes three different types of sorting algorithms. bubble_sort(lst), comp_count_sort(lst), and selection_sort(lst) implement Bubble Sort, Comparison Count Sort, and Selection Sort algorithms respectively. Both Bubble Sort and Selection Sort agorithm implementations in this file are in-place algorithms, whereas Comparison Count Sort is not. 

## Graph:
This module contains the Graph class that initializes a graph usning a dictionary of dictionaries. It includes methods to add edges (add_edge) to the graph. has_edge(v1, v2) checks if an edge exists between vertices v1 and v2. is_directed() is a boolean for showing whether the graph is directed or not. weight(v1, v2) returns the weight of the edge connecting vertices v1 and v2. num_vertices() returns the number of distinct vertices in the graph. vertex_iter() and edge_iter() return an iterator for the vertices and edges of the graph, whereas adjacent_iter(v) returns an iterator for the vertices adjacent to the vertex v. 
This module also contains fromfile(file) function that creates and returns a graph from the file provided in its parameter. 
The main() function allows the user to select a file via a browser select tool using tkinter.filedialog's tool askopenfilename(). The user can make and view graphs created from their files as many times as they would like.

## Graphalgs:
The k_clique(graph, k) finds the first complete sub-graph in graph, and shows it to the user instead of just notifying the user if there is one or not. The algorithm takes into account if the graph is directed or undirected, and also is a bit more efficient than the brute-force algorithm because it stops when it has found a k-sized clique within the graph and returns it to the user.
The main() function utilizes my Graph module to create a graph from a file that is selected by the user within the browser window (credit to askopenfilename()), and takes user input to which sized clique they want to find in the graph. This funtion runs indefinitely and lets the user make graphs and check k-sized cliques from multipe files (one at a time), until the user decides to quit.

## Subset Iterator:
The subset_iter.py includes the subsets(collection) function that creates the list of all subsets of the collection, and it also contaions the subset_partition(lst) function that partitions the provided lst into two in such a way that the sum of items in each partition is equal.

## n log n Sorts:
The n_log_n_sorts.py includes three different types of sorting algorithms. The first two being mergesort(lst) and quicksort(lst)  which are the two n log n sorts that implement Merge Sort and Quick Sort algorithms respectively. It also includes insertion_sort(lst) which implements the Insertion Sort algorithm. All three sorting algorithms in this file are in-place algorithms.

## Convex Hull:
The quickhull.py file contains the convex_hull(lst), convex_merge_sort(lst), convex_elim(lst), quick_hull(lst), determ(p1, p2, p3), reverse(lst), upper_hull(p_first, p_last, points), and lower_hull(p_first, p_last, points) functions. The convex_hull(lst) is the main function that is called on an unordered list of (x, y) tuples that is sorted using convex_merge_sort(lst) and then reduced to distinct points using convex_elim(lst). The convex_hull(lst) is called to retrieve the points that returns the convex hull points using determ, reverse, upper_hull and lower_hull helping functions.

## Heap Sort:
The heapsort.py file contains build_heap(lst, lst_size) which converts a list into a heap (starting at index 0) and uses heapify(lst, index, lst_size) as a helping function to achieve this. The last fnction is heap_sort(lst) which utilizes build_heap to first make a heap out of the provided list and then sort the list from there. 

## 2-3 Tree:
The tree23.py includes the classes Node and Tree23 that help in making balanced trees that can store 2 or 3 values in their nodes.

## Horspool:
The horspool.py includes the make_shift_table class that is used to assist in implementing the Horspool algorithm to find a given pattern within a text.

## Open Hash:
The open_hash.py file contains the class Node and the class IntDict that create a dictionary using open hashing. 

## Knapsack:
The knapsack.py file contains the Knapsack class which uses the concept of Dynamic Programming by storing the previously calculated values by the algorithm using the memoization technique provided by Python. It calculates the best valued subset of items from the ones provided by the user that can fit in the knapsack of specified capacity. 

## Rod Cuting:
The rod_cutting.py includes the RodCutting Class which uses the concept of Dynamic Programming by storing the previously calculated values by the algorithm using the memoization technique provided by Python. It calculates the lengths that the original rod should be cut into to get the best cost that can be attained from the buyers.

### Notes:
graph.py & graphics.py (created by John Zelle) are helping modules for these subset iterator and convex hull respectively. Also, I worked with Takeaki Doi on a few of the files in this portfolio.
