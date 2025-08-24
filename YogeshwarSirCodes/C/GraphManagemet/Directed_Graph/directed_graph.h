#ifndef _DIRECTED_GRAPH_H 
#define _DIRECTED_GRAPH_H 

#define SUCCESS 1 
#define G_INVALID_VERTEX 2 
#define G_INVALID_EDGE 3 
#define G_VERTEX_EXISTS 4 
#define G_EDGE_EXISTS 5 
#define G_INCONSISTENT 6 
#define G_NEGATIVE_PATH_CYCLE 7 

typedef int vertex_t; 
typedef int status_t; 
typedef enum color color_t; 
typedef struct hnode hnode_t; 
typedef hnode_t hlist_t; 
typedef struct vnode vnode_t; 
typedef vnode_t vlist_t; 
typedef struct edge_node edgenode_t; 
typedef edgenode_t edgelist_t; 
typedef struct graph graph_t; 

enum color{
    WHITE = 0, 
    GRAY, 
    BLACK
}; 

struct hnode{
    vertex_t v; 
    vnode_t* pv; 
    double w; 

    struct hnode* prev; 
    struct hnode* next; 
}; 

struct vnode{
    vertex_t v; 
    hlist_t* ph_list; 
    color_t color; 
    double d; 
    struct vnode* pred_vertex; 

    struct vnode* prev; 
    struct vnode* next; 
}; 

struct edge_node{
    vnode_t* pv_start;
    vnode_t* pv_end; 
    double w; 

    struct edge_node* prev; 
    struct edge_node* next; 
}; 

struct graph{
    vlist_t* pv_list; 
    unsigned int nr_vertices; 
    unsigned int nr_edges; 
};  

/* Directed Graph -> Interface Routines */
graph_t* create_graph(void); 
status_t add_vertex(graph_t* g, vertex_t v); 
status_t add_edge(graph_t* g, vertex_t v_start, vertex_t v_end, double w); 
status_t remove_vertex(graph_t* g, vertex_t v); 
status_t remove_edge(graph_t* g, vertex_t v_start, vertex_t v_end); 
void show_graph(graph_t* g, const char* msg); 
status_t get_edge_list(graph_t* g, edgelist_t** pp_list); 
void show_edge_list(edgelist_t* p_edge_list); 
status_t release_edge_list(edgelist_t** pp_list); 
status_t destroy_graph(graph_t** pp_g); 

/* Edge List Management Routines */
edgelist_t* e_create_list(void); 
status_t e_insert_end(
            edgelist_t* p_edge_list, 
            vnode_t* pv_start, 
            vnode_t* pv_end, 
            double w
        ); 
void e_generic_insert(edgenode_t* beg, edgenode_t* mid, edgenode_t* end); 
edgenode_t* e_get_node(vnode_t* pv_start, vnode_t* pv_end, double w); 

/* Vertical List Management Routines */
vlist_t* v_create_list(void); 
status_t v_insert_end(vlist_t* pv_list, vertex_t v); 
void v_generic_insert(vnode_t* beg, vnode_t* mid, vnode_t* end); 
void v_generic_delete(vnode_t* delete_node); 
vnode_t* v_search_node(vlist_t* pv_list, vertex_t v); 
vnode_t* v_get_node(vertex_t v); 

/* Horizontal List Management Routines */

hlist_t* h_create_list(void); 
status_t h_insert_end(hlist_t* ph_list, vertex_t v, vnode_t* pv, double w); 
status_t h_destroy_list(hlist_t** ph_list); 
void h_generic_insert(hnode_t* beg, hnode_t* mid, hnode_t* end); 
void g_generic_delete(hnode_t* delete_node); 
hnode_t* h_search_node(hlist_t* ph_list, vertex_t v); 
hnode_t* h_get_node(vertex_t v, vnode_t* pv, double w); 

/* Auxillary Routines */
void* xmalloc(size_t size_in_bytes); 

#endif 