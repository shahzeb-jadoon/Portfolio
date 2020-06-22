# graphalgs.py
# Graph Algorithms
# By: Shahzeb Jadoon


def k_clique(graph, k):
    """Checks whether the graph has a k-sized complete sub-graph

       pre: k is an int
       post: returns the list of vertices that comprise the k-sized 
             sub-graph (if present) in the graph provided as parameter,
             otherwise returns None
    """
    
    vertices = ""

    # create a str of all vertices
    for vertex in graph.vertex_iter():
        vertices += vertex

    vertices_combinations = []

    # create a list of all k-sized combinations of the vertices
    if graph.is_directed():
        vertices_combinations = list(permutations(vertices, k))

    else:
        vertices_combinations = list(combinations(vertices, k))

    clique = []

    # check whether there is a k-sized complete sub-graph
    for sets in vertices_combinations:
        found = True

        for i in range(k - 1):

            for j in range(i + 1, k):
                found = found and graph.has_edge(sets[i], sets[j])

                if found and i == k - 2 and j == k - 1:
                    clique = sets
                    return clique


def main():
    """This program shows the first occuring complete sub-graph of a size provided
       by the user from a file that is also provided by the user.
    """

    print("This program finds a complete sub-graph of a size identified by the user")
    print("within a graph provided by the user in the form of a text file\n")
    key_pressed = str(input("Would you like to continue? (Y/N) "))
    
    # continues on until user stops the program
    while key_pressed.lower()[0] == "y":
        print()
        input("Press enter key to select a file")

        # open a window for user to select the file in their file browser
        inFile = askopenfilename()
        print()
        clique_size = int(input("Enter the size of sub-graph: "))
        graph = fromfile(inFile)
        clique = k_clique(graph, clique_size)
        print("\nThe sub-graph of size", clique_size, "in", inFile, "is\n")
        print(clique)
        print("\nWould you like to search for another complete sub-graph within")
        key_pressed = str(input("another file? (Y/N) "))

    print("\nThank you for using this program!")

if __name__ == "__main__":
    from graph import Graph, fromfile
    from itertools import combinations, permutations
    from tkinter.filedialog import askopenfilename
    
    main()