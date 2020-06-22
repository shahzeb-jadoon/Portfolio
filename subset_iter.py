# subset_iter.py
# Subset Iterator
# By: Shahzeb Jadoon

def subsets(collection):
    """ Creates a list of all subsets of the collection provided

        pre: collection can be a list or a collection of items
        post: returns a list of all subsets of collection
    """

    collection = list(collection)

    if not collection:
        return [[]]

    tail = subsets(collection[1:])
    return tail + [[collection[0]] + item for item in tail]


def subset_partition(lst):
    """ Finds the two subsets that partition the lst in such a way that the sum of 
        elements in both subsets are equal

        pre: lst should be a list of numbers ( can be float or int)
        post: returns the two subsets with equal sum
    """

    if sum(lst) % 2 != 0:
        return [], []

    for subset in subsets(lst):
        sub_sum = sum(subset)
        items_left = lst[:]

        for element in subset:
            items_left.remove(element)

        if sub_sum == sum(items_left):
            return items_left, subset
            
    return [], []


def main():
    """ This program demonstrates the subsets algorithm and also the partition 
        algorithm which utilizes the subsets algorithm. 
    """

    print("This program demonstrates the subsets algorithm and partition algorithm")
    print("which utilizes the subsets algorithm. The subsets function returns all subsets")
    print("of a given collection whereas the partition function is used to divide the")
    print("list into two parts in such a way that the sum of both")
    print("parts is equal.\n")

    key_pressed = str(input("Would you like to see all possible subsets of a graph? (Y/N) "))

    if key_pressed[0].lower() == "y":

        num_vertices = int(input("\nHow many vertices should the graph have (up to 26)? "))

        vertices = []

        for i in range(num_vertices):
            vertices.append(ascii_lowercase[i])

        graph = Graph(vertices)

        for i in range(num_vertices - 1):

            for j in range(i + 1, num_vertices):
                graph.add_edge(vertices[i], vertices[j], randrange(0, 500))

        key_pressed = str(input("\nWould you like to see the vertices? (Y/N) "))

        if key_pressed[0].lower() == "y":
            
            for vertex in graph.vertex_iter():
                print(vertex)

        key_pressed = str(input("\nWould you like to see the edges? (Y/N) "))

        if key_pressed[0].lower() == "y":

            for edge in graph.edge_iter():
                print(edge)

        key_pressed = str(input("\nWould you like to see all the subsets of vertices? (Y/N) "))
        
        if key_pressed[0].lower() == "y":
            for subgraph in subsets(graph.vertex_iter()):
                print(subgraph)

        key_pressed = str(input("\nWould you like to partition a list into two equal subsets?"))

        if key_pressed[0].lower() == "y":
            for _ in range(3):
                lst = []

                for i in range(5):
                    lst.append(randrange(0, 5))

                print("\nThe initial list is:\n", lst)
                print("The partition is:\n", subset_partition(lst))
                
    elif key_pressed[0].lower() == "n":
        key_pressed = str(input("\nWould you like to partition a list into two equal subsets? (Y/N) "))

        if key_pressed[0].lower() == "y":
            for _ in range(3):
                lst = []

                for i in range(5):
                    lst.append(randrange(0, 5))

                print("\nThe initial list is:\n", lst)
                print("The partition is:\n", subset_partition(lst))

    else:
        print("\nInvalid Input")

    print("\nThank you for using the program!")


if __name__ == "__main__":
    from random import randrange, choice
    from string import ascii_lowercase
    from graph import Graph
    
    main()