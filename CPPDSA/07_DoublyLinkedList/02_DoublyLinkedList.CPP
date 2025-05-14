#include<iostream>

class DNode{

  public:
  int data;
  DNode *prev;
  DNode *next;

  DNode()
  {
    this->prev = nullptr;
    this->next = nullptr;
  }

  DNode(int newData)
  {
    this->data = newData;
    this->prev = nullptr;
    this->next = nullptr;
  }

};

class DoublyLinkedList{

  private:
  DNode *headNode;

  public:

  DoublyLinkedList()
  {
    this->headNode = new DNode;
    std::cout<<"headNode is created with address : "<<headNode<<" headNode->prev : "<<headNode->prev<<" headNode->next : "<<headNode->next<<std::endl;
  }

  void insertStart(int newData);
  void insertEnd(int newData);
  DNode *searchNode(int existingData);
  void insertAfter(int existingData, int newData);
  void insertBefore(int existingData, int newData);
  int isEmpty();
  int getFirst();
  int getLast();
  int popFirst();
  int popEnd();
  void removeFirst();
  void removeEnd();
  void showList();

  ~DoublyLinkedList()
  {
    DNode *temp;

    while(headNode != nullptr)
    {
      temp = headNode;
      headNode = temp->next;
      temp->prev = nullptr;
      std::cout<<"Freeing the memory : "<<temp<<" headNode is having the next address : "<<headNode<<std::endl;
    }
  }


};

void DoublyLinkedList::insertStart(int newData)
{
  DNode *newNode = new DNode(newData);

  newNode->next = headNode->next;
  newNode->prev = headNode;

  if(headNode->next != nullptr)
  {
    headNode->next->prev = newNode;
  }
  headNode->next = newNode;

  std::cout<<"newNode is created at the start with address : "<<newNode<<" newNode->prev : "<<newNode->prev<<" newNode->next : "<<newNode->next<<std::endl;
}

void DoublyLinkedList::insertEnd(int newData)
{
  DNode *newNode = new DNode(newData);

  DNode *temp = headNode;

  while(temp->next != nullptr)
  {
    temp = temp->next;
  }

  temp->next = newNode;
  newNode->prev = temp;

  std::cout<<"newNode is created at the end with address : "<<newNode<<" newNode->prev : "<<newNode->prev<<" newNode->next : "<<newNode->next<<std::endl;

}

DNode *DoublyLinkedList::searchNode(int existingData)
{
  DNode *temp = headNode->next;

  while(temp != nullptr)
  {
    if(temp->data == existingData)
      return(temp);

    temp = temp->next;
  }

  return(nullptr);
}

void DoublyLinkedList::insertAfter(int existingData, int newData)
{
  DNode *existingNode = searchNode(existingData);

  if(existingNode == nullptr)
  {
    std::cout<<"Failed to find the existingData : "<<existingData<<std::endl;
    exit(EXIT_FAILURE);
  }
  
  DNode *newNode = new DNode(newData);
  
  newNode->next = existingNode->next;
  newNode->prev = existingNode;

  if(existingNode->next != nullptr)
  {
    existingNode->next->prev = newNode;
  }
  existingNode->next = newNode;

  std::cout<<"newNode is created and insertAfter with address : "<<newNode<<" newNode->prev : "<<newNode->prev<<" newNode->next : "<<newNode->next<<std::endl;
 
}

void DoublyLinkedList::insertBefore(int existingData, int newData)
{
  DNode *existingNode = searchNode(existingData);

  if(existingNode == nullptr)
  {
    std::cout<<"Failed to find the existingData : "<<existingData<<std::endl;
    exit(EXIT_FAILURE);
  }

  DNode *newNode = new DNode(newData);

  newNode->next = existingNode;
  newNode->prev = existingNode->prev;
  existingNode->prev->next = newNode;
  existingNode->prev = newNode;


  std::cout<<"newNode is created and insertBefore with address : "<<newNode<<" newNode->prev : "<<newNode->prev<<" newNode->next : "<<newNode->next<<std::endl;

}

int DoublyLinkedList::isEmpty()
{
  if(headNode->next == NULL)
  {
    return(1);
  }
  else{
    return(0);
  }
}

int DoublyLinkedList::getFirst()
{
  if(isEmpty())
  {
    std::cout<<"Failed to apply getFirst() on empty list"<<std::endl;
    exit(EXIT_FAILURE);
  }

  return(headNode->next->data);
}

int DoublyLinkedList::getLast()
{
  if(isEmpty())
  {
    std::cout<<"Failed to apply getLast() on empty list"<<std::endl;
    exit(EXIT_FAILURE);
  }

  DNode *temp = headNode->next;
  while(temp->next != NULL)
  {
    temp = temp->next;
  }

  return(temp->data);
}

int DoublyLinkedList::popFirst()
{
  if(isEmpty())
  {
    std::cout<<"Failed to apply popFirst() on empty list"<<std::endl;
    exit(EXIT_FAILURE);
  }
  
  DNode *temp = headNode->next;

  headNode->next = temp->next;

  if(temp->next != nullptr)
  {
    temp->next->prev = headNode;
  }

  int data = temp->data;

  std::cout<<"Node is freed : "<<temp<<std::endl;
  
  delete temp;
  temp = nullptr;

  return(data);

}


int DoublyLinkedList::popEnd()
{
  if(isEmpty())
  {
    std::cout<<"Failed to apply popEnd() on empty list"<<std::endl;
    exit(EXIT_FAILURE);
  }

  DNode *temp = headNode->next;


  while(temp->next != nullptr)
  {
    temp = temp->next;
  }

  int data = temp->data;

  temp->prev->next = nullptr;

  std::cout<<"Node is freed : "<<temp<<std::endl;

  delete temp;
  temp = nullptr;

  return(data);
}



void DoublyLinkedList::removeFirst()
{
  if(isEmpty())
  {
    std::cout<<"Failed to apply removeFirst() on empty list"<<std::endl;
    exit(EXIT_FAILURE);
  }
  
  DNode *temp = headNode->next;

  headNode->next = temp->next;

  if(temp->next != nullptr)
  {
    temp->next->prev = headNode;
  }

  std::cout<<"Node is freed : "<<temp<<std::endl;
  
  delete temp;
  temp = nullptr;

}


void DoublyLinkedList::removeEnd()
{
  if(isEmpty())
  {
    std::cout<<"Failed to apply removeEnd() on empty list"<<std::endl;
    exit(EXIT_FAILURE);
  }

  DNode *temp = headNode->next;


  while(temp->next != nullptr)
  {
    temp = temp->next;
  }

  temp->prev->next = nullptr;

  std::cout<<"Node is freed : "<<temp<<std::endl;

  delete temp;
  temp = nullptr;

}


void DoublyLinkedList::showList()
{
  DNode *temp;

  temp = headNode->next;

  std::cout<<"[START]<->";
  while(temp != nullptr)
  {
    std::cout<<temp->data<<"<->";
    temp = temp->next;
  }
  std::cout<<"[END]"<<std::endl;
}



int main(void)
{
  DoublyLinkedList D1;

  for(int i = 1; i < 6; i++)
  {
    D1.insertStart(10*i);
  }

  for(int i = 6; i < 11; i++)
  {
    D1.insertEnd(10*i);
  }

  D1.showList();

  std::cout<<"--------Testing searchNode()----------"<<std::endl;
  DNode *searchData = D1.searchNode(-100);

  if(searchData)
  {
    std::cout<<"Data is present in the list at address : "<<searchData<<" searchData->prev : "<<searchData->prev<<" searchData->next : "<<searchData->next<<std::endl;
  }
  else{
    std::cout<<"Data is not present in the List"<<std::endl;
  }

  std::cout<<"----------Testing insertAfter()----------"<<std::endl;
  D1.insertAfter(30, 3333);
  D1.showList();
  std::cout<<"\n\n";

  std::cout<<"----------Testing insertBefore()----------"<<std::endl;
  D1.insertBefore(10, 5555);
  D1.showList();
  std::cout<<"\n\n";

  std::cout<<"----------Testing getFirst()----------"<<std::endl;
  int data = D1.getFirst();
  std::cout<<"First Data in Linked List is : "<<data<<std::endl;
  std::cout<<"Printing the Linked List After getFirst()"<<std::endl;
  D1.showList();
  std::cout<<"\n\n";

  std::cout<<"----------Testing getLast()----------"<<std::endl;
  int lastData = D1.getLast();
  std::cout<<"Last Data in Linked List is : "<<lastData<<std::endl;
  std::cout<<"Printing the Linked List After getLast()"<<std::endl;
  D1.showList();
  std::cout<<"\n\n";


  std::cout<<"----------Testing popFirst()----------"<<std::endl;
  int popFirstData = D1.popFirst();
  std::cout<<"First Data popped in Linked List is : "<<popFirstData<<std::endl;
  std::cout<<"Printing the Linked List After popFirst()"<<std::endl;
  D1.showList();
  std::cout<<"\n\n";


  std::cout<<"----------Testing popEnd()----------"<<std::endl;
  int popLastData = D1.popEnd();
  std::cout<<"Last Data popped in Linked List is : "<<popLastData<<std::endl;
  std::cout<<"Printing the Linked List After popEnd()"<<std::endl;
  D1.showList();
  std::cout<<"\n\n";

  std::cout<<"----------Testing removeFirst()----------"<<std::endl;
  D1.removeFirst();
  std::cout<<"Printing the Linked List After removeFirst()"<<std::endl;
  D1.showList();
  std::cout<<"\n\n";


  std::cout<<"----------Testing removeEnd()----------"<<std::endl;
  D1.removeEnd();
  std::cout<<"Printing the Linked List After removeEnd()"<<std::endl;
  D1.showList();
  std::cout<<"\n\n";


  return(0);
}
