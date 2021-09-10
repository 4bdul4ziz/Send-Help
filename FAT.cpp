#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector <pair <pair<int, int>, pair <int, int> > > vertPoints, horPoints;
    int n; cin >> n;
    for(int i = 1; i <= n; i++)
    {
        int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
        if(x1 == x2) vertPoints.push_back(make_pair(make_pair(x1, y1), make_pair(x2, y2))); // Vertical Line
        if(y1 == y2) horPoints.push_back(make_pair(make_pair(x1, y1), make_pair(x2, y2))); // Horizontal Line
    }
    vector <pair<int, int> > stairs;
    int vertCount = 0, horCount = 0, stairCount = 0;
    vector <pair <pair<int, int>, pair <int, int> > > :: iterator itr;
    for(int i = 0; i < horPoints.size(); i++)
    {
        for(int j = 0; j < vertPoints.size(); j++)
        {
            if(horPoints[i].second.first == vertPoints[j].first.first && horPoints[i].second.second == vertPoints[j].first.second)
            {
                if(stairs.size() == 0) stairs.push_back(horPoints[i].first); // Empty Insert
                stairs.push_back(vertPoints[j].first);
                stairs.push_back(vertPoints[j].second);
            }
            if(horPoints[i].first.first == vertPoints[j].first.first && horPoints[i].first.second == vertPoints[j].first.second)
            {
                stairs.push_back(vertPoints[j].second);
                stairs.push_back(vertPoints[j].first);
            }
        }
    }
    // Get Last Horizontal Line
    for(int i = 0; i < horPoints.size(); i++)
    {
        if(horPoints[i].first.first == stairs[stairs.size() - 1].first && horPoints[i].first.second == stairs[stairs.size() - 1].second)
        {
            stairs.push_back(horPoints[i].second);
            break;
        }
    }
    for(int i = 0; i < stairs.size(); i++) cout << stairs[i].first << "\t" << stairs[i].second << endl;
    return 0;
}