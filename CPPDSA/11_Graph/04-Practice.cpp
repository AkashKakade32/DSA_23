#include <iostream>

class EdgeNode {
private:
    int data;
    EdgeNode* next;
    explicit EdgeNode(int d) : data(d), next(nullptr) {}

    friend class Graph;
};

class VertexNode {
private:
    int data;
    EdgeNode* edgeHead;
    VertexNode* next;
    explicit VertexNode(int d) : data(d), edgeHead(nullptr), next(nullptr) {}

    friend class Graph;
};

class Graph {
private:
    VertexNode* head;

    // Utility to find a vertex node by its data
    VertexNode* findVertex(int data) const {
        VertexNode* curr = head;
        while (curr) {
            if (curr->data == data) return curr;
            curr = curr->next;
        }
        return nullptr;
    }

public:
    Graph() : head(nullptr) {}

    // Disable copy constructor and copy assignment operator to prevent pointer aliasing issues
    Graph(const Graph&) = delete;
    Graph& operator=(const Graph&) = delete;

    ~Graph() {
        VertexNode* vCurr = head;
        while (vCurr) {
            EdgeNode* eCurr = vCurr->edgeHead;
            while (eCurr) {
                EdgeNode* eTemp = eCurr;
                eCurr = eCurr->next;
                delete eTemp;
            }
            VertexNode* vTemp = vCurr;
            vCurr = vCurr->next;
            delete vTemp;
        }
    }

    void addVertex(int vertexData) {
        // Use a double pointer to find the end of the vertex list.
        // This allows us to modify 'head' or the 'next' of the last node uniformly.
        VertexNode** curr = &head;
        while (*curr) {
            if ((*curr)->data == vertexData) return; // Vertex already exists
            curr = &((*curr)->next);
        }
        *curr = new VertexNode(vertexData);
    }

    void addEdge(int vertex1, int vertex2) {
        if (vertex1 == vertex2) return; // Prevent self-loops

        VertexNode* v1 = findVertex(vertex1);
        VertexNode* v2 = findVertex(vertex2);

        if (!v1 || !v2) {
            std::cout << "Error: One or both vertices (" << vertex1 << ", " << vertex2 << ") not found." << std::endl;
            return;
        }

        // Add vertex2 to vertex1's adjacency list using double pointers
        EdgeNode** e1 = &(v1->edgeHead);
        while (*e1) {
            if ((*e1)->data == vertex2) break; // Edge already exists
            e1 = &((*e1)->next);
        }
        if (!*e1) *e1 = new EdgeNode(vertex2);

        // Add vertex1 to vertex2's adjacency list using double pointers
        EdgeNode** e2 = &(v2->edgeHead);
        while (*e2) {
            if ((*e2)->data == vertex1) break; // Edge already exists
            e2 = &((*e2)->next);
        }
        if (!*e2) *e2 = new EdgeNode(vertex1);
    }

    void printGraph() const {
        VertexNode* vCurr = head;
        while (vCurr) {
            std::cout << "[" << vCurr->data << "]: ";
            EdgeNode* eCurr = vCurr->edgeHead;
            while (eCurr) {
                std::cout << eCurr->data;
                if (eCurr->next) std::cout << "<-->";
                eCurr = eCurr->next;
            }
            std::cout << std::endl;
            vCurr = vCurr->next;
        }
    }
};

int main() {
    Graph graph;

    graph.addVertex(1);
    graph.addVertex(2);
    graph.addVertex(3);

    graph.addEdge(1, 2);
    graph.addEdge(1, 3);
    graph.addEdge(2, 3);

    std::cout << "Graph representation (using double pointers):" << std::endl;
    graph.printGraph();

    return 0;
}