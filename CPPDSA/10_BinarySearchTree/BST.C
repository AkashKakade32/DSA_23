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
  void inorderTraversal(Node *);
  void preorderTraversal(Node *);
  void postorderTraversal(Node *);
  int inorderSuccessor(Node *, int);
  void freeTree(Node *);

  //Variable Declarations
  Node *root = NULL;
  int i = 0;

  //Code
  int arr[13] = {100, 70, 150, 50, 30, 65, 80, 40, 120, 170, 250, 130, 300};

  for(i = 0; i<13; i++)
  {
    insertNode(&root, arr[i]);
  }

  printf("\n\n");
  printf("Inorder Traversal : ");
  inorderTraversal(root);
  printf("[END]\n");

  printf("\n");
  printf("Preorder Traversal : ");
  preorderTraversal(root);
  printf("[END]\n");

  printf("\n");
  printf("Postorder Traversal : ");
  postorderTraversal(root);
  printf("[END]\n");

  printf("Inorder Successor : %d \n", inorderSuccessor(root, 120));

  freeTree(root);

  return(0);

}

Node *createNode(int newData)
{
  //Variable Declarations
  Node *newNode = NULL;

  //Code
  newNode = (Node *)malloc(sizeof(Node));
  if(newNode == NULL)
  {
    printf("Failed to allocate memory to the newNode \n");
    exit(EXIT_FAILURE);
  }

  newNode->data = newData;

  newNode->right = NULL;
  newNode->left = NULL;
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
    printf("Root node is created : %p \n", (void *)*root);
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

void inorderTraversal(Node *root)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    inorderTraversal(run->left);
    printf("[%d]->", run->data);
    inorderTraversal(run->right);
  }
}

void preorderTraversal(Node *root)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    printf("[%d]->", run->data);
    preorderTraversal(run->left);
    preorderTraversal(run->right);
  }
}

void postorderTraversal(Node *root)
{
  //Variable Declarations
  Node *run;

  //Code
  run = root;

  if(run != NULL)
  {
    postorderTraversal(run->left);
    postorderTraversal(run->right);
    printf("[%d]->", run->data);
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
    if(run->data == searchData)
    {
      return(run);
    }
    else {
      if(searchData < run->data)
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

int inorderSuccessor(Node *root, int searchData)
{
  //Function Declarations
  Node *searchNode(Node *, int);

  //Variable Declarations
  Node *run;
  Node *currentNode;

  //Code
  currentNode = searchNode(root, searchData);
  if(currentNode == NULL)
  {
    printf("searchData is not present in the Tree \n");
    return(0);
  }

  if(currentNode->right != NULL)
  {
    run = currentNode->right;
    while(run->left != NULL)
    {
      run = run->left;
    }
    return(run->data);
  }

  Node *x = currentNode;
  Node *y = currentNode->parent;

  while((y->parent != NULL)&&(x == y->right))
  {
    x = y;
    y = y->parent;
  }

  return(y->data);

}


void freeTree(Node *root)
{
  if(root != NULL)
  {
    freeTree(root->left);
    freeTree(root->right);
    printf("Node is freed : %p \n", (void *)root);
    free(root);
    root = NULL;
  }
}
