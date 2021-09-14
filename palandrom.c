#include<stdio.h>
int main()
{
	int t,r,n,rev=0;
	printf("Enter the number\n");
	scanf("%d",&n);
	t=n;
	while(n>0)
	{
		r=n%10;
		rev=rev*10+r;
		n=n/10;
	}
	
	if(rev==t)
	{
		printf("palandrom");
	}
	else
	printf("not palandrom");
	return 0;
	
}
