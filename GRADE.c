/* AUTHOR :- RITUL SINGH
   DATE :- 02/09/2019
   TIME :- 00:38 */
#include<stdio.h>
int main()
{
	float phy,che,bio,hin,mat,percent,total; 
	printf("Enter the number of PHYSICS :-\t");
	scanf("%f",&phy);
	printf("Enter the number of CHEMISTRY :-\t");
	scanf("%f",&che);
	printf("Enter the number of BIOLOGY :-\t");
	scanf("%f",&bio);
	printf("Enter the number of HINDI :-\t");
	scanf("%f",&hin);
	printf("Enter the number of MATHEMATICS :-\t");
	scanf("%f",&mat);
	total= phy+che+bio+hin+mat;
	percent=total/5;
	if(percent>90)
	printf("GRADE 'A' ");
	else if (percent>80)
	printf("GRADE 'B' ");
	else if (percent>65)
	printf("GRADE 'C' ");
	else if (percent>50)
	printf("GRADE 'D' ");
	else if (percent>40)
	printf("GRADE 'E' ");
	else
	printf("GRADE 'F'\n ");
	return 0;
	
}
