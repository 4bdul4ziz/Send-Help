/*Write a C++ program to Add two Complex number.
 Define a class to get the complex number as real part and imaginery part and do the summation.*/

#include<iostream>
using namespace std;
class Complex {
    public:
        int real, imaginary;
    Complex()
    {
    }
    Complex(int tempReal, int tempImaginary)
    {
        real = tempReal;
        imaginary = tempImaginary;
    }
    
    Complex addComp(Complex C1, Complex C2)
    {
        Complex temp;
        temp.real = C1.real + C2.r eal;
        temp.imaginary = C1.imaginary + C2.imaginary;
        return temp;
    }
};

int main()
{
    int a, b, c, d;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);
    Complex C1(a,b);
    Complex C2(c,d);
    Complex C3;
    C3 = C3.addComp(C1, C2);
    cout << C3.real << "+" << C3.imaginary << "i";
    return 0;
}
}