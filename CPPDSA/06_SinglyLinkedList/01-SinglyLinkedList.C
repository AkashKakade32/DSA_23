#include<stdio.h>
#include<stdlib.h>

typedef struct node{
  int data;
  struct node *next;
}SNode;

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void insertStart(SNode *, int);
  void insertEnd(SNode *, int);
  SNode *searchNode(SNode *, SNode **, int);
  void insertBefore(SNode *, int, int);
  void insertAfter(SNode *, int, int);
  void removeNode(SNode *, int);
  int getStart(SNode *);
  int getEnd(SNode *);
  int popStart(SNode *);
  int popEnd(SNode *);
  void removeStart(SNode *);
  void removeEnd(SNode *);
  int length(SNode *);
  void showList(SNode *);
  void reverseList(SNode *);
  void freeList(SNode *);

  //Varibale Declarations
  SNode *headNode;
  SNode *currentNode;
  SNode *prevNode;
  int i = 0;

  //Code

  //Creating the dummy headNode
  headNode = (SNode *)malloc(sizeof(SNode));
  if(headNode == NULL)
  {
    printf("Failed to allocate the memory to the headNode \n");
    exit(EXIT_FAILURE);
  }
  headNode->next = NULL;

  printf("----------Testing length() of LinkedList----------\n");
  printf("Lenght : %d \n\n", length(headNode));
  
  printf("----------Testing insertStart()----------\n");
  for(i = 1; i<6; i++)
  {
    insertStart(headNode, 10*i);
  }
  showList(headNode);

  printf("----------Testing insertEnd()----------\n");
  for(i = 6; i<11; i++)
  {
    insertEnd(headNode, 10*i);
  }
  showList(headNode);

  printf("----------Testing searchNode() for middle node----------\n");
  currentNode = searchNode(headNode, &prevNode, 10);
  if(currentNode == NULL)
  {
    printf("No searchData found in the List \n");
  }
  else
  {
    printf("currentData is found at location : %p : %d || having previous node : %p : %d \n", (void *)currentNode, currentNode->data, (void *)prevNode, prevNode->data);
  }

  printf("----------Testing searchNode() for first node----------\n");
  currentNode = searchNode(headNode, &prevNode, 50);
  if(currentNode == NULL)
  {
    printf("No searchData found in the List \n");
  }
  else
  {
    printf("currentData is found at location : %p : %d || having previous node : %p : %d \n", (void *)currentNode, currentNode->data, (void *)prevNode, prevNode->data);
  }

  printf("----------Testing searchNode() for last node----------\n");
  currentNode = searchNode(headNode, &prevNode, 100);
  if(currentNode == NULL)
  {
    printf("No searchData found in the List \n");
  }
  else
  {
    printf("currentData is found at location : %p : %d || having previous node : %p : %d \n", (void *)currentNode, currentNode->data, (void *)prevNode, prevNode->data);
  }
  
  printf("\n\n");

  printf("----------Testing insertBefore() for middle node----------\n");
  insertBefore(headNode, 10, 1000);
  showList(headNode);

  printf("----------Testing insertBefore() for start node----------\n");
  insertBefore(headNode, 50, 5000);
  showList(headNode);

  printf("----------Testing insertBefore() for end node----------\n");
  insertBefore(headNode, 100, 5000);
  showList(headNode);
  
  printf("----------Testing insertBefore() for false data----------\n");
  insertBefore(headNode, 220, 7000);

  printf("\n\n");

  printf("----------Testing insertAfter() for middle node----------\n");
  insertAfter(headNode, 10, 7000);
  showList(headNode);

  printf("----------Testing insertAfter() for start node----------\n");
  insertAfter(headNode, 50, 8000);
  showList(headNode);

  printf("----------Testing insertAfter() for end node----------\n");
  insertAfter(headNode, 100, 9000);
  showList(headNode);
  
  printf("----------Testing insertAfter() for false data----------\n");
  insertBefore(headNode, 312, 7000);
  
  printf("\n\n");

  printf("----------Testing removeNode() for middle node----------\n");
  removeNode(headNode, 7000);
  showList(headNode);
  
  printf("----------Testing removeNode() for start node----------\n");
  removeNode(headNode, 5000);
  showList(headNode);
  
  printf("----------Testing removeNode() for end node----------\n");
  removeNode(headNode, 9000);
  showList(headNode);
  
  printf("----------Testing removeNode() for false data----------\n");
  removeNode(headNode, 312);
  
  printf("\n\n");

  printf("----------Testing getStart()----------\n");
  printf("First Data : %d \n", getStart(headNode));

  printf("----------Testing getEnd()----------\n");
  printf("Last Data : %d \n", getEnd(headNode));

  printf("\n\n");

  printf("----------Testing popStart()----------\n");
  printf("popStart : %d \n", popStart(headNode));
  showList(headNode);

  printf("----------Testing popEnd()----------\n");
  printf("popEnd : %d \n", popEnd(headNode));
  showList(headNode);
  
  printf("----------Testing popEnd()----------\n");
  printf("popEnd : %d \n", popEnd(headNode));
  showList(headNode);

  printf("----------Testing removeStart()----------\n");
  removeStart(headNode);
  showList(headNode);
  
  printf("----------Testing removeEnd()----------\n");
  removeEnd(headNode);
  showList(headNode);
  
  printf("----------Testing length() of LinkedList----------\n");
  printf("Lenght : %d \n\n", length(headNode));

  printf("\n\n");

  /*printf("----------Testing reverseList()----------\n");
  reverseList(headNode);
  showList(headNode);*/

  freeList(headNode);

  return(0);
}

SNode *createNode(int newData)
{
  //Variable Declarations
  SNode *newNode;

  //Code
  newNode = (SNode *)malloc(sizeof(SNode));
  if(newNode == NULL)
  {
    printf("Failed to allocate the memory to the newNode \n");
    exit(EXIT_FAILURE);
  }

  newNode->data = newData;
  newNode->next = NULL;

  return(newNode);
}

void insertStart(SNode *headNode, int newData)
{
  //Function Declarations
  SNode *createNode(int);

  //Variable Declarations
  SNode *newNode;

  //Code
  newNode = createNode(newData);

  newNode->next = headNode->next;
  headNode->next = newNode;
}

void insertEnd(SNode *headNode, int newData)
{
  //Function Declarations
  SNode *createNode(int);

  //variable Declarations
  SNode *temp;
  SNode *newNode;

  //Code
  temp = headNode;
  newNode = createNode(newData);

  while(temp->next != NULL)
  {
    temp = temp->next;
  }
  
  temp->next = newNode;
}

SNode *searchNode(SNode *headNode, SNode **prevNode, int searchData)
{
  //Variable Declarations
  SNode *temp;

  //Code
  temp = headNode->next;
  *prevNode = headNode;

  while(temp != NULL)
  {
    if(searchData == temp->data)
    {
      return(temp);
    }
    else
    {
      *prevNode = temp;
      temp = temp->next;
    }
  }

  return(NULL);
}

void showList(SNode *headNode)
{
  //Variable Declarations
  SNode *temp;

  //Code
  temp = headNode->next;

  printf("[START]-->");
  while(temp != NULL)
  {
    printf("[%d]-->", temp->data);
    temp = temp->next;
  }
  printf("[END] \n\n");
}

void insertBefore(SNode *headNode, int currentData, int newData)
{
  //Function Declarations
  SNode *createNode(int);
  SNode *searchNode(SNode *, SNode **, int);

  //Variable Declarations
  SNode *temp;
  SNode *newNode;
  SNode *currentNode;
  SNode *prevNode;

  //Code
  currentNode = searchNode(headNode, &prevNode, currentData);
  if(currentNode == NULL)
  {
    printf("currentData : %d is not present in the list \n", currentData);
    return;
  }

  newNode = createNode(newData);
  
  newNode->next = prevNode->next;
  prevNode->next = newNode;
}

void insertAfter(SNode *headNode, int currentData, int newData)
{
  //Function Declarations
  SNode *createNode(int);
  SNode *searchNode(SNode *, SNode **, int);

  //Variable Declarations
  SNode *temp;
  SNode *newNode;
  SNode *currentNode;
  SNode *prevNode;

  //Code
  currentNode = searchNode(headNode, &prevNode, currentData);
  if(currentNode == NULL)
  {
    printf("currentData : %d is not present in the list \n", currentData);
    return;
  }

  newNode = createNode(newData);

  newNode->next = currentNode->next;
  currentNode->next = newNode;
}

void removeNode(SNode *headNode, int rData)
{
  //Function Declarations
  SNode *searchNode(SNode *, SNode **, int);

  //Varibale Declarations
  SNode *currentNode;
  SNode *prevNode;

  //Code
  currentNode = searchNode(headNode, &prevNode, rData);
  if(currentNode == NULL)
  {
    printf("Data ro be removed is not present in the list rData : %d \n", rData);
    return;
  }

  prevNode->next = currentNode->next;

  free(currentNode);
  currentNode = NULL;
}

int getStart(SNode *headNode)
{
  //Varibale Declarations
  int data = 0;
  
  //Code
  if(headNode->next == NULL)
  {
    printf("Cannot applied getStart() on empty list \n");
    exit(EXIT_FAILURE);
  }

  data = headNode->next->data;

  return(data);

}

int getEnd(SNode *headNode)
{
  //Varibale Declarations
  int data = 0;
  SNode *temp;

  //Code
  if(headNode->next == NULL)
  {
    printf("Cannot applied getEnd() on empty list \n");
    exit(EXIT_FAILURE);
  }
  
  temp = headNode->next;

  while(temp->next != NULL)
  {
    temp = temp->next;
  }

  data = temp->data;

  return(data);

}

int popStart(SNode *headNode)
{
  //Varibale Declarations
  int data;
  SNode *firstNodeWithData;

  //Code
  if(headNode->next == NULL)
  {
    printf("Cannot applied popStart() on empty list \n");
    exit(EXIT_FAILURE);
  }

  firstNodeWithData = headNode->next;
  headNode->next = firstNodeWithData->next;

  data = firstNodeWithData->data;

  free(firstNodeWithData);
  firstNodeWithData = NULL;

  return(data);
  
}

int popEnd(SNode *headNode)
{
  
  //Variable Declarations
  int data;
  SNode *temp;
  SNode *prev;

  //Code
  if(headNode->next == NULL)
  {
    printf("Cannot applied popEnd() on the empty list \n");
    exit(EXIT_FAILURE);
  }

  temp = headNode->next;
  prev = headNode;

  while(temp->next != NULL)
  {
    prev = temp;
    temp = temp->next;
  }

  prev->next = NULL;

  data = temp->data;

  free(temp);
  temp = NULL;

  return(data);

}

void removeStart(SNode *headNode)
{
  //Varibale Declarations
  SNode *firstNodeWithData;

  //Code
  if(headNode->next == NULL)
  {
    printf("Cannot applied removeStart() on empty list \n");
    exit(EXIT_FAILURE);
  }

  firstNodeWithData = headNode->next;
  headNode->next = firstNodeWithData->next;

  free(firstNodeWithData);
  firstNodeWithData = NULL;
  
}

void removeEnd(SNode *headNode)
{
  
  //Variable Declarations
  SNode *temp;
  SNode *prev;

  //Code
  if(headNode->next == NULL)
  {
    printf("Cannot applied popEnd() on the empty list \n");
    exit(EXIT_FAILURE);
  }

  temp = headNode->next;
  prev = headNode;

  while(temp->next != NULL)
  {
    prev = temp;
    temp = temp->next;
  }

  prev->next = NULL;

  free(temp);
  temp = NULL;

}

int length(SNode *headNode)
{
  //Variable Declarations
  int ln = 0;
  SNode *temp;

  //Code
  temp = headNode->next;

  while(temp != NULL)
  {
    ln++;
    temp = temp->next;
  }

  return(ln);
}

void reverseList(SNode *headNode)
{
  //Variable Declarations
  SNode *originalFirstNode;
  SNode *run;
  SNode *temp;

  //Code
  originalFirstNode = headNode->next;
  run = originalFirstNode->next;

  while(run != NULL)
  {
    temp = run->next;
    printf("Current temp = %d \n", temp->data);
    run->next = headNode->next;
    headNode->next = run;
    run = temp->next;
  }

  originalFirstNode = NULL;
}

void freeList(SNode *headNode)
{
  //Code
  while(headNode != NULL)
  {
    SNode *temp = headNode;
    headNode = temp->next;
    printf("We are freeing the node : %p | %d \n", temp, temp->data);
    free(temp);
    temp = NULL;
  }
}
