#include<stdio.h>
#include<stdlib.h>

#define True 1
#define False 0
#define CAP 100

typedef struct node {
    int data;
    struct node *next;
    struct node *prev;
}DNode;

int main(int argc, char *argv[], char *envp[])
{
    //Function Declarations
    void createList(DNode **);
    int lengthOfList(DNode *);
    void insertStart(DNode *, int);
    void insertEnd(DNode *, int);
    DNode *searchNode(DNode *, int);
    void insertAfter(DNode *, int, int);
    void insertBefore(DNode *, int, int);
    void removeNode(DNode *, int);
    int getStart(DNode *);
    int getEnd(DNode *);
    int popStart(DNode *);
    int popEnd(DNode *);
    int isEmpty(DNode *);
    void printList(DNode *);
    void freeList(DNode *);

    //Variable Declarations
    DNode *headNode = NULL;
    int i = 1;
    DNode *currentNode = NULL;

    //Code
    
    createList(&headNode);

    printf("headNode is created : %p \n", (void *)headNode);

    printf("\n");

    printf("********** Testing length of List **********\n");
    printf("Length of List : %d \n", lengthOfList(headNode));

    printf("\n");
    
    printf("********** Testing insertStart() **********\n");
    while(i < 6)
    {
        insertStart(headNode, (10*i));
        i++;
    }
    printList(headNode);

    printf("********** Testing insertEnd() **********\n");
    while(i < 11)
    {
        insertEnd(headNode, (10*i));
        i++;
    }
    printList(headNode);

    printf("********** Testing searchNode() for first node **********\n");
    currentNode = searchNode(headNode, 50);
    if(currentNode != NULL)
    {
        printf("Data is found at location : %p \n", (void *)currentNode);
    }
    else
    {
        printf("searchData is not present in the list \n");
    }
    printf("\n");

    printf("********** Testing searchNode() for middle node **********\n");
    currentNode = searchNode(headNode, 10);
    if(currentNode != NULL)
    {
        printf("Data is found at location : %p \n", (void *)currentNode);
    }
    else
    {
        printf("searchData is not present in the list \n");
    }
    printf("\n");

    printf("********** Testing searchNode() for end node **********\n");
    currentNode = searchNode(headNode, 100);
    if(currentNode != NULL)
    {
        printf("Data is found at location : %p \n", (void *)currentNode);
    }
    else
    {
        printf("searchData is not present in the list \n");
    }
    printf("\n");


    printf("********** Testing searchNode() for false node **********\n");
    currentNode = searchNode(headNode, 1000);
    if(currentNode != NULL)
    {
        printf("Data is found at location : %p \n", (void *)currentNode);
    }
    else
    {
        printf("searchData is not present in the list \n");
    }
    printf("\n");


    printf("********** Testing insertAfter() for middle node **********\n");
    insertAfter(headNode, 10, 2000);
    printList(headNode);
    printf("\n");

    printf("********** Testing insertAfter() for first node **********\n");
    insertAfter(headNode, 50, 5000);
    printList(headNode);
    printf("\n");

    printf("********** Testing insertAfter() for last node **********\n");
    insertAfter(headNode, 100, 6000);
    printList(headNode);
    printf("\n");

    printf("********** Testing insertAfter() for false node **********\n");
    insertAfter(headNode, 900, 6000);
    printList(headNode);
    printf("\n");

    printf("\n");
    
    printf("********** Testing insertBefore() for middle node **********\n");
    insertBefore(headNode, 10, 200);
    printList(headNode);
    printf("\n");

    printf("********** Testing insertBefore() for first node **********\n");
    insertBefore(headNode, 50, 500);
    printList(headNode);
    printf("\n");

    printf("********** Testing insertBefore() for last node **********\n");
    insertBefore(headNode, 100, 600);
    printList(headNode);
    printf("\n");

    printf("********** Testing insertBefore() for false node **********\n");
    insertBefore(headNode, 700, 7000);
    printList(headNode);
    printf("\n");

    printf("\n");

    printf("********** Testing removeNode() for middle node **********\n");
    removeNode(headNode, 2000);
    printList(headNode);
    printf("\n");

    printf("********** Testing removeNode() for first node **********\n");
    removeNode(headNode, 500);
    printList(headNode);
    printf("\n");

    printf("********** Testing removeNode() for last node **********\n");
    removeNode(headNode, 6000);
    printList(headNode);
    printf("\n");

    printf("********** Testing removeNode() for false node **********\n");
    removeNode(headNode, 60000);
    printList(headNode);
    printf("\n");

    printf("\n");

    printf("********** Testing getStart() **********\n");
    printf("Data at the start : %d \n", getStart(headNode));

    printf("********** Testing getEnd() **********\n");
    printf("Data at the end : %d \n", getEnd(headNode));

    printf("\n");

    printf("********** Testing popStart() **********\n");
    printf("Data at the start : %d \n", popStart(headNode));
    printList(headNode);

    printf("********** Testing popEnd() **********\n");
    printf("Data at the end : %d \n", popEnd(headNode));
    printList(headNode);

    printf("********** Testing length of List **********\n");
    printf("Length of List : %d \n", lengthOfList(headNode));

    printf("\n");

    //Free the List
    freeList(headNode);

    printf("\n");

    //Freeing the headNode
    printf("Freeing the headNode : %p \n", (void *)headNode);
    free(headNode);
    headNode = NULL;

    return(0);
}

void createList(DNode **headNode)
{
    //Code
    *headNode = (DNode *)malloc(sizeof(DNode));
    if(*headNode == NULL)
    {
        printf("Failed to create the headNode \n");
        exit(EXIT_FAILURE);
    }
    (*headNode)->next = *headNode;
    (*headNode)->prev = *headNode;

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

void insertStart(DNode *headNode, int newData)
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

void insertEnd(DNode *headNode, int newData)
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

DNode *searchNode(DNode *headNode, int searchData)
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

void insertAfter(DNode *headNode, int searchData, int newData)
{
    //Function Declarations
    DNode *searchNode(DNode *, int);
    DNode *createNode(int);

    //Variable Declarations
    DNode *currentNode = NULL;
    DNode *newNode = NULL;

    //Code
    currentNode = searchNode(headNode, searchData);
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

void insertBefore(DNode *headNode, int searchData, int newData)
{
    //Function Declarations
    DNode *searchNode(DNode *, int);
    DNode *createNode(int);

    //Variable Declarations
    DNode *currentNode = NULL;
    DNode *newNode = NULL;

    //Code
    currentNode = searchNode(headNode, searchData);
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

void removeNode(DNode *headNode, int rData)
{
    //Function Declarations
    DNode *searchNode(DNode *, int);

    //Variable Declarations
    DNode *currentNode = NULL;

    //Code
    currentNode = searchNode(headNode, rData);
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

int popStart(DNode *headNode)
{
    //Function Declarations
    int isEmpty(DNode *);

    //Variable Declarations
    DNode *run;
    int data;

    //Code
    if(isEmpty(headNode))
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

int popEnd(DNode *headNode)
{
    //Function Declarations
    int isEmpty(DNode *);

    //Variable Declarations
    DNode *run;
    int data;

    //Code
    if(isEmpty(headNode))
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

void printList(DNode *headNode)
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

int getStart(DNode *headNode)
{
    //Function Declarations
    int isEmpty(DNode *);

    //Code
    if(isEmpty(headNode))
    {
        printf("getStart() cannot applied on empty list \n");
        exit(EXIT_FAILURE);
    }

    return(headNode->next->data);
}

int getEnd(DNode *headNode)
{
    //Function Declarations
    int isEmpty(DNode *);

    //Code
    if(isEmpty(headNode))
    {
        printf("getEnd() cannot applied on empty list \n");
        exit(EXIT_FAILURE);
    }
    return(headNode->prev->data);
}

int isEmpty(DNode *headNode)
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

int lengthOfList(DNode *headNode)
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

void freeList(DNode *headNode)
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
}