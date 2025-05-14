#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define CAP 10000000
#define True

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void inputArray(int *, int);
  void outputArray(int *, int);
  void insertionSort(int *, int);

  //Varable Declarations
  int *arr;
  int size;
  clock_t pTime;
  time_t vTime;
  
  //Code
  if(argc != 2)
  {
    printf("Command Line Argument is must : Only one int variable is allowed\n");
    return(1);
  }

  size = atoi(argv[1]);

  if(size <= 0)
  {
    printf("Commnad line int variable must be greater than 0\n");
    return(1);
  }

  arr = (int *)malloc(sizeof(int) * size);
  if(arr == NULL)
  {
    printf("Failed to allocate the size\n");
    return(1);
  }

  inputArray(arr, size);

  pTime = clock();
  vTime = time(NULL);

  insertionSort(arr, size);

  pTime = clock() - pTime;
  vTime = time(NULL) - vTime;

  outputArray(arr, size);
  
  printf("Total Processor Time : %f, Total Virtual Time : %lu\n",((float)pTime/CLOCKS_PER_SEC), vTime);
  
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

void insertionSort(int *arr, int size)
{
  int i = 0;
  int j = 0;
  int val = 0;

  while(i < size)
  {
    val = arr[i+1];
    j = i;

    while(j >= 0)
    {
      if(arr[j] > val)
      {
        arr[j+1] = arr[j];
      }
      else
      {
        break;
      }

      j--;
    }

    arr[j+1] = val;
    i++;
  }
}
