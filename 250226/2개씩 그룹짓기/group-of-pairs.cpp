#include <iostream>
#include <algorithm>
using namespace std;

int N;
int nums[2000];

int main() {
    cin >> N;

    for (int i = 0; i < 2 * N; i++) {
        cin >> nums[i];
    }

    sort(nums, nums + 2 * N);

    int max{ 0 };
    for(int i = 0; i < N; i++){
        int result = nums[i] + nums[2 * N - 1 - i];
        if(max < result){ max = result; }
    }
    cout << max << "\n";
    
    return 0;
}
