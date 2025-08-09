#include<iostream>

static int totalNodes = 0;

class DNode{
public:
int data;
DNode *next;
DNode *prev;

DNode(int newData)
{
  this->data = newData;
  this->next = nullptr;
  this->prev = nullptr;

  totalNodes++;
}

};

class DoublyLinkedList{
private:
DNode *headNode;

public:
DoublyLinkedList()
{
  headNode = new DNode(-1);
  headNode->next = headNode;
  headNode->prev = headNode;

  std::cout<<"headNode is created "<<headNode<<"\n";
}

~DoublyLinkedList()
{
  DNode *run = headNode->next;

  while(run != headNode)
  {
    DNode *runNext = run->next;

    delete run;
    totalNodes--;

    run = runNext;
  }

  delete run;
  totalNodes--;

  std::cout<<"Total Nodes destroyed are : "<<totalNodes<<std::endl;
}

void insertEnd(int);
void printList();
DNode *searchNode(int);
void removeNode(int);


};

void DoublyLinkedList::removeNode(int rData)
{
  DNode *rNode = searchNode(rData);

  if(rNode == nullptr)
  {
    std::cout<<rData<<" is not present in the List \n";
    return;
  }
  
  rNode->prev->next = rNode->next;
  rNode->next->prev = rNode->prev;

  delete rNode;
  totalNodes--;

}

DNode *DoublyLinkedList::searchNode(int searchData)
{
  DNode *run = headNode->next;

  while(run != headNode)
  {
    if(run->data == searchData)
    {
      return(run);
    }

    run = run->next;
  }

  return(nullptr);
}

void DoublyLinkedList::insertEnd(int newData)
{
  DNode *newNode = new DNode(newData);

  newNode->next = headNode;
  newNode->prev = headNode->prev;

  headNode->prev->next = newNode;
  headNode->prev = newNode;
}

void DoublyLinkedList::printList()
{
  DNode *run = headNode->next;

  std::cout<<"[START]<-->";
  while(run != headNode)
  {
    std::cout<<run->data<<"<-->";
    run = run->next;
  }
  std::cout<<"[END]\n\n";
}

int main(int argc, char *argv[], char *envp[])
{
  DoublyLinkedList D1;

  for(int i = 1; i < 10; i++)
  {
    D1.insertEnd(10*i);
  }

  D1.printList();

  D1.removeNode(50);
  D1.printList();

  std::cout<<"Total Nodes Created Are : "<<totalNodes<<"\n";

  return(0);
}
