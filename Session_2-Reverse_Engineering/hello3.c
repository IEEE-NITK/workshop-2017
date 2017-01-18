/*program to illustrate step and next*/

#include<stdio.h>

int print()
{
printf("Welcome!!You're in the print function\n");
return 0;
}

int main()
{
printf("Hey there!You're in the main function\n");
int var=print();
printf("You're back to main\n");
return 0;
}
