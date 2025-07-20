import math 
from DCDS import DCDS 


def geh(tb=False): 
    from sys import exc_info
    from traceback import print_tb
    exc_name, exc_data, exc_tb = exc_info() 
    print(exc_name.__name__, exc_data, sep=':')
    if tb: 
        print_tb(exc_tb)


class VertexExistsError(Exception): 
    pass


class VertexInvalidError(Exception): 
    pass 


class EdgeExistsError(Exception): 
    pass


class EdgeInvalidError(Exception): 
    pass 


class GraphInconsistentError(Exception):
    pass


class color: 
    WHITE = 1 
    GREY = 2 
    BLACK = 3 


class edge_iterator: 
    def __init__(self, G): 
        self.G = G 
    def __iter__(self): 
        return self 
    def __next__(self): 
        return self.G.__next__()

class hnode: 
    def __init__(self, vertex_number: int, w = 0.0):
        self.v = vertex_number 
        self.w = w
        self.color = color.WHITE
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
        run = head_node.next 
        while run is not head_node: 
            if run.v == v: 
                return run 
            run = run.next 
        return None 

    
    def __init__(self): 
        self.head_node = hnode(-1)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 


    def insert_end(self, v: int, w = 0.0) -> None: 
        hlist.generic_insert(self.head_node.prev, hnode(v, w), self.head_node)


class vnode: 
    def __init__(self, vertex_number: int): 
        self.v = vertex_number 
        self.adj_list = hlist() 
        self.color = color.WHITE
        self.prev = None 
        self.next = None 
         

class vlist: 
    @staticmethod
    def generic_insert(start: vnode, mid: vnode, end: vnode): 
        mid.next = end 
        mid.prev = start 
        start.next = mid 
        end.prev = mid 


    @staticmethod 
    def generic_delete(d_node: vnode): 
        d_node.prev.next = d_node.next 
        d_node.next.prev = d_node.prev 


    @staticmethod 
    def search_node(head_node: vnode, v: int) -> vnode: 
        run = head_node.next 
        while run is not head_node: 
            if run.v == v: 
                return run 
            run = run.next 
        return None 


    def __init__(self): 
        self.head_node= vnode(-1) 
        self.head_node.v = -1 
        self.head_node.adj_list = None 
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 

    
    def insert_end(self, v: int): 
        vlist.generic_insert(self.head_node.prev, vnode(v), self.head_node) 


class graph:  
    def __init__(self): 
        self.v_list = vlist() 
        self.nr_vertices = 0 
        self.nr_edges = 0 


    def add_vertex(self, v: int) -> None: 
        v_node = vlist.search_node(self.v_list.head_node, v)
        if v_node is not None: 
            raise VertexExistsError(f"{v} is already present")
        self.v_list.insert_end(v)
        self.nr_vertices += 1 


    def remove_vertex(self, v: int): 
        v_remove_node = vlist.search_node(self.v_list.head_node, v)
        if v_remove_node is None: 
            raise VertexInvalidError(f"{v} does not exist for removal")
        
        h_run = v_remove_node.adj_list.head_node.next 
        while h_run != v_remove_node.adj_list.head_node: 
            h_run_next = h_run.next
            vnode_of_adj_vertex = vlist.search_node(self.v_list.head_node, h_run.v) 
            hnode_of_v_in_h = hlist.search_node(vnode_of_adj_vertex.adj_list.head_node, v)
            hlist.generic_delete(hnode_of_v_in_h)
            del h_run 
            self.nr_edges -= 1
            h_run = h_run_next
        del v_remove_node.adj_list.head_node 
        v_remove_node.adj_list = None
        vlist.generic_delete(v_remove_node)
        self.nr_vertices -= 1 



    def add_edge(self, v_start:int, v_end: int, w = 0.0): 
        v_start_node = vlist.search_node(self.v_list.head_node, v_start)
        v_end_node = vlist.search_node(self.v_list.head_node, v_end)
        if v_start_node is None: 
            raise VertexInvalidError(f"{v_start} is not present in graph")
        if v_end_node is None: 
            raise VertexInvalidError(f"{v_end} is not present")
        h1 = hlist.search_node(v_start_node.adj_list.head_node, v_end)
        h2 = hlist.search_node(v_end_node.adj_list.head_node, v_start)
        
        if h1 is not None and h2 is not None:
            raise EdgeExistsError(f'Edge between {v_start} & {v_end} already exists')
        if (h1 is None and h2 is not None) or (h2 is None and h1 is not None): 
            raise GraphInconsistentError("Graph is corrupt")

        v_start_node.adj_list.insert_end(v_end, w)
        v_end_node.adj_list.insert_end(v_start, w)
        self.nr_edges += 1 


    def remove_edge(self, v_start: int, v_end: int): 
        v_start_node = vlist.search_node(self.v_list.head_node, v_start)
        v_end_node = vlist.search_node(self.v_list.head_node, v_end)
        if v_start_node is None: 
            raise VertexInvalidError(f"{v_start} is not present in graph")
        if v_end_node is None: 
            raise VertexInvalidError(f"{v_end} is not present")
        hnode_of_end_in_start = hlist.search_node(v_start_node.adj_list.head_node, v_end)
        hnode_of_start_in_end = hlist.search_node(v_end_node.adj_list.head_node, v_start)
        
        if hnode_of_end_in_start is None and hnode_of_start_in_end is None: 
            raise EdgeInvalidError(f'There is not edge between {v_start} & {v_end}')
        
        if (
            (hnode_of_start_in_end is None and hnode_of_end_in_start is not None) or 
            (hnode_of_end_in_start is None and hnode_of_start_in_end is not None)
        ): 
            raise GraphInconsistentError("Graph is correpted")
        
        hlist.generic_delete(hnode_of_end_in_start)
        hlist.generic_delete(hnode_of_start_in_end)
        self.nr_edges -= 1 

    
    def edges(self): 
        def get_edges(self): 
            L = [] 
            run_v = self.v_list.head_node.next 
            while run_v != self.v_list.head_node: 
                run_h = run_v.adj_list.head_node.next 
                while run_h != run_v.adj_list.head_node: 
                    if run_h.color == color.WHITE: 
                        L.append((run_v.v, run_h.v, run_h.w))
                        vnode_of_h = vlist.search_node(self.v_list.head_node, run_h.v)
                        h_of_first = hlist.search_node(vnode_of_h.adj_list.head_node, run_v.v)
                        h_of_first.color = color.BLACK
                    run_h = run_h.next
                run_v = run_v.next 
            return L 
        
        def insertion_sort(L): 
            for j in range(1, len(L)): 
                key = L[j]
                i = j - 1 
                while i > -1 and L[i][2] > key[2]: 
                    L[i+1] = L[i]
                    i = i - 1 
                L[i+1] = key 
            return L 

        def get_generator(lst: list):    
            for (u, v, w) in lst: 
                yield (u, v, w)
          
        return edge_iterator(get_generator(insertion_sort(get_edges(self))))
    
    
    def kruskal(self): 

        A = []
        D = DCDS() 
        run = self.v_list.head_node.next 
        while run != self.v_list.head_node: 
            D.make_set(run.v)
            run = run.next 
        
        for (u, v, w) in self.edges(): 
            uS = D.find_set(u)
            vS = D.find_set(v)
            if uS != vS: 
                A.append((u, v, w))
                D.union(u, v)

        return A 

    def __str__(self): 
        return_str = f'|G.V|={self.nr_vertices}, |G.E|={self.nr_edges}\n'
        v_run = self.v_list.head_node.next 
        while v_run != self.v_list.head_node: 
            return_str += f'[{v_run.v}]\t->\t'
            h_run = v_run.adj_list.head_node.next 
            while h_run != v_run.adj_list.head_node: 
                return_str += f'[{h_run.v}]<->'
                h_run = h_run.next
            return_str += '[END]\n'
            v_run = v_run.next 
        return return_str


if __name__ == '__main__':   
    try: 
        g = graph() 
    
        for v in range(1, 6): 
            g.add_vertex(v)

        E = [
            (1, 2, 0.5), (2, 3, 1.8), (4, 3, 2.0), (1, 4, 1.0), 
            (1, 3, 1.3), (2, 5, 0.7), (3, 5, 0.4), (4, 5, 1.2)
        ]
    
        for (v_start, v_end, w) in E: 
            g.add_edge(v_start, v_end, w)
    
        for (u, v, w) in g.edges(): 
            print("edge:", (u, v), "Weight:", w) 

        print("MST:")
        for (u, v, w) in g.kruskal():
            print("EDGE:", (u, v), "WEIGHT:", w)

        print("------------------------END------------------------")
    except: 
        geh() 