#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int x{ 0 };
    int y{ 0 };
    int dx[4] = { 0, 1, 0, -1 };  //0 1 2 3 
    int dy[4] = { 1, 0, -1, 0 }; //북동남서

    string command;
    cin >> command;
    
    int dir = 0;
    int t{ 0 };
    for (char c : command) {
        t++;

        if (c == 'L') {
            dir = (dir + 3) % 4;
        }
        else if (c == 'R') {
            dir = (dir + 1) % 4;
        }
        else if (c == 'F') {
            x = x + dx[dir];
            y = y + dy[dir];

            if (x == 0 && y == 0) {
                cout << t << "\n";
                return 0;
            }
        }
    }
    cout << -1 << "\n";
}