#include <iostream>
#include <string>
#include <tuple>
#include <vector>
#include <algorithm>
using namespace std;

int n;
string date[100];
string day[100];
string weather[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> date[i] >> day[i] >> weather[i];
    }

    vector<string> rainy_dates;
    vector<tuple<string, string, string>> v;
    for(int i = 0;i < n;i++){
        if(weather[i] == "Rain"){
            rainy_dates.push_back(date[i]);
            v.push_back(make_tuple(date[i], day[i], weather[i]));
        }
    }

    sort(rainy_dates.begin(), rainy_dates.end());
    for(int i = 0; i < v.size();i++){
        if(rainy_dates[0] == get<0>(v[i])){
            string a, b, c;
            tie(a, b, c) = v[i];
            cout << a << " " << b << " " << c << "\n";
        }
    }
    return 0;
}