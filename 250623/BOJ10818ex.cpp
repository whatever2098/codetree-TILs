#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main() {
    // I/O 속도 최적화
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N) || N <= 0) return 0;  // 입력 검증

    vector<int> nums(N);
    for (int i = 0; i < N; ++i) {
      cin >> nums[i];  // 사용자 입력값 저장
    }

    // 정렬을 통해 최솟값·최댓값을 찾음
    sort(nums.begin(), nums.end());
    cout << nums.front() << ' ' << nums.back() << '\n';

    return 0;
}//clang-format
