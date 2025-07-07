'''
Coding pattern required for implementing Bellman-Ford
for all edges e in G.E taken in non-decreasing order of their weights 
    # do something with e 
'''


class Edge: 
    def __init__(self, v_start, v_end, w=0.0): 
        self.v_start = v_start 
        self.v_end = v_end 
        self.w = w 

class DirectGraph: 
    def add_edge(self, v_start:int, v_end:int, w=0.0): 
        # step 1:   Validate v_start and v_end and get their vnode 
        # step 2:   Add hnode of v_end in adjecency list of v_start 
        # step 3:   if graph is undirected then add hnode entry of v_start 
        #           in adjecency list of v_end 
        # step 4:   add object of class Edge, created by Edge(v_start, v_end, w)
        #           In list of edges maintained in self.E
        #           self.E.add_edge(Edge(v_start, v_end, w))


#   Storage-wise efficient but difficult approach to implement: 
#   Extract edge data from adjecency list ON DEMAND 

# E = g.get_edges() 
# Then we should be able to return linked list edges (built in list if you want keep things 
# small) then 
# for e in E: # do something with e 

for e in g.edges(): 
    # do something with e 
    # advanced level iterator 