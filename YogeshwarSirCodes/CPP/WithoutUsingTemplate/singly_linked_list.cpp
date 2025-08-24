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
    friend std::ostream& operator<<(std::ostream& os, const list& sll); 
    private: 
        int data; 
        node* next; 
        node(int _data = 0) : data(_data), next(0){
        }
}; 

class list{
    private: 
        node* head_node; 

        node* search_node(int search_data){            
            for(node* n_run = head_node->next; n_run != 0; n_run = n_run->next)
                if(n_run->data == search_data)
                    return n_run; 
            return (0); 
        }

    public: 
        list() : head_node(new node){
        }

        ~list(){
            node* n_run; 
            node* n_run_next; 

            for(n_run = head_node->next; n_run != 0; n_run = n_run_next){
                n_run_next = n_run->next; 
                delete n_run; 
            }  

            delete head_node; 
            head_node = 0; 
        }

        void insert_start(int new_data){
            node* n_new = new node(new_data); 
            n_new->next = head_node->next; 
            head_node->next = n_new; 
        }

        void insert_end(int new_data){
            node* n_run = head_node; 
            
            while(n_run->next)
                n_run = n_run->next; 

            n_run->next = new node(new_data); 
        }

        void insert_after(int e_data, int new_data){
            node* e_node = search_node(e_data); 
            node* n_new = 0; 
            
            if(!e_node)
                throw value_error("insert_after:Bad existing data"); 
            
            n_new = new node(new_data); 
            n_new->next = e_node->next; 
            e_node->next = n_new; 
        }

        void insert_before(int e_data, int new_data){
            node* n_run = head_node->next; 
            node* n_run_pred = head_node; 
            node* new_node; 

            while(n_run != 0){
                if(n_run->data == e_data)
                    break; 
                n_run_pred = n_run; 
                n_run = n_run->next; 
            }

            if(!n_run)
                throw value_error("insert_before():Bad existing data"); 

            new_node = new node(new_data); 
            new_node->next = n_run_pred->next; 
            n_run_pred->next = new_node;
        }

        int get_start() const {
            if(empty())
                throw empty_error("get_start():empty list"); 
            return (head_node->next->data); 
        }

        int get_end() const {
            node* n_run;  

            if(empty())
                throw empty_error("get_end():empty list"); 

            n_run = head_node; 
            while(n_run->next != 0)
                n_run = n_run->next; 

            return n_run->data; 
        }

        int pop_start(){
            node* n_first;  
            int data; 

            if(empty())
                throw empty_error("pop_start():empty list"); 

            n_first = head_node->next; 
            data = n_first->data; 
            head_node->next = n_first->next; 
            free(n_first); 

            return (data); 
        }

        int pop_end(){
            node* n_run; 
            node* n_run_pred; 
            int data; 

            if(empty())
                throw empty_error("pop_end():empty list"); 

            n_run = head_node; 
            while(n_run->next != 0){
                n_run_pred = n_run; 
                n_run = n_run->next; 
            }

            n_run_pred->next = 0; 
            data = n_run->data; 
            free(n_run); 

            return (data); 
        }

        void remove_start(){
            node* n_first; 

            if(empty())
                throw empty_error("remove_start():list empty"); 

            n_first = head_node->next; 
            head_node->next = n_first->next; 
            free(n_first); 
        }

        void remove_end(){
            node* n_run; 
            node* n_run_pred; 

            if(empty())
                throw empty_error("remove_end():empty list"); 

            n_run = head_node; 
            while(n_run->next != 0){
                n_run_pred = n_run; 
                n_run = n_run->next; 
            }

            n_run_pred->next = 0; 
            free(n_run); 
        }

        void remove_data(int r_data){
            node* n_run = head_node->next; 
            node* n_run_pred = head_node; 

            while(n_run != 0){
                
                if(n_run->data == r_data){
                    n_run_pred->next = n_run->next; 
                    free(n_run); 
                    return; 
                }

                n_run_pred = n_run; 
                n_run = n_run->next; 
            }

            throw value_error("remove_data():invalid data"); 
        }

        size_t len() const{
            node* n_run = head_node->next; 
            size_t N = 0; 

            while(n_run != 0){
                N += 1; 
                n_run = n_run->next;
            }

            return (N); 
        }

        bool empty() const{
            return (head_node->next == 0); 
        }

        friend std::ostream& operator<<(
            std::ostream& os, 
            const list& sll
        ){
            os << "[START]->"; 
            for(
                node* n_run = sll.head_node->next; 
                n_run != 0; 
                n_run = n_run->next
            )
                os << "[" << n_run->data << "]->"; 
            os << "[END]" << std::endl;  

            return os; 
        }

        list operator+(const list& other_list){
            list new_list; 
            node* n_run; 

            for(
                n_run = head_node->next; 
                n_run != 0; 
                n_run = n_run->next
            )
                new_list.insert_end(n_run->data); 

            for(
                n_run = other_list.head_node->next; 
                n_run != 0; 
                n_run = n_run->next
            )
                new_list.insert_end(n_run->data);

            return new_list; 
        }

        void append(const list& other_list){
            node* n_run = head_node; 

            while(n_run->next != 0)
                n_run = n_run->next; 

            n_run->next = other_list.head_node->next; 
            free(other_list.head_node); 
        }

        list reversed_list() const{
            list r_list; 
            
            for(
                node* n_run = head_node->next; 
                n_run != head_node; 
                n_run = n_run->next
            )
                r_list.insert_start(n_run->data); 

            return r_list; 
        }

        void reverse(){
            node* n_run; 
            node* n_run_next; 
            node* n_first; 

            if(head_node->next == 0 || head_node->next->next == 0)
                return; 
            
            n_first = head_node->next; 
            n_run = head_node->next->next; 
            while(n_run != 0){
                n_run_next = n_run->next; 
                n_run->next = head_node->next; 
                head_node->next = n_run; 
                n_run = n_run_next; 
            }
            n_first->next = 0; 
        }

        static void test_list(void){
            list L; 

            std::cout << L; 

            for(int data = 0; data <= 100; data += 10)
                L.insert_end(data); 

            std::cout << "After insert_end():" << std::endl << L; 

            for(int data = 1000; data <= 10000; data += 1000)
                L.insert_start(data); 

            std::cout << "After insert_start():" << std::endl << L; 

            try{
                L.insert_after(-500, 10); 
            }catch(const value_error& exc){
                std::cout << exc.what() << std::endl; 
            }

            try{
                L.insert_before(2354636, 10); 
            }catch(const value_error& exc){
                std::cout << exc.what() << std::endl; 
            }

            L.insert_after(0, 100); 
            L.insert_before(0, 200); 

            std::cout << "After insert_after() and insert_before():" << std::endl << L; 

            int start_data = L.get_start(); 
            std::cout << "start_data:" << start_data << std::endl; 

            int end_data = L.get_end(); 
            std::cout << "end_data:" << end_data << std::endl;

            std::cout << "After get_start() and get_end():" << std::endl << L; 

            start_data = L.pop_start(); 
            end_data = L.pop_end(); 

            std::cout << "poped_start:" << start_data << std::endl 
                        << "poped_end:" << end_data << std::endl; 

            std::cout << "After pop_start() and pop_end():" << std::endl << L; 
        }
}; 

int main(void){
    list::test_list(); 
    return 0; 
}