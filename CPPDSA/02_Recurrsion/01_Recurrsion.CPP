#include<iostream>

int main(int argc, char **argv, char **envp)
{
  int recur(int);
  int a = 0;

  a = recur(7);

  printf("%d\n", a);

  return(0);
}

int recur(int n)
{
  if(n == 0)
  {
    return 0;
  }
  else
  {
    if (n == 1)
    {
      return 1;
    }
    else
    {
      return(n * recur(n-1) + n + recur(n-2));
    }
  }
}
