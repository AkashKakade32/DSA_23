#include<stdio.h>
#include<stdlib.h>

int main(int argc, char **argv, char **envp)
{
  //Function Declarations
  int binSearch(int, int, int *, int);

  //Variable Declarations
  int *arr;
  int length;
  int i = 0;
  int element = 0;

  //Code
  printf("Enter the size of the array : ");
  scanf("%d", &length);

  arr = (int *)calloc(length, sizeof(int));
  if(arr == NULL)
  {
    printf("Memory allocation to the arr is failed \n");
    return(1);
  }

  while(i < length)
  {
    printf("Enter the integer arr[%d] : ", i);
    scanf("%d", arr+i);
    i = i+1;
  }

  /*
  while(i < length)
  {
    printf("Elements in the array arr[%d] : %d \n", i, *(arr+i));
    i = i+1;
  }
  */

  printf("Enter the element you want to search in the array : ");
  scanf("%d", &element);

  int index = binSearch(0, length-1, arr, element);

  if(index != 1)
  {
    printf("Element %d is found at %d position \n", element, index);
  }
  else {
    printf("Element is not present in the array \n");
  }

  free(arr);
  arr = 0;

  return(0);
}

int binSearch(int si, int ei, int *arr, int SE)
{
  if(si <= ei)
  {
    int mi = (si+ei)/2;

    if(SE == *(arr+mi))
    {
      return(mi);
    }
    else
    {
      if(SE < *(arr+mi))
      {
        return binSearch(si, mi-1, arr, SE);
      }
      else
      {
        return binSearch(mi+1, ei, arr, SE);
      }
    }
  }
  
  return(1);
}


