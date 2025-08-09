#include<iostream>

class DNode{
private:
int data;
DNode *parent;
DNode *left;
DNode *right;

DNode(int data = -1)
{
    this->data = data;
    this->parent = nullptr;
    this->left = nullptr;
    this->right = nullptr;
}

friend class BinarySearchTree;

};

class BinarySearchTree{
private:
DNode *rootNode = nullptr;

public:
BinarySearchTree() = default;


void printTree()
{
    DNode *run = rootNode;

    std::cout<<"Preorder Traversal --> ";
    preorderTraversal(run);
    std::cout<<"[END] \n\n";

    std::cout<<"Inorder Traversal --> ";
    inorderTraversal(run);
    std::cout<<"[END] \n\n";
}

~BinarySearchTree()
{
    if(rootNode == nullptr)
    {
        return;
    }

    freeTree(rootNode);
    std::cout<<"All nodes are freed"<<std::endl;
}


void createNode(int);
void preorderTraversal(DNode *);
void inorderTraversal(DNode *);

void freeTree(DNode *);

};

void BinarySearchTree::createNode(int data)
{
    DNode *newNode = new DNode(data);

    if(rootNode == nullptr)
    {
        rootNode = newNode;
        std::cout<<"Root node is created with address "<<rootNode<<" Data = "<<rootNode->data<<"\n";
    }
    else
    {
        DNode *run = rootNode;

        while(true)
        {
            if(data <= run->data)
            {
                if(run->left == nullptr)
                {
                    run->left = newNode;
                    newNode->parent = run;
                    std::cout<<"NewNode is created at left "<<newNode<<" "<<newNode->data<<" Parent "<<newNode->parent->data<<"\n";
                    break;
                }
                else
                {
                    run = run->left;
                }
            }
            else
            {
                if(run->right == nullptr)
                {
                    run->right = newNode;
                    newNode->parent = run;
                    std::cout<<"NewNode is created at right "<<newNode<<" "<<newNode->data<<" Parent "<<newNode->parent->data<<"\n";

                    break;
                }
                else
                {
                    run = run->right;
                }
            }
        }
    }
}

void BinarySearchTree::preorderTraversal(DNode *dataNode)
{
    if(dataNode != nullptr)
    {
        std::cout<<dataNode->data<<"-->"<<" ";
        preorderTraversal(dataNode->left);
        preorderTraversal(dataNode->right);
    }
}


void BinarySearchTree::inorderTraversal(DNode *dataNode)
{
    if(dataNode != nullptr)
    {
        preorderTraversal(dataNode->left);
        std::cout<<dataNode->data<<"-->"<<" ";
        preorderTraversal(dataNode->right);
    }
}


void BinarySearchTree::freeTree(DNode *rootNode)
{
    if(rootNode != nullptr)
    {
        freeTree(rootNode->left);
        freeTree(rootNode->right);
        delete rootNode;
    }

}

int main(int argc , char *argv[], char *envp[])
{
    BinarySearchTree B1;

    int alloc[10] = {10, 5, 20, 11, 28, 32, 3, 6, 34, 13};

    for(int i = 0; i < 10; i++)
    {
        B1.createNode(alloc[i]);
    }

    B1.printTree();

    return(1);
}