#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

int n;
int nums[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    sort(nums, nums + n);
    for(int i = 0;i < n;i++){
        cout << nums[i] << " ";
    }
    cout << "\n";

    sort(nums, nums + n, greater<int>());
    for(int i = 0; i < n; i++){
        cout << nums[i] << " ";
    }
    cout << "\n";

    return 0;
}
