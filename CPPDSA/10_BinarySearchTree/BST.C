#include<stdio.h>
#include<stdlib.h>

#define True 1

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
  void inorderPrint(Node *);
  void preorderPrint(Node *);
  void postorderPrint(Node *);
  Node *searchNode(Node *, int);
  Node *inorderSuccessor(Node *, int);
  Node *preDeccessor(Node *, int);
  void freeTree(Node *);

  //Variable Declarations
  Node *root = NULL;
  int arr[9] = {100, 70, 60, 40, 80, 110, 105, 120, 118};
  int i = 0;
  Node *currentNode = NULL;

  //Code
  while(i < 9)
  {
    insertNode(&root, arr[i]);
    i++;
  }

  printf("\n");
  printf("Inorder Traversal : ");
  inorderPrint(root);
  printf("\n\n");

  printf("\n");
  printf("Preorder Traversal : ");
  preorderPrint(root);
  printf("\n\n");

  printf("\n");
  printf("Postorder Traversal : ");
  postorderPrint(root);
  printf("\n\n");



  currentNode = searchNode(root, 100);
  if(currentNode == NULL)
  {
    printf("searchData is not present in the Tree \n");
  }
  else {
    printf("searchData is present in the Tree : %p \n\n", (void *)currentNode);
  }

  currentNode = inorderSuccessor(root, 80);
  if(currentNode != NULL)
  {
    printf("inorderSuccessor node is = %p : %d \n\n", (void *)currentNode, currentNode->data);
  }

  currentNode = preDeccessor(root, 80);
  if(currentNode != NULL)
  {
    printf("preDeccessor node is = %p : %d \n\n", (void *)currentNode, currentNode->data);
  }

  
  
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
  Node *newNode;
  Node *run;

  //Code
  if(*root == NULL)
  {
    *root = createNode(newData);
    printf("root node is created : %p \n", (void *)*root);
  }
  else {
    newNode = createNode(newData);
    run = *root;

    while(True)
    {
      if(newData <= run->data)
      {
        if(run->left == NULL)
        {
          run->left = newNode;
          newNode->parent = run;
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
          break;
        }
        else {
          run = run->right;
        }
      }
    }
  }
}

void inorderPrint(Node *root)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    inorderPrint(run->left);
    printf("%d,",run->data);
    inorderPrint(run->right);
  }
}

void preorderPrint(Node *root)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    printf("%d,",run->data);
    preorderPrint(run->left);
    preorderPrint(run->right);
  }
}

void postorderPrint(Node *root)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    postorderPrint(run->left);
    postorderPrint(run->right);
    printf("%d,", run->data);
  }
}

Node *inorderSuccessor(Node *root, int searchData)
{
  //Function Declarations
  Node *searchNode(Node *, int);

  //Variable Declarations
  Node *currentNode;

  currentNode = searchNode(root, searchData);
  if(currentNode == NULL)
  {
    return(NULL);
  }
  else {
    if(currentNode->right != NULL)
    {
      Node *temp = currentNode->right;

      while(temp->left != NULL)
      {
        temp = temp->left;
      }

      return(temp);
    }
    else {
      Node *x = currentNode;
      Node *y = currentNode->parent;

      while((y != NULL)&&(x == y->right))
      {
        x = y;
        y = y->parent;
      }
      
      return(y);

    }
  }
}

Node *preDeccessor(Node *root, int searchData)
{
  //Function Declarations
  Node *searchNode(Node *, int);

  //Variable Declarations
  Node *currentNode;

  currentNode = searchNode(root, searchData);
  if(currentNode == NULL)
  {
    return(NULL);
  }
  else {
    if(currentNode->left != NULL)
    {
      Node *temp = currentNode->left;

      while(temp->right != NULL)
      {
        temp = temp->right;
      }

      return(temp);
    }
    else {
      Node *x = currentNode;
      Node *y = currentNode->parent;

      while((y != NULL)&&(x == y->left))
      {
        x = y;
        y = y->parent;
      }
      
      return(y);

    }
  }
}


Node *searchNode(Node *root, int searchData)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  while(True)
  {
    if(run->data == searchData)
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

  return(NULL);
}

void freeTree(Node *root)
{
  if(root != NULL)
  {
    freeTree(root->left);
    freeTree(root->right);
    printf("We are freeing the node : %p \n",(void *)root);
    free(root);
    root = NULL;
  }
}

