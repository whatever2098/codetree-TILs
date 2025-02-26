#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n;
int arr[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> middles;
    for(int i = 0;i < n;i++){
        if(i % 2 == 0){
            sort(arr, arr + i + 1);
            middles.push_back(arr[i / 2]);
        }
    }

    for(int e : middles){ cout << e << " "; }
    cout << "\n";

    return 0;
}