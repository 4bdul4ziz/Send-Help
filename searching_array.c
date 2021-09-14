#include<stdio.h>
int main()
{
	int n,i,ar[100],elem;
	printf("Enter the number of elements in array\n");
	scanf("%d",&n);
	printf("Enter the elements in array\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&ar[i]);
	}
	printf("Enter the element you can search\n");
	scanf("%d",&elem);
	for(i=0;i<n;i++)
	{
	    if(ar[i]==elem)
	    {
	    	printf("%d is present at location %d",elem,i+1);
	    	break;
		}
    else
    printf("%d is not present in a array\n",elem);
	break;
    }
    return 0;
}
