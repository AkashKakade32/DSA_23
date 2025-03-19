#include<stdio.h>

int main(int argc, char **argv, char **envp)
{
  //Function Declarations
  int binSearch(int, int, int[], int);

  //Variable Declarations
  int arr[] = {10,20,30,40,50,60,70,80,90};
  int length = sizeof(arr)/sizeof(arr[0]);
  int SE = 0;

  printf("Enter the search element : ");
  scanf("%d", &SE);
  
  int index = binSearch(0, length-1, arr, SE);

  if(index != 1)
  {
    printf("Search element %d found at position : %d \n", SE, index);
  }
  else {
    printf("Search element %d is not present in the array\n", SE);
  }

  return(0);
}

int binSearch(int si, int ei, int arr[], int SE)
{
  if(si <= ei)
  {
    int mi = (si+ei)/2;

    if(SE == arr[mi])
    {
      return mi;
    }
    else{
      if(SE < arr[mi])
      {
        return binSearch(si, mi-1, arr, SE);
      }
      else{
        return binSearch(mi+1, ei, arr, SE);
      }
    }
  }
  
  return(1);

}
