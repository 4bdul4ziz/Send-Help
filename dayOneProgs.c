//1
#include <stdio.h>
 
void main()
{
    int i, num1, num2, count = 0;
 
    printf("Enter the value of num1 and num2 \n");
    scanf("%d %d", &num1, &num2);
    /* Count the number and compute their sum*/
    printf("Integers divisible by 5 are \n");
    for (i = num1; i < num2; i++)
    {
        if (i % 5 == 0)
        {
            printf("%3d,", i);
            count++;
        
        }
    }
    printf("\n Number of integers divisible by 5 between %d and %d =
 %d\n", num1, num2, count);
    
}
//2
#include<stdio.h>  
 int main()    
{    
int n,sum=0,m;    
printf("Enter a number:");    
scanf("%d",&n);    
while(n>0)    
{    
m=n%10;    
sum=sum+m;    
n=n/10;    
}    
printf("Sum is=%d",sum);    
return 0;  
}  

//3
#include <stdio.h>
#define DAYS_IN_WEEK 7
 
void find(int number_of_days)
{
    int year, week, days;
     
    year = number_of_days / 365;
    week = (number_of_days % 365) /
            DAYS_IN_WEEK;
    days = (number_of_days % 365) %
            DAYS_IN_WEEK;
    printf("years = %d",year);
    printf("\nweeks = %d", week);
    printf("\ndays = %d ",days);    
}
 
int main()
{
    int number_of_days;
    scanf("%d",&number_of_days);
    find(number_of_days);
    return 0;
}

//4
#include <stdio.h>
 
int main()
{
 
    long binary1, binary2;
    int i = 0, remainder = 0, sum[20];
 
    printf("Enter the first binary number: ");
    scanf("%ld", &binary1);
    printf("Enter the second binary number: ");
    scanf("%ld", &binary2);
    while (binary1 != 0 || binary2 != 0)
    {
        sum[i++] =(binary1 % 10 + binary2 % 10 + remainder) % 2;
        remainder =(binary1 % 10 + binary2 % 10 + remainder) / 2;
        binary1 = binary1 / 10;
        binary2 = binary2 / 10;
    }
    if (remainder != 0)
        sum[i++] = remainder;
    --i;
    printf("Sum of two binary numbers: ");
    while (i >= 0)
        printf("%d", sum[i--]);
    return 0;
}

//5
#include <stdio.h>
 
main()
{
    int number, temp, digit1, digit2, digit3;
 
    printf("Print all Armstrong numbers between 1 and 1000:\n");
    number = 001;
    while (number <= 900)
    {
        digit1 = number - ((number / 10) * 10);
        digit2 = (number / 10) - ((number / 100) * 10);
        digit3 = (number / 100) - ((number / 1000) * 10);
        temp = (digit1 * digit1 * digit1) + (digit2 * digit2 * digit2) + (digit3 * digit3 * digit3);
        if (temp == number)
        {
            printf("\n Armstrong no is:%d", temp);
        }
        number++;
    }
}

//6
#include <stdio.h>
 
unsigned long amount=1000, deposit, withdraw;
int choice, pin, k;
char transaction ='y';
 
void main()
{
	while (pin != 1520)
	{
		printf("ATM PIN");
		scanf("%d", &pin);
		if (pin != 1520)
		printf("ENTER A VALID ATM PIN\n");
	}
	do
	{
		printf("ATM MACHINE WELCOME YOU!\n");
		printf("1. Check Balance\n");
		printf("2. Withdraw Cash\n");
		printf("3. Deposit Cash\n");
		printf("4. Quit\n");
		printf("Enter your OPTION: ");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			printf("\n THIS IS THE AMOUNT YOU GOT IN YOUR ACCOUNT : %lu ", amount);
			break;
		case 2:
			printf("\n HOW MUCH DO YOU WANT TO WITHDRAW? : ");
			scanf("%lu", &withdraw);
			if (withdraw % 100 != 0)
			{
				printf("\n ENTER THE AMOUNT IN THE MULTIPLES OF 100");
			}
			else if (withdraw >(amount - 500))
			{
				printf("\n YOU DON'T HAVE ENOUGH MONEY TO COMPLETE THIS WITHDRAWAL");
			}
			else
			{
				amount = amount - withdraw;
				printf("\n\n GET THE CASH!");
				printf("\n YOUR BALANCE AFTER THAT IS%lu", amount);
			}
			break;
		case 3:
			printf("\n ENTER THE AMOUNT TO DEPOSIT");
			scanf("%lu", &deposit);
                        amount = amount + deposit;
			printf("YOUR BALANCE IS %lu", amount);
			break;
		case 4:
			printf("\n THANK U USING ATM");
			break;
		default:
			printf("\n INVALID CHOICE");
		}
		printf("\n\n\n WOULD YOU LIKE TO MAKE ANOTHER TRANSACTION? (Y/N): \n");
		fflush(stdin);
		scanf("%c", &transaction);
		if (transaction == 'n'|| transaction == 'N')
                    k = 1;
	} while (!k);
	printf("\n\n ATM MACHINE THANKS YOU FOR YOUR USE");
}
//7
/*
 * C Program to display function without using the Main Function
 */
#include <stdio.h>
#define decode(s,t,u,m,p,e,d) m##s##u##t
#define begin decode(a,n,i,m,a,t,e)
 
int begin()
{
    printf(" helloworld ");
}

//8
#include<stdio.h>  
 int main()    
{    
 if(printf("hello world")){}    
return 0;  
}   

message.txt
5 KB

//9
/*
C Program to validate date (Check date is valid or not)- read date from user
and validate whether entered date is correct or not with checking of leap year.*/

#include <stdio.h>
#include <time.h>
#define MAX_YR  9999
#define MIN_YR  1900
typedef struct
{
    
} Date;

int  IsLeapYear(int year)
{
    return (((year % 4 == 0) &&
             (year % 100 != 0)) ||
            (year % 400 == 0));
}

int isValidDate(int dd,int mm,int yyyy)
{
    
    if (yyyy > MAX_YR ||yyyy < MIN_YR)
        return 0;
    if (mm < 1 ||mm > 12)
        return 0;
    if (dd < 1 ||dd > 31)
        return 0;
    
    if (mm == 2)
    {
        if (IsLeapYear(yyyy))
            return (dd <= 29);
        else
            return (dd <= 28);
    }
    
    if (mm == 4 ||mm == 6 ||mm == 9 ||mm == 11)
        return (dd <= 30);
    return 1;
}
int main(void)
{
    int yyyy;
    int mm;
    int dd;
    int status = 0; 
    
    printf("\n\n Enter date in format (day/month/year): ");
    scanf("%d/%d/%d",&dd,&mm,&yyyy);
    status = isValidDate(dd,mm,yyyy);
    if(status !=1)
    {
        printf("\n\n Please enter a valid date!\n");
    }
    else
    {
        printf("\n\n Date is valid!\n");
    }
    return 0;
}

//10
/*
EMI Calculator (C program to calculate EMI)
*/


#include <stdio.h>
#include <math.h>

int main()
{
    float principal, rate, time, emi;

    printf("Enter principal: ");
    scanf("%f", &principal);

    printf("Enter rate: ");
    scanf("%f", &rate);

    printf("Enter time in year: ");
    scanf("%f", &time);

    rate = rate / (12 * 100); /*one month interest*/
    time = time * 12; /*one month period*/

    emi = (principal * rate * pow(1 + rate, time)) / (pow(1 + rate, time) - 1);

    printf("Monthly EMI is= %f\n", emi);

    return 0;
}