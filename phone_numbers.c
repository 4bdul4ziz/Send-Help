/*A phone number, such as (212) 767-8900, can be thought of as having   three parts: the area code (212),
the exchange (767), and the number (8900).
Write a program that uses a structure to store these three parts of a phone number separately.
Call the structure phone. Create two structure variables of type phone. Initialize one, and have the user
input a number for the other one. Then display both numbers. The interchange might look like this:

Example:

Input
Enter your area code, exchange, and number: 415 555 1212

Output:
My number is (212) 767-8900
Your number is (415) 555-1212*/

#include<stdio.h>

struct number{
    int ac;
    int ex;
    int num;
};

int main(){
    int input1, input2, input3;
    //scanf("%d", &two.ac); //areacode
    //scanf("%d", &two.ex); //exchange
    //scanf("%d", &two.num); //num
    
    struct number one, two;
    one.ac = 212;
    one.ex = 767;
    one.num = 8900;
    
    scanf("%d", &two.ac);
    scanf("%d", &two.ex);
    scanf("%d", &two.num);
    
    printf("My Number is (%d) %d-%d\n", one.ac, one.ex, one.num);
    printf("Your Number is (%d) %d-%d", two.ac, two.ex, two.num);
    return 0;
}
