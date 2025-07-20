class ElementExistsError(Exception): 
    pass 

class int_node: 
    def __init__(self, n: int): 
        self.n = n 
        self.prev = None 
        self.next = None 
        

class Set: 
    @staticmethod 
    def generic_insert(start: int_node, mid: int_node, end: int_node): 
        mid.next = end 
        mid.prev = start 
        start.next = mid 
        end.prev = mid 


    @staticmethod 
    def generic_delete(node: int_node): 
        node.prev.next = node.next 
        node.next.prev = node.prev


    def __init__(self, x = None): 
        self.head_node = int_node(None) 
        self.representative_element = x 
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node
        
        if x is not None: 
            self.insert_end(x)


    def insert_end(self, x: int): 
        if x not in self: 
            Set.generic_insert(self.head_node.prev, int_node(x), self.head_node)


    def append(self, other): 
        if type(self) != type(other): 
            raise TypeError(f'other must be of type Set')
        run = other.head_node.next 
        while run != other.head_node: 
            self.insert_end(run.n)
            run = run.next 

        
    def destroy(self): 
        run = None 
        run_next = None 

        run = self.head_node.next 
        while run != self.head_node: 
            run_next = run.next 
            del run 
            run = run_next 

        del self.head_node 


    def __contains__(self, x: int): 
        run = self.head_node.next 
        while run != self.head_node: 
            if run.n == x: 
                return True 
            run = run.next 
        return False 
    

class DCDS_node: 
    def __init__(self, mS: Set): 
        self.mS = mS 
        self.prev = None 
        self.next = None 


class DCDS: 


    @staticmethod 
    def generic_insert(start: DCDS_node, mid: DCDS_node, end: DCDS_node): 
        mid.next = end 
        mid.prev = start 
        start.next = mid 
        end.prev = mid 


    @staticmethod 
    def generic_delete(node: DCDS_node): 
        node.prev.next = node.next 
        node.next.prev = node.prev


    def __init__(self): 
        self.head_node = DCDS_node(None)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 

    
    def insert_end(self, mS: Set): 
        DCDS.generic_insert(self.head_node.prev, DCDS_node(mS), self.head_node)


    def remove_set(self, mS: Set): 
        run = self.head_node.next 
        while run != self.head_node: 
            if run.mS == mS: 
                break 
            run = run.next
        else: 
            raise ValueError("Bad Set") 

        run.mS.destroy() 
        DCDS.generic_delete(run)


    def make_set(self, x: int): 
        run = self.head_node.next 
        while run != self.head_node: 
            if x in run.mS: 
                raise ElementExistsError(f'{x} exists in DCDS')
            run = run.next 
        self.insert_end(Set(x))

    
    def union(self, u: int, v: int) -> None: 
        uS = self.find_set(u)
        vS = self.find_set(v)
        if uS is None or vS is None: 
            raise ValueError(f"Either {u} or {v} are not in DCDS")
        uS.append(vS)
        self.remove_set(vS)
        

    def find_set(self, x: int) -> Set: 
        run = self.head_node.next 
        while run != self.head_node: 
            if x in run.mS: 
                return run.mS
            run = run.next 
        return None 
    

    def show(self): 
        run1 = self.head_node.next 
        while run1 != self.head_node: 
            print(f"SET:REPRESENTATIVE:[{run1.mS.representative_element}]##ELEMENTS->", end='')
            run2 = run1.mS.head_node.next 
            while run2 != run1.mS.head_node: 
                print(f"[{run2.n}]->", end='')
                run2 = run2.next
            print("[END]")
            run1 = run1.next


if __name__ == '__main__':
    G  = {
        'V': [1, 2, 3, 4, 5, 6, 7, 8, 9], 
        'E': [
                (1, 2), (2, 3), (3, 4), (4, 1), 
                (5, 6), (6, 7), (7, 5), (8, 9)
            ]
    }

    D = DCDS() 
    for v in G['V']: 
        D.make_set(v)

    for (u, v) in G['E']: 
        uS = D.find_set(u)
        vS = D.find_set(v)
        if uS != vS: 
            D.union(u, v)

    D.show() 
