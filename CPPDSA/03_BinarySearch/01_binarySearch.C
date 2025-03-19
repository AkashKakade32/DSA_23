#include<stdio.h>

int main(int argc, char **argv, char **envp)
{
  //Function Declarations
  void binSearch(int, int, int[], int);

  //Variable Declarations
  int arr[] = {10,20,30,40,50,60,70,80,90,100};
  int length = sizeof(arr)/sizeof(arr[0]);

  //Code
  printf("Lenght of array is : %d and Size of array is : %lu \n", length, sizeof(arr));

  binSearch(0, length-1, arr, 80);
  
  return(0);
}

void binSearch(int si, int ei, int arr[], int SE)
{
  if(si<=ei)
  {
    int mi = (si+ei)/2;

    if(SE == arr[mi])
    {
      printf("Element present in the array at position : %d \n", mi);
    }
    else
    {
      if(SE < arr[mi])
      {
        binSearch(si, mi-1, arr, SE); 
      }
      else
      {
        binSearch(mi+1, ei, arr, SE);
      }
    }
  }
}



