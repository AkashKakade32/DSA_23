#include <stdio.h>
#include <stdlib.h>

// hnode for adjacency list
typedef struct hnode {
    int v;
    struct hnode *next, *prev;
} hnode;

// Adjacency list (hlist)
typedef struct hlist {
    hnode *head;
} hlist;

hnode* createHNode(int v) {
    hnode* newNode = (hnode*)malloc(sizeof(hnode));
    newNode->v = v;
    newNode->next = newNode->prev = NULL;
    return newNode;
}

void hlistInit(hlist* list) {
    list->head = createHNode(-1);  // Dummy node
    list->head->next = list->head;
    list->head->prev = list->head;
}

void hlistInsertEnd(hlist* list, int v) {
    hnode* newNode = createHNode(v);
    hnode* tail = list->head->prev;

    newNode->next = list->head;
    newNode->prev = tail;

    tail->next = newNode;
    list->head->prev = newNode;
}

hnode* hlistSearch(hlist* list, int v) {
    hnode* run = list->head->next;
    while (run != list->head) {
        if (run->v == v) return run;
        run = run->next;
    }
    return NULL;
}

void hlistDelete(hnode* node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
    free(node);
}

// vnode for vertex list
typedef struct vnode {
    int v;
    hlist adjList;
    struct vnode *next, *prev;
} vnode;

// Vertex list (vlist)
typedef struct vlist {
    vnode* head;
} vlist;

vnode* createVNode(int v) {
    vnode* newNode = (vnode*)malloc(sizeof(vnode));
    newNode->v = v;
    hlistInit(&newNode->adjList);
    newNode->next = newNode->prev = NULL;
    return newNode;
}

void vlistInit(vlist* list) {
    list->head = createVNode(-1);  // Dummy node
    list->head->next = list->head;
    list->head->prev = list->head;
}

void vlistInsertEnd(vlist* list, int v) {
    vnode* newNode = createVNode(v);
    vnode* tail = list->head->prev;

    newNode->next = list->head;
    newNode->prev = tail;

    tail->next = newNode;
    list->head->prev = newNode;
}

vnode* vlistSearch(vlist* list, int v) {
    vnode* run = list->head->next;
    while (run != list->head) {
        if (run->v == v) return run;
        run = run->next;
    }
    return NULL;
}

void vlistDelete(vnode* node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
    free(node);
}

// Graph
typedef struct graph {
    vlist vList;
} graph;

void initGraph(graph* g) {
    vlistInit(&g->vList);
}

void addVertex(graph* g, int v) {
    if (vlistSearch(&g->vList, v) != NULL) {
        printf("Vertex %d already exists\n", v);
        return;
    }
    vlistInsertEnd(&g->vList, v);
}

void addEdge(graph* g, int vStart, int vEnd) {
    vnode* vStartNode = vlistSearch(&g->vList, vStart);
    vnode* vEndNode = vlistSearch(&g->vList, vEnd);

    if (!vStartNode || !vEndNode) {
        printf("Invalid edge %d - %d\n", vStart, vEnd);
        return;
    }

    if (hlistSearch(&vStartNode->adjList, vEnd) != NULL) {
        printf("Edge %d - %d already exists\n", vStart, vEnd);
        return;
    }

    hlistInsertEnd(&vStartNode->adjList, vEnd);
    hlistInsertEnd(&vEndNode->adjList, vStart);
}

void removeEdge(graph* g, int vStart, int vEnd) {
    vnode* vStartNode = vlistSearch(&g->vList, vStart);
    vnode* vEndNode = vlistSearch(&g->vList, vEnd);

    if (!vStartNode || !vEndNode) return;

    hnode* h1 = hlistSearch(&vStartNode->adjList, vEnd);
    hnode* h2 = hlistSearch(&vEndNode->adjList, vStart);

    if (!h1 || !h2) return;

    hlistDelete(h1);
    hlistDelete(h2);
}

void removeVertex(graph* g, int v) {
    vnode* rNode = vlistSearch(&g->vList, v);
    if (!rNode) return;

    hnode* run = rNode->adjList.head->next;
    while (run != rNode->adjList.head) {
        hnode* next = run->next;

        vnode* neighbor = vlistSearch(&g->vList, run->v);
        if (neighbor) {
            hnode* backEdge = hlistSearch(&neighbor->adjList, v);
            if (backEdge) hlistDelete(backEdge);
        }
        hlistDelete(run);
        run = next;
    }

    free(rNode->adjList.head); // Free dummy node
    vlistDelete(rNode);
}

void printGraph(graph* g) {
    vnode* vRun = g->vList.head->next;
    while (vRun != g->vList.head) {
        printf("[%d] -> ", vRun->v);
        hnode* hRun = vRun->adjList.head->next;
        while (hRun != vRun->adjList.head) {
            printf("[%d] -> ", hRun->v);
            hRun = hRun->next;
        }
        printf("[END]\n");
        vRun = vRun->next;
    }
}

void freeGraph(graph* g) {
    vnode* vRun = g->vList.head->next;
    while (vRun != g->vList.head) {
        vnode* nextV = vRun->next;

        hnode* hRun = vRun->adjList.head->next;
        while (hRun != vRun->adjList.head) {
            hnode* nextH = hRun->next;
            free(hRun);
            hRun = nextH;
        }

        free(vRun->adjList.head); // dummy node
        free(vRun);
        vRun = nextV;
    }

    free(g->vList.head); // dummy vertex node
}

int main() {
    graph g;
    initGraph(&g);

    for (int i = 0; i < 8; i++)
        addVertex(&g, i);

    int edges[][2] = {
        {0,1},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,0},
        {1,6},{6,3},{5,2},{7,2}
    };
    int numEdges = sizeof(edges)/sizeof(edges[0]);

    for (int i = 0; i < numEdges; i++)
        addEdge(&g, edges[i][0], edges[i][1]);

    printf("Graph:\n");
    printGraph(&g);

    removeEdge(&g, 2, 3);
    removeEdge(&g, 5, 6);
    printf("\nAfter removing edges:\n");
    printGraph(&g);

    removeVertex(&g, 2);
    removeVertex(&g, 5);
    printf("\nAfter removing vertices:\n");
    printGraph(&g);

    freeGraph(&g);

    return 0;
}
