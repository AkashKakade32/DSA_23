#include<iostream>

int main(int argc, char **argv, char **envp)
{

int arr[10] = {74, 12, 85, 96, 82, 23, 38, 58, 98, 68};

int i = 0;
int j = 0;
int val = 0;
int length = sizeof(arr)/sizeof(arr[0]);

while(i < length)
{
val = arr[i+1];
j = i;

while(j>=0)
{

if(arr[j]>val)
{
arr[j+1] = arr[j];
}
else{
break;
}

j = j-1;

}

arr[j+1] = val;

i = i+1;

}

i = 0;

std::cout<<"Values are : ";

while(i < length)
{
std::cout<<arr[i]<<" ";
i = i+1;
}

std::cout<<std::endl;

return(0);
}
