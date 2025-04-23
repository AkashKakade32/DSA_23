#include<stdio.h>
#include<stdlib.h>

typedef struct node{
  int data;
  struct node *next;
}NODE;

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void inserStart(NODE **, int);
  void insertEnd(NODE **, int);
  NODE *searchList(NODE **, int, NODE **);
  void showList(NODE **);
  void freeList(NODE **);

  //Variable Declarations
  NODE *headNode = NULL;
  int i = 1;
  NODE *prevNode;
  NODE *currentNode;
  int searchData = 100;

  //Testing insertStart()

  while(i < 6)
  {
    inserStart(&headNode, (10*i));
    i++;
  }

  //Testing insertEnd()

  i = 6;

  while(i < 11)
  {
    insertEnd(&headNode, (10*i));
    i++;
  }

  //Display the LinkedList

  showList(&headNode);

  //Testing the searchList()

  currentNode = searchList(&headNode, searchData, &prevNode);
  if(prevNode == currentNode)
  {
    printf("Data = %d is found at headNode having address = %p \n\n", searchData, (void *)currentNode);
  }
  else {
    if(currentNode != NULL)
    {
      printf("Data = %d is found at position = %p having previous node address = %p \n\n", searchData, (void *)currentNode, (void *)prevNode);
    }
    else{
      printf("Data = %d is not present in the list \n\n", searchData);
    }
  }

  //Free The Linked List

  freeList(&headNode);

  free(headNode);
  
  return(0);
}

void inserStart(NODE **headNode, int data)
{
  NODE *newNode;

  newNode = (NODE *)malloc(sizeof(NODE));
  if(newNode == NULL)
  {
    printf("Memory allocation is failed \n");
    exit(EXIT_FAILURE);
  }
  
  newNode->data = data;
  newNode->next = NULL;

  if(*headNode == NULL)
  {
    printf("Linked List is empty. \n");
    *headNode = newNode;
  }
  else{
    newNode->next = *headNode;
    *headNode = newNode;
  }

  printf("Node is inserted in the Linked List at the starting position before the current node = %p <-- %p \n\n", (void *)newNode, (void *)newNode->next);

}

void insertEnd(NODE **headNode, int data)
{
  NODE *newNode;

  newNode = (NODE *)malloc(sizeof(NODE));
  if(newNode == NULL)
  {
    printf("Failed to allocate the memory \n");
    exit(EXIT_FAILURE);
  }

  newNode->data = data;
  newNode->next = NULL;

  if(*headNode == NULL)
  {
    printf("Linked List is empty \n");
    *headNode = newNode;
  }
  else {
    NODE *temp;
    temp = *headNode;

    while(temp->next != NULL)
    {
      temp = temp->next;
    }
    temp->next = newNode;

    printf("Node is inserted in the Linked List at the end after the node = %p --> %p\n\n", (void *)temp, (void *)temp->next);
  }
}

NODE *searchList(NODE **headNode, int data, NODE **prevNode)
{
  NODE *temp;
  temp = (*headNode)->next;

  while(temp != NULL)
  {
    
    if(temp->data == data)
    {
      return temp;
    }

    *prevNode = temp;

    temp = temp->next;

  }

  return NULL;
}

void showList(NODE **headNode)
{
  NODE *temp;
  temp = *headNode;

  printf("Displaying the Linked List \n");

  printf("[START]-->");
  while(temp != NULL)
  {
    printf("[%d]-->", temp->data);
    temp = temp->next;
  }
  printf("[END]\n\n");
}

void freeList(NODE **headNode)
{
  NODE *temp;

  while(*headNode != NULL)
  {
    temp = *headNode;
    *headNode = temp->next;
    printf("Node is free having memory address = %p\n", (void *)temp);
    free(temp);
  }

  printf("Current address of headNode is = %p \n\n", (void *)*headNode);
}



