#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

#define value first
#define idx second

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<pair<int, int>> v;
    v.reserve(N);

    for(int i{0};i < N;i++){
        int val;
        cin >> val;
        v.push_back({val, i});    
    }

    sort(v.begin(), v.end(), [](const pair<int, int>& a, const pair<int, int>& b){
        if(a.value != b.value){ return a.value < b.value; }
        return a.idx < b.idx;
    });

    vector<int> P(N);
    for(int sorted_idx{0};sorted_idx < N;sorted_idx++){
        int original_idx = v[sorted_idx].idx;
        P[original_idx] = sorted_idx + 1;
    }

    for(auto e : P){
        cout << e << " ";
    }
}