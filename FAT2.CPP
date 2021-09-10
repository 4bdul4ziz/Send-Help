/*A faculty can avail vacation in both summer and winter. Given the details of the faculties and their vacation period in a file, design an algorithm and write a C++ code to check if a set of faculties are available on a particular day.

Faculty vacation files will contain stream of characters with details such as user name of the faculty, vacation start-date (separated by '/') and vacation end-date (separated by '/'). If the faculty is not in vacation on the given day then print “Available” and print “Not available” otherwise. A delimiter '#' is used to separate every field and record of user in the input file.

Details of vacation of a faculty is given in the following format:

 

janaki#01/05/2017#02/06/2017#Meena#10/05/2017#02/06/2017#

 

The above line indicates that the first faculty name is janaki, start-date of vacation is 01/05/2017 and end-date of vacation is 02/06/2017, and the second faculty name is Meena, vacation start-date is 10/05/2017 and the end-date of vacation is 02/06/2017. When a student checks for availability of faculty janaki on the date 30/04/2017 the program must print “Available” and when the user checks for availability of faculty janaki on the date 30/05/2017 the program must print “Not available”.

Develop OOP models as required.

Hint: date and time are predefined names in c++ so don't name your class/struct with ‘date’ and ‘time’

Input Format

Name of the file with faculty vacation details
Number of faculties to be checked

Name of faculty2 to be checked

Date to be checked for faculty1 (separated by '/')

Name of faculty2 to be checked

Date to be checked for faculty1 (separated by '/')

...

Name of faculty-n to be checked

Date to be checked for faculty-n (separated by '/')

Output Format

For each faculty, print either 'Available' or 'Not available'*/

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <map>
using namespace std;

class Date
{

    int day, month, year;
    friend int mask(Date);

public:
    Date(int d, int m, int y)
    {
        day = d;
        month = m;
        year = y;
    }
};

int mask(Date d)
{
    return d.year * 10000 + d.month * 100 + d.day;
}

vector<string> split(string &s, char delim)
{
    stringstream ss(s);
    string item;
    vector<string> elems;
    while (getline(ss, item, delim))
    {
        elems.push_back(item);
    }
    return elems;
}

Date getdate(string s)
{
    vector<string> v = split(s, '/');
    return Date(stoi(v[0]), stoi(v[1]), stoi(v[2]));
}

struct startend
{
    int start;
    int end;
};

int main()
{
    string fname;
    cin >> fname;
    ifstream f;
    f.open(fname);
    string s;
    map<string, startend> mp;
    while (!f.eof())
    {

        getline(f, s);
        vector<string> v = split(s, '#');

        for (int i = 0; i < v.size(); i += 3)
        {
            mp[v[i]] = {mask(getdate(v[i + 1])), mask(getdate(v[i + 2]))};
        }
    }
    f.close();

    int n;
    cin >> n;
    string name;
    int dd, mm, yyyy;
    vector<string> answers;
    for (int i = 0; i < n; i++)
    {
        cin >> name >> dd >> mm >> yyyy;
        Date d(dd, mm, yyyy);
        struct startend st = mp[name];
        if (mask(d) > st.start && mask(d) < st.end)
        {
            cout << "Not available\n";
        }
        else
        {
            cout << "Available\n";
        }
    }

    return 0;
}