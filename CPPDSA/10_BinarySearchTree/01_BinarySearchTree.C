#include<stdio.h>
#include<stdlib.h>

#define True 1

typedef struct node{
  int data;
  struct node *right;
  struct node *left;
  struct node *parent;
}Node;

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void insertNode(Node **, int);
  void freeTree(Node *);

  //Variable Declarations
  Node *root = NULL;

  //Code
  insertNode(&root, 100);
  insertNode(&root, 200);
  insertNode(&root, 50);
  insertNode(&root, 60);
  
  printf("Address of root node : %p \n", (void *)root);

  freeTree(root);

  return(0);
}

Node *createNode(int newData)
{
  //Variable Declarations
  Node *newNode;

  //Code

  newNode = (Node *)malloc(sizeof(Node));
  if(newNode == NULL)
  {
    printf("Failed to allocate the memory to the newNode \n");
    exit(EXIT_FAILURE);
  }

  newNode->data = newData;
  newNode->left = NULL;
  newNode->right = NULL;
  newNode->parent = NULL;
  
  return(newNode);
}

void insertNode(Node **root, int newData)
{
  //Function Declarations
  Node *createNode(int);
  
  //Variable Declarations
  Node *temp;
  Node *newNode;

  //Code
  if(*root == NULL)
  {
    *root = createNode(newData);
    printf("root node is created with : %p \n", (void *)*root);
  }
  else {

    temp = *root;
    newNode = createNode(newData);

    while(True)
    {
      if(newData <= temp->data)
      {
        if(temp->left == NULL)
        {
          temp->left = newNode;
          temp->left->parent = temp;
          printf("newNode is inserted at left having address : %p ||| Parent : %p \n", (void *)newNode, (void *)temp);
          break;
        }
        else {
          temp = temp->left;
        }
      }
      else {
        if(temp->right == NULL)
        {
          temp->right = newNode;
          temp->right->parent = temp;
          printf("newNode is inserted at right having address : %p ||| Parent : %p \n", (void *)newNode, (void *)temp);
          break;
        }
        else {
          temp = temp->right;
        }
      }
    }
  }

}

void freeTree(Node *root)
{
  if(root != NULL)
  {
    freeTree(root->left);
    freeTree(root->right);
    printf("We are freeing the node : %p \n", (void *)root);
    free(root);
  }
}










