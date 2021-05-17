#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int temp = n, c = 0;
    while (n != 0)
    {
        int d = n % 10;
        if (d == 1)
        {
            c++;
        }
        n /= 10;
    }
    if (c % 2 == 0)
    {
        temp *= 10;
    }
    else
    {
        temp = temp * 10 + 1;
    }
    printf("%d", temp);
    return 0;
}