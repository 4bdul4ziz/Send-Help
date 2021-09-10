/*Ravi is a civil engineer. he wants to calculate the distance between two buildings or objects.
The  distance values are given  in feet and inches. Write a C program to calculate the distance.
Use structure to define distance and use function to add the distance.
Display the result in feets and inches.

1 feet= 12 inches

example:

Input:

Enter first distance in feet & inches: 10 feet  8 inches
Enter second distance in feet & inches: 5feet  7 inches

Output:

Total distance- Feet: 16, Inches: 3 */
#include <stdio.h>

typedef struct
{
    int feet;
    int inch;
}distance;

int main()
{
    distance d1, d2, sum;
    scanf("%d%d", &d1.feet, &d1.inch);
    scanf("%d%d", &d2.feet, &d2.inch);
    
    sum.inch = d1.inch + d2.inch;
    sum.feet = d1.feet + d2.feet;
    
    if(sum.inch>=12){
        sum.feet += sum.inch/12;
        sum.inch %= 12;
    }
    printf("%d", sum.feet);
    printf("\n%d",sum.inch);
    return 0;
}