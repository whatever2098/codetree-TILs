#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, -1, 0, 1};

    vector<vector<int>> grid(N, vector<int>(N));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }

    int result = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int cnt = 0;

            for (int dir = 0; dir < 4; dir++) {
                int nx = i + dx[dir];
                int ny = j + dy[dir];

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                    continue;
                }

                if (grid[nx][ny] == 1) {
                    cnt++;
                }
            }

            if (cnt >= 3) {
                result++;
            }
        }
    }

    cout << result << "\n";

    return 0;
}