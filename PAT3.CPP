#include<iostream>
using namespace std;
class Time{
	private:
		int hour;
		int minute;
        int second;
	public:
		Time(int hr = 0, int min = 0, int sec = 0){
			hour = hr;
			minute = min;
            second = sec;
		}
		Time add(Time t){
			Time temp;
			temp.minute = minute + t.minute;
			temp.hour = hour + t.hour;
			if(temp.minute >= 60){
				temp.hour++;
				temp.minute -= 60;
			}
            if(temp.second >= 60){
                temp.hour++;
                temp.second -= 60;
            }
			return temp;
		}
		void display(){
			cout<<hour<<":"<<minute<<":"<<second<<endl;
		}
};

int main(){

    int a,b,c,d,e,f;
    cin>>a;
    cin>>b;
    cin>>c;
    cin>>d;
    cin>>e;
    cin>>f;

	Time t1(a,b,c), t2(d,e,f),t3;
	t3 = t1.add(t2);
	t1.display();
	t2.display();
	t3.display();
	return 0;
}