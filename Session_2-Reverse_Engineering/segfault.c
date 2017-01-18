/* debugging for segfaults*/

#include<stdio.h>

void foo()
{
char *x=0;
*x=3;
}

int main()
{
foo();
return 0;
}

