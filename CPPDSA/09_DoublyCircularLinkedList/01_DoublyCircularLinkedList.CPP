#include<iostream>

class DNode{
  public:
  int data;
  DNode *next;
  DNode *prev;

  DNode()
  {
    this->next = nullptr;
    this->prev = nullptr;
  }

  DNode(int newData)
  {
    this->data = newData;
    this->next = nullptr;
    this->prev = nullptr;
  }
};

class linkedList{
  private:
  DNode *headNode;

  public:
  linkedList()
  {
    headNode = new DNode;
    headNode->next = headNode;
    headNode->prev = headNode;

    std::cout<<"headNode is created : "<<headNode<<"\n"<<std::endl;
  }

  ~linkedList()
  {

    std::cout<<"headNode->prev : "<<headNode->prev->data<<"\n";
    DNode *temp = headNode;
    headNode = headNode->next;

    while(headNode != temp)
    {
      DNode *temp2 = headNode;
      headNode = headNode->next;
      std::cout<<"We are freeing the node : "<<temp2<<"\n";
      delete temp2;
      temp2 = nullptr;
    }

    std::cout<<"We are freeing the headNode : "<<temp<<std::endl;
    delete temp;
    temp = nullptr;
  }
  
  void insertStart(int);
  void insertEnd(int);
  DNode *searchNode(int);
  void insertAfter(int, int);
  void insertBefore(int, int);
  void removeNode(int);
  int getStart();
  int getEnd();
  void removeStart();
  void removeEnd();
  int popStart();
  int popEnd();
  bool isEmpty();
  int lengthList();
  void showList();

};

void linkedList::insertStart(int newData)
{
  DNode *newNode = new DNode(newData);

  newNode->next = headNode->next;
  newNode->prev = headNode;

  if(headNode->next == headNode)
  {
    headNode->prev = newNode;
  }
  else
  {
    headNode->next->prev = newNode;
  }

  headNode->next = newNode;
}

void linkedList::insertEnd(int newData)
{
  DNode *temp = headNode;

  while(temp->next != headNode)
  {
    temp = temp->next;
  }

  DNode *newNode = new DNode(newData);

  newNode->next = temp->next;
  newNode->prev = temp;
  temp->next->prev = newNode;
  temp->next = newNode;
}

DNode *linkedList::searchNode(int searchData)
{
  DNode *temp = headNode->next;

  while(temp != headNode)
  {
    if(temp->data == searchData)
    {
      return(temp);
    }
    temp = temp->next;
  }

  return(nullptr);
}

void linkedList::insertAfter(int searchData, int newData)
{
  DNode *currentNode = searchNode(searchData);

  if(currentNode == nullptr)
  {
    std::cout<<"Data to be searched is not found : "<<searchData<<std::endl;
    exit(EXIT_FAILURE);
  }

  DNode *newNode = new DNode(newData);

  newNode->next = currentNode->next;
  newNode->prev = currentNode;

  if(currentNode->next == headNode)
  {
    currentNode->next->prev = newNode;
  }
  else
  {
    currentNode->next->prev = newNode;
  }
  currentNode->next = newNode;
}

void linkedList::insertBefore(int searchData, int newData)
{
  DNode *currentNode = searchNode(searchData);

  if(currentNode == nullptr)
  {
    std::cout<<"Data to be searched is not found : "<<searchData<<std::endl;
    exit(EXIT_FAILURE);
  }

  DNode *newNode = new DNode(newData);

  newNode->next = currentNode;
  newNode->prev = currentNode->prev;

  currentNode->prev->next = newNode;
  currentNode->prev = newNode;
}

void linkedList::removeNode(int rData)
{
  DNode *currentNode = searchNode(rData);
  
  if(currentNode == nullptr)
  {
    std::cout<<"Data to be removed not found rData : \n"<<rData;
    exit(EXIT_FAILURE);
  }
  
  currentNode->prev->next = currentNode->next;

  if(currentNode->next == headNode)
  {
    currentNode->next->prev = currentNode->prev;
  }
  else
  {
    currentNode->next->prev = currentNode->prev;
  }

  delete currentNode;
  currentNode = nullptr;

}

bool linkedList::isEmpty()
{
  if(headNode->next == headNode)
  {
    return(true);
  }
  else{
    return(false);
  }
}

int linkedList::getStart()
{
  if(isEmpty())
  {
    std::cout<<"Cannot applied getStart() on empty list \n";
    exit(EXIT_FAILURE);
  }

  return(headNode->next->data);
}

int linkedList::popStart()
{
  if(isEmpty())
  {
    std::cout<<"Cannot applied popStart() on empty list \n";
    exit(EXIT_FAILURE);
  }

  DNode *temp = headNode->next;

  headNode->next = temp->next;
  temp->next->prev = temp->prev;
  
  int data = temp->data;

  delete temp;
  temp = nullptr;

  return(data);
}


int linkedList::popEnd()
{
  if(isEmpty())
  {
    std::cout<<"Cannot applied popEndt() on empty list \n";
    exit(EXIT_FAILURE);
  }

  DNode *temp = headNode->next;

  while(temp->next != headNode)
  {
    temp = temp->next;
  }

  int data = temp->data;

  temp->prev->next = temp->next;
  temp->next->prev = temp->prev;

  delete temp;
  temp = nullptr;

  return(data);

}

int linkedList::getEnd()
{
  if(isEmpty())
  {
    std::cout<<"Cannot applied getEndt() on empty list \n";
    exit(EXIT_FAILURE);
  }

  DNode *temp = headNode->next;

  while(temp->next != headNode)
  {
    temp = temp->next;
  }

  return(temp->data);

}


void linkedList::removeStart()
{
  if(isEmpty())
  {
    std::cout<<"Cannot applied popStart() on empty list \n";
    exit(EXIT_FAILURE);
  }

  DNode *temp = headNode->next;

  headNode->next = temp->next;
  temp->next->prev = temp->prev;

  delete temp;
  temp = nullptr;
}


void linkedList::removeEnd()
{
  if(isEmpty())
  {
    std::cout<<"Cannot applied popEndt() on empty list \n";
    exit(EXIT_FAILURE);
  }

  DNode *temp = headNode->next;

  while(temp->next != headNode)
  {
    temp = temp->next;
  }

  temp->prev->next = temp->next;
  temp->next->prev = temp->prev;

  delete temp;
  temp = nullptr;

}

int linkedList::lengthList()
{
  int count = 0;

  DNode *temp = headNode->next;

  while(temp != headNode)
  {
    count++;
    temp = temp->next;
  }

  return(count);
}


void linkedList::showList()
{
  DNode *temp = headNode->next;

  std::cout<<"[START]-->";
  while(temp != headNode)
  {
    std::cout<<"<--["<<temp->data<<"]-->";
    temp = temp->next;
  }
  std::cout<<"[END]"<<std::endl;
}

int main(int argc, char *argv[], char *envp[])
{
  //Code
  linkedList L1;

  std::cout<<"----------Testing isEmpty()----------\n";
  bool test = L1.isEmpty();
  std::cout<<"Linked List Empty : "<<test<<"\n";

  std::cout<<"\n";

  std::cout<<"----------Testing insertStart()----------\n";
  for(int i = 1; i<6; i++)
  {
    L1.insertStart(10*i);
  }
  L1.showList();
  
  std::cout<<"\n";

  std::cout<<"----------Testing insertEnd()----------\n";
  for(int i = 6; i<11; i++)
  {
    L1.insertEnd(10*i);
  }
  L1.showList();

  std::cout<<"\n";

  std::cout<<"----------Testing searchNode() for middle node----------\n";
  DNode *currentNode = L1.searchNode(10);
  if(currentNode == nullptr)
  {
    std::cout<<"searchData is not present in the List \n";
  }
  else
  {
    std::cout<<"searchData is found at position : "<<currentNode<<"\n";
  }

  std::cout<<"\n";
  
  std::cout<<"----------Testing searchNode() for last node----------\n";
  currentNode = L1.searchNode(100);
  if(currentNode == nullptr)
  {
    std::cout<<"searchData is not present in the List \n";
  }
  else
  {
    std::cout<<"searchData is found at position : "<<currentNode<<"\n";
  }

  std::cout<<"\n";

  std::cout<<"----------Testing searchNode() for start node----------\n";
  currentNode = L1.searchNode(50);
  if(currentNode == nullptr)
  {
    std::cout<<"searchData is not present in the List \n";
  }
  else
  {
    std::cout<<"searchData is found at position : "<<currentNode<<"\n";
  }

  std::cout<<"\n";

  std::cout<<"---------Testing insertAfter() for middle node---------\n";
  L1.insertAfter(10, 5000);
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing insertAfter() for first node---------\n";
  L1.insertAfter(50, 6000);
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing insertAfter() for last node---------\n";
  L1.insertAfter(100, 7000);
  L1.showList();

  std::cout<<"\n";
  
  std::cout<<"---------Testing insertBefore() for middle node---------\n";
  L1.insertBefore(10, 500);
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing insertBefore() for first node---------\n";
  L1.insertBefore(50, 600);
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing insertBefore() for last node---------\n";
  L1.insertBefore(100, 700);
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing removeNode() for middle node---------\n";
  L1.removeNode(10);
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing removeNode() for first node---------\n";
  L1.removeNode(600);
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing removeNode() for last node---------\n";
  L1.removeNode(7000);
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing getStart()---------\n";
  int firstData = L1.getStart();
  std::cout<<"First data : "<<firstData<<"\n";
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing getEnd()---------\n";
  int last = L1.getEnd();
  std::cout<<"Last data : "<<last<<"\n";
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing popStart()---------\n";
  firstData = L1.popStart();
  std::cout<<"First data : "<<firstData<<"\n";
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing popEnd()---------\n";
  last = L1.popEnd();
  std::cout<<"Last data : "<<last<<"\n";
  L1.showList();

  std::cout<<"\n";
  
  std::cout<<"---------Testing removeStart()---------\n";
  L1.removeStart();
  L1.showList();

  std::cout<<"\n";

  std::cout<<"---------Testing removeEnd()---------\n";
  L1.removeEnd();
  L1.showList();

  std::cout<<"\n";

  std::cout<<"Curent length of Linked List : "<<L1.lengthList()<<"\n";


  return(0);
}
