#include<stdio.h>
#include<stdlib.h>

#define True 1
#define False 0

typedef struct node{
  int data;
  struct node *left;
  struct node *right;
  struct node *parent;
}Node;

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void insertNode(Node **, int);
  void freeTree(Node *);
  void inorder(Node *);
  void preorder(Node *);
  void postorder(Node *);
  Node *searchNode(Node *, int);

  //Varibale Declarations
  Node *root = NULL;
  Node *currentNode = NULL;

  //Code
  insertNode(&root, 100);
  insertNode(&root, 70);
  insertNode(&root, 80);
  insertNode(&root, 60);
  insertNode(&root, 40);
  insertNode(&root, 110);
  insertNode(&root, 120);
  insertNode(&root, 105);
  insertNode(&root, 118);

  printf("\n\n");
  printf("Inorder Traversal : ");
  inorder(root);
  printf("\n\n");

  printf("Preorder Traversal : ");
  preorder(root);
  printf("\n\n");

  printf("Postorder Traversal : ");
  postorder(root);
  printf("\n\n");

  currentNode = searchNode(root, 90);
  if(currentNode != NULL)
  {
    
    printf("currentNode : %p = %d || Parent : %p\n\n", (void *)currentNode, currentNode->data, (void *)currentNode->parent);
  }
  
  //Free the tree
  freeTree(root);
  root = NULL;

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
  Node *newNode;
  Node *run;

  //Code
  if(*root == NULL)
  {
    *root = createNode(newData);
    printf("root is created : %p \n", (void *)*root);
    return;
  }
  else {
    run = *root;
    newNode = createNode(newData);

    while(True)
    {
      if(newData <= run->data)
      {
        if(run->left == NULL)
        {
          run->left = newNode;
          newNode->parent = run;
          printf("newNode is inserted at left : %p = %d | Parent : %d \n", (void *)newNode, newNode->data, newNode->parent->data);
          break;
        }
        else {
          run = run->left;
        }
      }
      else {
        if(run->right == NULL)
        {
          run->right = newNode;
          newNode->parent = run;
          printf("newNode is inserted at right : %p = %d | Parent : %d \n", (void *)newNode, newNode->data, newNode->parent->data);
          break;
        }
        else {
          run = run->right;
        }
      }
    }
  }

}

void inorder(Node *root)
{
  //Varibale Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    inorder(run->left);
    printf("%d, ", run->data);
    inorder(run->right);
  }
}

void preorder(Node *root)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    printf("%d, ", run->data);
    preorder(run->left);
    preorder(run->right);
  }
}

void postorder(Node *root)
{
  //Varibale Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    postorder(run->left);
    postorder(run->right);
    printf("%d, ", run->data);
  }
}

Node *searchNode(Node *root, int searchData)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  while(run != NULL)
  {
    if(searchData == run->data)
    {
      return(run);
    }
    else {
      if(searchData <= run->data)
      {
        run = run->left;
      }
      else {
        run = run->right;
      }
    }
  }
  
  printf("searchData : %d is not found in the Tree \n", searchData);
  return(NULL);
}

void freeTree(Node *root)
{
  if(root != NULL)
  {
    freeTree(root->left);
    freeTree(root->right);
    printf("We are freeing the node : %p \n", (void *)root);
    free(root);
    root = NULL;
  }
}
