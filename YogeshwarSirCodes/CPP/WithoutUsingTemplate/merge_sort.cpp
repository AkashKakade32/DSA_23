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

        static void merge(int* a, long long p, long long q, long long r){
            long long N1 = q - p + 1; 
            long long N2 = r - q; 
            int* a1 = new int[N1]; 
            int* a2 = new int[N2]; 
            long long i, j, k; 

            memcpy(
                reinterpret_cast<void*>(a1), 
                reinterpret_cast<void*>(a + p), 
                N1 * sizeof(int) 
            ); 

            memcpy(
                reinterpret_cast<void*>(a2), 
                reinterpret_cast<void*>(a + q + 1), 
                N2 * sizeof(int) 
            ); 

            k = 0; 
            i = 0; 
            j = 0; 
            while(true){
                if(a1[i] <= a2[j]){
                    a[p+k++] = a1[i++]; 
                    if(i == N1){
                        memcpy(
                            reinterpret_cast<void*>(a + p + k), 
                            reinterpret_cast<void*>(a2 + j), 
                            (N2 - j) * sizeof(int)
                        ); 
                        break; 
                    }
                }else{
                    a[p+k++] = a2[j++]; 
                    if(j == N2){
                        memcpy(
                            reinterpret_cast<void*>(a + p + k), 
                            reinterpret_cast<void*>(a1 + i), 
                            (N1 - i) * sizeof(int)
                        ); 
                        break; 
                    }
                }
            }

            delete[] a1; 
            a1 = 0; 

            delete[] a2; 
            a2 = 0; 
        }

        static void merge_sort(int* a, long long p, long long r){
            if(p < r){
                long long q = (p + r)/2; 
                merge_sort(a, p, q); 
                merge_sort(a, q+1, r); 
                merge(a, p, q, r); 
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
            merge_sort(pa, 0, N-1); 
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