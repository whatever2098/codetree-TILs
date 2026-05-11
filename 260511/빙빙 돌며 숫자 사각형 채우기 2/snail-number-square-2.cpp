#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = { 0, 1, 0, -1 };//아래쪽, 오른쪽, 위쪽, 왼쪽
    int number{ 1 };
    int x = 0;
    int y = 0;
    int dir{ 0 };
    
    vector<vector<int>> grid(N, vector<int>(M, 0));
    grid[x][y] = number;

    while (N * M > number) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (nx < 0 || nx >= N || ny < 0 || ny >= M || grid[nx][ny] != 0) {
            dir = (dir + 1) % 4; continue;
        }
        x = nx;
        y = ny;

        number++;
        grid[x][y] = number;
    }

    for (int i{ 0 }; i < N; i++) {
        for (int j{ 0 }; j < M; j++) {
            cout << grid[i][j] << " ";
        }
        cout << "\n";
    }
}