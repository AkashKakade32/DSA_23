#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define CAP 10000000

int main(int argc, char *argv[], char *envp[])
{
  //Function Declarations
  void inputArray(int *, int);
  void outputArray(int *, int);
  void quick_sort(int *, int, int);

  //Variable Declarations
  int *arr;
  int size;
  time_t vTime;
  
  if(argc != 2)
  {
    printf("Command Line Argument is Must : Only one int argument is allowed \n");
    return(1);
  }

  size = atoi(argv[1]);
  if(size <= 0)
  {
    printf("You must enter the int argument greater than 0\n");
  }

  arr = (int *)malloc(sizeof(int) * size);
  if(arr == NULL)
  {
    printf("Failed to allocate the memory to arr\n");
    return(1);
  }

  inputArray(arr, size);

  vTime = time(NULL);
  quick_sort(arr, 0, size-1);
  vTime = time(NULL) - vTime;

  outputArray(arr, size);

  printf("Time to sort the array using quick_sort : %ld \n", vTime);

  free(arr);
  arr = 0;

  return(0);
}

void inputArray(int *arr, int size)
{
  //Variable Declarations
  int i = 0;

  //Code
  while(i < size)
  {
    arr[i] = rand()%CAP;
    i++;
  }
}

void outputArray(int *arr, int size)
{
  //Variable Declarations
  int i = 0;
  //Code
  while(i < size)
  {
    printf("arr[%d] = %d\n", i, arr[i]);
    i++;
  }
}

int partition(int *arr, int p, int r)
{
  //Variable Declarations
  int pivot = arr[r];
  int i = p-1;
  int j = p;
  int temp = 0;

  while(j < r)
  {
    if(arr[j] <= pivot)
    {
      i = i+1;
      temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
    j++;
  }

  temp = arr[i+1];
  arr[i+1] = arr[r];
  arr[r] = temp;

  return(i+1);
}

void quick_sort(int *arr, int p, int r)
{
  //Function Declarations 
  int partition(int *, int, int);

  //Variable Declarations
  int q;

  if(p<r)
  {
    q = partition(arr, p, r);
    quick_sort(arr, p, q-1);
    quick_sort(arr, q+1, r);
  }

}


