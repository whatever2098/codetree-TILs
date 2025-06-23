// BOJ 2750 수 정렬하기 - 디버깅 및 개선 버전
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // I/O 최적화
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    // cout.tie(nullptr); // 불필요하므로 제거 가능

    int N;
    if (!(cin >> N) || N <= 0) return 0; // 입력 검증 추가

    vector<int> v(N);
    for (int i = 0; i < N; ++i) {
        cin >> v[i];
    }

    // 오름차순 정렬
    sort(v.begin(), v.end());

    // 결과 출력
    for (int x : v) {
        cout << x << '\n';
    }

    return 0;
}