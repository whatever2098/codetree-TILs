#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int n;
string word[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> word[i];
    }

    sort(word, word + n);
    for ( int i = 0; i < n; i++){
        cout << word[i] << "\n";
    }

    return 0;
}