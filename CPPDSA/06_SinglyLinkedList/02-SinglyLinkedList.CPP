#include<iostream>

class SNode{
  public:
  int data;
  SNode *next;

  SNode()
  {
    this->next = nullptr;
  }

  SNode(int newData)
  {
    this->data = newData;
    this->next = nullptr;
  }
};

class SinglyLinkedList{
  private:
  SNode *headNode;

  public:
  SinglyLinkedList()
  {
    headNode = new SNode;
  }

  ~SinglyLinkedList()
  {
    //Variable Declarations
    SNode *temp;

    //Code
    while(headNode != nullptr)
    {
      temp = headNode;
      headNode = headNode->next;
      std::cout<<"We are freeing the node : "<<temp<<"\n";
      delete temp;
    }
  }
  
  void insertStart(int);
  void insertEnd(int);
  SNode *searchNode(SNode **, int);
  void insertAfter(int, int);
  void insertBefore(int, int);
  void showList();

};

void SinglyLinkedList::insertStart(int newData)
{
  //Variable Declarations
  SNode *newNode;

  //Code
  newNode = new SNode(newData);

  newNode->next = headNode->next;
  headNode->next = newNode;
}

void SinglyLinkedList::insertEnd(int newData)
{
  //Variable Declarations
  SNode *run;
  SNode *newNode;

  //Code
  run = headNode;

  while(run->next != nullptr)
  {
    run = run->next;
  }

  newNode = new SNode(newData);

  run->next = newNode;

}

void SinglyLinkedList::showList()
{
  //Variable Declarations
  SNode *run;

  //Code
  run = headNode->next;
  std::cout<<"[START]-->";
  while(run != nullptr)
  {
    std::cout<<run->data<<"-->";
    run = run->next;
  }
  std::cout<<"[END]\n\n";

}

void SinglyLinkedList::insertAfter(int searchData, int newData)
{

}

SNode *SinglyLinkedList::searchNode(SNode **prevNode, int searchData)
{
  //Variable Declarations
  SNode *run;

  //Code
  run = headNode->next;
  *prevNode = headNode;

  while(run != nullptr)
  {
    if(searchData == run->data)
    {
      return(run);
    }
    else
    {
      *prevNode = run;
      run = run->next;
    }
  }

  return(nullptr);
}

int main(int argc, char *argv[], char *envp[])
{

  SinglyLinkedList S1;
  
  std::cout<<"----------Testing insertStart()----------\n";
  for(int i = 1; i<6; i++)
  {
    S1.insertStart(10*i);
  }
  S1.showList();

  std::cout<<"----------Testing insertEnd()----------\n";
  for(int i = 6; i<11; i++)
  {
    S1.insertEnd(10*i);
  }
  S1.showList();

  SNode *currentNode;
  SNode *prevNode;

  std::cout<<"----------Testing searchNode() for middle node----------\n";
  currentNode = S1.searchNode(&prevNode, 10);
  if(currentNode == nullptr)
  {
    std::cout<<"No searchData found in the List \n";
  }
  else
  {
    std::cout<<"currentData is found at location : "<<currentNode<<" : "<<currentNode->data<<" || having previous node : "<<prevNode<<" : "<<prevNode->data<<"\n";
  }

  std::cout<<"----------Testing searchNode() for first node----------\n";
  currentNode = S1.searchNode(&prevNode, 50);
  if(currentNode == nullptr)
  {
    std::cout<<"No searchData found in the List \n";
  }
  else
  {
    std::cout<<"currentData is found at location : "<<currentNode<<" : "<<currentNode->data<<" || having previous node : "<<prevNode<<" : "<<prevNode->data<<"\n";
  }


  std::cout<<"----------Testing searchNode() for last node----------\n";
  currentNode = S1.searchNode(&prevNode, 100);
  if(currentNode == nullptr)
  {
    std::cout<<"No searchData found in the List \n";
  }
  else
  {
    std::cout<<"currentData is found at location : "<<currentNode<<" : "<<currentNode->data<<" || having previous node : "<<prevNode<<" : "<<prevNode->data<<"\n";
  }

  return(0);
}
