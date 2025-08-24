#include <stdio.h> 
#include <stdlib.h> 
#include <math.h> 
#include <assert.h>
#include "directed_graph.h"

/* Directed Graph -> Interface Routines */
graph_t* create_graph(void){
    graph_t* g = NULL; 

    g = (graph_t*)xmalloc(sizeof(graph_t)); 
    g->pv_list = v_create_list(); 
    g->nr_vertices = 0; 
    g->nr_edges = 0; 

    return (g); 
}

status_t add_vertex(graph_t* g, vertex_t v){
    vnode_t* pv_node = NULL; 
    status_t status; 

    pv_node = v_search_node(g->pv_list, v); 
    if(pv_node != NULL)
        return (G_VERTEX_EXISTS); 

    status = v_insert_end(g->pv_list, v);
    assert(status == SUCCESS); 
    g->nr_vertices += 1; 

    return (SUCCESS);  
}

status_t add_edge(graph_t* g, vertex_t v_start, vertex_t v_end, double w){
    vnode_t* pv_start = NULL; 
    vnode_t* pv_end = NULL; 
    status_t status; 

    pv_start = v_search_node(g->pv_list, v_start); 
    if(pv_start == NULL)
        return (G_INVALID_VERTEX); 

    pv_end = v_search_node(g->pv_list, v_end); 
    if(pv_end == NULL)
        return (G_INVALID_VERTEX); 

    status = h_insert_end(pv_start->ph_list, v_end, pv_end, w);
    assert(status == SUCCESS); 
    g->nr_edges += 1; 

    return (SUCCESS); 
}

status_t remove_vertex(graph_t* g, vertex_t v){
    vnode_t* pv_node = NULL; 
    hnode_t* ph_run = NULL; 
    hnode_t* ph_run_next = NULL; 

    pv_node = v_search_node(g->pv_list, v); 
    if(pv_node == NULL)
        return (G_INVALID_VERTEX); 

    for(ph_run = pv_node->ph_list->next; 
        ph_run != pv_node->ph_list; 
        ph_run = ph_run_next){
        ph_run_next = ph_run->next; 
        free(ph_run); 
        g->nr_edges -= 1; 
    }

    free(pv_node->ph_list); 
    v_generic_delete(pv_node); 
    g->nr_vertices -= 1; 

    return (SUCCESS); 
}

status_t remove_edge(graph_t* g, vertex_t v_start, vertex_t v_end){
    vnode_t* pv_start = NULL; 
    hnode_t* ph_node = NULL;

    pv_start = v_search_node(g->pv_list, v_start); 
    if(pv_start == NULL)
        return (G_INVALID_VERTEX); 
    
    ph_node = h_search_node(pv_start->ph_list, v_end); 
    if(ph_node == NULL)
        return (G_INVALID_EDGE); 

    g_generic_delete(ph_node); 
    g->nr_edges -= 1; 

    return (SUCCESS); 
}

void show_graph(graph_t* g, const char* msg){
    vnode_t* pv_run = NULL; 
    hnode_t* ph_run = NULL; 

    if(msg)
        puts(msg); 

    printf(
        "DIRECTED GRAPH G:|G.V|=%u, |G.E|=%u\n", 
        g->nr_vertices, 
        g->nr_edges
    ); 

    for(
        pv_run = g->pv_list->next; 
        pv_run != g->pv_list; 
        pv_run = pv_run->next
    )
    {
        printf("[%d]\t->\t", pv_run->v); 
        for(
            ph_run = pv_run->ph_list->next;
            ph_run != pv_run->ph_list; 
            ph_run = ph_run->next
        ){
            printf("[%d]<->", ph_run->v); 
        }
        puts("[END]"); 
    }
}

status_t get_edge_list(graph_t* g, edgelist_t** pp_list){
    vnode_t* pv_run = NULL; 
    hnode_t* ph_run = NULL; 
    edgelist_t* p_edge_list = NULL; 
    status_t status; 

    p_edge_list = e_create_list(); 

    for(
        pv_run = g->pv_list->next; 
        pv_run != g->pv_list; 
        pv_run = pv_run->next
    ){
        for(
            ph_run = pv_run->ph_list->next; 
            ph_run != pv_run->ph_list; 
            ph_run = ph_run->next)
            {
                status = e_insert_end(p_edge_list, pv_run, ph_run->pv, ph_run->w); 
                assert(status == SUCCESS); 
        }
    }

    *pp_list = p_edge_list; 
    return (SUCCESS); 
}

void show_edge_list(edgelist_t* p_edge_list){
    edgenode_t* pe_run = NULL; 

    puts("--------[START EDGE LIST]--------");
    for(
        pe_run = p_edge_list->next; 
        pe_run != p_edge_list; 
        pe_run = pe_run->next
    ){
        printf("{[%d]->[%d]|%.3lf}\n", pe_run->pv_start->v, pe_run->pv_end->v, pe_run->w); 
    }
    puts("--------[END EDGE LIST]--------"); 
}

status_t release_edge_list(edgelist_t** pp_list){
    edgelist_t* p_edge_list = NULL; 
    edgenode_t* pe_run = NULL; 
    edgenode_t* pe_run_next = NULL; 
    
    p_edge_list = *pp_list; 
    for(pe_run = p_edge_list->next; pe_run != p_edge_list; pe_run = pe_run_next){
        pe_run_next = pe_run->next; 
        free(pe_run); 
    }

    free(p_edge_list); 
    *pp_list = NULL; 

    return (SUCCESS);
}

status_t destroy_graph(graph_t** pp_g){
    graph_t* g = NULL; 
    vnode_t* pv_run = NULL; 
    vnode_t* pv_run_next = NULL; 
    status_t status; 

    g = *pp_g; 

    for(
        pv_run = g->pv_list->next; 
        pv_run != g->pv_list; 
        pv_run = pv_run_next
    ){
        pv_run_next = pv_run->next; 
        status = h_destroy_list(&pv_run->ph_list); 
        assert(status==SUCCESS); 
    }

    free(g->pv_list); 
    free(g); 

    *pp_g = NULL; 
    
    return (SUCCESS); 
}

edgelist_t* e_create_list(void){
    edgelist_t* p_edge_list = NULL; 

    p_edge_list = (edgelist_t*)xmalloc(sizeof(edgelist_t)); 
    p_edge_list->pv_start = NULL; 
    p_edge_list->pv_end = NULL; 
    p_edge_list->w = 0.0; 
    p_edge_list->prev = p_edge_list; 
    p_edge_list->next = p_edge_list; 

    return (p_edge_list); 
}

status_t e_insert_end(
            edgelist_t* p_edge_list, 
            vnode_t* pv_start,
            vnode_t* pv_end, 
            double w
        ){
    e_generic_insert(p_edge_list->prev, e_get_node(pv_start, pv_end, w), p_edge_list); 
    return (SUCCESS); 
}

void e_generic_insert(edgenode_t* beg, edgenode_t* mid, edgenode_t* end){
    mid->next = end; 
    mid->prev = beg; 
    beg->next = mid; 
    end->prev = mid; 
}

edgenode_t* e_get_node(vnode_t* pv_start, vnode_t* pv_end, double w){
    edgenode_t* p_edge = NULL; 

    p_edge = (edgenode_t*)xmalloc(sizeof(edgenode_t)); 
    p_edge->pv_start = pv_start; 
    p_edge->pv_end = pv_end; 
    p_edge->w = w; 

    return (p_edge); 
}

/* Vertical List Management Routines */
vlist_t* v_create_list(void){
    vlist_t* pv_new_list = NULL; 

    pv_new_list = (vnode_t*)xmalloc(sizeof(vnode_t)); 
    pv_new_list->v = -1; 
    pv_new_list->ph_list = NULL; 
    pv_new_list->color = WHITE; 
    pv_new_list->d = INFINITY; 
    pv_new_list->pred_vertex = NULL; 

    pv_new_list->prev = pv_new_list; 
    pv_new_list->next = pv_new_list; 

    return (pv_new_list); 
}

status_t v_insert_end(vlist_t* pv_list, vertex_t v){
    v_generic_insert(pv_list->prev, v_get_node(v), pv_list); 
    return (SUCCESS); 
}

void v_generic_insert(vnode_t* beg, vnode_t* mid, vnode_t* end){
    mid->next = end; 
    mid->prev = beg; 
    beg->next = mid; 
    end->prev = mid; 
}

void v_generic_delete(vnode_t* delete_node){
    delete_node->prev->next = delete_node->next; 
    delete_node->next->prev = delete_node->prev; 
    free(delete_node); 
}

vnode_t* v_search_node(vlist_t* pv_list, vertex_t v){
    vnode_t* pv_run = NULL; 

    for(pv_run = pv_list->next; pv_run != pv_list; pv_run = pv_run->next)
        if(pv_run->v == v)
            return (pv_run); 

    return (NULL); 
}

vnode_t* v_get_node(vertex_t v){
    vnode_t* pv_new_node = NULL; 

    pv_new_node = (vnode_t*)xmalloc(sizeof(vnode_t)); 
    pv_new_node->v = v; 
    pv_new_node->ph_list = h_create_list(); 
    pv_new_node->color = WHITE; 
    pv_new_node->d = INFINITY; 
    pv_new_node->pred_vertex = NULL; 

    return (pv_new_node); 
}

/* Horizontal List Management Routines */

hlist_t* h_create_list(void){
    hlist_t* ph_list = NULL; 

    ph_list = h_get_node(-1, NULL, 0.0); 
    ph_list->prev = ph_list; 
    ph_list->next = ph_list; 

    return (ph_list); 
}

status_t h_insert_end(hlist_t* ph_list, vertex_t v, vnode_t* pv, double w){
    h_generic_insert(ph_list->prev, h_get_node(v, pv, w), ph_list);
    return (SUCCESS);  
}

status_t h_destroy_list(hlist_t** pph_list){
    hlist_t* ph_list = NULL; 
    hnode_t* ph_run = NULL; 
    hnode_t* ph_run_next = NULL; 

    ph_list = *pph_list; 
    for(ph_run = ph_list->next; ph_run != ph_list; ph_run = ph_run_next){
        ph_run_next = ph_run->next; 
        free(ph_run); 
    }

    free(ph_list); 
    *pph_list = NULL; 

    return (SUCCESS); 
}

void h_generic_insert(hnode_t* beg, hnode_t* mid, hnode_t* end){
    mid->next = end; 
    mid->prev = beg; 
    beg->next = mid; 
    end->prev = mid; 
}

void g_generic_delete(hnode_t* delete_node){
    delete_node->prev->next = delete_node->next; 
    delete_node->next->prev = delete_node->prev; 
    free(delete_node); 
}

hnode_t* h_search_node(hlist_t* ph_list, vertex_t v){
    hnode_t* ph_run = NULL; 

    for(ph_run = ph_list->next; ph_run != ph_list; ph_run = ph_run->next) 
        if(ph_run->v == v)
            return (ph_run); 

    return (NULL); 
}

hnode_t* h_get_node(vertex_t v, vnode_t* pv, double w){
    hnode_t* ph_new_node = NULL; 

    ph_new_node = (hnode_t*)xmalloc(sizeof(hnode_t)); 
    ph_new_node->v = v; 
    ph_new_node->pv = pv; 
    ph_new_node->w = w; 

    return (ph_new_node); 
}

/* Auxillary Routines */
void* xmalloc(size_t size_in_bytes){
    void* ptr = NULL; 

    ptr = malloc(size_in_bytes); 
    if(ptr == NULL){
        fprintf(stderr, "fatal:out of memory\n"); 
        exit(EXIT_FAILURE); 
    }

    return (ptr); 
}