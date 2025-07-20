#include<stdio.h>
#include<stdlib.h>

static int memoryCount = 0;

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

    memoryCount++;

    newNode->data = v;
    newNode->next = NULL;
    newNode->prev = NULL;

    return(newNode);
}

void hListInit(hList *list)
{
    list->headNode = hListCreateNode(-1);

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

    memoryCount--;
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

    memoryCount++;

    hListInit(&newNode->adjList);

    newNode->data = v;
    newNode->next = NULL;
    newNode->prev = NULL;

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

    memoryCount--;
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
        //printf("Vertex %d is already present in the Graph \n");
        return;
    }

    vListInsertEnd(&g->verticalList, v);
}

void addEdge(Graph *g, int startData, int endData)
{
    vNode *vStartNode = vListSearchNode(&g->verticalList, startData);
    if(vStartNode == NULL)
    {
        //printf("Vertex %d is not present in the Graph \n", startData);
        return;
    }

    vNode *vEndNode = vListSearchNode(&g->verticalList, endData);
    if(vEndNode == NULL)
    {
        //printf("Vertex %d is not present in the Graph \n", endData);
        return;
    }

    if(hListSearchNode(&vEndNode->adjList, startData) != NULL)
    {
        //printf("Edge is alredy present between %d and %d \n", startData, endData);
        return;
    }

    if(hListSearchNode(&vStartNode->adjList, endData) != NULL)
    {
        //printf("Edge is alredy present between %d and %d \n", startData, endData);
        return;
    }

    hListInsertEnd(&vStartNode->adjList, endData);
    hListInsertEnd(&vEndNode->adjList, startData);
}

void removeVertex(Graph *g, int vertex)
{
    vNode *vRun = vListSearchNode(&g->verticalList, vertex);

    if(vRun == NULL)
    {
        printf("Vertex %d is not present in the Graph \n", vertex);
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
        printf("[%d]\t-->\t", vRun->data);

        hNode *hRun = vRun->adjList.headNode->next;

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
    vNode *vRun = g->verticalList.headNode->next;

    while(vRun != g->verticalList.headNode)
    {
        vNode *vRunNext = vRun->next;
        hNode *hRun = vRun->adjList.headNode->next;

        while(hRun != vRun->adjList.headNode)
        {
            hNode *hRunNext = hRun->next;

            free(hRun);
            hRun = NULL;
            memoryCount--;

            hRun = hRunNext;
        }
        free(vRun->adjList.headNode);
        vRun->adjList.headNode = NULL;
        memoryCount--;

        free(vRun);
        vRun = NULL;
        memoryCount--;

        vRun = vRunNext;
    }
    free(g->verticalList.headNode->adjList.headNode);
    g->verticalList.headNode->adjList.headNode = NULL;
    memoryCount--;

    free(g->verticalList.headNode);
    g->verticalList.headNode == NULL;
    memoryCount--;

    printf("Current Memory count is %d \n", memoryCount);
}

int main(int argc, char *argv[], char *envp[])
{
    Graph g;

    initGraph(&g);

    int arr[100];

    for(int i = 0; i<100; i++)
    {
        arr[i] = rand() % 100;
    }

    for(int i = 0; i<100; i++)
    {
        addVertex(&g, arr[i]);
    }

    for(int i = 0; i<100; i++)
    {
        addEdge(&g, arr[rand()%100], arr[rand()%100]);
    }

    removeVertex(&g, 83);

    printGraph(&g);

    freeGraph(&g);

    return(0);
}
