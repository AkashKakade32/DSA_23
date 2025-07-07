#include<stdio.h>
#include<stdlib.h>

#define True 1
#define False 0

typedef struct node{
  int data;
  struct node *left;
  struct node *right;
  struct node *parent;
}bNode;

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void insertNode(bNode **, int);
  void inorderTraversal(bNode *);
  void preorderTraversal(bNode *);
  void postorderTraversal(bNode *);
  bNode *inorderSuccessor(bNode *, int);
  bNode *inorderPredeccessor(bNode *, int);
  void removeNode(bNode **, int);
  void freeList(bNode *);

  //Varibale Declarations
  bNode *root = NULL;
  int arr[13] = {100, 70, 150, 50, 30, 65, 80, 40, 120, 170, 250, 130, 300};
  int i = 0;
  bNode *currentNode = NULL;

  //Code
  for(i = 0; i<13; i++)
  {
    insertNode(&root, arr[i]);
  }

  printf("********** Testing inorderTraversal **********\n");
  printf("[START]->");
  inorderTraversal(root);
  printf("[END] \n");
  printf("\n");

  printf("********** Testing preorderTraversal **********\n");
  printf("[START]->");
  preorderTraversal(root);
  printf("[END] \n");
  printf("\n");

  printf("********** Testing postorderTraversal **********\n");
  printf("[START]->");
  postorderTraversal(root);
  printf("[END] \n");
  printf("\n");

  printf("********** Testing inorderSuccessor **********\n");
  currentNode = inorderSuccessor(root, 50);
  if(currentNode == NULL)
  {
    printf("Inorder Successor of node is not present in the Tree \n");
  }
  else
  {
    printf("Inorder Successor = %d \n", currentNode->data);
  }

  currentNode = inorderSuccessor(root, 100);
  if(currentNode == NULL)
  {
    printf("Inorder Successor of node is not present in the Tree \n");
  }
  else
  {
    printf("Inorder Successor = %d \n", currentNode->data);
  }
  printf("\n");

  printf("********** Testing inorderPredeccessor **********\n");
  currentNode = inorderPredeccessor(root, 50);
  if(currentNode == NULL)
  {
    printf("Inorder Predeccessor of node is not present in the Tree \n");
  }
  else
  {
    printf("Inorder Predeccessor = %d \n", currentNode->data);
  }

  currentNode = inorderPredeccessor(root, 100);
  if(currentNode == NULL)
  {
    printf("Inorder Predeccessor of node is not present in the Tree \n");
  }
  else
  {
    printf("Inorder Predeccessor = %d \n", currentNode->data);
  }
  printf("\n");

  printf("********** Testing remove node **********\n");
  i = 0;
  while(i < 13)
  {
    removeNode(&root, arr[i]);
    i++;
  }
  printf("\n");
  printf("Traversals After the Deletion Of Tree \n");
  printf("[START]->");
  inorderTraversal(root);
  printf("[END] \n");
  printf("\n");

  printf("[START]->");
  preorderTraversal(root);
  printf("[END] \n");
  printf("\n");

  printf("[START]->");
  postorderTraversal(root);
  printf("[END] \n");
  printf("\n");

  printf("********** Testing insertNode() for repopulating the Tree **********\n");

  for(i = 0; i<13; i++)
  {
    insertNode(&root, arr[i]);
  }

  printf("\n");

  printf("********** Testing inorderTraversal **********\n");
  printf("[START]->");
  inorderTraversal(root);
  printf("[END] \n");
  printf("\n");

  printf("********** Testing preorderTraversal **********\n");
  printf("[START]->");
  preorderTraversal(root);
  printf("[END] \n");
  printf("\n");

  printf("********** Testing postorderTraversal **********\n");
  printf("[START]->");
  postorderTraversal(root);
  printf("[END] \n");
  printf("\n");


  //Free the List
  freeList(root);

  return(0);

}

bNode *createNode(int newData)
{
  //Variable Declarations
  bNode *newNode = NULL;

  //Code
  newNode = (bNode *)malloc(sizeof(bNode));
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

void insertNode(bNode **root, int newData)
{
  //Function Declarations
  bNode *createNode(int);

  //Variable Declarations
  bNode *newNode = NULL;
  bNode *run = NULL;

  //Code
  newNode = createNode(newData);

  if(*root == NULL)
  {
    *root = newNode;
    return;
  }

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
      else
      {
        run = run->left;
      }
    }
    else
    {
      if(run->right == NULL)
      {
        run->right = newNode;
        newNode->parent = run;
        break;
      }
      else
      {
        run = run->right;
      }
    }
  }

}

void removeNode(bNode **root, int rData)
{
  //Function Declarations
  bNode *searchNode(bNode *, int);

  //Variable Declarations
  bNode *rNode = NULL;
  bNode *replaceNode = NULL;

  //Code
  rNode = searchNode(*root, rData);
  if(rNode == NULL)
  {
    printf("Node to be delete : %d is not present in the Tree \n", rData);
    return;
  }

  //Case 1 : rNode->left is NULL but rNode->right may be NULL or may not be NULL
  if(rNode->left == NULL)
  {
    if(rNode->parent == NULL)
    {
      *root = rNode->right;
    }
    else
    {
      if(rNode == rNode->parent->left)
      {
        rNode->parent->left = rNode->right;
      }
      else
      {
        if(rNode == rNode->parent->right)
        {
          rNode->parent->right = rNode->right;
        }
      }
    }

    //If rNode->right != NULL then update the parent of right subtree of rNoded
    if(rNode->right != NULL)
    {
      rNode->right->parent = rNode->parent;
    }

  }
  
  //Case 2 : If rNode->right == NULL and rNode->left != NULL
  else
  {
    if(rNode->right == NULL)
    {
      if(rNode->parent == NULL)
      {
        *root = rNode->left;
      }
      else
      {
        if(rNode == rNode->parent->left)
        {
          rNode->parent->left = rNode->left;
        }
        else
        {
          if(rNode == rNode->parent->right)
          {
            rNode->parent->right = rNode->left;
          }
        }
      }

      rNode->left->parent = rNode->parent;

    }

    //Case 3 : If rNode has both the sub-trees
    if((rNode->right != NULL) && (rNode->left != NULL))
    {
      replaceNode = rNode->right;
      while(replaceNode->left != NULL)
      {
        replaceNode = replaceNode->left;
      }

      if(replaceNode != rNode->right)
      {
        replaceNode->parent->left = replaceNode->right;
        if(replaceNode->right != NULL)
        {
          replaceNode->right->parent = replaceNode->parent;
        }

        replaceNode->right = rNode->right;
        replaceNode->right->parent = replaceNode;

      }

      replaceNode->left = rNode->left;
      replaceNode->left->parent = replaceNode;

      if(rNode->parent == NULL)
      {
        *root = replaceNode;
      }
      else
      {
        if(rNode == rNode->parent->left)
        {
          rNode->parent->left = replaceNode;
        }
        else
        {
          if(rNode == rNode->parent->right)
          {
            rNode->parent->right = replaceNode;
          }
        }
      }

      replaceNode->parent = rNode->parent;

    }

  }

  printf("We are freeing the node : %p || %d \n", (void *)rNode, rNode->data);
  free(rNode);
  rNode = NULL;

}

bNode *searchNode(bNode *root, int searchData)
{
  //Variable Declarations
  bNode *run = NULL;

  //Code
  run = root;

  while(run != NULL)
  {
    if(run->data == searchData)
    {
      return(run);
    }
    else
    {
      if(searchData < run->data)
      {
        run = run->left;
      }
      else
      {
        run = run->right;
      }
    }
  }
  return(NULL);
}

void inorderTraversal(bNode *root)
{
  //Variable Declarations
  bNode *run = NULL;

  //Code
  run = root;

  if(run != NULL)
  {
    inorderTraversal(run->left);
    printf("%d->", run->data);
    inorderTraversal(run->right);
  }
}

void preorderTraversal(bNode *root)
{
  //Variable Declarations
  bNode *run = NULL;

  //Code
  run = root;

  if(run != NULL)
  {
    printf("%d->", run->data);
    preorderTraversal(run->left);
    preorderTraversal(run->right);
  }
}

void postorderTraversal(bNode *root)
{
  //Variable Declarations
  bNode *run = NULL;

  //Code
  run = root;

  if(run != NULL)
  {
    postorderTraversal(run->left);
    postorderTraversal(run->right);
    printf("%d->", run->data);
  }
}

bNode *inorderSuccessor(bNode *root, int searchData)
{
  //Function Declarations
  bNode *searchNode(bNode *, int);

  //Variable Declarations
  bNode *run = NULL;
  bNode *currentNode = NULL;
  bNode *parentNode = NULL;

  //Code
  currentNode = searchNode(root, searchData);
  if(currentNode == NULL)
  {
    printf("searchData : %d is not available in the Tree \n", searchData);
    return(NULL);
  }

  if(currentNode->right != NULL)
  {
    run = currentNode->right;

    while(run->left != NULL)
    {
      run = run->left;
    }
    return(run);
  }

  parentNode = currentNode->parent;

  while((parentNode->parent != NULL) && (currentNode == parentNode->right))
  {
    currentNode = parentNode;
    parentNode = parentNode->parent;
  }

  return(parentNode);

}

bNode *inorderPredeccessor(bNode *root, int searchData)
{
  //Function Declarations
  bNode *searchNode(bNode *, int);

  //Variable Declarations
  bNode *run = NULL;
  bNode *currentNode = NULL;
  bNode *parentNode = NULL;

  //Code
  currentNode = searchNode(root, searchData);
  if(currentNode == NULL)
  {
    printf("searchData : %d is not available in the Tree \n", searchData);
    return(NULL);
  }

  if(currentNode->left != NULL)
  {
    run = currentNode->left;

    while(run->right != NULL)
    {
      run = run->right;
    }
    return(run);
  }

  parentNode = currentNode->parent;

  while((parentNode->parent != NULL) && (currentNode == parentNode->left))
  {
    currentNode = parentNode;
    parentNode = parentNode->parent;
  }

  return(parentNode);

}

void freeList(bNode *root)
{
  //Code
  if(root != NULL)
  {
    freeList(root->left);
    freeList(root->right);
    printf("We are freeing the node : %p \n", (void *)root);
    free(root);
    root = NULL;
  }
}