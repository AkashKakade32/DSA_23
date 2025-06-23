#include <cstdlib>
#include<stdio.h>
#include<stdlib.h>

#define True 1
#define False 0

typedef struct dnode{
  int data;
  struct dnode *prev;
  struct dnode *next;
}DNode;

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void insertStart(DNode **, int);
  void insertEnd(DNode **, int);
  DNode *searchNode(DNode **, int);
  void insertAfter(DNode **, int, int);
  void insertBefore(DNode **, int, int);
  int getFirst(DNode **headNode);
  int getLast(DNode **headNode);
  int popStart(DNode **headNode);
  int popEnd(DNode **headNode);
  void showList(DNode **);
  void freeList(DNode **);

  //Variable Declarations
  DNode *headNode;

  //Code

  //Assigning Memory to the headNode
  headNode = (DNode *)malloc(sizeof(DNode));
  if(headNode == NULL)
  {
    printf("Failed to allocate the memory \n");
    return(1);
  }
  printf("Address of headNode = %p \n\n\n", (void *)headNode);
  headNode->next = NULL;
  headNode->prev = NULL;
  
  /*for(int i = 1; i < 6; i++)
  {
    insertStart(&headNode, 10*i);
  }

  for(int i = 6; i<11; i++)
  {
    insertEnd(&headNode, 10*i);
  }*/

  int i = 0;

  while(i < 1000)
  {
    insertStart(&headNode, (rand() % 1000));
    i++;
  }

  printf("\nDisplaying the Doubly Linked List \n");

  showList(&headNode);

  printf("----------Testing searchNode----------\n");
  DNode *currentNode = searchNode(&headNode, 10);
  if(currentNode == NULL)
  {
    printf("No currnet data is found in Doubly Linked List \n");
  }
  else {
    printf("Data found is = %d at address %p \n", currentNode->data, (void *)currentNode);
  }

  printf("----------Testing insertAfter----------\n");
  insertAfter(&headNode, 100, 10000);
  printf("Displaying the Doubly Linked List \n");
  showList(&headNode);
  
  printf("----------Testing insertBefore----------\n");
  insertBefore(&headNode, 20, 50000);
  printf("Displaying the Doubly Linked List \n");
  showList(&headNode);

  printf("---------Testing getFirst() and getLast()-------- \n");
  int first = getFirst(&headNode);
  int last = getLast(&headNode);

  printf("First and last element of linked list is = %d / %d \n", first, last);

  printf("\n-----------Testing popStart()----------\n");
  first = popStart(&headNode);
  printf("First popped element is = %d \n", first);

  printf("Printing the list after popFirst() \n");
  showList(&headNode);

  printf("---------Testing popEnd()----------\n");
  last = popEnd(&headNode);
  printf("last popped element is = %d \n", last);

  printf("Printing the list after popEnd() \n");
  showList(&headNode);

  //Freeing up the allocated memory
  freeList(&headNode);
  printf("free headNode = %p \n", (void *)headNode);
  free(headNode);
  headNode = NULL;

  return(0);
}

void insertStart(DNode **headNode, int newData)
{
  void freeList(DNode **);

  DNode *newNode;

  newNode = (DNode *)malloc(sizeof(DNode));
  if(newNode == NULL)
  {
    printf("Failed to allocate the memory \n");
    
    freeList(headNode);

    exit(EXIT_FAILURE);
  }

  newNode->prev = NULL;
  newNode->next = NULL;
  newNode->data = newData;

  newNode->next = (*headNode)->next;
  newNode->prev = *headNode;
  if ((*headNode)->next != NULL)
  {
    (*headNode)->next->prev = newNode;
  }
  (*headNode)->next = newNode;

  printf("Node is inserted at the start = %p \n", (void *)newNode);
}

void insertEnd(DNode **headNode, int newData)
{
  void freeList(DNode **);

  DNode *temp;
  DNode *newNode;

  temp = (*headNode)->next;

  newNode = (DNode *)malloc(sizeof(DNode));
  if(newNode == NULL)
  {
    printf("Failed to allocate the memory \n");

    freeList(headNode);

    exit(EXIT_FAILURE);
  }
  newNode->next = NULL;
  newNode->prev = NULL;
  newNode->data = newData;

  while(temp->next != NULL)
  {
    temp = temp->next;
  }
  temp->next = newNode;
  newNode->prev = temp;

  printf("Node is inserted at the end = %p \n", (void *)newNode);

}

DNode *searchNode(DNode **headNode, int existingData)
{
  DNode *temp;
  temp = (*headNode)->next;
  while(temp != NULL)
  {
    if(temp->data == existingData)
    {
      return(temp);
    }
    temp = temp->next;
  }
  return(NULL);
}

void insertAfter(DNode **headNode, int existingData, int newData)
{
  DNode *searchNode(DNode **headNode, int);
  void freeList(DNode **);

  DNode *currentNode;

  currentNode = searchNode(headNode, existingData);
  if(currentNode == NULL)
  {
    printf("No existing Data is found \n");
  }
  else {
    DNode *newNode;

    newNode = (DNode *)malloc(sizeof(DNode));
    if(newNode == NULL)
    {
      printf("Failed to allocate the memory \n");
      freeList(headNode);
      exit(EXIT_FAILURE);
    }

    newNode->next = NULL;
    newNode->prev = NULL;
    newNode->data = newData;

    newNode->next = currentNode->next;
    newNode->prev = currentNode;
    if(currentNode->next != NULL)
    {
      currentNode->next->prev = newNode;
    }
    currentNode->next = newNode;
  }

}

void insertBefore(DNode **headNode, int existingData, int newData)
{
  DNode *searchNode(DNode **headNode, int);
  void freeList(DNode **);

  DNode *currentNode;

  currentNode = searchNode(headNode, existingData);
  if(currentNode == NULL)
  {
    printf("No existing data is found \n");
  }
  else{
    DNode *newNode;

    newNode = (DNode *)malloc(sizeof(DNode));
    if(newNode == NULL)
    {
      printf("Failed to allocate the memory \n");
      freeList(headNode);
      exit(EXIT_FAILURE);
    }

    newNode->next = NULL;
    newNode->prev = NULL;
    newNode->data = newData;

    newNode->next = currentNode;
    newNode->prev = currentNode->prev;
    currentNode->prev->next = newNode;
    currentNode->prev = newNode;
  }
}

int getFirst(DNode **headNode)
{
  int isEmpty(DNode **);
  
  if(isEmpty(headNode))
  {
    printf("Cannot Applied on the Empty List \n");
    exit(EXIT_FAILURE);
  }

  int data = (*headNode)->next->data;
  return data;
}

int getLast(DNode **headNode)
{

 int isEmpty(DNode **);
  
  if(isEmpty(headNode))
  {
    printf("Cannot Applied on the Empty List \n");
    exit(EXIT_FAILURE);
  }

  DNode *temp;
  temp = *headNode;

  while(temp->next != NULL)
  {
    temp = temp->next;
  }

  return(temp->data);
}

int popStart(DNode **headNode)
{

 int isEmpty(DNode **);
  
  if(isEmpty(headNode))
  {
    printf("Cannot Applied on the Empty List \n");
    exit(EXIT_FAILURE);
  }

  DNode *newNode;

  newNode = (*headNode)->next;

  int data = newNode->data;
  
  if(newNode->next != NULL)
  {
    newNode->next->prev = *headNode;
  }

  (*headNode)->next = newNode->next;

  printf("Node is freed = %p \n\n", (void *)newNode);

  free(newNode);

  return(data);

}

int popEnd(DNode **headNode)
{
  int isEmpty(DNode **);
  
  if(isEmpty(headNode))
  {
    printf("Cannot Applied on the Empty List \n");
    exit(EXIT_FAILURE);
  }

  DNode *temp;

  temp = (*headNode)->next;

  while(temp->next != NULL)
  {
    temp = temp->next;
  }

  int data = temp->data;

  temp->prev->next = NULL;

  printf("Node is freed = %p \n\n", (void *)temp);

  return(data);

}

int isEmpty(DNode **headNode)
{
  if((*headNode)->next != NULL)
  {
    return(False);
  }
  else{
    return(True);
  }
}

void showList(DNode **headNode)
{
  DNode *temp;
  temp = (*headNode)->next;
  printf("[START]<->");
  while(temp != NULL)
  {
    printf("[%d]<->", temp->data);
    temp = temp->next;
  }
  printf("[END]\n\n");
}

void freeList(DNode **headNode)
{
  DNode *temp;
  while(*headNode != NULL)
  {
    temp = *headNode;
    temp->prev = NULL;
    *headNode = temp->next;
    printf("Freeing the node containing address = %p \n", (void *)temp);
    free(temp);
  }
}
