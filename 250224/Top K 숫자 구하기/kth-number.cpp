#include <iostream>
#include <algorithm>
using namespace std;

int N, k;
int nums[1000];

int main() {
    ios_base::sync_with_stdio;
    cin.tie(0);  cout.tie(0);

    cin >> N >> k;

    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    sort(nums, nums + N);
    cout << nums[k - 1] << "\n";

    return 0;
}
