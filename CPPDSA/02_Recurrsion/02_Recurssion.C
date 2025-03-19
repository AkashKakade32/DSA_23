#include<stdio.h>
#include<stdlib.h>

int main(int argc, char **argv, char **envp)
{
  //Function Declarations
  char alphaCapital(char, int, int);
  char alphaSmall(char, int, int);

  //Variable Declarations
  char c = 64;
  char s = 96;
  int index = 0;
  int value = 0;
  
  printf("Enter the value : ");
  scanf("%d", &value);

  if(value <= 0)
  {
    printf("Value must be greater than 0\n");
    exit(1);
  }

  char ch = alphaCapital(c, 0, value);
  char xch = alphaSmall(s, 0, value);

  printf("Entered Character is : %c and %c\n", ch, xch);
  return(0);
}

char alphaCapital(char c, int index, int value)
{
  if(index == value)
  {
    return c;
  }
  else {
    return alphaCapital(c+1, index+1, value);
  }
}

char alphaSmall(char c, int index, int value)
{
  if(index == value)
  {
    return c;
  }
  else {
    return alphaSmall(c+1, index+1, value);
  }
}

