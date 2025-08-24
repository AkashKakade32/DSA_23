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

class no_predecessor_error : public std::runtime_error{
    public: 
        no_predecessor_error(const char* msg) : std::runtime_error(msg){
        }
}; 

class no_successor_error : public std::runtime_error{
    public: 
        no_successor_error(const char* msg) : std::runtime_error(msg){
        }
}; 

class bst_node{
    friend class bst; 
    friend std::ostream& operator<<(std::ostream& os, const bst& tree); 
    private: 
        int data; 
        bst_node* left; 
        bst_node* right; 
        bst_node* parent; 
        bst_node(int _data = 0) : data(_data), left(0), right(0), parent(0){
        }
}; 

class bst{
    private:
        enum TRAVERSAL_ORDER;  
        bst_node* root; 
        size_t nr_elements; 
        TRAVERSAL_ORDER traversal_order;
        
        static void preorder(bst_node* root){
            if(root){
                std::cout <<  "[" << root->data << "]-"; 
                preorder(root->left);
                preorder(root->right); 
            }
        }

        static void inorder(bst_node* root){
            if(root){
                inorder(root->left);
                std::cout <<  "[" << root->data << "]-"; 
                inorder(root->right); 
            }
        }

        static void postorder(bst_node* root){
            if(root){
                postorder(root->left);
                postorder(root->right); 
                std::cout <<  "[" << root->data << "]-";   
            }  
        }

        static void destroy_nodelevel(bst_node* root){
            if(root){
                destroy_nodelevel(root->left); 
                destroy_nodelevel(root->right); 
                delete root; 
            }
        }

        static bst_node* inorder_successor_nodelevel(bst_node* node){
            bst_node* run; 
            bst_node* x; 
            bst_node* y; 

            if(node->right != 0){
                run = node->right;
                while(run->left != 0)
                    run = run->left; 
                return (run);  
            }

            x = node; 
            y = x->parent; 
            while(y != 0 && y->right == x){
                x = y; 
                y = x->parent; 
            }

            return (y);
        }

        static bst_node* inorder_predecessor_nodelevel(bst_node* node){
            bst_node* run; 
            bst_node* x; 
            bst_node* y; 

            if(node->left != 0){
                run = node->left;
                while(run->right != 0)
                    run = run->right; 
                return (run);  
            }

            x = node; 
            y = x->parent; 
            while(y != 0 && y->left == x){
                x = y; 
                y = x->parent; 
            }

            return (y);
        }

        bst_node* search_node(int search_data){
            bst_node* run = root; 
            while(run != 0){
                if(run->data == search_data)
                    return run;
                else if(search_data < run->data)
                    run = run->left; 
                else 
                    run = run->right; 
            }
            return 0; 
        }

    public: 
        typedef enum TRAVERSAL_ORDER{
            INORDER=0, 
            PREORDER, 
            POSTORDER
        }TRAVERSAL_ORDER; 

        TRAVERSAL_ORDER get_order() const {
            return traversal_order; 
        }

        void set_order(TRAVERSAL_ORDER new_traversal_order){
            traversal_order = new_traversal_order; 
        }

        bst() : root(0), traversal_order(INORDER){
        }

        ~bst(){
            destroy_nodelevel(root); 
        }

        void insert(int new_data){
            bst_node* n_run; 

            if(root == 0){
                root = new bst_node(new_data); 
                ++nr_elements; 
                return; 
            }

            n_run = root; 
            while(true){
                if(new_data <= n_run->data){
                    if(n_run->left == 0){
                        n_run->left = new bst_node(new_data); 
                        n_run->left->parent = n_run; 
                        break; 
                    }else{
                        n_run = n_run->left; 
                    }
                }else{
                    if(n_run->right == 0){
                        n_run->right = new bst_node(new_data); 
                        n_run->right->parent = n_run; 
                        break; 
                    }else{
                        n_run = n_run->right; 
                    }
                }
            }

            nr_elements += 1; 
        }

        bool search(int search_data) const {
            bst_node* run = root; 
            while(run != 0){
                if(run->data == search_data) 
                    return true; 
                else if(search_data < run->data)
                    run = run->left; 
                else 
                    run = run->right; 
            }
            return false; 
        }

        void remove(int r_data){
            bst_node* z = 0; 
            bst_node* y = 0; 

            z = search_node(r_data); 
            if(z == 0)
                throw value_error("data given for removal does not exist the tree"); 

            if(z->left == 0){
                if(z->parent == 0)
                    root = z->right; 
                else if(z == z->parent->left)
                    z->parent->left = z->right; 
                else 
                    z->parent->right = z->right; 
                if(z->right != 0)
                    z->right->parent = z->parent; 
            }else if(z->right == 0){
                if(z->parent == 0)
                    root = z->left; 
                else if(z == z->parent->left)
                    z->parent->left = z->left; 
                else 
                    z->parent->right = z->left; 
                z->left->parent = z->parent; 
            }else{
                y = z->right; 
                while(y->left != 0)
                    y = y->left; 

                if(z->right != y){
                    y->parent->left = y->right; 
                    if(y->right != 0)
                        y->right->parent = y->parent; 
                    y->right = z->right; 
                    y->right->parent = y; 
                }

                if(z->parent == 0)
                    root = y; 
                else if(z == z->parent->left)
                    z->parent->left = y; 
                else 
                    z->parent->right = y; 
                y->parent = z->parent; 

                y->left = z->left; 
                y->left->parent = y; 
            }

            delete z; 
            z = 0; 

            nr_elements -= 1; 
        }

        int inorder_predecessor(int e_data){
            bst_node* p_pred_node = 0; 
            bst_node* p_ext_node = 0; 

            p_ext_node = search_node(e_data); 
            if(p_ext_node == 0)
                throw value_error("inroder_predecessor():e_data not found"); 
            
            p_pred_node = inorder_predecessor_nodelevel(p_ext_node); 
            if(p_pred_node == 0)    
                throw no_predecessor_error("inorder_predecessor():predecessor does not exist of a given data"); 
            
            return p_pred_node->data; 
        }

        int inorder_successor(int e_data){
            bst_node* p_succ_node = 0; 
            bst_node* p_ext_node = 0; 

            p_ext_node = search_node(e_data); 
            if(p_ext_node == 0)
                throw value_error("inroder_predecessor():e_data not found"); 
            
            p_succ_node = inorder_successor_nodelevel(p_ext_node); 
            if(p_succ_node == 0)    
                throw no_successor_error("inorder_successor():successor does not exist of a given data"); 
            
            return p_succ_node->data; 
        }

        friend std::ostream& operator<<(std::ostream& os, const bst& tree){
            os << "[START]-"; 
            switch(tree.traversal_order){
                case INORDER: 
                    bst::inorder(tree.root);  
                    break; 

                case PREORDER: 
                    bst::preorder(tree.root); 
                    break; 

                case POSTORDER: 
                    bst::postorder(tree.root); 
                    break; 

                default: 
                    throw value_error("operator<<:invalid traversal order"); 
            }
            os << "[END]" << std::endl; 
            return os; 
        }

        static void test_bst(void){
            int data[] = {100, 150, 50, 25, 75, 125, 175, 200, 250, 15, 5, 7,9, 60, 110, 105}; 
            bst* tree = new bst; 

            for(size_t i = 0; i < sizeof(data)/sizeof(data[0]); ++i)
                tree->insert(data[i]); 

            std::cout << "INORDER:" << std::endl << *tree; 
            tree->set_order(bst::PREORDER); 
            std::cout << "PREORDER:" << std::endl << *tree; 
            tree->set_order(bst::POSTORDER); 
            std::cout << "POSTORDER:" << std::endl << *tree;   

            //TODO : add unit tests 

            delete tree; 
            tree = 0; 
        }
}; 

int main(void){
    bst::test_bst(); 
    return EXIT_SUCCESS; 
}