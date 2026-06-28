#include <iostream>

class EdgeNodes {
private:
  int edgeData;
  EdgeNodes *next;

  EdgeNodes() : next(nullptr) {}

  EdgeNodes(int newData) : edgeData(newData), next(nullptr) {}

  friend class VertexNodes;
  friend class Graph;
};

class VertexNodes {
private:
  int vertexData;
  EdgeNodes *edgeList;
  VertexNodes *next;

  VertexNodes() : edgeList(nullptr), next(nullptr) {}
  VertexNodes(int newData)
      : vertexData(newData), edgeList(new EdgeNodes()), next(nullptr) {}

  friend class Graph;
};

class Graph {
private:
  VertexNodes *vertexList;

  VertexNodes *findVertex(int);
  EdgeNodes *findEdge(VertexNodes *, int);

public:
  Graph() : vertexList(new VertexNodes()) {}

  Graph(const Graph &other) = delete;
  Graph& operator=(const Graph &other) = delete;

  void addVertex(int);
  void printGraph() const;
  void addEdge(int, int);
  ~Graph();
};

VertexNodes *Graph::findVertex(int vData) {
  VertexNodes *temp = vertexList->next;

  while (temp != nullptr) {
    if (temp->vertexData == vData) {
      return temp;
    }
    temp = temp->next;
  }

  return nullptr;
}

EdgeNodes *Graph::findEdge(VertexNodes *vList, int eData)
{
  EdgeNodes *temp = vList->edgeList->next;

  while(temp != nullptr)
  {
    if(temp->edgeData == eData)
    {
      return temp;
    }
    temp = temp->next;
  }

  return nullptr;
}

void Graph::addVertex(int vData) {

  if(findVertex(vData) != nullptr)
  {
    std::cout<<"Node is already present in the Graph"<<std::endl;
    return;
  }

  VertexNodes *temp = vertexList;
  while (temp->next != nullptr) {
    temp = temp->next;
  }
  temp->next = new VertexNodes(vData);
}

void Graph::printGraph() const {
  VertexNodes *temp = vertexList->next;

  while (temp != nullptr) {
    std::cout << "[" << temp->vertexData << "] : ";
    EdgeNodes *edgeTemp = temp->edgeList->next;

    while (edgeTemp != nullptr) {
      std::cout << "[" << edgeTemp->edgeData << "]-->";
      edgeTemp = edgeTemp->next;
    }
    std::cout << "[END]" << std::endl;
    temp = temp->next;
  }
}

void Graph::addEdge(int srcData, int destData)
{
  VertexNodes *srcNode = findVertex(srcData);
  VertexNodes *destNode = findVertex(destData);

  if((srcNode == nullptr) || (destNode == nullptr))
  {
    std::cout<<"Vertex Error"<<std::endl;
    return;
  }

  if((findEdge(srcNode, destData) != nullptr) || (findEdge(destNode, srcData) != nullptr))
  {
    std::cout<<"Edge Between : "<<srcData<<" "<<destData<<" is alredy existed"<<std::endl;
    return;
  }

  EdgeNodes *temp = srcNode->edgeList;
  while(temp->next != nullptr)
  {
    temp = temp->next;
  }
  temp->next = new EdgeNodes(destData);

  temp = destNode->edgeList;
  while(temp->next != nullptr)
  {
    temp = temp->next;
  }
  temp->next = new EdgeNodes(srcData);
}

Graph::~Graph()
{
  VertexNodes *temp = vertexList->next;
  
  while(temp != nullptr)
  {
    EdgeNodes *edgeTemp = temp->edgeList->next;

    while(edgeTemp != nullptr)
    {
      EdgeNodes *nextEdge = edgeTemp->next;
      delete edgeTemp;
      edgeTemp = nextEdge;
    }
    delete temp->edgeList;
    VertexNodes *tempNext = temp->next;
    delete temp;
    temp = tempNext;
  }
  delete vertexList;
}

int main(void) {
  Graph g;

  for (int i = 1; i < 11; i++) {
    g.addVertex(i);
  }

  g.addEdge(1,2);
  g.addEdge(3,2);
  g.addEdge(4,1);
  g.addEdge(5,7);
  g.addEdge(9,8);
  g.addEdge(8,1);
  g.addEdge(7,5);
  g.addEdge(4,7);
  g.addEdge(6,3);

  g.printGraph();

  return (0);
}
