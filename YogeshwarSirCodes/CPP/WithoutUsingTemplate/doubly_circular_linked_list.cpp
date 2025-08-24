#define _CRT_RAND_S 
#include <iostream> 
#include <stdexcept> 
#include <cstdlib> 
#include <cstring>

class value_error : public std::runtime_error{
    public: 
        value_error(const char* msg) : std::runtime_error(msg){
        }
}; 

class empty_error : public std::runtime_error{
    public: 
        empty_error(const char* msg) : std::runtime_error(msg){
        }
}; 

class node{
    friend class list; 
    friend std::ostream& operator<<(std::ostream& os, const list& dcll); 
    private: 
        int data; 
        node* prev; 
        node* next; 

        node(int _data = 0) : data(_data), prev(0), next(){
        }
}; 

class list{
    private: 
        node* head_node; 

        node* search_node(int search_data){
            for(node* n_run = head_node->next; 
                n_run != head_node; 
                n_run = n_run->next)
                if(n_run->data == search_data)
                    return n_run; 
            return 0; 
        }

        static void generic_insert(node* beg, node* mid, node* end){
            mid->next = end; 
            mid->prev = beg; 
            beg->next = mid; 
            end->prev = mid; 
        }

        static void generic_delete(node* delete_node){
            delete_node->prev->next = delete_node->next; 
            delete_node->next->prev = delete_node->prev; 
            delete delete_node; 
        }

    public: 
        list() : head_node(new node) {
            head_node->prev = head_node; 
            head_node->next = head_node; 
        }

        ~list(){
            node* n_run, *n_run_next; 
            for(n_run = head_node->next; n_run != head_node; n_run = n_run_next){
                n_run_next = n_run->next; 
                delete n_run; 
            }
            delete head_node; 
            head_node = 0; 
        }

        void insert_start(int new_data){
            generic_insert(head_node, new node(new_data), head_node->next); 
        }

        void insert_end(int new_data){
            generic_insert(head_node->prev, new node(new_data), head_node); 
        }

        void insert_after(int e_data, int new_data){
            node* e_node = search_node(e_data); 
            if(!e_node)
                throw value_error("insert_after():bad existing data"); 
            generic_insert(e_node, new node(new_data), e_node->next); 
        }

        void insert_before(int e_data, int new_data){
            node* e_node = search_node(e_data); 
            if(!e_node)
                throw value_error("insert_before():bad existing data"); 
            generic_insert(e_node->prev, new node(new_data), e_node); 
        }

        int get_start() const{
            if(empty())
                throw empty_error("get_start():empty list"); 
            return head_node->next->data; 
        }

        int get_end() const{
            if(empty())
                throw empty_error("get_start():empty list"); 
            return head_node->prev->data; 
        }

        int pop_start(){
            if(empty())
                throw empty_error("get_start():empty list"); 
            int data = head_node->next->data; 
            generic_delete(head_node->next);
            return data;  
        }

        int pop_end(){
            if(empty())
                throw empty_error("get_start():empty list"); 
            int data = head_node->prev->data; 
            generic_delete(head_node->prev); 
            return data; 
        }

        void remove_start(){
            if(empty())
                throw empty_error("get_start():empty list"); 
            generic_delete(head_node->next); 
        }

        void remove_end(){
            if(empty())
                throw empty_error("get_start():empty list"); 
            generic_delete(head_node->prev); 
        }

        bool empty() const{
            return (head_node->next == head_node && head_node->prev == head_node); 
        }

        size_t size() const{
            size_t L = 0; 
            for(node* n_run = head_node->next; n_run != head_node; n_run = n_run->next)
                ++L; 
            return L; 
        }

        friend std::ostream& operator<<(std::ostream& os, const list& dcll); 

        class iterator{
            private: 
                node* curr_node; 
            public: 
                iterator(node* _node = 0) : curr_node(_node){
                }

                iterator operator++(){
                    curr_node = curr_node->next; 
                    return *this; 
                }

                iterator operator--(){
                    curr_node = curr_node->prev; 
                    return *this; 
                }

                iterator operator++(int){
                    iterator tmp_iter(curr_node); 
                    curr_node = curr_node->next; 
                    return tmp_iter; 
                }

                iterator operator--(int){
                    iterator tmp_iter(curr_node); 
                    curr_node = curr_node->prev; 
                    return tmp_iter; 
                }

                int operator*(){
                    return this->curr_node->data; 
                }

                bool operator==(const iterator& other_iter){
                    return curr_node == other_iter.curr_node; 
                }

                bool operator!=(const iterator& other_iter){
                    return curr_node != other_iter.curr_node; 
                }
        }; 

        iterator begin(){
            return iterator(head_node->next);
        }

        iterator end(){
            return iterator(head_node); 
        }
}; 

std::ostream& operator<<(std::ostream& os, const list& dcll){
    os << "[START]<->"; 
    for(
        node* n_run = dcll.head_node->next; 
        n_run != dcll.head_node; 
        n_run = n_run->next
    )
        os << "[" << n_run->data << "]<->";
    os << "[END]" << std::endl;  
    return os; 
}

int main(void){
    list* pList = new list; 

    for(int data = 0; data <= 100; data += 10)
        pList->insert_end(data); 

    std::cout << "LIST:" << std::endl << *pList; 

    for(list::iterator iter = pList->begin(); 
        iter != pList->end(); 
        ++iter) 
        std::cout << "*iter=" << *iter << std::endl; 

    delete pList; 
    pList = 0; 

    return EXIT_SUCCESS; 
}

