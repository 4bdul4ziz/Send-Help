
/*Rahul wants to find the sum of numbers he entered in system.
Each time he wants to enter different count of numbers. 
Write a C program to read different count of numbers in an array, 
and print sum of all elements along with inputted array element without wasting memory.

Hint:
Use Dynamic Memory Allocation to vary size of array.*/

#include <stdio.h>
#include <conio.h>
int sumofarray(int a[],int n,int i);

int main()
{   
    //initial array declaration

    int a[1000],i,n,sum;
    //declare that
   
    //get the friggin size
    scanf("%d", &n);
 
    //then the elements within that size
    for(i=0; i<n; i++)
    {
        scanf("%d", &a[i]);
    }
    //use function thingy
    sum=sumofarray(a,n,0);
     printf("%d",sum);
 
    return 0;
}
int sumofarray(int a[],int n,int i)
{
 	if(i<n)
    return a[i]+sumofarray(a,n,++i);
	   
    return 0;
 	
}