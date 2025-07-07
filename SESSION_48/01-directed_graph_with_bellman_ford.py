from math import inf as INFINITY 

class VertexInvalidError(Exception): pass 
class VertexExistsError(Exception): pass
class EdgeInvalidError(Exception): pass
class EdgeExistsError(Exception): pass
class GraphInconsistentError(Exception): pass


class color: 
    WHITE = 1
    GRAY = 2 
    BLACK = 3


class hnode: 
    def __init__(self, v: int, w = 0.0): 
        self.v = v 
        self.w = w 
        self.prev = None 
        self.next = None 


class hlist: 
    @staticmethod 
    def generic_insert(start: hnode, mid: hnode, end: hnode) -> None: 
        mid.next = end 
        mid.prev = start 
        start.next = mid 
        end.prev = mid 

    
    @staticmethod 
    def generic_delete(d_node: hnode) -> None: 
        d_node.prev.next = d_node.next 
        d_node.next.prev = d_node.prev 

    
    @staticmethod 
    def search_node(head_node: hnode, v: int) -> hnode: 
        h_run = head_node.next 
        while h_run is not head_node: 
            if h_run.v == v: 
                return h_run 
            h_run = h_run.next 
        return None 
    
    
    def __init__(self): 
        self.head_node = hnode(-1)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 


    def insert_end(self, v: int, w = 0.0) -> None: 
        hlist.generic_insert(self.head_node.prev, hnode(v, w), self.head_node)
    

class vnode: 
    def __init__(self, v: int): 
        self.v = v 
        self.h_list = hlist()
        self.color = color.WHITE
        self.v_pred = None 
        self.d = INFINITY
        self.prev = None 
        self.next = None 


class vlist: 
    @staticmethod 
    def generic_insert(start: vnode, mid: vnode, end: vnode) -> None: 
        mid.next = end 
        mid.prev = start 
        start.next = mid 
        end.prev = mid 

    
    @staticmethod 
    def generic_delete(d_node: vnode) -> None: 
        d_node.prev.next = d_node.next 
        d_node.next.prev = d_node.prev 

    
    @staticmethod 
    def search_node(head_node: vnode, v: int) -> vnode: 
        v_run = head_node.next 
        while v_run is not head_node: 
            if v_run.v == v: 
                return v_run 
            v_run = v_run.next 
        return None 
    
    
    def __init__(self): 
        self.head_node = vnode(-1)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 


    def insert_end(self, v: int) -> None: 
        vlist.generic_insert(self.head_node.prev, vnode(v), self.head_node)


class edge_iterator: 
    def __init__(self, G): 
        self.G = G 
    def __iter__(self): 
        return self 
    def __next__(self): 
        return self.G.__next__()
    def sorted(self): 
        def get_generator(lst: list): 
            for x in lst: 
                yield x 
        L = list(self.G)
        for j in range(1, len(L)): 
            key = L[j]
            i = j - 1 
            while i > -1 and L[i][2] > key[2]: 
                L[i+1] = L[i]
                i = i - 1 
            L[i+1] = key
        return edge_iterator(get_generator(L))
    

class DirectedGraph: 
    def __init__(self): 
        self.v_list = vlist() 
        del self.v_list.head_node.h_list
        self.nr_vertices = 0 
        self.nr_edges = 0 


    def add_vertex(self, v: int) -> None: 
        if vlist.search_node(self.v_list.head_node, v) is not None: 
            raise VertexExistsError(f'{v} is already added in graph')
        self.v_list.insert_end(v)
        self.nr_vertices += 1 


    def remove_vertex(self, v: int) -> None: 
        vnode_of_v = vlist.search_node(self.v_list.head_node, v)
        if vnode_of_v is None: 
            raise VertexInvalidError(f'vertex to be removed {v} does not exist')
        # This loop removes all edges of which 'v' is a starting vertex 
        h_run = vnode_of_v.h_list.head_node.next 
        while h_run is not v_node_of_v.h_list.head_node: 
            h_run_next = h_run.next 
            del h_run 
            self.nr_edges -= 1
            h_run = h_run_next
        vlist.generic_delete(vnode_of_v)
        self.nr_vertices -= 1 

        # This loop removes all edges of which 'v' is an ending vertex 
        v_run = self.v_list.head_node.next 
        while v_run is not self.v_list.head_node: 
            h_run = v_run.h_list.head_node.next 
            while h_run is not v_run.h_list.head_node: 
                h_run_next = h_run.next 
                if h_run.v == v: 
                    hlist.generic_delete(h_run)
                    self.nr_edges -= 1 
                h_run = h_run_next
            v_run = v_run.next 


    def add_edge(self, v_start: int, v_end: int, w = 0.0) -> None: 
        vnode_of_start_vertex = vlist.search_node(self.v_list.head_node, v_start)
        vnode_of_end_vertex = vlist.search_node(self.v_list.head_node, v_end)

        if vnode_of_start_vertex is None or vnode_of_end_vertex is None: 
            raise VertexInvalidError(f"{v_start} or {v_end} or both are invalid")

        hnode_of_end_vertex = hlist.search_node(vnode_of_start_vertex.h_list.head_node, v_end)
        if hnode_of_end_vertex is not None: 
            raise EdgeExistsError(f'Edge between {v_start} and {v_end} exists')
        
        vnode_of_start_vertex.h_list.insert_end(v_end, w)
        self.nr_edges += 1 


    def remove_edge(self, v_start: int, v_end: int) -> None:
        vnode_of_start_vertex = vlist.search_node(self.v_list.head_node, v_start) 
        if vnode_of_start_vertex is None: 
            raise VertexInvalidError(f'{v_start} does not exist')
        hnode_of_end_vertex = hlist.search_node(vnode_of_start_vertex.h_list.head_node, v_end)
        if hnode_of_end_vertex is None: 
            raise EdgeInvalidError(f'The edge to be deleted {v_start}->{v_end} does not exist')
        hlist.generic_delete(hnode_of_end_vertex)
        self.nr_edges -= 1 


    def get_nr_edges(self): 
        return self.nr_edges 


    def get_nr_vertices(self): 
        return self.nr_vertices


    def edges(self): 
        def get_generator(self): 
            v_run = self.v_list.head_node.next 
            while v_run is not self.v_list.head_node: 
                h_run = v_run.h_list.head_node.next 
                while h_run is not v_run.h_list.head_node: 
                    vnode_of_h_run = vlist.search_node(self.v_list.head_node, h_run.v)
                    T = (v_run, vnode_of_h_run, h_run.w)
                    yield T 
                    h_run = h_run.next 
                v_run = v_run.next 
        return edge_iterator(get_generator(self))


    def __str__(self): pass 


    def bellman_ford(self): 
        def initialize_single_source(vnode_of_source_vertex): 
            v_run = self.v_list.head_node.next 
            while v_run != self.v_list.head_node: 
                v_run.d = INFINITY 
                v_run.v_pred = None 
                v_run = v_run.next 
            vnode_of_source_vertex.d = 0.0


        def relax(vnode_of_start_vertex: vnode, vnode_of_end_vertex: vnode, w: float) -> None: 
            if vnode_of_end_vertex.d > vnode_of_start_vertex.d + w: 
                vnode_of_end_vertex.d = vnode_of_start_vertex.d + w 
                vnode_of_end_vertex.v_pred = vnode_of_start_vertex

        initialize_single_source(self)

        for i in range(1, len(self.get_nr_vertices())): 
            for (vnode_of_start, vnode_of_end, w) in self.edges():
                relax(vnode_of_start, vnode_of_end, w)
        

        for (vnode_of_start, vnode_of_end, w) in self.edges(): 
            if vnode_of_end.d > vnode_of_start.d + w: 
                return False 
            
        return True 

if __name__ == '__main__': 
    dg = DirectedGraph() 
    
    for v in range(1, 6): 
        dg.add_vertex(v)
    
    E = [
        (1, 2, 0.5), (2, 3, 1.8), (4, 3, 2.0), (1, 4, 1.0), 
        (1, 3, 1.3), (2, 5, 0.7), (3, 5, 0.4), (4, 5, 1.2)
    ]

    for (v_start, v_end, w) in E: 
        dg.add_edge(v_start, v_end, w)

    print("All edges:")
    for (vnode_start, vnode_end, w) in dg.edges().sorted(): 
        print('[', vnode_start.v, vnode_end.v, w, ']', sep='|')
        