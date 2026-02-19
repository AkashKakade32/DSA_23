#include <cstdlib>
#include <iostream>

class DNode {
public:
  int data;
  DNode *next;
  DNode *prev;

  DNode(int newData) : data(newData) {
    next = nullptr;
    prev = nullptr;
  }

  DNode() {};
};

class DCL {
private:
  DNode *headNode;

public:
  DCL() {
    headNode = new DNode();
    headNode->next = headNode;
    headNode->prev = headNode;

    std::cout << "headNode is created : " << headNode << std::endl;
  }

  ~DCL() {
    DNode *run = headNode->next;

    while (run != headNode) {
      DNode *runNext = run->next;
      std::cout << "We are freeing the node : " << run << std::endl;
      delete run;
      run = runNext;
    }

    std::cout << "We are deleting the headNode : " << run << std::endl;
    delete run;
  }

  void insertStart(int num);
  void insertEnd(int num);
  int pop();
  void printList();
};

void DCL::insertStart(int num) {
  DNode *newNode = new DNode(num);

  newNode->next = headNode->next;
  newNode->prev = headNode;

  headNode->next = newNode;
  newNode->next->prev = newNode;
}

void DCL::insertEnd(int num) {
  DNode *newNode = new DNode(num);

  newNode->next = headNode;
  newNode->prev = headNode->prev;

  headNode->prev->next = newNode;
  headNode->prev = newNode;
}

int DCL::pop() {
  DNode *run = headNode->next;

  if (run == headNode) {
    std::cout << "Stack is empty" << std::endl;
    exit(EXIT_FAILURE);
  }

  int popNum = run->data;
  headNode->next = run->next;
  run->next->prev = headNode;

  delete run;

  return (popNum);
}

void DCL::printList() {
  DNode *run = headNode->next;

  std::cout << "[START]-->";
  while (run != headNode) {
    std::cout << "[" << run->data << "]" << "-->";
    run = run->next;
  }
  std::cout << "[END]" << std::endl;
}

int main(void) {
  DCL dl;

  for (int i = 1; i < 11; i++) {
    dl.insertStart(i);
  }

  for (int i = 2; i < 21; i++) {
    dl.insertEnd(i);
  }

  dl.printList();

  for (int i = 0; i < 10; i++) {
    int a = dl.pop();
    std::cout << "Popped Element is : " << a << std::endl;
  }

  dl.printList();

  return (0);
}
