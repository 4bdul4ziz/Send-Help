#include <iostream>
#include <math.h>
using namespace std;
 
 
class calculator
{
    double A,B;
 
public:
    void input()
    {
        cout<<"Enter the first number : ";
        cin>>A;
        cout<<"Enter the second number : ";
        cin>>B;
    }
 
    double add()
    {
        return A+B;
    }
 
    double sub()
    {
        return A-B;
    }
 
    double mul()
    {
        return A*B;
    }
 
    double div()
    {
        if(B==0)
        {
            cout<<"Division by Zero not possible" <<endl;
            return INFINITY;
        }
        else {
            return A/B;
        }
    }
};
int main()
{
    int ch;
    calculator obj;
    cout<<"Enter 1 to add 2 numbers\n";
    cout<<"Enter 2 to subtract 2 numbers \n";
    cout<<"Enter 3 to Multiply 2 numbers \n";
    cout<<"Enter 4 to divide 2 numbers \n";
    cout<<"Enter any option other than 1-4 to exit\n";
 
    do{   //using do while so the loop undergoes iteration atleast once without condition check
        cout<<"Enter your input choice: ";
        cin>>ch;
        switch(ch)
        {
        case 1:
            obj.input();
            cout<<"The addition of 2 numbers is : "<<obj.add() <<endl;
            break;
        case 2:
            obj.input();
            cout<<"The subtraction of 2 numbers is : "<<obj.sub() <<endl;
            break;
        case 3:
            obj.input();
            cout<<"The multiplication of 2 numbers is : "<<obj.mul() <<endl;
            break;
        case 4:
            obj.input();
            cout<<"The division of 2 numbers is : "<<obj.div()<<endl;
            break;
        default:
            cout<<"Exiting calculator.."<<endl;
            break;
        }
    }
    while (ch>=1 && ch<=4);
 
    return 0;
}
