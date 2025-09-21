#include<iostream>

class DNode {
    public:
    int data;
    DNode *next;
    DNode *prev;

    DNode(int newData)
    {
      this->data = newData;
      this->next = nullptr;
      this->prev = nullptr;
    }
  };


class DCL {
  private:
  DNode *headNode;

  public:
  DCL() 
  {
    headNode = new DNode(-1);
    headNode->next = headNode;
    headNode->prev = headNode;

    std::cout<<"headNode is created : "<<headNode<<"\n";
  }

  ~DCL()
  {
    DNode *run = headNode->next;

    while(run != headNode)
    {
      DNode *runNext = run->next;
      std::cout<<"Node is freed having memory address : "<<run<<"\n";
      delete run;
      run = nullptr;

      run = runNext;
    }

    std::cout<<"headNode is also freed : "<<headNode<<std::endl;
    delete headNode;
  }
  

  //Function Declarations
  DNode *createNode(int);
  void insertEnd(int);
  void printList();

};

DNode *DCL::createNode(int newData)
{
  DNode *newNode = new DNode(newData);

  if(newNode == nullptr)
  {
    std::cout<<"Failed to allocate the memory to the newNode"<<std::endl;
    exit(EXIT_FAILURE);
  }

  return(newNode);
}

void DCL::insertEnd(int newData)
{
  DNode *newNode = createNode(newData);

  newNode->next = headNode;
  newNode->prev = headNode->prev;

  headNode->prev->next = newNode;
  headNode->prev = newNode;
}

void DCL::printList()
{
  DNode *run = headNode->next;

  while(run != headNode)
  {
    std::cout<<"["<<run->data<<"]-->";
    run = run->next;
  }
  std::cout<<"\n";
}

int main(int argc, char *argv[], char *envp[])
{

  DCL dList;
  
  for(int i = 1; i<10; i++)
  {
    dList.insertEnd(10*i);
  }

  dList.printList();

  return(0);
}
