#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int N, K;
    string T;
    cin >> N >> K >> T;
    
    vector<string> strs;

    for(int i{ 0 };i < N;i++){
        string str;
        cin >> str;
        
        bool include_t{ true };
        for(int j{ 0 };j < T.length();j++){
            if(str[j] != T[j]){ include_t = false; break; }
        }

        if(include_t) strs.push_back(str);
    }

    sort(strs.begin(), strs.end());
    cout << strs[K - 1] << "\n";
}