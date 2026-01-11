#include <iostream>
#include <algorithm>
#include <tuple>
#include <vector>
using namespace std;

vector<tuple<string, int, int>> people;

bool cmp(const tuple<string, int, int>& a, const tuple<string, int, int>& b){
    string name1, name2;
    int h1, h2, w1, w2;
    tie(name1, h1, w1) = a;
    tie(name2, h2, w2) = b;

    if(h1 != h2) return h1 < h2;
    if(w1 != w2) return w1 > w2;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    while(n--){
        string name;
        int h, w;
        cin >> name >> h >> w;
        people.push_back(make_tuple(name, h, w));
    }

    sort(people.begin(), people.end(), cmp);

    for (auto person : people){
        string name;
        int h, w;
        tie(name, h, w) = person;
        cout << name << " " << h << " " << w << "\n";
    }

}