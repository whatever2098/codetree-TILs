#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    int dx[4] = { -1, 1, 0, 0 }; 
    int dy[4] = { 0, 0, -1, 1 };  //위 아래 왼쪽 오른쪽
    vector<vector<bool>> colored(N, vector<bool>(N, false));

    for (int i{ 0 }; i < M; i++) {
        int r, c;
        cin >> r >> c;
        r--;
        c--;
        colored[r][c] = true;
        
        int colorCnt{ 0 };

        for (int dir{ 0 }; dir < 4; dir++) {
            int nx = r + dx[dir];
            int ny = c + dy[dir];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N)continue;
            if (colored[nx][ny] == false) continue;

            colorCnt++;
        }
        cout << ((colorCnt == 3) ? 1 : 0) << "\n";
    }
    
}