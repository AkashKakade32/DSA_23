#define _CRT_RAND_S
#include <iostream> 
#include <stdexcept>
#include <cstdlib>  
#include <cstring> 

class array{
    private: 
        int* pa; 
        long long N; 
        int cap; 

        static int partition(int* pa, long long p, long long r) 
        {
            long long i, j; 
            int tmp, pivot; 

            pivot = pa[r]; 
            i = p - 1; 

            for(j = p; j < r; ++j){
                if(pa[j] <= pivot){
                    i = i + 1; 
                    tmp = pa[i]; 
                    pa[i] = pa[j]; 
                    pa[j] = tmp; 
                }
            }

            tmp = pa[i+1]; 
            pa[i+1] = pa[r]; 
            pa[r] = tmp; 

            return (i+1); 
        }

        static void quick_sort(int* pa, long long p, long long r){
            int q; 
            if(p < r){
                q = partition(pa, p, r); 
                quick_sort(pa, p, q-1); 
                quick_sort(pa, q+1, r); 
            }
        }

    public: 
        array(long long _N){
            if(_N < 0)
                throw std::domain_error("Size cannot be negative"); 
            N = _N; 
            pa = new int[_N];         
            cap = 1000000;     
        }

        ~array(){
            delete[] pa; 
            pa = 0;
        }        

        int& operator[](const long long& index){
            if(index < 0 || index >= N)
                throw std::out_of_range("Array index out of range"); 
            return *(pa+index); 
        }

        int get_cap() const {
            return cap; 
        }

        void set_cap(int new_cap){
            if(new_cap <= 0)
                std::runtime_error("Cap must be positive"); 
            cap = new_cap; 
        }

        void fill(){
            unsigned int num; 
            srand(time(0)); 
            for(long long i = 0; i < N; ++i){
                rand_s(&num);
                pa[i] = num % cap;  
            } 
        }

        void sort(){
            quick_sort(pa, 0, N-1); 
        }

        friend std::ostream& operator<<(std::ostream& os, const array& arr); 
}; 

std::ostream& operator<<(std::ostream& os, const array& arr){
    for(long long i = 0; i < arr.N; ++i)
        os << "arr[" << i << "]:" << arr.pa[i] << std::endl;
    return os;  
}

int main(int argc, char* argv[]){
    if(argc != 2){
        std::cerr   << "UsageError:Correct usage is:"
                    << argv[0] << "number_of_array_elements"
                    << std::endl; 
        exit(EXIT_FAILURE); 
    }

    try{
        array* p_array = new array(atoll(argv[1]));
        p_array->fill(); 
        std::cout << "Before sort:" << std::endl << *p_array; 
        p_array->sort(); 
        std::cout << "After sort:" << std::endl << *p_array; 
        delete p_array; 
        p_array = 0; 
    }catch(std::exception& exc){
        std::cerr << exc.what() << std::endl; 
        exit(EXIT_FAILURE); 
    }

    return (EXIT_SUCCESS); 
}