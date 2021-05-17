#include<iostream>
using namespace std;
public: class time
{
    int hour;
    int min;
    int sec;

    void get();
    void print();
    time add(int);
};
int main(){
    time t1, t2;
    int min;
    t1.get();
    cin >> min;
    t2.print();
    return 0;
}
void time::get()
{
    cin >> hour >> min >> sec;
}
void time::print()
{
    cout << hour << "\t"<< min << "\t"<< sec << endl;
}
time time::add(int m)
{
    time t2;
    int hr;
    t2.sec = sec;
    t2.min = min+m;
    t2.hour = hour;
    if(t2.min>=60){
        int hr;
        hr = t2.min/60;
        t2.min = t2.min-hr*60;
        t2.hour = t2.hour + hr;
    }
    return t2;
}

