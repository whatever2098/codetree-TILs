#include <iostream>
#include <vector>
using namespace std;

// 최대공약수 (GCD): 유클리드 호제법
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

// 최소공배수 (LCM)
int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

// 재귀적으로 배열의 LCM 계산
int get_lcm_recursive(const vector<int>& arr, int index) {
    if (index == 0) return arr[0];
    return lcm(get_lcm_recursive(arr, index - 1), arr[index]);
}

int main() {
    vector<int> arr = {12, 18, 30};
    int result = get_lcm_recursive(arr, arr.size() - 1);
    cout << "LCM: " << result << endl;
    return 0;
}
