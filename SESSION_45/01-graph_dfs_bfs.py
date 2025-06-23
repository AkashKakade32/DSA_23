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


class hnode: 
    def __init__(self, vertex_number: int):
        self.v = vertex_number 
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


    def insert_end(self, v: int) -> None: 
        hlist.generic_insert(self.head_node.prev, hnode(v), self.head_node)


class vnode: 
    def __init__(self, vertex_number: int): 
        self.v = vertex_number 
        self.adj_list = hlist() 
        self.prev = None 
        self.next = None 
        self.color = color.WHITE 


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



    def add_edge(self, v_start:int, v_end: int): 
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

        v_start_node.adj_list.insert_end(v_end)
        v_end_node.adj_list.insert_end(v_start)
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


    def dfs(self) -> None:

        def reset(head_node: vnode): 
            v_run = head_node.next 
            while v_run != head_node: 
                v_run.color = color.WHITE
                v_run = v_run.next

        def dfs_visit(self, u: vnode) -> None:
            '''
                @u: vnode 
                @v_adj_vnode: vnode 
                @v_adj: hnode
            '''
            print(f"[{u.v}]->", end='')
            u.color = color.GREY
            v_adj = u.adj_list.head_node.next 
            while v_adj != u.adj_list.head_node: 
                v_adj_vnode = vlist.search_node(self.v_list.head_node, v_adj.v)    
                if v_adj_vnode.color == color.WHITE: 
                    dfs_visit(self, v_adj_vnode)
                v_adj = v_adj.next
            u.color = color.BLACK

        reset(self.v_list.head_node)

        print("[START]->", end='')
        v_run = self.v_list.head_node.next 
        while v_run != self.v_list.head_node: 
            if v_run.color == color.WHITE: 
                dfs_visit(self, v_run) 
            v_run = v_run.next 
        print("[END]") 

    def bfs(self, v: int) -> None:
        def reset(head_node: vnode): 
            v_run = head_node.next 
            while v_run != head_node: 
                v_run.color = color.WHITE
                v_run = v_run.next
        reset(self.v_list.head_node)
        v_node = vlist.search_node(self.v_list.head_node, v)
        if v_node is None: 
            raise VertexInvalidError(f"bfs():Start vertex {v} is invalid")
        print("[START]->", end='')
        Q = []
        Q.append(v_node)
        while len(Q) != 0: 
            vn = Q.pop(0)
            vn.color = color.BLACK 
            print(f'[{vn.v}]->', end='')
            h_run = vn.adj_list.head_node.next 
            while h_run != vn.adj_list.head_node: 
                h_in_v = vlist.search_node(self.v_list.head_node, h_run.v)
                if h_in_v.color == color.WHITE and h_in_v not in Q: 
                    Q.append(h_in_v)
                h_run = h_run.next
        print("[END]")
    
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
    print('----Creating connected and disconnected graph object for testing dfs() and bfs()----')
    g = graph() 
    for v in range(1, 7): 
        g.add_vertex(v) 


    edges = [
                (1, 2), (5, 6), (2, 4), 
                (3, 6), (3, 5), (2, 3), 
                (4, 5), (6, 1), (3, 1), 
                (3, 4) 
            ]
    

    for (v_start, v_end) in edges: 
        g.add_edge(v_start, v_end) 

    print('Printing connected graph()')
    print(g)

    g_disconnected = graph() 
    for v in range(1, 12): 
        g_disconnected.add_vertex(v)

    edges = [
                (1, 4), (2, 3), (3, 4), (1, 2), 
                (6, 7), (7, 5), (5, 6), (10, 11), 
                (11, 8), (8, 9), (9, 10)
            ]
    
    for (v_start, v_end) in edges: 
        g_disconnected.add_edge(v_start, v_end)

    print('Printing disconnected graph()')
    print(g_disconnected)

    print('----Testing dfs()-----')
    
    print('Testing dfs() on connected graph')
    g.dfs() 
    print('Testing dfs() on disconnected graph')
    g_disconnected.dfs() 
    print("graph:dfs:all ok")

    print('----Testing bfs()----')
    print('Testing connected graph')
    for i in range(1, 7): 
        print(f'BFS with root_vertex:{i}')
        g.bfs(i)
    print('Testing disconnected graph')
    for i in range(1, 12): 
        print(f'BFS with root_vertex:{i}')
        g_disconnected.bfs(i)