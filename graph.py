# graph.py
# Graph Class
# By: Shahzeb Jadoon

class Graph:
    """This class is used to represent a graph that is comprised
       of named vertices that are joined via edges of different
       weights. 
    """

    def __init__(self, vertices, directed = False):
        """Initiates the Graph Class

           pre: vertices is a list of vertex labels & directed
                is a Boolean value indicating whether th graph
                is directed or not.
           post: creates a dictionary of dictionaries to
                 indicate the vertices and the edges 
        """

        self.edges = {v:{} for v in vertices}
        self.directed = directed

    def add_edge(self, vertex1, vertex2, weight = 1):
        """Adds vertex2 as an edge to vertex1 if graph is directed,
           otherwise adds vertex1 to vertex2, and vice-versa.
        
           pre: vertex1 & vertex2 are vertex labels that are
                connected via an edge of the given weight
           post: adds two vertices with the specified weight
                 using the dictionary representation
        """

        if self.directed:
            self.edges[vertex1][vertex2] = weight

        # edge connects both in case of undirected
        else:
            self.edges[vertex1][vertex2] = weight
            self.edges[vertex2][vertex1] = weight

    def has_edge(self, vertex1, vertex2):
        """Returns a Boolean indicating vertex1 is adjacent to vertex2
        """

        return vertex2 in self.edges[vertex1]

    def is_directed(self):
        """Returns a boolean indicating whether the graph is directed or not
        """

        return self.directed

    def weight(self, vertex1, vertex2):
        """Returns the weight off edge from vertex1 to vertex2
        """

        return self.edges[vertex1][vertex2]

    def num_vertices(self):
        """Returns the number of distinct vertices are in the graph
        """

        return len(self.edges)

    def vertex_iter(self):
        """Returns an iterator for vertices
        """

        return iter(self.edges)

    def edge_iter(self):
        """Returns an iterator for edges
        """

        for vertex1 in self.edges:
            for vertex2 in self.edges[vertex1]:
                yield (vertex1, vertex2)

    def adjacent_iter(self, vertex):
        """Returns an iterator for the adjacent vertices to the 
           provided vertex
        """

        return iter(self.edges[vertex])

    
def fromfile(filename):
    """Iterates through the provided file and returns a graph
       from with the given vertices and egdes in the file

       pre: filename should be a str, and it should contain directed/
            undirected on the first line, distinct vertices on the second 
            line (separated by spaces), and edges on the rest of the lines 
            format: undirected
                    a b c d
                    a b
                    b c
                    c d
                    d a
       post: returns a dictionary implementation of the graph 
             provided in the file
    """

    openfile = open(filename, "r")
    directed = openfile.readline()[:-1].lower() == "directed"
    
    vertices = []

    # create a list of distinct vertices from the file
    for vertex in openfile.readline().split(" "):
        if vertex[-1:] == "\n":
            vertices.append(vertex[:-1])
        else:
            vertices.append(vertex)

    graph = Graph(vertices, directed)

    # add edges to the graph
    for edge in openfile.read()[:-1].split("\n"):
        try:
            vertex1, vertex2 = edge.split(" ")
            graph.add_edge(vertex1, vertex2)

        except:
            vertex1, vertex2, weight = edge.split(" ")
            graph.add_edge(vertex1, vertex2, weight)

    openfile.close()

    return graph

def main():
    """Lets the user create a graph from a file, and look at 
       the vertices and edges
    """

    print("This program allows the user to build a graph from a file")
    key_pressed = str(input("Would you like to start? (Y/N) "))
    
    # keeps running until the user says to stop
    while key_pressed.lower()[0] == "y":

        # ask the user for the filename
        inFile = askopenfilename()
        graph = fromfile(inFile)

        print("Would you like to know the number of distinct vertices")
        key_pressed = str(input("in your graph? (Y/N)"))

        if key_pressed.lower()[0] == "y":
            print(graph.num_vertices())

        print()
        print("Would you like to see the distinct vertices in the graph?")
        key_pressed = str(input("(Y/N) "))
        
        if key_pressed.lower()[0] == "y":

            for vertex in graph.vertex_iter():
                print(vertex)

        print()
        print("Would you like to see all the edges in your graph?")
        key_pressed = str(input("(Y/N)"))

        if key_pressed.lower()[0] == "y":

            for edge in graph.edge_iter():
                print(edge)
        
        print("Thank you for using this program!\n")
        key_pressed = str(input("Would you like to create a graph from another file? (Y/N) "))

if __name__ == "__main__":
    from tkinter.filedialog import askopenfilename
    
    main()