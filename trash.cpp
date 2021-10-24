#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(NULL));
    ofstream out;
    out.open("f.txt");

    string s = "";
    for (int i = 0; i < 20000; ++i) {s.push_back(rand() % 256);}
    out << s;

    out.close();
}
