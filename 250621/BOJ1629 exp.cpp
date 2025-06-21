// BOJ 1629: A^B mod C를 빠르게 계산하는 분할 정복(재귀) 알고리즘

#include <iostream>             // cin, cout 사용을 위해
using namespace std;            // std:: 접두어 생략

// a^b % c를 반환하는 함수
long long modPow(long long a, long long b, long long c) {
    if (b == 0) 
        return 1 % c;          // 지수가 0이면 a^0 = 1 → 1 mod c

    long long half = modPow(a, b / 2, c);  
                              // a^(b/2) % c를 재귀 호출로 계산
    long long result = (half * half) % c;  
                              // (a^(b/2))^2 = a^b (b가 짝수일 때) → mod c

    if (b % 2 == 1)                
        result = (result * (a % c)) % c;  
                              // b가 홀수면 한 번 더 a를 곱해줘야 함

    return result;              // 최종 결과 반환
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);           // 입출력 속도 최적화

    long long A, B, C;          
    cin >> A >> B >> C;         // A, B, C 입력받기

    cout << modPow(A, B, C);    // 재귀 함수 호출 결과 출력
    return 0;                   // 정상 종료
}
