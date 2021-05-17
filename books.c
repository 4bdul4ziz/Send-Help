/*Write a c program for the following problem,

A bookshop uses a personal computer to maintain the inventory of books that are being sold at the shop. 
The list includes details such as author, title, isbn number, price, author, stock position. 
Whenever a customer wants a book, the shopkeeper inputs the title or isbn number and the system replies whether the book is available or not. 
If it is not, an appropriate message is displayed. If book is in the list, then the system displays the book
details and asks for number of copies. If the requested copies are available, the total cost of the books is displayed;
 otherwise the message “Requested copies are not in stock” is displayed.

Note: ISBN number is 9 digit( EX: 1234-5678) and the validity of the isbn should be checked before storing the ISBN value.


Expected screen output will be:*/

#include <stdio.h>
#include <stdlib.h>
struct board
{
    char b[4][4];
    int n;
};
int main()
{
    struct board bird;
    scanf("%d",&bird.n);
    int size=bird.n;
    for (int i=0;i<size;i++)
    {
        for (int j=0;j<size;j++)
        {
            scanf("%c ",&bird.b[i][j]);
        }
    }
    printf("%c",bird.b[0][0]);
    for (int i=0;i<size;i++)
    {
        for (int j=0;j<size;j++)
        {
            printf("%c ",bird.b[i][j]);
        }
        printf("\n");
    }
    int ro=size;
    int co=size;
    int counter=0;
    if (ro>2 && co>2)
    {
        for (int i=0;i<ro-1;i++)
        {
            for (int j=0;j<co-2;j++)
            {
                if ((bird.b[i][j] == bird.b[i+1][j]) && (bird.b[i][j] == bird.b[i+2][j]) && (bird.b[i][j] == bird.b[i+2][j+1]) && (bird.b[i][j] == bird.b[i+2][j+2]))
                {
                    printf("Yes");
                    counter+=1;
                }
            }
        }
    }
    if(counter==0)
    {
        printf("No");
    }
    return 0;
}