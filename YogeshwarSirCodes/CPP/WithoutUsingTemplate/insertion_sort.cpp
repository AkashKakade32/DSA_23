#define _CRT_RAND_S
#include <iostream> 
#include <stdexcept>
#include <cstdlib>  

class array{
    private: 
        int* pa; 
        long long N; 
        int cap; 

        static void insertion_sort(int* a, long long N){
            long long i, j; 
            int key; 

            for(j = 1; j < N; ++j){
                key = a[j]; 
                for(i = j - 1; i > -1 && a[i] > key; --i)
                    a[i+1] =a[i]; 
                a[i+1] = key; 
            }
        }

    public: 
        array(long long _N){
            if(_N <= 0)
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
                throw std::runtime_error("Cap must be positive"); 
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
            insertion_sort(pa, N); 
        }

        void show() {
            for(long long i = 0; i < N; ++i)
                std::cout << "pa[" << i << "]:" << pa[i] << std::endl; 
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

    int* pa = NULL; 

    return (EXIT_SUCCESS); 
}

// myDate.set_day(5); 

// Date::set_day(&myDate, 5); 

// pushl $5 
// pushl $myDate 
// call Date::set_day 
// addl $8, %esp

// Date* pDate = new Date(1,1,1970); 
// pushl $12 
// call _znw
// addl $4, %esp
// pushl $1970 
// pushl $1 
// pushl $1 
// pushl %eax
// call Date::Date 
// addl $16, %esp 
// movl %eax, myDate 

// C++ Primer -> 4th Edition (800-900)
// inside COM -> Del Rodgerson 
// Template Programming : Complete Guide -> 1st edition (600) (PART 1 | 6 chapters)

// The standard Template Library -> 1st edition (800-900)
// C++ primer -> (5th edition part) -> 11 specific (100)
// C++ programming : principles & tehcniques 14 specific (50-100)
// C++ 17 -> Jossuits (300)
// C++ 17 move semantics (jossuits) (250)
// template programming : complete guide -> 2nd edition (C++ 17 templates) -> 800
/////////////////////////////////////////////////////////////////////////////////////
// C++ 20 -> Jossuits 
//////////////////////////////////////////////////////////////////////////////////////
// Inside C++ Object Model -> Liepmaan 
// Object Oriented C -> Alex Tobius Schneider 
// Design & Evolution of C++ -> Stroupstrup 

// Array A(10); 

// std::cout << A; 