#include<stdio.h>
 

long factorial(int n);
 
int main()
{
    int n;
    scanf("%d",&n);
    long val=factorial(n);
    printf("val: %ld\n",val);
    return 0;
}
 
long factorial(int n)
{
    long result=1;
    while(n--)
    {
        result*=n;
    }
    return result;
}
