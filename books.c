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
#include<conio.h>
#include<stdio.h>
#include<string.h>
class stock
{
    char author[50];
    char title[50];
    char pub[50];
    double price;
    int numcopies;
   public:
               stock();
               int access_title(char a[]);
               void input();
               void getdata(int);

};



