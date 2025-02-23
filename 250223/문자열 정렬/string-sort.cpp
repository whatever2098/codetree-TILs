#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

string str;

int main() {
    cin >> str;

    sort(str.begin(), str.end());
    cout << str << "\n";
    return 0;
}