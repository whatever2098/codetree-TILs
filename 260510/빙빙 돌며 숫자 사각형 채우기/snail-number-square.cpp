#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    int number{ 1 };

    int dx[4] = { 0, 1, 0, -1 };
    int dy[4] = { 1, 0, -1, 0 };

    vector<vector<int>> grid(N, vector<int>(M, 0));
    int x{ 0 };
    int y{ 0 };
    grid[x][y] = number;
    int dir{ 0 };

    while (N * M > number) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (nx < 0 || nx >= N || ny < 0 || ny >= M || grid[nx][ny] != 0) {
            dir = (dir + 1) % 4;
            continue;
        }

        x = nx;
        y = ny;

        grid[x][y] = ++number;
    }

    for (int i{ 0 }; i < N; i++) {
        for (int j{ 0 }; j < M; j++) {
            cout << grid[i][j] << " ";
        }
        cout << "\n";
    }
}