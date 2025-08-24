#include <iostream> 
#include <stdexcept>
#include <cstdlib> 
#include <cstring> 
#include <cassert> 

// graph exceptions 
class vertex_invalid_error : public std::runtime_error{
    public: 
        vertex_invalid_error(const char* msg) : std::runtime_error(msg){
        }
};  

class edge_invalid_error : public std::runtime_error{
    public: 
        edge_invalid_error(const char* msg) : std::runtime_error(msg){
        }
}; 

class vertex_exists_error : public std::runtime_error{
    public: 
        vertex_exists_error(const char* msg) : std::runtime_error(msg){
        }
}; 

class edge_exists_error : public std::runtime_error{
    public: 
        edge_exists_error(const char* msg) : std::runtime_error(msg){
        }
}; 

class graph_inconsistent_error : public std::runtime_error{
    public: 
        graph_inconsistent_error(const char* msg) : std::runtime_error(msg){
        }
}; 

typedef enum color{
    WHITE=1, 
    GRAY, 
    BLACK
}color_t; 

class edge{
    public: 
        int v_start; 
        int v_end; 
        double w;
        edge(int _v_start, int _v_end, double _w=0.0) : v_start(_v_start), 
                                                        v_end(_v_end), 
                                                        w(_w){
        }                                             
}; 

class hnode{
    friend class vnode; 
    friend class vlist; 
    friend class hlist; 
    friend class graph; 
    friend std::ostream& operator<<(std::ostream& os, const graph& g);
    private: 
        int v; 
        vnode* pv; 
        double w; 
        hnode* prev; 
        hnode* next; 

        hnode(int _v, vnode* _pv, double _w) :  v(_v), pv(_pv), w(_w), 
                                                prev(0), next(0){
        }

        hnode() : v(-1), pv(0), w(0.0), prev(0), next(0){

        }
}; 

class hlist{
    friend class vnode; 
    friend class vlist; 
    friend class graph; 
    friend std::ostream& operator<<(std::ostream& os, const graph& g);
    private: 
        hnode* head_node; 
        
        static void generic_insert(hnode* beg, hnode* mid, hnode* end){
            mid->next = end; 
            mid->prev = beg; 
            beg->next = mid; 
            end->prev = mid; 
        }

        static void generic_delete(hnode* delete_node){
            delete_node->prev->next = delete_node->next; 
            delete_node->next->prev = delete_node->prev; 
            delete delete_node; 
        }

        hnode* search_node(int v){
            for(hnode* run = head_node->next; run != head_node; run = run->next)
                if(run->v == v)
                    return (run); 
            return (0); 
        }

        hlist() : head_node(new hnode(0, 0, 0.0)){
            head_node->prev = head_node; 
            head_node->next = head_node; 
        } 

    public: 
        ~hlist(){
            hnode* run; 
            hnode* run_next; 

            for(run = head_node->next; run != head_node; run = run_next){
                run_next = run->next; 
                delete run; 
            }

            delete head_node; 
            head_node = 0; 
        }

        void insert_end(int v, vnode* pv, double w=0.0){
            generic_insert(head_node->prev, new hnode(v, pv, w), head_node); 
        }

        void remove_vertex(int v){
            hnode* delete_node = search_node(v); 
            if(delete_node == 0)
                throw vertex_invalid_error("hlist::remove_vertex():invalid vertex"); 
            generic_delete(delete_node); 
        }
}; 

class vnode{
    friend class vlist; 
    friend class graph; 
    friend std::ostream& operator<<(std::ostream& os, const graph& g); 
    private: 
        int v; 
        hlist* h_list; 
        color_t color; 

        vnode* pred_vertex; 
        double prio_field; 

        vnode* prev; 
        vnode* next; 

        vnode(int _v, bool is_hlist=true) : v(_v), color(WHITE), 
                                            pred_vertex(0), prio_field(0.0), 
                                            prev(0), next(0){
            if(is_hlist == true)
                h_list = new hlist; 
        }
}; 

class vlist{
    friend class graph; 
    friend std::ostream& operator<<(std::ostream& os, const graph& g); 
    private: 
        vnode* head_node; 

        static void generic_insert(vnode* beg, vnode* mid, vnode* end){
            mid->next = end; 
            mid->prev = beg; 
            beg->next = mid; 
            end->prev = mid; 
        }

        static void generic_delete(vnode* delete_node){
            delete_node->prev->next = delete_node->next; 
            delete_node->next->prev = delete_node->prev; 
            delete delete_node; 
        }

        vnode* search_node(int v) const{
            for(vnode* run = head_node->next; run != head_node; run = run->next)
                if(run->v == v)
                    return run; 
            return 0; 
        }

        vlist() : head_node(new vnode(0, false)){
            head_node->prev = head_node; 
            head_node->next = head_node; 
        }

    public: 
        void insert_end(int v){
            generic_insert(head_node->prev, new vnode(v), head_node); 
        }

        bool does_vertex_exist(int v) const {
            vnode* vnode = search_node(v); 
            return (vnode != 0); 
        }
}; 

class graph{
    friend std::ostream& operator<<(std::ostream& os, const graph& g); 
    private: 
        vlist* v_list; 
        size_t nr_vertices; 
        size_t nr_edges; 
    public: 
        static void test_graph(void){
            edge E[] = {
                edge(1, 2), edge(2, 3), edge(3, 4), edge(4, 5), 
                edge(5, 6), edge(6, 7), edge(7, 8), edge(8, 1), 
                edge(2, 5), edge(6, 2), edge(4, 7), edge(1, 6), 
                edge(3, 8), edge(7, 3), edge(1, 5), edge(2, 7)
            }; 

            try{
                graph* g = new graph; 
                for(int v = 1; v <= 8; ++v)
                    g->add_vertex(v);  
                for(size_t i = 0; i < sizeof(E)/sizeof(E[0]); ++i)
                   g->add_edge(E[i].v_start, E[i].v_end); 
                std::cout << "GRAPH INITIAL STATE:" << std::endl << *g; 

                g->remove_edge(2, 3); 
                g->remove_edge(4, 7); 
                g->remove_edge(1, 8); 
             
                std::cout << "GRAPH AFTER REMOVING EDGES (2, 3), (4, 7), (1, 8):"
                            << std::endl << *g; 

                g->remove_vertex(2); 
                g->remove_vertex(3); 

                std::cout << "GRAPH AFTER REMOVING VERTICES 2, 3" << std::endl << *g; 
                
                delete g; 
                g = 0; 
            }catch(const std::exception& e){
                std::cout << e.what() << std::endl; 
                exit(EXIT_FAILURE); 
            }
        }

        graph() : v_list(new vlist), nr_vertices(0), nr_edges(0){
            
        }

        ~graph(){
            vnode* run; 
            vnode* run_next;
            for(
                run = v_list->head_node->next; 
                run != v_list->head_node; 
                run = run_next
            ){
                run_next = run->next; 
                delete run->h_list;
            }

            delete v_list->head_node; 
        }

        // advanced consideration -> copy control 
        graph(const graph&) = delete; 
        graph& operator=(const graph&) = delete; 

        void add_vertex(int v){
            if(v_list->does_vertex_exist(v) == true)
                throw vertex_exists_error("add_vertex():vertex exists"); 
            v_list->insert_end(v); 

            nr_vertices += 1; 
        }

        void remove_vertex(int v){
            vnode* pv = v_list->search_node(v); 
            if(pv == 0)
                throw vertex_invalid_error("graph::remove_vertex():invalid vertex"); 
            
         
            for(
                hnode* run = pv->h_list->head_node->next; 
                run != pv->h_list->head_node; 
                run = run->next
            ){
                run->pv->h_list->remove_vertex(v); 
                nr_edges -= 1; 
            }
            delete pv->h_list; 
            vlist::generic_delete(pv); 
            nr_vertices -= 1; 
        }

        void add_edge(int v_start, int v_end, double w = 0.0){
            if(v_start == v_end)
                throw vertex_invalid_error("add_edge():self is not allowed"); 

            vnode* pv_start = v_list->search_node(v_start); 
            if(pv_start == 0)
                throw vertex_invalid_error("add_edge():v_start invalid"); 

            vnode* pv_end = v_list->search_node(v_end); 
            if(pv_end == 0)
                throw vertex_invalid_error("add_edge():v_end invalid"); 

            pv_start->h_list->insert_end(v_end, pv_end, w);
            pv_end->h_list->insert_end(v_start, pv_start, w); 

            nr_edges += 1; 
        }

        void remove_edge(int v_start, int v_end){
            vnode* pv_start = v_list->search_node(v_start); 
            if(pv_start == 0)
                throw vertex_invalid_error("remove_edge():graph inconsistent"); 

            vnode* pv_end = v_list->search_node(v_end); 
            if(pv_end == 0)
                throw graph_inconsistent_error("remove_edge():graph inconsistent"); 

            pv_start->h_list->remove_vertex(v_end); 
            pv_end->h_list->remove_vertex(v_start); 

            nr_edges -= 1; 
        }
}; 

std::ostream& operator<<(std::ostream& os, const graph& g){
    os  << "|G.V|=" << g.nr_vertices << std::endl 
        << "|G.E|=" << g.nr_edges << std::endl; 
    for(
        vnode* v_run = g.v_list->head_node->next; 
        v_run != g.v_list->head_node; 
        v_run = v_run->next
    ){
        os << "["<< v_run->v <<"]\t<->\t"; 
        for(
            hnode* h_run = v_run->h_list->head_node->next; 
            h_run != v_run->h_list->head_node; 
            h_run = h_run->next
        ){
            os << "[" << h_run->v <<"]<->"; 
        }
        os << "[END]" << std::endl; 
    } 

    return os; 
}

int main(void){
    graph::test_graph(); 
    return 0; 
}