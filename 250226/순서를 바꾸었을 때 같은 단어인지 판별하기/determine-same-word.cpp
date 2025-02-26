#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string word1;
string word2;

int main() {
    cin >> word1;
    cin >> word2;

    sort(word1, word1 + (int)word1.length());
    sort(word2, word2 + (int)word2.length());

    cout << ((word1 == word2)? "Yes" : "No") << "\n";

    return 0;
}
