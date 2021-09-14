#include<stdio.h>
int main()
{
	int m,n,AND,OR,NOT,XOR;
	printf("Enter the value of m and n");
	scanf("%d %d",&m,&n);
	AND = (m&n);
	OR = (m|n);
	NOT = (~n);
	XOR = (m^n);
	printf("AND %d\n",AND);
	printf("OR %d\n",OR);
	printf("not %d\n",NOT);
	printf("XOR %d",XOR);
	
}
