#include <iostream> 
#include <stdexcept>
#include <cstdlib> 
#include <cstring> 
#include <cassert> 

class list_empty : public std::runtime_error{
    public: 
        list_empty(const char* msg) : std::runtime_error(msg){
        }
}; 

class queue_empty : public std::runtime_error{
    public: 
        queue_empty(const char* msg) : std::runtime_error(msg){
        }
}; 

class node{
    friend class list; 
    private: 
        int data; 
        node* prev; 
        node* next; 
        node(int _data = 0) : data(_data), prev(0), next(0){
        }
}; 

class list{
    private: 
        node* head_node; 

        static void generic_insert(node* start, node* mid, node* end){
            mid->next = end; 
            mid->prev = start; 
            start->next = mid; 
            end->prev = start; 
        }

        static void generic_delete(node* delete_node){
            delete_node->prev->next = delete_node->next; 
            delete_node->next->prev = delete_node->prev; 
            delete delete_node; 
        }

    public: 
        list() : head_node(new node){
            head_node->prev = head_node; 
            head_node->next = head_node; 
        }

        ~list(){
            node* run = 0; 
            node* run_next = 0; 

            for(run = head_node->next; run != head_node; run = run->next){
                run_next = run->next; 
                delete run; 
            }
        }

        void insert_end(int new_data){
            generic_insert(head_node, new node(new_data), head_node->next); 
        }

        int get_start() const {
            if(empty())
                throw list_empty("get_start():cannot get start of the empty list"); 
            return head_node->next->data; 
        }

        int get_end() const {
            if(empty())
                throw list_empty("get_end():cannot get end of the empty list"); 
            return head_node->prev->data; 
        }

        int pop_start(){
            if(empty())
                throw list_empty("get_start():cannot get start of the empty list"); 
            int start_data = head_node->next->data; 
            generic_delete(head_node->next); 
            return start_data; 
        }

        int pop_end(){
            if(empty())
                throw list_empty("get_start():cannot get start of the empty list"); 
            int end_data = head_node->prev->data; 
            generic_delete(head_node->prev); 
            return end_data; 
        }

        bool empty() const {
            return head_node->prev == head_node && head_node->next == head_node; 
        } 
}; 

class queue{
    private: 
        list* lst; 
    public: 
        queue() : lst(new list){
        }

        ~queue(){
            delete lst; 
            lst = 0; 
        }

        void enqueue(int new_data){
            lst->insert_end(new_data); 
        }

        int peek() const {
            try{
                return lst->get_start(); 
            }catch(list_empty& e){
                throw queue_empty("peek():Cannot peek from the empty queue"); 
            }
        }

        int dequeue(){
            try{
                return lst->pop_end(); 
            }catch(list_empty& e){
                throw queue_empty("peek():Cannot peek from the empty queue"); 
            }
        }

        bool empty() const {
            return lst->empty(); 
        }

        static void test_queue(void){

        }
}; 

int main(void){
    queue::test_queue(); 
    return EXIT_SUCCESS; 
}