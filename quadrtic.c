#include<stdio.h>
#include<math.h>
int main()
{
	float a,b,c,d,r1,r2,real,imag;
	printf("Enter the coff. a , b , c\n\n");
	scanf("%f %f %f",&a,&b,&c);
	d = b*b-4*a*c;
	if(d>0)
	{
		r1=(-b+sqrt(d))/2*a;
		r2=(-b-sqrt(d))/2*a;
		printf("\n\n Roots are : %.2f and %.2f",r1,r2);
	}
	else if(d==0)
	{
		r1=r2=-b/2*a;
		printf("\n\n Roots are : %.2f and %.2f",r1,r2);
	}
	else
	{
		real=-b/2*a;
		imag= sqrt(-d)/2*a;
		printf("\n\n Roots are : %.2f + %.2f and %.2f - i%.2f",real,imag);
	}
	return 0;
}
