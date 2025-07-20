#include<stdio.h>
#include<stdlib.h>

static int countMemory = 0;

typedef struct hnode{
    int data;
    struct hnode *next;
    struct hnode *prev;
}hNode;

typedef struct hlist{
    hNode *headNode;
}hList;

hNode *hListCreateNode(int v)
{
    hNode *newNode = (hNode *)malloc(sizeof(hNode));

    if(newNode == NULL)
    {
        printf("Failed to allocate the memory to the hNode \n");
        exit(EXIT_FAILURE);
    }

    newNode->data = v;
    newNode->next = NULL;
    newNode->prev = NULL;

    countMemory++;

    return(newNode);
}

void hListInit(hList *list)
{
    list->headNode = hListCreateNode(-1); //Dummy node data

    list->headNode->next = list->headNode;
    list->headNode->prev = list->headNode;
}

void hListInsertEnd(hList *list, int v)
{
    hNode *newNode = hListCreateNode(v);

    newNode->next = list->headNode;
    newNode->prev = list->headNode->prev;

    list->headNode->prev->next = newNode;
    list->headNode->prev = newNode;
}

hNode *hListSearchNode(hList *list, int searchData)
{
    hNode *run = list->headNode->next;

    while(run != list->headNode)
    {
        if(run->data == searchData)
        {
            return(run);
        }

        run = run->next;
    }

    return(NULL);
}

void hListDeleteNode(hNode *rNode)
{
    rNode->prev->next = rNode->next;
    rNode->next->prev = rNode->prev;

    free(rNode);
    rNode = NULL;
    countMemory--;
}

typedef struct vnode{
    int data;
    hList adjList;

    struct vnode *next;
    struct vnode *prev;
}vNode;

typedef struct vlist{
    vNode *headNode;
}vList;

vNode *vListCreateNode(int v)
{
    vNode *newNode = (vNode *)malloc(sizeof(vNode));

    if(newNode == NULL)
    {
        printf("Failed to allocate the memory to the vNode \n");
        exit(EXIT_FAILURE);
    }

    newNode->data = v;
    newNode->next = NULL;
    newNode->prev = NULL;

    hListInit(&newNode->adjList);

    countMemory++;

    return(newNode);
}

void vListInit(vList *list)
{
    list->headNode = vListCreateNode(-1);

    list->headNode->next = list->headNode;
    list->headNode->prev = list->headNode;
}

void vListInsertEnd(vList *list, int v)
{
    vNode *newNode = vListCreateNode(v);

    newNode->next = list->headNode;
    newNode->prev = list->headNode->prev;

    list->headNode->prev->next = newNode;
    list->headNode->prev = newNode;
}

vNode *vListSearchNode(vList *list, int searchData)
{
    vNode *run = list->headNode->next;

    while(run != list->headNode)
    {
        if(run->data == searchData)
        {
            return(run);
        }

        run = run->next;
    }

    return(NULL);

}

void vListDeleteNode(vNode *rNode)
{
    rNode->prev->next = rNode->next;
    rNode->next->prev = rNode->prev;

    free(rNode);
    rNode = NULL;
    countMemory--;
}

typedef struct graph{
    vList verticalList;
}Graph;

void initGraph(Graph *g)
{
    vListInit(&g->verticalList);
}

void addVertex(Graph *g, int v)
{
    if(vListSearchNode(&g->verticalList, v) != NULL)
    {
        printf("Vertex %d is already present in the Graph \n", v);
        return;
    }

    vListInsertEnd(&g->verticalList, v);
}

void addEdge(Graph *g, int startData, int endData)
{
    vNode *vRunStart = vListSearchNode(&g->verticalList, startData);

    if(vRunStart == NULL)
    {
        printf("Vertex %d is not present in the Graph \n", startData);
        return;
    }

    vNode *vRunEnd = vListSearchNode(&g->verticalList, endData);

    if(vRunEnd == NULL)
    {
        printf("Vertex %d is not present in the Graph \n", endData);
        return;
    }

    if(hListSearchNode(&vRunStart->adjList, endData) != NULL)
    {
        printf("Edge is alredy prsent between %d - %d \n", startData, endData);
        return;
    }

    hListInsertEnd(&vRunStart->adjList, endData);
    hListInsertEnd(&vRunEnd->adjList, startData);
}

void removeEdge(Graph *g, int startData, int endData)
{
    vNode *vRunStart = vListSearchNode(&g->verticalList, startData);
    if(vRunStart == NULL)
    {
        printf("Vertex %d is not available in the Graph \n", startData);
        return;
    }

    vNode *vRunEnd = vListSearchNode(&g->verticalList, endData);
    if(vRunEnd == NULL)
    {
        printf("Vertex %d is not available in the Graph \n", endData);
        return;
    }

    hNode *hRunStart = hListSearchNode(&vRunStart->adjList, endData);
    if(hRunStart == NULL)
    {
        printf("Edge Between %d and %d is not present in the Graph \n", endData, startData);
        return;
    }

    hNode *hRunEnd = hListSearchNode(&vRunEnd->adjList, startData);
    if(hRunEnd == NULL)
    {
        printf("Edge between %d and %d is not present in the Graph \n", startData, endData);
        return;
    }

    hListDeleteNode(hRunStart);
    hListDeleteNode(hRunEnd);
}

void removeVertex(Graph *g, int vertex)
{
    vNode *vRun = vListSearchNode(&g->verticalList, vertex);

    if(vRun == NULL)
    {
        printf("Vertex V is not present in the Graph \n", vertex);
        return;
    }

    hNode *hRun = vRun->adjList.headNode->next;

    while(hRun != vRun->adjList.headNode)
    {
        hNode *hRunNext = hRun->next;

        vNode *vInHRun = vListSearchNode(&g->verticalList, hRun->data);
        hNode *hInVHRun = hListSearchNode(&vInHRun->adjList, vRun->data);
        
        hListDeleteNode(hInVHRun);
        hListDeleteNode(hRun);

        hRun = hRunNext;
    }

    hListDeleteNode(vRun->adjList.headNode);

    vListDeleteNode(vRun);
}

void printGraph(Graph *g)
{
    vNode *vRun = g->verticalList.headNode->next;

    while(vRun != g->verticalList.headNode)
    {
        hNode *hRun = vRun->adjList.headNode->next;

        printf("[%d]\t-->\t", vRun->data);
        while(hRun != vRun->adjList.headNode)
        {
            printf("[%d]-->", hRun->data);
            hRun = hRun->next;
        }

        printf("[END] \n");

        vRun = vRun->next;
    }
}

void freeGraph(Graph *g)
{
    int memoryCount = 0;

    vNode *vRun = g->verticalList.headNode->next;

    while(vRun != g->verticalList.headNode)
    {
        vNode *vRunNext = vRun->next;

        hNode *hRun = vRun->adjList.headNode->next;

        //printf("[%p]\t-->\t", (void *)vRun);

        while(hRun != vRun->adjList.headNode)
        {
            hNode *hRunNext = hRun->next;
            //printf("[%p]-->", (void *)hRun);
            free(hRun);
            memoryCount++;
            hRun = NULL;
            hRun = hRunNext;
        }
        free(vRun->adjList.headNode);
        memoryCount++;
        vRun->adjList.headNode = NULL;

        //printf("\n");

        free(vRun);
        memoryCount++;
        vRun = NULL;

        vRun = vRunNext;
    }

    free(g->verticalList.headNode->adjList.headNode);
    memoryCount++;
    g->verticalList.headNode->adjList.headNode = NULL;

    free(g->verticalList.headNode);
    memoryCount++;
    g->verticalList.headNode = NULL;

    printf("Memory count to free = %d || %d", countMemory, memoryCount);
}

int main(int argc, char *argv[], char *envp[])
{
    Graph g;

    initGraph(&g);

    for(int i = 0; i<8; i++)
    {
        addVertex(&g, i);
    }

    int edges[][2] = {
        {0,1},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,0},
        {1,6},{6,3},{5,2},{7,2}
    };

    int edgeNumber = sizeof(edges)/sizeof(edges[0]);

    for(int i = 0; i<edgeNumber; i++)
    {
        addEdge(&g, edges[i][0], edges[i][1]);
    }

    removeEdge(&g, 2, 3);

    printGraph(&g);

    removeVertex(&g, 1);

    printf("\n");

    printGraph(&g);

    freeGraph(&g);

    return(0);
}