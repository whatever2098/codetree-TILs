// BOJ 11729: 하노이 탑 이동 순서 출력 (원반 N개 → 기둥 1에서 3으로)

#include <iostream>             // cin, cout 사용
#include <vector>               // moves 벡터 사용
using namespace std;            // std:: 접두어 생략

vector<pair<int,int>> moves;    // (from → to) 이동 기록을 저장할 전역 벡터

// n개의 원반을 from 기둥에서 to 기둥으로 aux 기둥을 보조로 사용해 옮기는 함수
void hanoi(int n, int from, int to, int aux) {
    if (n == 1) {
        moves.emplace_back(from, to);  // 원반 하나를 곧바로 이동
        return;                        // 재귀 탈출
    }
    hanoi(n - 1, from, aux, to);      // n-1개를 보조 기둥(aux)으로 이동
    moves.emplace_back(from, to);     // 남은 가장 큰 원반을 목표 기둥(to)으로 이동
    hanoi(n - 1, aux, to, from);      // 보조 기둥(aux)에 있던 n-1개를 목표 기둥(to)으로 이동
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);                // 입출력 최적화

    int N; 
    cin >> N;                        // 원반 개수 입력

    long long count = (1LL << N) - 1;  
                                    // 이동 횟수 = 2^N - 1
    cout << count << "\n";          // 이동 횟수 출력

    hanoi(N, 1, 3, 2);              // 하노이 함수 실행 (1→3, 보조는 2)
    for (auto &mv : moves) {
        cout << mv.first             // 출발 기둥 번호
             << " " 
             << mv.second            // 도착 기둥 번호
             << "\n";                // 한 줄에 하나씩 출력
    }

    return 0;                        // 정상 종료
}
