#include<iostream>

class Graph;

class EdgeNodes
{
    private:
    int edgeData;
    int weight;
    EdgeNodes *next;

    EdgeNodes() : next(nullptr) {}
    EdgeNodes(int newData, int newWeight) : edgeData(newData), weight(newWeight), next(nullptr) {}

    friend class VertexNodes;
    friend class Graph;
    friend std::ostream& operator<<(std::ostream &out, const Graph &g);

};

class VertexNodes
{
    private:
    int vertexData;
    EdgeNodes *edgeList;
    VertexNodes *next;

    VertexNodes() : edgeList(nullptr), next(nullptr) {}
    VertexNodes(int newData) : vertexData(newData), edgeList(new EdgeNodes()), next(nullptr)
    {
        edgeList->next = nullptr;
    }

    friend class Graph;
    friend std::ostream& operator<<(std::ostream &out, const Graph &g);
};

class Graph
{
    private:
    VertexNodes *vertexList;

    VertexNodes *findVertex(const int) const;
    EdgeNodes *findEdge(const VertexNodes *, const int) const;

    public:
    Graph() : vertexList(new VertexNodes())
    {
        vertexList->next = nullptr;
    }

    Graph(const Graph &oth) = delete;
    Graph &operator=(const Graph &oth) = delete;

    void addVertex(const int);
    void addEdge(const int, const int, const int);
    void removeEdge(const int srcData, const int destData);
    void removeVertex(const int);

    friend std::ostream& operator<<(std::ostream &out, const Graph &g);

    ~Graph();

};

VertexNodes *Graph::findVertex(const int vData) const
{
    VertexNodes *temp = vertexList->next;

    while(temp != nullptr)
    {
        if(temp->vertexData == vData)
        {
            return(temp);
        }
        temp = temp->next;
    }

    return(nullptr);
}

EdgeNodes *Graph::findEdge(const VertexNodes *vList, const int eData) const
{
    EdgeNodes *temp = vList->edgeList->next;

    while(temp != nullptr)
    {
        if(temp->edgeData == eData)
        {
            return(temp);
        }

        temp = temp->next;
    }

    return(nullptr);
}

void Graph::addVertex(const int vData)
{
    if(findVertex(vData) != nullptr)
    {
        std::cout<<"Vertex : "<<vData<<" is already present in the Graph."<<std::endl;
        return;
    }

    VertexNodes *temp = vertexList;

    while(temp->next != nullptr)
    {
        temp = temp->next;
    }
    temp->next = new VertexNodes(vData);
}

void Graph::addEdge(const int srcData, const int destData, const int weight)
{
    VertexNodes *srcNode = findVertex(srcData);
    VertexNodes *destNode = findVertex(destData);

    if((srcNode == nullptr) || (destNode == nullptr))
    {
        std::cout<<"Vertex Error to add Edge between : "<<srcData<<destData<<std::endl;
        return;
    }

    if((findEdge(srcNode, destData) != nullptr) || (findEdge(destNode, srcData) != nullptr))
    {
        std::cout<<"Edge Between : "<<srcData<<" "<<destData<<" is already present."<<std::endl;
        return;
    }

    EdgeNodes *temp = srcNode->edgeList;
    while(temp->next != nullptr)
    {
        temp = temp->next;
    }
    temp->next = new EdgeNodes(destData, weight);

    temp = destNode->edgeList;
    while(temp->next != nullptr)
    {
        temp = temp->next;
    }
    temp->next = new EdgeNodes(srcData, weight);
}

void Graph::removeEdge(int src, int dest)
{
    VertexNodes *srcNode = findVertex(src);
    VertexNodes *destNode = findVertex(dest);

    if((srcNode == nullptr) || (destNode == nullptr))
    {
        std::cout<<"Vertices are not present in the Graph"<<std::endl;
        return;
    }

    EdgeNodes *srcToDest = findEdge(srcNode, dest);
    EdgeNodes *destToSrc = findEdge(destNode, src);

    if((srcToDest == nullptr) || (destToSrc == nullptr))
    {
        std::cout<<"Edges are not present in the Graph"<<std::endl;
        return;
    }

    EdgeNodes *temp = srcNode->edgeList;
    while(temp->next != srcToDest)
    {
        temp = temp->next;
    }
    temp->next = srcToDest->next;
    delete srcToDest;

    temp = destNode->edgeList;
    while(temp->next != destToSrc)
    {
        temp = temp->next;
    }
    temp->next = destToSrc->next;
    delete destToSrc;

}

void Graph::removeVertex(const int vData)
{
    VertexNodes *temp = findVertex(vData);

    if(temp == nullptr)
    {
        std::cout<<"Vertex is not present in the Graph"<<std::endl;
        return;
    }

    EdgeNodes *edgeTemp = temp->edgeList->next;

    while(edgeTemp != nullptr)
    {
        VertexNodes *edgeInV = findVertex(edgeTemp->edgeData);

        EdgeNodes *vInEdge = findEdge(edgeInV, vData);

        EdgeNodes *tempEdgeNode = edgeInV->edgeList;
        while(tempEdgeNode->next != vInEdge)
        {
            tempEdgeNode = tempEdgeNode->next;
        }
        tempEdgeNode->next = vInEdge->next;
        delete vInEdge;

        EdgeNodes* edgeTempNext = edgeTemp->next;
        delete edgeTemp;
        edgeTemp = edgeTempNext;
    }

    delete temp->edgeList;

    VertexNodes *mainTemp = vertexList;

    while(mainTemp->next != temp)
    {
        mainTemp = mainTemp->next;
    }
    mainTemp->next = temp->next;
    delete temp;

}

Graph::~Graph()
{
    VertexNodes *temp = vertexList->next;

    while(temp != nullptr)
    {
        EdgeNodes *tempEdge = temp->edgeList->next;

        while(tempEdge != nullptr)
        {
            EdgeNodes *tempEdgeNext = tempEdge->next;
            delete tempEdge;
            tempEdge = tempEdgeNext;
        }
        delete temp->edgeList;

        VertexNodes *tempNext = temp->next;
        delete temp;
        temp = tempNext; 
    }

    delete vertexList;
}

std::ostream& operator<<(std::ostream &out, const Graph &g)
{
    VertexNodes *temp = g.vertexList->next;

    while(temp != nullptr)
    {
        out<<"Vertex : ["<<temp->vertexData<<"] :: ";

        EdgeNodes *tempEdge = temp->edgeList->next;
        while(tempEdge != nullptr)
        {
            out<<"["<<tempEdge->edgeData<<"]"<<"("<<tempEdge->weight<<")-->";
            tempEdge = tempEdge->next;
        }
        out<<"[END]"<<std::endl;
        temp = temp->next;
    }

    return(out);
}

int main()
{

    Graph g;

    for(int i = 1; i<=10; i++)
    {
        g.addVertex(i * 10);
    }

    int arr[][3] = {
        {10, 20, 1}, {10, 30, 2}, {20, 40, 2}, {40, 90, 5}, {50, 80, 3},
        {100, 50, 5}, {70, 60, 1}, {20, 80, 6}, {50, 70, 2}, {30, 50, 2},
        {90, 10, 8}, {100, 50, 5}, {50, 80, 3}
    };

    int size = sizeof(arr) / sizeof(arr[0]);

    for(int i = 0; i < size; i++)
    {
        g.addEdge(arr[i][0], arr[i][1], arr[i][2]);
    }

    std::cout<<g;

    std::cout<<"Removing Edge from Graph : (20,80), (50,70)"<<std::endl;

    g.removeEdge(20,80);
    g.removeEdge(50,70);

    std::cout<<g;

    std::cout<<"Removing Vertices from Graph :"<<std::endl;
    for(int i = 1; i<=10; i++)
    {
        g.removeVertex(i * 10);
    }

    std::cout<<g;

    std::cout<<"Again Populating the Graph :"<<std::endl;

    for(int i = 1; i<=10; i++)
    {
        g.addVertex(i * 10);
    }

    for(int i = 0; i < size; i++)
    {
        g.addEdge(arr[i][0], arr[i][1], arr[i][2]);
    }

    std::cout<<g;

    return(0);
}
