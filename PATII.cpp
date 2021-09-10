/*Create two classes Distance_metre and Distance_Feet which store the value of distances. First class stores distances in meters and centimeters and second class stores in feet and inches.
Write a program that can read values for the class objects and add one object of  Distance_metre with another object of  Distance_Feet . 
Use a friend function to carry out the addition operation. The object that stores the results may be any class object, depending on the units in which the results are required.
Get choice from the user to display the distance (1) meters (2) feet.

The display should be in the format of feet and inches or meters and centimeters depending on the object on display. ( Do the necessary conversion for feet and meter)

Note: Conversion:

Inches per Centimeter = 2.54

Centimeter to Inches = .3048

Meter= 100cm, Foot= 12 inches

Example:

Enter distance in meter - centimeter : 15 65

Enter distance in feet - inches : 2 5

After adding( based on Choice from user)

(1)Distance = 16 m & 38.66 cm

 (2)Distance = 53 ft & 9.63204 inches*/

#include<iostream>

using namespace std;

class Distance_Feet;
class Distance_metre
{
    public:
        float m, c;
    public:
        void accept()
        {
           // cout<<"Enter distance in meter - centimeter : ";
            cin>>m>>c;
        }
        friend void sum(Distance_metre d1, Distance_Feet d2);
};

class Distance_Feet
{
        float f, i;
    public:
        void accept()
        {
            //cout<<"Enter distance in feet - inches : ";
            cin>>f>>i;
        }
        friend void sum(Distance_metre d1, Distance_Feet d2);
};
void sum(Distance_metre d1, Distance_Feet d2)
{
    int choose, n1, n2, n3, ans, metre, cm, feet, inch;
    n1 = d2.i*2.54;
    n2=d2.f*0.3048;
    n3=d1.m*100;
    ans=((d1.c+n3) + (n1+n2));
    metre=ans/100;
    cm=ans%100;
    feet=metre/0.3048;
    inch=cm/2.54;
    
    cin>>choose;
    if(choose==1){ 
    cout<<metre<<"m"<<cm<<"c.m";
    }
    else{
    cout<<feet<<"ft &"<<inch<<"inches";
   }
}
int main()
{
    Distance_metre d1;
    Distance_Feet d2;
    d1.accept();
    d2.accept();
    sum(d1,d2);
    return 0;
}