#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define CAP 10000000
#define True 1

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void inputArray(int *, int);
  void outputArray(int *, int);
  void merge(int *, int, int, int);
  void merge_sort(int *, int, int);

  //Variable Declarations
  int *arr;
  int size;
  clock_t pTime;
  time_t vTime;

  //Code
  if(argc != 2)
  {
    printf("Command line argument is must : Only one int variable is allowed\n");
    return(1);
  }

  size = atoi(argv[1]);

  if(size <= 0)
  {
    printf("Entered argument size should be greater than 0 \n");
    return(1);
  }

  arr = (int *)malloc(sizeof(int) * size);
  if(arr == NULL)
  {
    printf("Failed to allocate the memory\n");
    return(1);
  }

  inputArray(arr, size);
  
  pTime = clock();
  vTime = time(NULL);

  merge_sort(arr, 0, size-1);

  pTime = clock() - pTime;
  vTime = time(NULL) - vTime;

  outputArray(arr, size);

  printf("Time Taken By Processor : %f, Total Virtual Time : %lu\n", ((float)pTime/CLOCKS_PER_SEC), vTime);


  free(arr);
  arr = 0;

  return(0);
}

void inputArray(int *arr, int size)
{
  int i = 0;

  while(i < size)
  {
    arr[i] = rand()%CAP;
    i++;
  }
}

void outputArray(int *arr, int size)
{
  int i = 0;

  while(i < size)
  {
    printf("arr[%d] : %d\n", i, arr[i]);
    i++;
  }
}

void merge(int *arr, int p, int q, int r)
{
  int N1 = q-p+1;
  int N2 = r-q;
  int i = 0;
  int j = 0;
  int k = 0;

  int *L1 = (int *)malloc(sizeof(int) * N1);
  if(L1 == NULL)
  {
    printf("Failed to allocate the memory to L1 \n");
    exit(EXIT_FAILURE);
  }

  int *L2 = (int *)malloc(sizeof(int) * N2);
  if(L2 == NULL)
  {
    printf("Failed to allocate the memory to L2 \n");
    exit(EXIT_FAILURE);
  }

  while(i < N1)
  {
    L1[i] = arr[p+i];
    i++;
  }

  i = 0;
  while(i < N2)
  {
    L2[i] = arr[q+1+i];
    i++;
  }

  i = 0;

  while(True)
  {
    if(L1[i] <= L2[j])
    {
      arr[p+k] = L1[i];
      i++;
      k++;
      if(i == N1)
      {
        while(j < N2)
        {
          arr[p+k] = L2[j];
          j++;
          k++;
        }
        break;
      }
    }
    else {
      arr[p+k] = L2[j];
      j++;
      k++;
      if(j == N2)
      {
        while(i < N1)
        {
          arr[p+k] = L1[i];
          i++;
          k++;
        }
        break;
      }
    }

  }

  free(L1);
  L1 = 0;

  free(L2);
  L2 = 0;
}

void merge_sort(int *arr, int p, int r)
{
  if(p < r)
  {
    int q = (p+r)/2;
    merge_sort(arr, p, q);
    merge_sort(arr, q+1, r);
    merge(arr, p, q, r);
  }
}
