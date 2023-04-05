/* AUTHOR :- RITUL SINGH
   DATE :- 02/09/2019
   TIME :- 01:22
   END TIME:- 01:35 */
#include<stdio.h>
int main()
{
	double number;
	printf("Enter a number:\n ");
    scanf("%lf", &number);
    if (number <= 0.0)
    {
    if (number == 0.0)
    printf("You entered 0.");
    else
    printf("You entered a negative number.");
    }
    else
    printf("You entered a positive number.");
    return 0;
}