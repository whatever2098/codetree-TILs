#include <iostream>
#include <cmath>    // round
#include <iomanip>  // fixed, setprecision
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N) || N <= 0) {
        return 0; // 비정상 입력 방어
    }

    double sum = 0.0;
    for (int i = 0; i < N; ++i) {
        double x;
        cin >> x;
        sum += x;
    }

    double avg = sum / N;

    // 소수 첫째 자리까지 반올림한 값 계산
    double avg1 = round(avg * 10) / 10.0;

    // 항상 한 자리까지 보이게 출력
    cout << fixed << setprecision(1) << avg1 << "\n";

    // 요구사항대로 실수 비교로 등급 판정
    if (avg >= 4.0) {
        cout << "Perfect\n";
    } else if (avg >= 3.0) {
        cout << "Good\n";
    } else {
        cout << "Poor\n";
    }

    return 0;
}


