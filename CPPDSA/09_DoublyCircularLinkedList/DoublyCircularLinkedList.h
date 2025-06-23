#define True 1
#define False 0
#define CAP 100

typedef struct node {
    int data;
    struct node *next;
    struct node *prev;
}DNode;

DNode *headNode;

void createList()
{
    //Code
    headNode = (DNode *)malloc(sizeof(DNode));
    if(headNode == NULL)
    {
        printf("Failed to create the headNode \n");
        exit(EXIT_FAILURE);
    }
    headNode->next = headNode;
    headNode->prev = headNode;

}

DNode *createNode(int newData)
{
    //Variable Declarations
    DNode *newNode = NULL;

    //Code
    newNode = (DNode *)malloc(sizeof(DNode));
    if(newNode == NULL)
    {
        printf("Failed to allocate the memory to the newNode \n");
        exit(EXIT_FAILURE);
    }

    newNode->data = newData;
    newNode->next = NULL;
    newNode->prev = NULL;

    return(newNode);
}

int isEmpty()
{
    //Code
    if(headNode->next == headNode)
    {
        return(True);
    }
    else
    {
        return(False);
    }    
}

void insertStart(int newData)
{
    //Function Declarations
    DNode *createNode(int);

    //Variable Declarations
    DNode *newNode = NULL;

    //Code
    newNode = createNode(newData);

    newNode->next = headNode->next;
    newNode->prev = headNode;

    headNode->next->prev = newNode;
    headNode->next = newNode;
}

void insertEnd(int newData)
{
    //Function Declarations
    DNode *createNode(int);

    //Variable Declarations
    DNode *newNode = NULL;

    //Code
    newNode = createNode(newData);

    newNode->next = headNode->prev->next;
    newNode->prev = headNode->prev;

    headNode->prev->next = newNode;
    headNode->prev = newNode;
}

DNode *searchNode(int searchData)
{
    //Variable Declarations
    DNode *run;

    //Code
    run = headNode->next;

    while(run != headNode)
    {
        if(run->data == searchData)
        {
            return(run);
        }

        run = run->next;
    }

    return(NULL);
}

void insertAfter(int searchData, int newData)
{
    //Function Declarations
    DNode *searchNode(int);
    DNode *createNode(int);

    //Variable Declarations
    DNode *currentNode = NULL;
    DNode *newNode = NULL;

    //Code
    currentNode = searchNode(searchData);
    if(currentNode == NULL)
    {
        return;
    }

    newNode = createNode(newData);

    newNode->next = currentNode->next;
    newNode->prev = currentNode;

    currentNode->next->prev = newNode;
    currentNode->next = newNode;

}

void insertBefore(int searchData, int newData)
{
    //Function Declarations
    DNode *searchNode(int);
    DNode *createNode(int);

    //Variable Declarations
    DNode *currentNode = NULL;
    DNode *newNode = NULL;

    //Code
    currentNode = searchNode(searchData);
    if(currentNode == NULL)
    {
        return;
    }

    newNode = createNode(newData);

    newNode->next = currentNode;
    newNode->prev = currentNode->prev;

    currentNode->prev->next = newNode;
    currentNode->prev = newNode;

}

void removeNode(int rData)
{
    //Function Declarations
    DNode *searchNode(int);

    //Variable Declarations
    DNode *currentNode = NULL;

    //Code
    currentNode = searchNode(rData);
    if(currentNode == NULL)
    {
        return;
    }

    currentNode->prev->next = currentNode->next;
    currentNode->next->prev = currentNode->prev;

    printf("We are freeing the node : %d (%p) \n", currentNode->data, (void *)currentNode);
    free(currentNode);
    currentNode = NULL;
}

int popStart()
{
    
    //Variable Declarations
    DNode *run;
    int data;

    //Code
    if(isEmpty())
    {
        printf("popStart() cannot applied on empty list \n");
        exit(EXIT_FAILURE);
    }

    run = headNode->next;
    data = run->data;

    run->prev->next = run->next;
    run->next->prev = run->prev;

    free(run);
    run = NULL;

    return(data);

}

int popEnd()
{

    //Variable Declarations
    DNode *run;
    int data;

    //Code
    if(isEmpty())
    {
        printf("popEnd() cannot applied on empty list \n");
        exit(EXIT_FAILURE);
    }

    run = headNode->prev;
    data = run->data;

    run->prev->next = run->next;
    run->next->prev = run->prev;

    free(run);
    run = NULL;

    return(data);

}

void printList()
{
    //Variable Declarations
    DNode *run = headNode->next;

    printf("[START]<->");
    while(run != headNode)
    {
        printf("[%d]<->", run->data);
        run = run->next;
    }
    printf("[END] \n\n");

    //Printing using prev to check the prev linking

    // run = headNode->prev;

    // printf("[END]<->");
    // while(run != headNode)
    // {
    //     printf("[%d]<->", run->data);
    //     run = run->prev;
    // }
    // printf("[START] \n\n");
}

int getStart()
{
    //Code
    if(isEmpty())
    {
        printf("getStart() cannot applied on empty list \n");
        exit(EXIT_FAILURE);
    }

    return(headNode->next->data);
}

int getEnd()
{
    //Code
    if(isEmpty())
    {
        printf("getEnd() cannot applied on empty list \n");
        exit(EXIT_FAILURE);
    }
    return(headNode->prev->data);
}

int lengthOfList()
{
    //Variable Declarations
    int length = 0;
    DNode *run = NULL;

    //Code
    run = headNode->next;

    while(run != headNode)
    {
        run = run->next;
        length++;
    }

    return(length);
}

void freeList()
{
    //Variable Declarations
    DNode *run = NULL;
    DNode *temp = NULL;

    run = headNode->next;

    while(run != headNode)
    {
        temp = run;
        run = run->next;
        
        printf("Freeing the node : %p \n", (void *)temp);

        free(temp);
        temp = NULL;
    }

    printf("We are freeing the headNode : %p \n", (void *)headNode);
    free(headNode);
    headNode = NULL;
}