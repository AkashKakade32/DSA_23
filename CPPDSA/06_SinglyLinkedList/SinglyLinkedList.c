#include<stdio.h>
#include<stdlib.h>

typedef struct node{
  int data;
  struct node *next;
}Node;

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void insertStart(Node **, int);
  void insertEnd(Node **, int);
  Node *searchNode(Node **, int, Node **);
  void insertAfter(Node **, int, int);
  void insertBefore(Node **, int, int);
  Node *getFirst(Node **);
  Node *getEnd(Node **);
  int popFirst(Node **);
  int popEnd(Node **);
  void removeStart(Node **);
  void removeEnd(Node **);
  void removeData(Node **, int);
  int lengthOfTheList(Node **);
  void showList(Node **);
  void freeList(Node **);

  //Variables Declarations
  Node *headNode;
  Node *prevNode;


  //Memory allocation for headNode to use it as a dummy node
  headNode = (Node*)malloc(sizeof(Node));
  if(headNode == NULL)
  {
    printf("Failed to allocate the memory \n");
    return(1);
  }
  headNode->next = NULL;



  for(int i = 1; i<6; i++)
  {
    insertStart(&headNode, (10*i));
  }

  for(int i = 6; i<11; i++)
  {
    insertEnd(&headNode, (10*i));
  }

  showList(&headNode);

  Node *currentNode = searchNode(&headNode, 20, &prevNode);
  if(currentNode == NULL)
  {
    printf("searchData is not present in the list \n");
  }
  else{
    printf("Data %d is found at address = %p having the previous node = %p and data = %d\n\n", currentNode->data, (void *)currentNode, (void *)prevNode, prevNode->data);
  }

  insertAfter(&headNode, 10, 600);
  insertAfter(&headNode, 100, 50000);
  insertBefore(&headNode, 10, 500);
  insertBefore(&headNode, 50, 3000);

  showList(&headNode);

  Node *firstNode = getFirst(&headNode);
  if(firstNode == NULL)
  {
    printf("Linked List is empty failed to get firstNode \n\n");
  }
  else{
    printf("Address of first node is = %p and data = %d \n\n", (void *)firstNode, firstNode->data);
  }

  Node *lastNode = getEnd(&headNode);
  if(lastNode == NULL)
  {
    printf("Linked List is empty failed to get the lastNode \n\n");
  }
  else{
    printf("Address of lastNode is = %p and Data = %d \n\n", (void *)lastNode, lastNode->data);
  }

  printf("Printing the Linked List after getFirst() and getEnd() to show data is not removed \n");

  showList(&headNode);

  int data = popFirst(&headNode);
  printf("Popped frist data is = %d \n\n", data);

  data = popEnd(&headNode);
  printf("Popped last data is = %d \n\n", data);
  
  printf("Printing the linked list after popStart() and popEnd() to show data is removed \n");
  showList(&headNode);

  removeStart(&headNode);
  removeEnd(&headNode);

  printf("Printing the Linked List After the removeStart() and removeEnd() \n");
  showList(&headNode);

  removeData(&headNode, 600);
  printf("Printing Linked List After removeData() \n\n");
  showList(&headNode);

  int length = lengthOfTheList(&headNode);
  printf("Length of the Linked List is = %d \n\n", length);
  
  currentNode = searchNode(&headNode, -500, &prevNode);
  if(currentNode == NULL)
  {
    printf("Data is not present in the list \n\n");
  }
  
  freeList(&headNode);
  free(headNode);

  return(0);
}

void insertStart(Node **headNode, int data)
{
  Node *newNode;

  newNode = (Node *)malloc(sizeof(Node));
  if(newNode == NULL)
  {
    printf("Failed to allocate the memory\n");
    exit(EXIT_FAILURE);
  }

  newNode->data = data;
  newNode->next = NULL;

  if((*headNode)->next == NULL)
  {
    (*headNode)->next = newNode;
  }
  else {
    newNode->next = (*headNode)->next;
    (*headNode)->next = newNode;
  }
  printf("Node is inserted at the start of Linked List = %p <-- %p \n\n", (void *)newNode->next, (void *)newNode);
}

void insertEnd(Node **headNode, int data)
{
  Node *newNode;
  Node *temp;

  newNode = (Node *)malloc(sizeof(Node));
  if(newNode == NULL)
  {
    printf("Failed to allocate the memory \n\n");
    exit(EXIT_FAILURE);
  }

  newNode->data = data;
  newNode->next = NULL;
  
  temp = (*headNode)->next;

  while(temp->next != NULL)
  {
    temp = temp->next;
  }
  temp->next = newNode;

  printf("Node is inserted at the end of Linked List = %p --> %p \n\n", (void *)temp, (void *)temp->next);

}

Node *searchNode(Node **headNode, int searchData, Node **prevNode)
{
  Node *temp = NULL;

  temp = (*headNode)->next;
  *prevNode = *headNode;

  while(temp != NULL)
  {
    if(temp->data == searchData)
    {
      return(temp);
    }
    *prevNode = temp;
    temp = temp->next;
  }
  return(NULL);
}

void insertAfter(Node **headNode, int data, int newData)
{
  Node *searchNode(Node **, int, Node **);

  Node *currentNode, *prevNode;
  Node *temp = *headNode;

  currentNode = searchNode(&temp, data, &prevNode);
  if(currentNode == NULL)
  {
    printf("Data is not present in the list \n");
    exit(EXIT_FAILURE);
  }
  else{

    Node *newNode;
    newNode = (Node *)malloc(sizeof(Node));
    if(newNode == NULL)
    {
      printf("Failed to allocate the memory\n");
      exit(EXIT_FAILURE);
    }

    newNode->data = newData;
    newNode->next = NULL;
    
    newNode->next = currentNode->next;
    currentNode->next = newNode;

    printf("New node = %p is inserted between %p and %p \n\n", (void *)newNode, (void *)currentNode, (void *)newNode->next);
  }

}

void insertBefore(Node **headNode, int data, int newData)
{
  Node *searchNode(Node **, int, Node **);

  Node *currentNode, *prevNode;
  Node *temp = *headNode;

  currentNode = searchNode(&temp, data, &prevNode);
  if(currentNode == NULL)
  {
    printf("Data is not present in the list \n");
    exit(EXIT_FAILURE);
  }
  else {
    Node *newNode;
    newNode = (Node *)malloc(sizeof(Node));
    if(newNode == NULL)
    {
      printf("Failed to allocate the memory \n");
      exit(EXIT_FAILURE);
    }

    newNode->data = newData;
    newNode->next = NULL;

    newNode->next = prevNode->next;
    prevNode->next = newNode;

    printf("New node = %p is inserted between %p and %p \n\n", (void *)newNode, (void *)prevNode, (void *)newNode->next);
  }
}

int isEmpty(Node **headNode)
{
  if((*headNode)->next == NULL)
  {
    exit(EXIT_FAILURE);
  }
  else{
    return(0);
  }
}

Node *getFirst(Node **headNode)
{
  int isEmpty(Node **);
  
  if(isEmpty(headNode))
  {
    printf("getFirst() cannot applied on the empty Linked List \n\n");
    exit(EXIT_FAILURE);
  }
  else{
    return((*headNode)->next);
  }

}

Node *getEnd(Node **headNode)
{
  int isEmpty(Node **);

  if(isEmpty(headNode))
  {
    printf("getEnd() cannot applied on the empty Linked List \n\n");
    exit(EXIT_FAILURE);
  }
  else{
    Node *temp = (*headNode)->next;

    while(temp->next != NULL)
    {
      temp = temp->next;
    }

    return(temp);
  }
}

int popFirst(Node **headNode)
{
  if((*headNode)->next == NULL)
  {
    printf("popEnd() cannot applied on the Empty List \n\n");
    exit(EXIT_FAILURE);
  }
  else{

    Node *temp;

    temp = (*headNode)->next;
    int data = temp->data;
    (*headNode)->next = temp->next;
    free(temp);
    return(data);
  }
}

int popEnd(Node **headNode)
{
  if((*headNode)->next == NULL)
  {
    printf("popEnd() cannot applied on the Empty List \n\n");
    exit(EXIT_FAILURE);
  }
  else{
    Node *temp = (*headNode)->next;
    Node *prev = *headNode;

    while(temp->next != NULL)
    {
      prev = temp;
      temp = temp->next;
    }
    int data = temp->data;
    prev->next = NULL;
    free(temp);
    return(data);
  }
}

void removeStart(Node **headNode)
{
  if((*headNode)->next == NULL)
  {
    printf("removeStart() cannot applied on the Empty List \n\n");
    exit(EXIT_FAILURE);
  }
  else{
    Node *temp;
    temp = (*headNode)->next;
    (*headNode)->next = temp->next;
    free(temp);
  }
}

void removeEnd(Node **headNode)
{
  if((*headNode)->next == NULL)
  {
    printf("removeEnd() cannot applied on the Empty List \n\n");
    exit(EXIT_FAILURE);
  }
  else{
    Node *temp = (*headNode)->next;
    Node *prev = *headNode;

    while(temp->next != NULL)
    {
      prev = temp;
      temp = temp->next;
    }
    prev->next = NULL;
    free(temp);
  }
}

void removeData(Node **headNode, int rData)
{
  Node *searchNode(Node **, int, Node **);
  
  Node *currentNode, *prevNode;

  Node *temp = *headNode;

  currentNode = searchNode(&temp, rData, &prevNode);
  if(currentNode == NULL)
  {
    printf("Data to be removed is not present in the List \n\n");
    exit(EXIT_FAILURE);
  }

  prevNode->next = currentNode->next;
  free(currentNode);

}

int lengthOfTheList(Node **headNode)
{
  Node *temp = *headNode;
  int length = 0;

  while(temp->next != NULL)
  {
    length++;
    temp = temp->next;
  }

  return(length);
}

void showList(Node **headNode)
{
  Node *temp;
  temp = (*headNode)->next;
  printf("[START]-->");
  while(temp != NULL)
  {
    printf("[%d]-->", temp->data);
    temp = temp->next;
  }
  printf("[END]\n\n");
}

void freeList(Node **headNode)
{
  Node *temp;

  while((*headNode)->next != NULL)
  {
    temp = (*headNode)->next;
    (*headNode)->next = temp->next;
    printf("We are freeing the node containing address = %p \n\n", (void *)temp);
    free(temp);
  }
}
